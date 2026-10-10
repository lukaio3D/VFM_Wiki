"""Punktmassen-Flugmodell der VFM-Jets, kalibriert an den digitalisierten Performance-Kurven.

Struktur (aus den Daten bestätigt, siehe UEBERGABE.md):
- Spiel-Atmosphäre: Dichte  rho = rho0 * exp(-h / H);  wahre Fahrt  V = KIAS * r(h, KIAS)  (aus der 9G-Linie).
- Lift-Limit:   n_L = q * SCLmax(M) / W,  q = rho V² / 2,  9 G hartes Limit.
- Schub/Widerstand:  T(h, M) = q * SCD0(M) + KS * (n W)² / q  im stationären Kurvenflug (Ps = 0).
  T und SCD0 sind stückweise linear über Mach (VFM nutzt offenbar frei geformte Kurven).
  Schub ist gewichtsunabhängig, induzierter Widerstand ~ (n W)² (Test: n_s * W über Fuel-Stände konstant).

Achtung: Aus Ps = 0 allein ist der gemeinsame Maßstab von Schub und Widerstand nicht bestimmbar.
Er wird über MASSSTAB_C festgelegt, gemessen per Beschleunigungsflug (messflug.py).
Belastbar ist damit der Überschuss T - D (Energiegewinn und -verlust); wie er sich auf Schub und
Widerstand verteilt, bleibt offen.

Aufruf: python modell.py  -> Fit, Kreuzvalidierung, daten/modell_parameter.json
"""
import csv
import json
import os
import numpy as np
from scipy.optimize import least_squares

HIER = os.path.dirname(os.path.abspath(__file__))
DATEN = os.path.join(HIER, 'daten')
g, KT, LB, FT, RHO0 = 9.80665, 0.514444, 4.44822, 0.3048, 1.225
JETS = ['T-15', 'T-16', 'T-18']
HOEHEN = [0, 10000, 20190]
# Maßstab von Schub und Widerstand, gemessen: Beschleunigungsläufe 10.000 ft, 100 % Fuel, 2026-10-10
# (messflug.py; Schubüberschuss bei 1 G, 300–500 KIAS: T-15 1,40, T-16 1,02, T-18 0,95 x Gewicht)
MASSSTAB_C = {'T-15': 2.608, 'T-16': 2.440, 'T-18': 1.783}


def schall(h_ft):
    return np.sqrt(1.4 * 287.05 * (288.15 - 0.0065 * h_ft * FT))


def lade():
    """Kurvenpunkte als Arrays je (Jet, Kurve): h [ft], KIAS, W [N], omega [rad/s], Corner-KIAS."""
    tab = {(r['bild'], r['jet']): r for r in csv.DictReader(open(os.path.join(DATEN, 'tabellen_2026-10.csv')))}
    roh = {}
    for p in csv.DictReader(open(os.path.join(DATEN, 'kurven_2026-10.csv'))):
        t = tab[(p['bild'], p['jet'])]
        roh.setdefault((p['jet'], p['kurve']), []).append(
            (float(p['hoehe_ft']), float(p['kias']), float(p['gewicht_lbs']) * LB,
             np.radians(float(p['rate_dps'])), float(t['corner_kias'])))
    return {k: np.array(v) for k, v in roh.items()}, tab


def fit_r(daten):
    """V/KIAS je Höhe aus der 9G-Linie (omega = g sqrt(80) / V), linear in KIAS."""
    alle = np.vstack([daten[(j, 'instant')] for j in JETS])
    h, k, W, w, c = alle.T
    par = {}
    for hh in HOEHEN:
        s = (h == hh) & (k > c + 15) & (k < 700) & (w > 0.05)
        b, a = np.polyfit(k[s] - 400, g * np.sqrt(80) / w[s] / KT / k[s], 1)
        par[hh] = (float(a), float(b))
    return par


class Atmosphaere:
    def __init__(self, r_par, H):
        self.r_par, self.H = r_par, H
        hs = np.array(HOEHEN, float)
        self._la = np.polyfit(hs, np.log([r_par[h][0] for h in HOEHEN]), 2)
        self._b = np.array([r_par[h][1] for h in HOEHEN])
        self._hs = hs

    def r(self, h, k):
        return np.exp(np.polyval(self._la, h)) + np.interp(h, self._hs, self._b) * (k - 400)

    def rho(self, h):
        return RHO0 * np.exp(-np.asarray(h) * FT / self.H)

    def zustand(self, h, k):
        V = k * KT * self.r(h, k)
        return V, 0.5 * self.rho(h) * V ** 2, V / schall(h)


