"""Wertet Messflüge (aus dem Quest-Video abgelesene HUD-Werte) gegen das Flugmodell aus.

- Beschleunigungsläufe: spezifische Überschussleistung Ps = V dV/dt / g + dh/dt, daraus (T - D) / W bei 1 G.
  Damit wird der Maßstab c von Schub und Widerstand festgelegt, den die Diagramme allein offenlassen.
  Belastbar ist nur der Überschuss T - D; wie er sich auf Schub und Widerstand verteilt, bleibt offen.
- Mach-Anzeige gegen wahre Fahrt: Schallgeschwindigkeit im Spiel.
- Kurve: G und Drehrate aus dem HUD gegen ω = g sqrt(n² - 1) / V (Prüfung der Atmosphäre) und gegen das Modell.

Aufruf: python messflug.py daten/messflug_t15_2026-10-10.csv T-15
"""
import csv
import sys
import numpy as np
import modell as M

KT, FT, g, LB = M.KT, M.FT, M.g, M.LB
GEWICHT_VOLL = {'T-15': 42160, 'T-16': 26787, 'T-18': 41226}
# Fuel Flow mit Nachbrenner laut Cockpit-Anzeige [lbs/s]
AB_LBS_PRO_S = {'T-15': 35.0,   # ~115.000–140.000 PPH
                'T-16': 16.3,   # ~58.700 PPH
                'T-18': 35.0}   # nicht abgelesen, wie T-15 angenommen


def lade(pfad):
    zeilen = list(csv.DictReader(open(pfad)))
    f = lambda z, k: float(z[k]) if z[k] else np.nan
    return {ph: np.array([[f(z, k) for k in ('t_s', 'kias', 'mach', 'hoehe_ft', 'g', 'rate_dps')]
                          for z in zeilen if z['phase'] == ph])
            for ph in dict.fromkeys(z['phase'] for z in zeilen)}


def gewicht(jet, mess, phase, t):
    """Gewicht [N] bei 100 % Fuel zu Beginn minus Nachbrenner-Verbrauch in allen Läufen davor."""
    ab = 0.0
    for ph, d in mess.items():
        if ph == phase:
            return (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * (ab + t - d[0, 0])) * LB
        ab += d[-1, 0] - d[0, 0]
    raise KeyError(phase)


