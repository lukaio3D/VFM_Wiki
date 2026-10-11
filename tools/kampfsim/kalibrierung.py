"""Prüft die Dynamik des Kampfsimulators gegen die Messflüge (10.000 ft, voller Tank).

- Voller Zug ab 450 KIAS: G und KIAS über die Zeit gegen das Video (Startzeitpunkt an der ersten
  gemessenen G ausgerichtet).
- Erster Turn aus 450 KIAS: Kursänderung nach 4 und 8 s (Wiki-Tabelle „Der erste Turn aus 450 KIAS“).
- Beschleunigung 300 -> 500 KIAS.

Aufruf: python kalibrierung.py
"""
import csv
import os
import numpy as np
import sim as S

DATEN = os.path.join(S.HIER, '..', 'flugmodell', 'daten')


def manoever(m, typ, kias0=450.0, dauer=10.0, dt=0.02, alpha_grenze=None, n_ziel=None, gas=1.0, start_alpha=2.0):
    """Einzelner Jet, Kurve mit Lift Vector so geneigt, dass die Höhe gehalten wird (soweit möglich)."""
    atm = S.Atmo(m)
    fl = S.Flotte(m, [typ])
    h = 10000 * S.FT
    V = float(atm.tas(np.array(h), np.array(kias0)))
    W = fl.W_voll.copy()
    alpha = np.array([start_alpha])
    a_gr = fl.alpha_lim if alpha_grenze is None else np.array([alpha_grenze])
    kurs, out = 0.0, []
    for i in range(int(dauer / dt) + 1):
        t = i * dt
        rho = atm.rho(np.array([h]))
        q = 0.5 * rho * V * V
        M = V / atm.schall(np.array([h]))
        kias = atm.kias(np.array([h]), np.array([V]))
        T = fl.schub(rho, M) * gas
        scd0, ks, sclm = fl.polare(q, M)
        if n_ziel is None:
            a_cmd = a_gr
        else:
            a_cmd = np.minimum(fl.alpha_von_c(n_ziel(kias) * W / (q * sclm)), a_gr)
        da = (a_cmd - alpha) / S.ANNAHMEN['alpha_tau_s']
        alpha = alpha + np.clip(da, -S.ANNAHMEN['alpha_rate_ab_dps'], fl.alpha_rate) * dt
        L = np.minimum(fl.c_von_alpha(alpha) * q * sclm, 9 * W)
        n = float((L / W)[0])
        D = fl.widerstand(q, scd0, ks, sclm, L, alpha)
        # Kurve in der Horizontalen, so weit n reicht; Rest sinkt (wie im Video, leichter Sinkflug)
        n_h = np.sqrt(max(n * n - 1, 0))
        omega = S.g * n_h / V
        out.append((t, float(kias[0]), n, float(alpha[0]), kurs, h / S.FT))
        kurs += np.degrees(omega) * dt
        V = float(V + (T - D)[0] / (W[0] / S.g) * dt)
        W = W - fl.burn * dt
    return np.array(out)


def lade_zug(jet):
    pfad = os.path.join(DATEN, f'zug_{jet.lower().replace("-", "")}_2026-10-10.csv')
    z = [r for r in csv.DictReader(open(pfad)) if r['phase'] == 'zug']
    return np.array([[float(r['t_s']), float(r['kias']), float(r['g']), float(r['alpha'] or 'nan')] for r in z])


def main():
    m = S.lade_modell()
    print('Voller Zug (Modell startet bei KIAS und α des ersten Messpunkts)')
    for jet in S.JETS:
        mess = lade_zug(jet)
        sim = manoever(m, jet, kias0=mess[0, 1], dauer=mess[-1, 0] - mess[0, 0] + 0.1, start_alpha=mess[0, 3],
                       alpha_grenze=35.0 if jet == 'T-18' else None)
        print(f'  {jet}:   t   G mess / Modell   KIAS mess / Modell   α mess / Modell')
        for tm, k, n, a in mess[::2]:
            ts = tm - mess[0, 0]
            print(f'        {ts:4.1f}   {n:4.1f} / {np.interp(ts, sim[:, 0], sim[:, 2]):4.1f}'
                  f'        {k:4.0f} / {np.interp(ts, sim[:, 0], sim[:, 1]):4.0f}'
                  f'        {a:3.0f} / {np.interp(ts, sim[:, 0], sim[:, 3]):3.0f}')
        voll = manoever(m, jet, dauer=8, alpha_grenze=35.0 if jet == 'T-18' else None)
        print(f'        ab 1 G und 450 KIAS: Höchst-G {voll[:, 2].max():.1f} nach {voll[np.argmax(voll[:, 2]), 0]:.1f} s')

    print('\nErster Turn aus 450 KIAS: Kurs nach 4 / 8 s, KIAS nach 8 s (gezählt ab 10 °/s wie im Wiki)')
    def zeile(name, d):
        # ab Drehrate > 10 °/s
        rate = np.gradient(d[:, 4], d[:, 0])
        i0 = np.argmax(rate > 10)
        t0, k0 = d[i0, 0], d[i0, 4]
        f = lambda s: np.interp(t0 + s, d[:, 0], d[:, 4]) - k0
        print(f'  {name:34} {f(4):5.0f}° {f(8):5.0f}°   {np.interp(t0 + 8, d[:, 0], d[:, 1]):4.0f} KIAS')
    for jet in S.JETS:
        zeile(f'{jet} voller Zug', manoever(m, jet, dauer=14))
        if jet == 'T-18':
            zeile('T-18 voller Zug α 35°', manoever(m, jet, dauer=14, alpha_grenze=35.0))
    print('  Wiki (gemessen): T-15 77/146 (~286), T-16 70/141 (~365), T-18 35° 70/127 (~281)')

    print('\nBeschleunigung 300 -> 500 KIAS (1 G, gerade): Modell vs. gemessen 8,4 / 11,5 / 12,3 s')
    for jet in S.JETS:
        d = manoever(m, jet, kias0=300, dauer=20, n_ziel=lambda k: 1.0 + 0 * k, start_alpha=0)
        print(f'  {jet}: {np.interp(500, d[:, 1], d[:, 0]):.1f} s')


if __name__ == '__main__':
    main()
