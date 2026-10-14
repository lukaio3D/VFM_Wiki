"""Einzelnen Kampf simulieren und als Bild zeigen: Draufsicht, Höhe, Speed, G.

Aufruf: python zeige.py T-15 "hin/flach/320/Pure" T-16 "hin/tief/480/Lag" [versatz_m] [datei.png]
Strategie-Kurzform: wende/ebene/v_ziel/verfolgung[/alpha][/ab]  (wende: hin|weg|durch; ebene: steilhoch|hoch|flach|tief)
"""
import sys
import numpy as np
import sim as S

WENDE = {'hin': 1, 'weg': -1, 'durch': 0}
EBENE = {'steilhoch': 60, 'hoch': 25, 'flach': 0, 'tief': -30}


def parse(txt):
    t = txt.split('/')
    return dict(wende=WENDE[t[0]], ebene=EBENE[t[1]], v_ziel=float(t[2]), lag=1.0 if t[3].lower() == 'lag' else 0.0,
                alpha_kampf=float(t[4]) if len(t) > 4 and t[4] != 'ab' else 26.0, merge_ab=float(t[-1] == 'ab'))


def kampf(typ_a, sa, typ_b, sb, versatz_m=S.RANKED['versatz_m'], t_max=S.RUNDENZEIT_S):
    m = S.lade_modell()
    fa = {k: np.array([sa[k]]) for k in S.STRATEGIE_FELDER}
    fb = {k: np.array([sb[k]]) for k in S.STRATEGIE_FELDER}
    return S.simuliere(m, typ_a, typ_b, fa, fb, dict(versatz_m=versatz_m), t_max=t_max, spur_alle=0.2)


def bild(r, typ_a, sa, typ_b, sb, datei):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    sp = r['spur']
    t = np.array([s['t'] for s in sp])
    P = np.array([s['P'] for s in sp]) / S.FT
    k = np.array([s['kias'] for s in sp])
    n = np.array([s['n'] for s in sp])
    gun = np.array([s['gun'] for s in sp])
    tr = np.array([s['treffer'] for s in sp])
    fig, ax = plt.subplots(2, 2, figsize=(13, 10))
    farben = ('C0', 'C3')
    namen = (f'{typ_a} {S.strategie_name(sa, typ_a)}', f'{typ_b} {S.strategie_name(sb, typ_b)}')
    for j in (0, 1):
        ax[0, 0].plot(P[:, j, 0], P[:, j, 1], color=farben[j], lw=1, label=namen[j])
        for ti in range(0, len(t), 25):
            ax[0, 0].annotate(f'{t[ti]:.0f}', P[ti, j, :2], fontsize=6, color=farben[j])
        sch = gun[:, j]
        ax[0, 0].plot(P[sch, j, 0], P[sch, j, 1], '.', ms=3, color=farben[j])
        ax[0, 1].plot(t, P[:, j, 2], color=farben[j])
        ax[1, 0].plot(t, k[:, j], color=farben[j])
        ax[1, 1].plot(t, n[:, j], color=farben[j], lw=0.8)
        ax[1, 1].plot(t, tr[:, j] * 10, '--', color=farben[j], lw=0.8)
    ax[0, 0].set_aspect('equal'); ax[0, 0].legend(fontsize=8); ax[0, 0].set_title('Draufsicht [ft], Zahlen = Sekunden, Punkte = Gun-Modus')
    ax[0, 1].set_title('Höhe [ft]'); ax[1, 0].set_title('KIAS'); ax[1, 1].set_title('G (durchgezogen), Trefferzeit x10 s (gestrichelt)')
    erg = {1: f'{typ_a} gewinnt', -1: f'{typ_b} gewinnt', 0: 'offen'}[int(r['ergebnis'][0])]
    fig.suptitle(f'{erg} (t = {min(r["t_a"][0], r["t_b"][0]):.1f} s)')
    for a in ax.flat:
        a.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(datei, dpi=70)


if __name__ == '__main__':
    typ_a, sa, typ_b, sb = sys.argv[1], parse(sys.argv[2]), sys.argv[3], parse(sys.argv[4])
    vers = float(sys.argv[5]) if len(sys.argv) > 5 else S.RANKED['versatz_m']
    datei = sys.argv[6] if len(sys.argv) > 6 else 'kampf.png'
    r = kampf(typ_a, sa, typ_b, sb, vers)
    print({k: v[0] for k, v in r.items() if k != 'spur'})
    bild(r, typ_a, sa, typ_b, sb, datei)
