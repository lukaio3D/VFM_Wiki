"""Turnier: jede Strategie gegen jede, für alle Paarungen und Startgeometrien -> ergebnisse/*.npz

Ranked-Start: beide 450 KIAS auf 10.000 ft, Head-on, Merge nach ~5 s, seitlicher Versatz 150 m bzw. 600 m.

Aufruf: python turnier.py [--schnell]
"""
import itertools
import os
import sys
import time
from multiprocessing import Pool
import numpy as np
import sim as S

AUS = os.path.join(S.HIER, 'ergebnisse')
WENDE = (1, -1, 0)
EBENE = (60, 25, 0, -30)
V_ZIEL = (280, 360, 440, 520)
LAG = (0.0, 1.0)
MERGE_AB = (0, 1)
GEOMETRIEN = {'versatz_150m': dict(versatz_m=150.0), 'versatz_600m': dict(versatz_m=600.0)}
PAARUNGEN = [('T-15', 'T-15'), ('T-16', 'T-16'), ('T-18', 'T-18'),
             ('T-15', 'T-16'), ('T-15', 'T-18'), ('T-16', 'T-18')]
BLOCK = 6000


def strategien(jet):
    alphas = (26.0, 35.0) if jet == 'T-18' else (99.0,)
    return [dict(wende=w, ebene=e, v_ziel=v, lag=l, alpha_kampf=a, merge_ab=mab)
            for w, e, v, l, a, mab in itertools.product(WENDE, EBENE, V_ZIEL, LAG, alphas, MERGE_AB)]


def block(args):
    typ_a, typ_b, geo, ia, ib, sa, sb = args
    m = S.lade_modell()
    fa = {k: np.array([sa[i][k] for i in ia]) for k in S.STRATEGIE_FELDER}
    fb = {k: np.array([sb[i][k] for i in ib]) for k in S.STRATEGIE_FELDER}
    r = S.simuliere(m, typ_a, typ_b, fa, fb, GEOMETRIEN[geo])
    r.pop('spur')
    return typ_a, typ_b, geo, ia, ib, r


def main():
    os.makedirs(AUS, exist_ok=True)
    auftraege = []
    for typ_a, typ_b in PAARUNGEN:
        sa, sb = strategien(typ_a), strategien(typ_b)
        paare = np.array(list(itertools.product(range(len(sa)), range(len(sb)))))
        for geo in GEOMETRIEN:
            for k in range(0, len(paare), BLOCK):
                p = paare[k:k + BLOCK]
                auftraege.append((typ_a, typ_b, geo, p[:, 0], p[:, 1], sa, sb))
    print(f'{len(auftraege)} Blöcke', flush=True)
    t0 = time.time()
    felder = ('ergebnis', 't_a', 't_b', 'absturz_a', 'absturz_b', 'offensiv_a', 'offensiv_b', 'min_kias_a', 'min_kias_b')
    ges = {}
    with Pool(max(os.cpu_count() - 1, 1)) as pool:
        for i, (typ_a, typ_b, geo, ia, ib, r) in enumerate(pool.imap_unordered(block, auftraege)):
            key = (typ_a, typ_b)
            na, nb = len(strategien(typ_a)), len(strategien(typ_b))
            if key not in ges:
                ges[key] = {f: np.zeros((na, nb, len(GEOMETRIEN))) for f in felder}
            gi = list(GEOMETRIEN).index(geo)
            for f in felder:
                ges[key][f][ia, ib, gi] = r[f]
            print(f'  {i + 1}/{len(auftraege)} {typ_a} vs {typ_b} {geo}: {time.time() - t0:.0f} s', flush=True)
    for (typ_a, typ_b), d in ges.items():
        np.savez_compressed(os.path.join(AUS, f'{typ_a}_vs_{typ_b}.npz'), geometrien=list(GEOMETRIEN), **d)
    print('fertig', flush=True)


if __name__ == '__main__':
    main()
