"""Beispielkämpfe für das Wiki: je Paarung die stärkste reine Strategie beider Seiten (Nash-Mischung)
-> docs/public/images/sim/<a>_vs_<b>.png

Aufruf: python bilder.py
"""
import os
import numpy as np
import auswertung as AW
import turnier as TU
import zeige as Z

ZIEL = os.path.join(Z.S.HIER, '..', '..', 'docs', 'public', 'images', 'sim')


def main():
    os.makedirs(ZIEL, exist_ok=True)
    for typ_a, typ_b in TU.PAARUNGEN:
        if typ_a == typ_b:
            continue
        d = AW.lade(typ_a, typ_b)
        v, x, y = AW.nash(d['ergebnis'].mean(axis=2))
        sa, sb = TU.strategien(typ_a)[int(np.argmax(x))], TU.strategien(typ_b)[int(np.argmax(y))]
        r = Z.kampf(typ_a, sa, typ_b, sb, 150.0)
        datei = os.path.join(ZIEL, f'{typ_a.lower().replace("-", "")}_vs_{typ_b.lower().replace("-", "")}.png')
        Z.bild(r, typ_a, sa, typ_b, sb, datei)
        print(datei, r['ergebnis'][0])


if __name__ == '__main__':
    main()
