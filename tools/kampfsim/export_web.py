"""Exportiert Flugmodell und Annahmen für den 3D-Simulator (app/)
-> app/public/data/modell.json

Aufruf: python export_web.py
"""
import json
import os
import sim as S

ZIEL = os.path.join(S.HIER, '..', '..', 'app', 'public', 'data')


def modell():
    m = S.lade_modell()
    atm = S.Atmo(m)
    fl = S.Flotte(m, S.JETS)
    jets = {}
    for i, t in enumerate(S.JETS):
        jets[t] = dict(scl=fl.scl[i].tolist(), x=fl.x[i], a0=fl.a0[i], a1=fl.a1[i], kx=fl.kx[i], kst=fl.kst[i],
                       lnT=fl.lnT[i].tolist(), lnD=fl.lnD[i].tolist(), alpha_lim=fl.alpha_lim[i],
                       alpha_max=fl.alpha_max[i], c_lim=fl.c_lim[i], alpha0=fl.alpha0[i], c35=fl.c35[i],
                       stall=bool(fl.stall[i]), W_voll=fl.W_voll[i], W_leer=fl.W_leer[i], burn=fl.burn[i],
                       alpha_rate=fl.alpha_rate[i])
    return dict(atm=dict(H=atm.H, la=atm.la.tolist(), hs=atm.hs.tolist(), b=atm.b.tolist()),
                MK=fl.MK.tolist(), cb=fl.cb, a_stall=fl.a_stall, sig10=fl.sig10, annahmen=S.ANNAHMEN, jets=jets)


def main():
    os.makedirs(ZIEL, exist_ok=True)
    json.dump(modell(), open(os.path.join(ZIEL, 'modell.json'), 'w'), default=float)
    print('ok')


if __name__ == '__main__':
    main()
