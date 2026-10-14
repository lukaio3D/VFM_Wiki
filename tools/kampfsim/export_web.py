"""Exportiert Flugmodell (Originalkurven, kalibriert) und Annahmen für den 3D-Simulator (app/)
-> app/public/data/modell.json

Aufruf: python export_web.py
"""
import json
import os
import sim as S

ZIEL = os.path.join(S.HIER, '..', '..', 'app', 'public', 'data')


def modell():
    """Modelltabellen (flugmodell/export_original.py) plus Annahmen und α-Anstieg des Simulators."""
    m = S.lade_modell()
    for t, j in m['jets'].items():
        j['alpha_rate'] = S.ALPHA_RATE_AUF[t]
    m['annahmen'] = S.ANNAHMEN
    return m


def main():
    os.makedirs(ZIEL, exist_ok=True)
    json.dump(modell(), open(os.path.join(ZIEL, 'modell.json'), 'w'), default=float)
    print('ok')


if __name__ == '__main__':
    main()