def scl(par, M):
    c0, c1, c2 = par
    return c0 + c1 * (M - 0.5) + c2 * (M - 0.5) ** 2


def rate(n, V):
    return np.degrees(g * np.sqrt(np.clip(n ** 2 - 1, 0, None)) / V)


def lift_daten(daten, tab, jet):
    h, k, W, w, c = daten[(jet, 'instant')].T
    s = (k > 180) & (k < c - 8)
    tc = np.array([(float(t['hoehe_ft']), float(t['corner_kias']), float(t['gewicht_lbs']) * LB)
                   for (b, j), t in tab.items() if j == jet])
    return (h[s], k[s], W[s], w[s]), tc


def fit_lift(daten, tab, r_par):
    """H gemeinsam für alle Jets, SCLmax(M) je Jet (Instant-Linie unter Corner + Corner-Punkte mit n = 9)."""
    ld = {j: lift_daten(daten, tab, j) for j in JETS}

    def res(x):
        atm = Atmosphaere(r_par, x[0] * 1000)
        out = []
        for i, j in enumerate(JETS):
            par = x[1 + 3 * i:4 + 3 * i]
            (h, k, W, w), tc = ld[j]
            V, q, M = atm.zustand(h, k)
            n = np.sqrt((w * V / g) ** 2 + 1)
            out.append((q * scl(par, M) / W - n) / 0.1)
            V, q, M = atm.zustand(tc[:, 0], tc[:, 1])
            out.append((q * scl(par, M) / tc[:, 2] - 9) / 0.05 * 3)
        return np.concatenate(out)

    sol = least_squares(res, [8.5, 80, 0, 0, 42, 0, 0, 68, 0, 0])
    return sol.x[0] * 1000, {j: [float(v) for v in sol.x[1 + 3 * i:4 + 3 * i]] for i, j in enumerate(JETS)}


MK = np.round(np.arange(0.2, 1.65, 0.1), 2)   # Mach-Stützstellen für Schub- und Widerstandskurve
NK = len(MK)
GLAETTE = 3.0                                 # Gewicht der Krümmungsstrafe


def schub_widerstand(p, h, M, atm):
    """Schub = t0 * sigma^x * tau(M), SCD0 = cd0(M) (stückweise linear in Mach), KS = 2e-3 * (1 + k1 (M - 0,5)²)."""
    x, k1 = p[0], p[1]
    tau = np.exp(np.interp(M, MK, p[2:2 + NK]))
    cd0 = np.exp(np.interp(M, MK, p[2 + NK:2 + 2 * NK]))
    T = 1e5 * (atm.rho(h) / RHO0) ** x * tau
    ks = 2e-3 * (1 + k1 * (M - 0.5) ** 2)     # Maßstab fest (K/S ~ 0,1 / 50 m²), siehe Kopf
    return T, cd0, ks


def modellrate(p, scl_par, atm, h, k, W):
    V, q, M = atm.zustand(h, k)
    T, cd0, ks = schub_widerstand(p, h, M, atm)
    n_s = np.sqrt(np.clip((T - q * cd0) * q / ks, 0, None)) / W
    return rate(np.minimum(np.minimum(n_s, q * scl(scl_par, M) / W), 9.0), V)


def sus_daten(daten, jet, hoehen):
    h, k, W, w, c = daten[(jet, 'sustained')].T
    s = np.isin(h, hoehen) & (k > 180)
    return h[s], k[s], W[s], np.degrees(w[s])


def fit_sustained(d, atm, scl_par):
    h, k, W, r = d
    # Datenpunkte am 9G-Limit oder unter 1 °/s tragen nichts zur Polare bei, bleiben aber im Fehler
    def res(p):
        e = modellrate(p, scl_par, atm, h, k, W) - r
        krumm = np.concatenate([np.diff(p[2:2 + NK], 2), np.diff(p[2 + NK:], 2)]) * GLAETTE
        return np.concatenate([e / np.sqrt(len(e)) * 30, krumm])
    # Start: T/W ~ 0,9 und SCD0 ~ 1 m² (Kampfjet-typisch), sonst klebt alles am 9G-Limit ohne Gradient
    x0 = np.concatenate([[0.8, 0.0], np.log(np.full(NK, 0.9 * np.median(W) / 1e5)), np.log(np.full(NK, 1.0))])
    lb = np.concatenate([[0.2, -3], np.full(2 * NK, -8)])
    ub = np.concatenate([[1.6, 5], np.full(2 * NK, 8)])
    return least_squares(res, x0, bounds=(lb, ub), loss='soft_l1', f_scale=0.3).x