def main(pfad, jet):
    daten, tab = M.lade()
    atm = M.Atmosphaere(M.fit_r(daten), M.fit_lift(daten, tab, M.fit_r(daten))[0])
    H, scl = M.fit_lift(daten, tab, M.fit_r(daten))
    p = M.fit_sustained(M.sus_daten(daten, jet, M.HOEHEN), atm, scl[jet])
    mess = lade(pfad)

    print('Mach-Anzeige gegen wahre Fahrt (Modell-Atmosphäre):')
    a_spiel = []
    for ph, d in mess.items():
        t, k, ma, h = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
        s = ~np.isnan(ma) & ~np.isnan(k)
        V = k[s] * KT * atm.r(h[s], k[s])
        a_spiel += list(V / ma[s])
    a_spiel = np.array(a_spiel)
    print(f'  Schallgeschwindigkeit im Spiel ~10.000 ft: {np.median(a_spiel) / KT:.0f} kt '
          f'(ISA: {M.schall(10000) / KT:.0f} kt), Streuung ±{np.std(a_spiel) / KT:.0f} kt, n={len(a_spiel)}')

    print(f'\nBeschleunigung {jet} (1 G, Vollgas): gemessen vs. Modell (roher Maßstab)')
    gemessen, roh, punkte = [], [], []
    for ph, d in mess.items():
        if not ph.startswith('lauf'):
            continue
        t, k, h = d[:, 0], d[:, 1], d[:, 3]
        V = k * KT * atm.r(h, k)
        hm = h * FT
        for i in range(3, len(t) - 2):      # zentrale Differenz über ±1 s; Hochlaufen des Triebwerks und Gas raus weg
            dVdt = (V[i + 1] - V[i - 1]) / (t[i + 1] - t[i - 1])
            dhdt = (hm[i + 1] - hm[i - 1]) / (t[i + 1] - t[i - 1])
            Ps = V[i] * dVdt / g + dhdt
            W = gewicht(jet, mess, ph, t[i])
            _, q, Mach = atm.zustand(h[i], k[i])
            T, cd0, ks = M.schub_widerstand(p, h[i], Mach, atm)
            ueber_roh = (T - q * cd0 - ks * W ** 2 / q) / W
            gemessen.append(Ps / V[i]); roh.append(ueber_roh)
            punkte.append((ph, k[i], dVdt / KT, Ps / FT, Ps / V[i], Mach))
    gemessen, roh = np.array(gemessen), np.array(roh)
    c = np.sum(gemessen * roh) / np.sum(roh * roh)      # (T - D)_gemessen = c * (T - D)_Modell
    print('  Lauf    KIAS  dV/dt[kt/s]  Ps[ft/s]  (T-D)/W gemessen  Modell(kalibriert)')
    for (ph, k, a, ps, td, Mach), r in zip(punkte, roh):
        print(f'  {ph:6} {k:5.0f}  {a:9.1f}  {ps:8.0f}   {td:12.3f}     {c * r:12.3f}   M {Mach:.2f}')
    rest = gemessen - c * roh
    kias = np.array([pt[1] for pt in punkte])
    band = (kias >= 300) & (kias <= 500)
    print(f'  Schubüberschuss (T-D)/W bei 1 G, 300–500 KIAS: {np.mean(gemessen[band]):.2f} '
          f'(Spanne {gemessen[band].min():.2f}–{gemessen[band].max():.2f})')
    print(f'  Maßstab c = {c:.3f}; Rest RMS {np.sqrt(np.mean(rest ** 2)):.3f} '
          f'(= {np.sqrt(np.mean(rest ** 2)) / np.mean(gemessen) * 100:.0f} %)')

    if 'kurve' in mess:
        d = mess['kurve']
        t, k, h, n, w = d[:, 0], d[:, 1], d[:, 3], d[:, 4], d[:, 5]
        s = ~np.isnan(k) & ~np.isnan(h) & ~np.isnan(n) & ~np.isnan(w) & (n > 6)
        V = k[s] * KT * atm.r(h[s], k[s])
        w_formel = np.degrees(g * np.sqrt(n[s] ** 2 - 1) / V)
        print(f'\nKurve: HUD-Drehrate vs. g·√(n²−1)/V: Mittel {np.mean(w[s]):.2f} vs {np.mean(w_formel):.2f} °/s '
              f'(Abweichung {np.mean(w[s] - w_formel):+.2f} °/s)')
        # Energiebilanz in der Kurve: Ps als Steigung der Energiehöhe h + V²/2g über die Zeit
        s = ~np.isnan(k) & ~np.isnan(h) & ((n > 6) | np.isnan(n))
        V_all = k[s] * KT * atm.r(h[s], k[s])
        Ps_mess = np.polyfit(t[s], h[s] * FT + V_all ** 2 / (2 * g), 1)[0]
        W = gewicht(jet, mess, 'kurve', np.mean(t[s]))
        n_m, k_m, h_m = np.nanmean(n[n > 6]), np.mean(k[s]), np.mean(h[s])
        Vm, q, Mach = atm.zustand(h_m, k_m)
        T, cd0, ks = M.schub_widerstand(p, h_m, Mach, atm)
        Ps_mod = c * (T - q * cd0 - ks * (n_m * W) ** 2 / q) / W * Vm
        n_sus = min(np.sqrt(max(T - q * cd0, 0) * q / ks) / W, 9.0)
        print(f'  t {t[s][0]:.0f}–{t[s][-1]:.0f} s: {k_m:.0f} KIAS, {n_m:.2f} G im Mittel, Gewicht ~{W / LB:,.0f} lbs')
        print(f'  Ps gemessen {Ps_mess / FT:+.0f} ft/s, Modell {Ps_mod / FT:+.0f} ft/s; '
              f'Modell-Sustained bei dieser Speed: {n_sus:.2f} G = {M.rate(n_sus, Vm):.1f} °/s')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
