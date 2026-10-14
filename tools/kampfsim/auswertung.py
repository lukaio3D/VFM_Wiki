"""Wertet das Turnier aus: Spielwert, beste Strategien (Nash), Wirkung einzelner Entscheidungen.

Für jede Paarung ist die Auszahlung aus Sicht von A: +1 Abschuss durch A, -1 durch B, 0 offen nach 150 s
(Absturz zählt als Abschuss für den Gegner), gemittelt über die Startgeometrien (der Pilot kennt den Versatz
vorher nicht). Das Nash-Gleichgewicht des Nullsummenspiels zeigt, welche Mischung aus Strategien gegen jeden
Gegner am besten abschneidet; der Spielwert ist das Ergebnis, wenn beide optimal wählen.

Aufruf: python auswertung.py  -> ergebnisse/bericht.md
"""
import os
import numpy as np
from scipy.optimize import linprog
import sim as S
import turnier as TU

AUS = TU.AUS


def nash(P):
    """Zeilenspieler maximiert. Rückgabe Wert, Mischung Zeile, Mischung Spalte."""
    def loese(A):
        n, k = A.shape
        c = np.zeros(n + 1); c[-1] = -1
        A_ub = np.hstack([-A.T, np.ones((k, 1))])
        res = linprog(c, A_ub=A_ub, b_ub=np.zeros(k), A_eq=[np.r_[np.ones(n), 0]], b_eq=[1],
                      bounds=[(0, None)] * n + [(None, None)], method='highs')
        return res.x[-1], res.x[:n]
    v, x = loese(P)
    _, y = loese(-P.T)
    return v, x, y


def zeitwertung(d):
    """Offene Kämpfe wie im Ranked nach Zeit: wer deutlich länger offensiv war (> 10 s), bekommt ±0,5."""
    diff = d['offensiv_a'] - d['offensiv_b']
    return np.where(d['ergebnis'] != 0, d['ergebnis'], 0.5 * np.sign(diff) * (np.abs(diff) > 10))


def lade(typ_a, typ_b):
    d = np.load(os.path.join(AUS, f'{typ_a}_vs_{typ_b}.npz'))
    return {k: d[k] for k in d.files}


def beschreibe(s, jet):
    return S.strategie_name(s, jet)


def marginal(strats, werte, feld):
    out = {}
    for s, w in zip(strats, werte):
        out.setdefault(s[feld], []).append(w)
    return {k: float(np.mean(v)) for k, v in out.items()}


FELD_NAMEN = {'wende': ('Drehrichtung am Merge', {1: 'hin', -1: 'weg (One-Circle)', 0: 'durch (Extend)'}),
              'ebene': ('Ebene', {60: 'steil hoch', 25: 'hoch', 0: 'flach', -30: 'tief'}),
              'v_ziel': ('Ziel-Speed', {v: f'{v} KIAS' for v in TU.V_ZIEL}),
              'lag': ('Verfolgung', {0.0: 'Pure', 1.0: 'Lag'}),
              'alpha_kampf': ('α beim Kurven', {26.0: '26°', 35.0: '35°', 99.0: '–'})}


def bericht():
    zeilen = ['# Kampfsimulation: Ergebnisse', '',
              'Erzeugt von `auswertung.py`. Auszahlung aus Sicht des ersten Jets: +1 Abschuss, −1 abgeschossen, '
              '0 offen nach 150 s; Mittel über beide Startgeometrien.', '']
    gesamt = {}
    for typ_a, typ_b in TU.PAARUNGEN:
        d = lade(typ_a, typ_b)
        sa, sb = TU.strategien(typ_a), TU.strategien(typ_b)
        P = d['ergebnis'].mean(axis=2)
        v, x, y = nash(P)
        v_zeit = nash(zeitwertung(d).mean(axis=2))[0]
        gesamt[(typ_a, typ_b)] = (v, v_zeit)
        zeilen += [f'## {typ_a} gegen {typ_b}', '',
                   f'Spielwert (beide optimal): **{v:+.2f}**, mit Zeitwertung {v_zeit:+.2f} · Anteil Kämpfe mit Abschuss: '
                   f'{np.mean(d["ergebnis"] != 0) * 100:.0f} % · Abstürze A/B: {d["absturz_a"].mean() * 100:.1f} / '
                   f'{d["absturz_b"].mean() * 100:.1f} %', '']
        for wer, strats, mix, Pm, jet in (('A', sa, x, P, typ_a), ('B', sb, y, -P.T, typ_b)):
            gegen_nash = Pm @ (y if wer == 'A' else x)
            gegen_alle = Pm.mean(axis=1)
            zeilen.append(f'**{jet} ({wer})**: optimale Mischung')
            for i in np.argsort(-mix)[:6]:
                if mix[i] < 0.02:
                    break
                zeilen.append(f'- {mix[i] * 100:3.0f} % {beschreibe(strats[i], jet)} '
                              f'(gegen alle: {gegen_alle[i]:+.2f})')
            beste = np.argsort(-gegen_alle)[:5]
            zeilen.append(f'- beste gegen ein breites Feld: ' + '; '.join(
                f'{beschreibe(strats[i], jet)} ({gegen_alle[i]:+.2f})' for i in beste))
            for feld, (name, namen) in FELD_NAMEN.items():
                mg = marginal(strats, gegen_alle, feld)
                if len(mg) > 1:
                    zeilen.append(f'- {name}: ' + ', '.join(f'{namen.get(k, k)} {w:+.2f}' for k, w in
                                                            sorted(mg.items(), key=lambda kv: -kv[1])))
            zeilen.append('')
    zeilen += ['## Übersicht Spielwerte', '', '| Paarung | Wert für den ersten Jet | mit Zeitwertung |', '|---|---|---|']
    zeilen += [f'| {a} gegen {b} | {v:+.2f} | {vz:+.2f} |' for (a, b), (v, vz) in gesamt.items()]
    text = '\n'.join(zeilen) + '\n'
    open(os.path.join(AUS, 'bericht.md'), 'w', encoding='utf-8').write(text)
    print(text)


if __name__ == '__main__':
    bericht()