def kontrollplot(daten, atm, scl_par):
    """Digitalisierte Sustained-Kurven (Punkte) gegen das Modell (Linien) -> daten/kontrolle/modell_fit.png"""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(3, 3, figsize=(15, 11))
    for i, jet in enumerate(JETS):
        p = fit_sustained(sus_daten(daten, jet, HOEHEN), atm, scl_par[jet])
        for j, h in enumerate(HOEHEN):
            a = ax[i, j]
            hh, k, W, r = sus_daten(daten, jet, [h])
            for c, Wu in enumerate(np.unique(W)):
                s = W == Wu
                a.plot(k[s], r[s], '.', ms=2, color=f'C{c}', label=f'{Wu / LB:,.0f} lbs')
                kk = np.arange(180, k.max() + 1, 2.0)
                a.plot(kk, modellrate(p, scl_par[jet], atm, h + 0 * kk, kk, Wu + 0 * kk), 'k-', lw=0.7)
            a.set_title(f'{jet}, {h} ft (Punkte: Spiel, Linie: Modell)')
            a.set_xlabel('KIAS'); a.set_ylabel('Sustained Rate °/s')
            a.set_ylim(0, 26); a.grid(alpha=0.3); a.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(DATEN, 'kontrolle', 'modell_fit.png'), dpi=80)


def main():
    daten, tab = lade()
    r_par = fit_r(daten)
    print('Spiel-Atmosphäre: wahre Fahrt / KIAS bei 400 KIAS (Steigung je KIAS)')
    for h in HOEHEN:
        print(f'  {h:>5} ft: {r_par[h][0]:.4f}  ({r_par[h][1]:+.6f})')
    H, scl_par = fit_lift(daten, tab, r_par)
    atm = Atmosphaere(r_par, H)
    print(f'Dichte: rho = rho0 * exp(-h / {H:.0f} m)  ->  10.000 ft: {atm.rho(10000) / RHO0:.3f}, '
          f'20.190 ft: {atm.rho(20190) / RHO0:.3f}  (ISA: 0,738 / 0,543)')

    print('\nLift-Limit: Corner-Speed Modell minus Tabelle [KIAS], je Bedingung')
    ks = np.arange(200, 600, 0.5)
    for jet in JETS:
        fehler = []
        for (bild, j), t in sorted(tab.items()):
            if j == jet:
                V, q, M = atm.zustand(float(t['hoehe_ft']), ks)
                n = q * scl(scl_par[jet], M) / (float(t['gewicht_lbs']) * LB)
                fehler.append(float(ks[np.argmax(n >= 9)] - float(t['corner_kias'])))
        print(f'  {jet}: {fehler}')

    ergebnisse = {'atmosphaere': {'H_m': H, 'r': {str(h): r_par[h] for h in HOEHEN}}, 'jets': {}}
    print('\nSustained Rate: RMS-Abweichung [°/s] je Höhe, alle Kurvenpunkte und Fuel-Stände')
    print('  ' + ' ' * 40 + '   '.join(f'{h:>6} ft' for h in HOEHEN))
    for jet in JETS:
        for name, hoehen in [('alle Höhen', HOEHEN), ('ohne 10.000 ft (Interpolation)', [0, 20190]),
                             ('ohne 20.190 ft (Extrapolation)', [0, 10000])]:
            p = fit_sustained(sus_daten(daten, jet, hoehen), atm, scl_par[jet])
            zeile = []
            for h in HOEHEN:
                hh, k, W, r = sus_daten(daten, jet, [h])
                e = modellrate(p, scl_par[jet], atm, hh, k, W) - r
                zeile.append(f"{np.sqrt(np.mean(e ** 2)):6.2f}{'' if h in hoehen else '*':1}")
            print(f'  {jet} {name:34} ' + '   '.join(zeile), flush=True)
            if name == 'alle Höhen':
                ergebnisse['jets'][jet] = {
                    'SCLmax_m2': dict(zip(['c0', 'c1', 'c2'], scl_par[jet])),
                    'schub_widerstand_roh': {'x': float(p[0]), 'k1': float(p[1]), 'mach': MK.tolist(),
                                             'ln_tau': p[2:2 + NK].tolist(), 'ln_cd0': p[2 + NK:].tolist()},
                    'massstab_c': MASSSTAB_C[jet],
                }
    print('  (* = Höhe nicht im Fit, also Vorhersage)')
    kontrollplot(daten, atm, scl_par)
    with open(os.path.join(DATEN, 'modell_parameter.json'), 'w') as f:
        json.dump(ergebnisse, f, indent=2)


if __name__ == '__main__':
    main()
