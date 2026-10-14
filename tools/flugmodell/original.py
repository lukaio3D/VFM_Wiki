"""Flugmodell der VFM-Jets aus den Originaldaten des Spiels (tools/spieldaten/lesen.py).

Das Spiel rechnet mit Flächen: jede Fläche hat eine Größe und ein Profil mit Auftriebs- und Widerstandskurve
über den Anstellwinkel. Als Punktmasse zusammengefasst (Steuerflächen unausgeschlagen, kein Schiebewinkel):

  L = KL * sigma(h) * V² * SL(α)              SL(α) = Σ Flächen  A * CL * liftCurve(α_Fläche) * Anteil senkrecht zur Bahn
  D = KD * sigma(h) * V² * (SD(α) + KB * baseDrag) * machDrag(M)
                                              SD(α) = Σ Flächen  A * CD * dragCurve(α_Fläche)
  α_Fläche aus der Lage der Flächennormale (schräge Leitwerke tragen mit, senkrechte haben α = 0).
  Der Schub wirkt entlang der Rumpfachse: T sin α trägt zum Lastvielfachen bei, T cos α wirkt gegen D.
  T = maxThrust * (Nachbrenner ? abThrustMul : 1) * thrustMach(M) * thrustDensity(1,225 sigma) [* thrustAoA(α)]   [kN]
  Masse = Leermasse + Treibstoff * Dichte [t], Kräfte in kN

sigma(h) ist die Dichtekurve des Spiels über der Höhe in Metern. Aus den Daten nicht ablesbar sind nur die
Faktoren KL, KD, KB aus dem Spielcode; kalibrieren.py legt sie an den Messungen fest -> daten/original_kalibrierung.json.

Die Spieldaten selbst liegen nur lokal (tools/spieldaten/ausgabe/spieldaten.json, gitignored).
"""
import json
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
SPIELDATEN = HIER.parent / 'spieldaten' / 'ausgabe' / 'spieldaten.json'
KALIBRIERUNG = HIER / 'daten' / 'original_kalibrierung.json'
g, KT, FT, LB = 9.80665, 0.514444, 0.3048, 4.44822
JETS = {'T-15': 'Eagle', 'T-16': 'Viper', 'T-18': 'Hornet'}
TANK = {'T-15': 6100, 'T-16': 3200, 'T-18': 5000}   # maxFuel, eindeutig je Jet


class Kurve:
    """Unity-AnimationCurve: kubisch Hermite zwischen den Stützstellen, außerhalb konstant."""
    def __init__(self, keys):
        k = np.array(keys, float).reshape(-1, 4)
        self.t, self.v, self.ein, self.aus = k.T

    def __call__(self, x):
        x = np.asarray(x, float)
        t, v = self.t, self.v
        if len(t) == 0:
            return np.ones_like(x)
        if len(t) == 1:
            return np.full_like(x, v[0])
        xc = np.clip(x, t[0], t[-1])
        i = np.clip(np.searchsorted(t, xc, side='right') - 1, 0, len(t) - 2)
        dt = t[i + 1] - t[i]
        s = (xc - t[i]) / dt
        h00, h10, h01, h11 = 2 * s**3 - 3 * s**2 + 1, s**3 - 2 * s**2 + s, -2 * s**3 + 3 * s**2, s**3 - s**2
        return h00 * v[i] + h10 * dt * self.aus[i] + h01 * v[i + 1] + h11 * dt * self.ein[i + 1]


def lade_spieldaten(pfad=SPIELDATEN):
    if not Path(pfad).exists():
        raise FileNotFoundError(f'{pfad} fehlt. Erst tools/spieldaten/lesen.py auf dem Rechner mit VFM ausführen.')
    return json.loads(Path(pfad).read_text(encoding='utf-8'))


def lade_kalibrierung(pfad=KALIBRIERUNG):
    return json.loads(Path(pfad).read_text(encoding='utf-8')) if Path(pfad).exists() else {'KL': 1.0, 'KD': 1.0, 'KB': 1.0}


