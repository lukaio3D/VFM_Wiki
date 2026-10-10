"""Wertet Ausroll- und Max-G-Messflüge (aus Quest-Videos abgelesene HUD-Werte) gegen das Flugmodell aus.

- Ausrollen im Leerlauf ohne Speedbrake, 1 G: Ps = -(D - T_leer) V / W. Mit T_leer ≈ 0 (Fuel Flow im
  Leerlauf ~1 % des Nachbrenners) folgt der Widerstand D direkt; zusammen mit dem gemessenen Überschuss
  T - D aus den Beschleunigungsläufen trennt das Schub und Widerstand.
- Voller Zug bei ~450 KIAS: erreichte G gegen das Lift-Limit aus den Diagrammen und Energieverlust gegen
  das Modell bei gleicher G.

Aufruf: python zug_ausrollen.py daten/zug_t15_2026-10-10.csv T-15
"""
import csv
import sys
import numpy as np
import modell as M

KT, FT, g, LB = M.KT, M.FT, M.g, M.LB
GEWICHT_VOLL = {'T-15': 42160, 'T-16': 26787, 'T-18': 41226}
# Nachbrenner-Sekunden vor Ausrollen bzw. Zug (aus dem Video), Verbrauch wie in messflug.py
AB_SEK = {'T-15': (6, 18), 'T-16': (8, 17), 'T-18': (10, 19)}
AB_LBS_PRO_S = {'T-15': 35.0, 'T-16': 16.3, 'T-18': 35.0}


def lade(pfad):
    zeilen = list(csv.DictReader(open(pfad)))
    f = lambda z, k: float(z[k]) if z[k] else np.nan
    keys = ('t_s', 'kias', 'mach', 'hoehe_ft', 'g', 'rate_dps', 'alpha')
    return {ph: np.array([[f(z, k) for k in keys] for z in zeilen if z['phase'] == ph])
            for ph in ('ausrollen', 'zug')}


def main(pfad, jet):
    daten, tab = M.lade()
    r_par = M.fit_r(daten)
    H, scl = M.fit_lift(daten, tab, r_par)
    atm = M.Atmosphaere(r_par, H)
    p = M.fit_sustained(M.sus_daten(daten, jet, M.HOEHEN), atm, scl[jet])
    c = M.MASSSTAB_C[jet]
    mess = lade(pfad)

    # --- Ausrollen ---
    d = mess['ausrollen']
    t, k, h = d[:, 0], d[:, 1], d[:, 3]
    W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * AB_SEK[jet][0]) * LB
    V = k * KT * atm.r(h, k)
    print(f'{jet} Ausrollen (Leerlauf, 1 G, ~{W / LB:,.0f} lbs): Widerstand D/W gemessen vs. Modell')
    print('   KIAS    Mach  dV/dt[kt/s]  D/W gemessen  D/W Modell  T/W Modell (Überschuss + D)')
    gem, mod, tw = [], [], []
    for i in range(1, len(t) - 1, 3):
        dVdt = (V[i + 1] - V[i - 1]) / (t[i + 1] - t[i - 1])
        dhdt = (h[i + 1] - h[i - 1]) * FT / (t[i + 1] - t[i - 1])
        Ps = V[i] * dVdt / g + dhdt
        _, q, Mach = atm.zustand(h[i], k[i])
        T, cd0, ks = M.schub_widerstand(p, h[i], Mach, atm)
        D_mod = c * (q * cd0 + ks * W ** 2 / q) / W
        ueber = c * (T - q * cd0 - ks * W ** 2 / q) / W
        gem.append(-Ps / V[i]); mod.append(D_mod); tw.append(ueber - Ps / V[i])
        print(f'   {k[i]:4.0f}   {Mach:.2f}    {dVdt / KT:6.1f}      {-Ps / V[i]:.3f}       {D_mod:.3f}       {tw[-1]:.2f}')
    gem, mod = np.array(gem), np.array(mod)
    print(f'   Verhältnis gemessen / Modell: {np.mean(gem / mod):.2f} (Spanne {np.min(gem / mod):.2f}–{np.max(gem / mod):.2f})')
    print(f'   -> Schub bei Vollgas (Nachbrenner) auf 10.000 ft: T/W ≈ {np.mean(tw):.2f} '
          f'(Spanne {np.min(tw):.2f}–{np.max(tw):.2f}), Annahme Leerlaufschub ≈ 0')

    # --- Voller Zug ---
    d = mess['zug']
    t, k, h, n, w, al = d[:, 0], d[:, 1], d[:, 3], d[:, 4], d[:, 5], d[:, 6]
    W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * AB_SEK[jet][1]) * LB
    print(f'\n{jet} voller Zug ab ~{k[0]:.0f} KIAS (~{W / LB:,.0f} lbs): erreichte G vs. Lift-Limit der Diagramme')
    print('   t     KIAS   G gemessen  Lift-Limit Diagramm  Verhältnis  α')
    verh = []
    for i in range(len(t)):
        hh = h[i] if not np.isnan(h[i]) else np.interp(t[i], t[~np.isnan(h)], h[~np.isnan(h)])
        _, q, Mach = atm.zustand(hh, k[i])
        nL = min(q * M.scl(scl[jet], Mach) / W, 9.0)
        verh.append(n[i] / nL)
        print(f'   {t[i]:5.1f}  {k[i]:4.0f}   {n[i]:4.1f}         {nL:4.1f}              {n[i] / nL:.2f}     {al[i]:.0f}')
    verh = np.array(verh)
    hm = ~np.isnan(h)
    s = hm & (n >= np.nanmax(n) * 0.5)
    Vs = k[s] * KT * atm.r(h[s], k[s])
    E = h[s] * FT + Vs ** 2 / (2 * g)
    i0 = int(np.argmax(n[s]))
    # Energieverlust nach Erreichen der Höchst-G, als Mittel über den Zug
    Ps = np.polyfit(t[s][i0:], E[i0:], 1)[0]
    n_m = np.mean(n[s][i0:]); k_m = np.mean(k[s][i0:]); h_m = np.mean(h[s][i0:])
    Vm, q, Mach = atm.zustand(h_m, k_m)
    T, cd0, ks = M.schub_widerstand(p, h_m, Mach, atm)
    Ps_mod = c * (T - q * cd0 - ks * (n_m * W) ** 2 / q) / W * Vm
    dkdt = np.polyfit(t[s][i0:], k[s][i0:], 1)[0]
    print(f'   Höchst-G {np.nanmax(n):.1f} bei {k[np.nanargmax(n)]:.0f} KIAS; erreicht/Lift-Limit im Mittel '
          f'{np.mean(verh[k < k[np.nanargmax(n)]]):.2f} unterhalb davon')
    print(f'   Energieverlust ab Höchst-G: Ps {Ps / FT:+.0f} ft/s gemessen, Modell bei gleicher G (Ø {n_m:.1f} G, '
          f'{k_m:.0f} KIAS) {Ps_mod / FT:+.0f} ft/s; Speed sinkt um {-dkdt:.0f} kt/s (inkl. Sinkflug)')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
