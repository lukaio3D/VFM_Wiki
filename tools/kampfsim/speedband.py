"""T-16 (und T-15): welche Kampf-Speed ist bei welchem Fuel-Stand am besten?

Eigene Strategien mit feinem Speed-Raster gegen die stärksten Gegner-Strategien aus dem Haupt-Turnier
(Nash-Mischung, gewichtet). Gleicher Fuel-Stand für beide.
Aufruf: python speedband.py T-16
"""
import itertools
import sys
from multiprocessing import Pool
import numpy as np
import sim as S
import turnier as TU
import auswertung as AW

V_FEIN = (360, 380, 400, 420, 440, 460, 480, 500)
FUEL = (1.0, 0.5, 0.15)


def eigene(jet):
    return [dict(wende=w, ebene=e, v_ziel=v, lag=l, alpha_kampf=99.0 if jet != 'T-18' else 26.0, merge_ab=m)
            for w, e, v, l, m in itertools.product((1, -1), (0, -30), V_FEIN, (0.0, 1.0), (0, 1))]


def gegner(jet, gegen):
    a, b = (jet, gegen) if (jet, gegen) in TU.PAARUNGEN else (gegen, jet)
    d = AW.lade(a, b)
    v, x, y = AW.nash(d['ergebnis'].mean(axis=2))
    mix = y if a == jet else x
    st = TU.strategien(gegen)
    i = np.argsort(-mix)[:20]
    w = mix[i] / mix[i].sum()
    return [st[k] for k in i], w


def lauf(args):
    jet, gegen, fuel = args
    eig = eigene(jet)
    geg, w = gegner(jet, gegen)
    paare = list(itertools.product(range(len(eig)), range(len(geg))))
    m = S.lade_modell()
    E, K = [], []
    for geo in TU.GEOMETRIEN.values():
        fa = {k: np.array([eig[i][k] for i, _ in paare]) for k in S.STRATEGIE_FELDER}
        fb = {k: np.array([geg[j][k] for _, j in paare]) for k in S.STRATEGIE_FELDER}
        r = S.simuliere(m, jet, gegen, fa, fb, geo, aenderung={'fuel_start': fuel})
        E.append(r['ergebnis']); K.append(r['kias_a'])
    E = np.mean(E, 0).reshape(len(eig), len(geg)) @ w
    K = np.mean(K, 0).reshape(len(eig), len(geg)) @ w
    return jet, gegen, fuel, eig, E, K


def main(jet):
    auftraege = [(jet, g, f) for g in S.JETS for f in FUEL]
    with Pool() as pool:
        res = pool.map(lauf, auftraege)
    for jet, gegen, fuel, eig, E, K in res:
        print(f'\n{jet} gegen {gegen}, {int(fuel * 100)} % Fuel: Ergebnis je Ziel-Speed (Mittel über die Strategie-Varianten; '
              f'beste Variante) und tatsächlich geflogene Ø KIAS im Kampf')
        for v in V_FEIN:
            I = [i for i, s in enumerate(eig) if s['v_ziel'] == v]
            b = I[int(np.argmax(E[I]))]
            print(f'   Ziel {v}: Ø {np.mean(E[I]):+.2f}  beste {E[b]:+.2f} ({S.strategie_name(eig[b], jet)}, Ø {K[b]:.0f} KIAS)')


if __name__ == '__main__':
    main(sys.argv[1])