class Atmosphaere:
    def __init__(self, sd):
        ac = next(x for x in sd['AerodynamicsController'] if x['atmosDensityCurve'])
        self.sigma_kurve = Kurve(ac['atmosDensityCurve'])

    def sigma(self, h_m):
        return self.sigma_kurve(h_m)

    @staticmethod
    def schall(h_m):
        return np.sqrt(1.4 * 287.05 * np.maximum(288.15 - 0.0065 * np.asarray(h_m, float), 216.65))


class Jet:
    # x-Achse der Schub-Dichtekurve: absolute Dichte 1,225 * sigma passt besser zu den Sustained-Kurven als sigma
    # (Summe der RMS-Fehler 4,0 statt 5,4 °/s über 3 Jets × 3 Höhen; bei 10.000 ft sind beide fast gleich).
    DICHTE_ACHSE = 1.225

    def __init__(self, typ, sd, kal=None):
        self.typ, intern = typ, JETS[typ]
        kal = kal or lade_kalibrierung()
        if 'jets' in kal:   # Format von kalibrieren.py: Faktoren je Jet
            k = kal['jets'][typ]
            kal = {'KL': k['KL'], 'KD': k['KD'], 'KB': k['kB']}
        self.KL, self.KD, self.KB = kal['KL'], kal['KD'], kal['KB']
        name = lambda klasse, n: next(x for x in sd[klasse] if x['_name'] == n)
        s = name('JetSpecs', f'{intern}Specs')
        e = name('JetEngineSpecs', f'{intern}EngineSpecs')
        jc = next(x for x in sd['JetController'] if x['jetSpecs'] == f'{intern}Specs')
        tank = next(x for x in sorted(sd['FuelTank'], key=lambda x: (x['_datei'], x['_id'])) if x['maxFuel'] == TANK[typ])
        profile = {x['_name']: x for x in sd['Aerodynamics']}

        self.m_leer = s['mass']                                   # t
        self.m_fuel = tank['maxFuel'] * tank['fuelDensity']       # t
        self.alpha_lim, self.alpha_lim2 = s['aoaLimit1'], s['aoaLimit2']
        self.pyr = s['pyrRates']
        self.g_limit = s['gLimitCurve'][0][1]
        self.mach_drag = Kurve(s['customMachWaveDrag']) if s['useCustomMachWaveDrag'] else None
        self.base_drag, self.brake_drag = jc['baseDrag'], jc['brakeDrag']

        self.T_max, self.ab = e['maxThrust'], e['abThrustMul']
        self.thrust_mach, self.thrust_dichte = Kurve(e['thrustMachCurve']), Kurve(e['thrustDensityCurve'])
        self.thrust_aoa = Kurve(e['thrustAoACurve']) if e['useThrustAoACurve'] else None
        self.min_output = e['minOutput']
        self.thrust_fuel_ratio, self.ab_drain = e['thrustFuelRatio'], e['abDrainMul']

        self.flaechen = []
        for w in jc['fluegel']:
            p = profile[w['profil']]
            n = np.array(w['normale'], float)
            self.flaechen.append(dict(name=w['name'], A=w['flaeche'], n=n / np.linalg.norm(n), CL=p['liftCoefficient'],
                                      CD=p['dragCoefficient'], lift=Kurve(p['liftCurve']), drag=Kurve(p['dragCurve'])))
        self.alpha_tab = np.arange(-10.0, 90.01, 0.25)
        self.SL_tab = self._SL(self.alpha_tab)
        self.SD_tab = self._SD(self.alpha_tab)
        m = (self.alpha_tab >= 0) & (self.alpha_tab <= self.alpha_lim2)
        self.alpha_peak = float(self.alpha_tab[m][np.argmax(self.SL_tab[m])])   # Flügel-α beim Auftriebsmaximum

    # Summen über die Flächen. Körperachsen wie Unity: x rechts, y oben, z vorn. Anströmung bei α: aus
    # Richtung v = (0, -sin α, cos α). Lokaler Anstellwinkel einer Fläche = Winkel zwischen v und Flächenebene,
    # Auftrieb senkrecht zu v in der Ebene aus v und Normale (perpLiftVector), Widerstand entlang v.
    def _summen(self, alpha):
        a = np.radians(np.asarray(alpha, float))
        v = np.stack([np.zeros_like(a), -np.sin(a), np.cos(a)], -1)
        oben = np.stack([np.zeros_like(a), np.cos(a), np.sin(a)], -1)     # senkrecht zu v, Symmetrieebene
        SL = np.zeros_like(a); SD = np.zeros_like(a)
        for f in self.flaechen:
            vn = -(v @ f['n'])
            ak = np.degrees(np.arcsin(np.clip(vn, -1, 1)))
            quer = f['n'] - (v @ f['n'])[..., None] * v                  # Normale ohne Anteil entlang v
            ql = np.linalg.norm(quer, axis=-1)
            richtung = (quer @ np.eye(3)) / np.maximum(ql, 1e-9)[..., None]
            L = f['A'] * f['CL'] * f['lift'](np.abs(ak)) * np.sign(ak)
            SL += L * np.einsum('...i,...i', richtung, oben)
            SD += f['A'] * f['CD'] * f['drag'](np.abs(ak))
        return SL, SD

    def _SL(self, alpha):
        return self._summen(alpha)[0]

    def _SD(self, alpha):
        return self._summen(alpha)[1]

    def SL(self, alpha):
        return np.interp(alpha, self.alpha_tab, self.SL_tab)

    def SD(self, alpha, kS=1.0):
        """Widerstandssumme; kS skaliert den Anstieg jenseits des Auftriebsmaximums (Kalibrierung, T-18)."""
        sd = np.interp(alpha, self.alpha_tab, self.SD_tab)
        if kS == 1.0:
            return sd
        sp = np.interp(self.alpha_peak, self.alpha_tab, self.SD_tab)
        return np.where(np.abs(alpha) > self.alpha_peak, sp + kS * (sd - sp), sd)

    def masse(self, fuel=1.0):
        return self.m_leer + fuel * self.m_fuel

    def gewicht(self, fuel=1.0):                                   # kN
        return self.masse(fuel) * g

    def machfaktor(self, M):
        return self.mach_drag(M) if self.mach_drag else np.ones_like(np.asarray(M, float))

    def schub(self, sigma, M, nachbrenner=True, alpha=0.0):       # kN
        T = self.T_max * (self.ab if nachbrenner else 1.0) * self.thrust_mach(M) * self.thrust_dichte(self.DICHTE_ACHSE * sigma)
        return T * (self.thrust_aoa(np.abs(alpha)) if self.thrust_aoa else 1.0)

    def auftrieb(self, sigma, V, alpha):                           # kN
        return self.KL * sigma * V * V * self.SL(alpha)

    def widerstand(self, sigma, V, alpha, M, bremse=False):        # kN
        S = self.SD(alpha) + self.KB * (self.base_drag + (self.brake_drag if bremse else 0.0))
        return self.KD * sigma * V * V * S * self.machfaktor(M)

    def alpha_fuer_L(self, L, sigma, V):
        """Kleinster α >= 0, bei dem der Auftrieb L erreicht wird (nan, wenn nicht erreichbar bis aoaLimit2)."""
        bed = L / (self.KL * sigma * V * V)
        m = (self.alpha_tab >= 0) & (self.alpha_tab <= self.alpha_lim2)
        a, s = self.alpha_tab[m], self.SL_tab[m]
        k = np.argmax(s)
        return np.where(bed <= s[k], np.interp(bed, np.maximum.accumulate(s[:k + 1]), a[:k + 1]), np.nan)


def flotte(sd=None, kal=None):
    sd = sd or lade_spieldaten()
    return Atmosphaere(sd), {t: Jet(t, sd, kal) for t in JETS}
