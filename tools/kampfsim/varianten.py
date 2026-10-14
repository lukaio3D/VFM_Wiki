"""Empfindlichkeit: Halten die Ergebnisse, wenn die nicht gemessenen Annahmen anders sind?

Je Paarung werden die stärksten Strategien aus dem Haupt-Turnier (Nash-Mischung plus die besten gegen ein
breites Feld) unter geänderten Annahmen erneut gegeneinander gerechnet.

Aufruf: python varianten.py  -> ergebnisse/varianten.md
"""
import itertools
import os
from multiprocessing import Pool
import numpy as np
import sim as S
import turnier as TU
import auswertung as AW

VARIANTEN = {
    'Basis': {},
    'Rollrate × 0,75 (Dämpfungskurve in Knoten gelesen)': {'rollrate_faktor': 0.75},
    'Rollrate × 0,5': {'rollrate_faktor': 0.5},
    'Alle Jets 180 °/s (alte Annahme)': {'rollrate_fest_dps': 180.0},
    'Abschuss erst nach 1,0 s Treffern': {'treffer_s_bis_abschuss': 1.0},
    'Gun-Reichweite 600 m (~2.000 ft)': {'gun_r_max_m': 600.0},
    'T-16 Schub +5 % (Sustained wie im Messflug)': {'schub_T-16': 1.05},
    '50 % Fuel': {'fuel_start': 0.5},
    'T-18 ohne 35° beim Schuss (max. 26°)': {'alpha_max_T-18': 26.0},
}
K = 16


def auswahl(typ_a, typ_b):
    d = AW.lade(typ_a, typ_b)
    P = d['ergebnis'].mean(axis=2)
    v, x, y = AW.nash(P)
    ia = list(dict.fromkeys(list(np.argsort(-x)[:K // 2]) + list(np.argsort(-P.mean(axis=1)))))[:K]
    ib = list(dict.fromkeys(list(np.argsort(-y)[:K // 2]) + list(np.argsort(P.mean(axis=0)))))[:K]
    return ia, ib


def lauf(args):
    typ_a, typ_b, name, ia, ib = args
    sa, sb = TU.strategien(typ_a), TU.strategien(typ_b)
    paare = list(itertools.product(ia, ib))
    m = S.lade_modell()
    erg = []
    for geo in TU.GEOMETRIEN.values():
        fa = {k: np.array([sa[i][k] for i, _ in paare]) for k in S.STRATEGIE_FELDER}
        fb = {k: np.array([sb[j][k] for _, j in paare]) for k in S.STRATEGIE_FELDER}
        erg.append(S.simuliere(m, typ_a, typ_b, fa, fb, geo, aenderung=VARIANTEN[name])['ergebnis'])
    P = np.mean(erg, axis=0).reshape(len(ia), len(ib))
    return typ_a, typ_b, name, ia, ib, P


def main():
    auftraege = []
    for typ_a, typ_b in TU.PAARUNGEN:
        ia, ib = auswahl(typ_a, typ_b)
        for name in VARIANTEN:
            auftraege.append((typ_a, typ_b, name, ia, ib))
    zeilen = ['# Empfindlichkeit der Ergebnisse', '',
              f'Je Paarung die {K} stärksten Strategien je Seite aus dem Haupt-Turnier, neu gerechnet mit geänderten '
              'Annahmen. Wert = Ergebnis bei optimaler Wahl beider (aus Sicht des ersten Jets); dazu die stärkste '
              'Strategie je Seite in der jeweiligen Variante.', '']
    res = {}
    with Pool(max(os.cpu_count() - 1, 1)) as pool:
        for typ_a, typ_b, name, ia, ib, P in pool.imap_unordered(lauf, auftraege):
            res[(typ_a, typ_b, name)] = (ia, ib, P)
            print(typ_a, typ_b, name, flush=True)
    for typ_a, typ_b in TU.PAARUNGEN:
        sa, sb = TU.strategien(typ_a), TU.strategien(typ_b)
        zeilen += [f'## {typ_a} gegen {typ_b}', '', '| Variante | Wert | stärkste A | stärkste B |', '|---|---|---|---|']
        for name in VARIANTEN:
            ia, ib, P = res[(typ_a, typ_b, name)]
            v, x, y = AW.nash(P)
            zeilen.append(f'| {name} | {v:+.2f} | {S.strategie_name(sa[ia[int(np.argmax(x))]], typ_a)} '
                          f'| {S.strategie_name(sb[ib[int(np.argmax(y))]], typ_b)} |')
        zeilen.append('')
    text = '\n'.join(zeilen) + '\n'
    open(os.path.join(TU.AUS, 'varianten.md'), 'w', encoding='utf-8').write(text)
    print(text)


if __name__ == '__main__':
    main()
