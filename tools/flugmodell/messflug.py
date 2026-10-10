"""Wertet Messflüge (aus dem Quest-Video abgelesene HUD-Werte) gegen das Flugmodell aus.

- Beschleunigungsläufe: spezifische Überschussleistung Ps = V dV/dt / g + dh/dt, daraus (T - D) / W bei 1 G.
  Damit wird der Maßstab von Schub und Widerstand festgelegt, den die Diagramme allein offenlassen.
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
AB_LBS_PRO_S = 35.0   # Fuel Flow mit Nachbrenner ~115.000–140.000 PPH laut Cockpit-Anzeige


def lade(pfad):
    zeilen = list(csv.DictReader(open(pfad)))
    f = lambda z, k: float(z[k]) if z[k] else np.nan
    return {ph: np.array([[f(z, k) for k in ('t_s', 'kias', 'mach', 'hoehe_ft', 'g', 'rate_dps')]
                          for z in zeilen if z['phase'] == ph])
            for ph in dict.fromkeys(z['phase'] for z in zeilen)}


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
            W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S * (t[i] - t[2])) * LB if ph == 'lauf1' else \
                (GEWICHT_VOLL[jet] - AB_LBS_PRO_S * (16 + t[i] - t[2])) * LB
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
    W50 = float(tab[('00000ft_050', jet)]['gewicht_lbs']) * LB
    T0, _, _ = M.schub_widerstand(p, 0, 0.4, atm)
    print(f'  Maßstab c = {c:.3f}  ->  T/W (Meereshöhe, M 0,4, 50 % Fuel) = {c * T0 / W50:.2f}; '
          f'Rest RMS {np.sqrt(np.mean(rest ** 2)):.3f} (= {np.sqrt(np.mean(rest ** 2)) / np.mean(gemessen) * 100:.0f} %)')

    if 'kurve' in mess:
        d = mess['kurve']
        t, k, h, n, w = d[:, 0], d[:, 1], d[:, 3], d[:, 4], d[:, 5]
        s = ~np.isnan(k) & ~np.isnan(n) & ~np.isnan(w) & (n > 6)
        V = k[s] * KT * atm.r(h[s], k[s])
        w_formel = np.degrees(g * np.sqrt(n[s] ** 2 - 1) / V)
        print(f'\nKurve: HUD-Drehrate vs. g·√(n²−1)/V: Mittel {np.mean(w[s]):.2f} vs {np.mean(w_formel):.2f} °/s '
              f'(Abweichung {np.mean(w[s] - w_formel):+.2f} °/s)')
        # Energiebilanz in der Kurve: Ps aus Speed- und Höhenänderung, Modell bei gleicher G
        V_all = k * KT * atm.r(h, k)
        i0, i1 = np.where(t == 89)[0][0], np.where(t == 105)[0][0]
        Ps_mess = ((V_all[i1] ** 2 - V_all[i0] ** 2) / (2 * g) + (h[i1] - h[i0]) * FT) / (t[i1] - t[i0])
        W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S * 55) * LB
        n_m = np.nanmean(n[(t >= 89) & (t <= 105)])
        k_m = np.nanmean(k[(t >= 89) & (t <= 105)])
        h_m = np.nanmean(h[(t >= 89) & (t <= 105)])
        Vm, q, Mach = atm.zustand(h_m, k_m)
        T, cd0, ks = M.schub_widerstand(p, h_m, Mach, atm)
        Ps_mod = c * (T - q * cd0 - ks * (n_m * W) ** 2 / q) / W * Vm
        n_sus = min(np.sqrt(max(T - q * cd0, 0) * q / ks) / W, 9.0)
        print(f'  t 89–105 s: {k_m:.0f} KIAS, {n_m:.2f} G im Mittel, Gewicht ~{W / LB:,.0f} lbs')
        print(f'  Ps gemessen {Ps_mess / FT:+.0f} ft/s, Modell {Ps_mod / FT:+.0f} ft/s; '
              f'Modell-Sustained bei dieser Speed: {n_sus:.2f} G = {M.rate(n_sus, Vm):.1f} °/s')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
