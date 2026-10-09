"""Punktmassen-Flugmodell, angepasst an die VFM-Ingame-Performance-Analyse (Stand Dez 2025, vor v1.1).

Parameter je Jet: S*CLmax, Mach-Abfall von CLmax, Schub T0, Schub-Lapse, S*CD0, K/S,
Wellenwiderstand B, Mcr. Ausgabe: Daten vs. Modell fuer Instant/Sustained Rate.
Aufruf: python fit.py
"""
import numpy as np
from scipy.optimize import least_squares
g=9.80665; KT=0.514444; LB=4.44822; FT=0.3048
def atm(h_ft):
    h=h_ft*FT; T=288.15-0.0065*h; p=101325*(T/288.15)**5.2559
    return p, p/(287.05*T), np.sqrt(1.4*287.05*T)
def cas2(k,h):
    p,rho,a=atm(h); vc=k*KT
    qc=101325*((1+0.2*(vc/340.294)**2)**3.5-1)
    M=np.sqrt(5*((qc/p+1)**(2/7)-1)); return M, M*a, 0.7*p*M**2, rho
# W = Gewicht lbs (50 %, 100 % Fuel); (Hoehe ft, Fuel %): (Instant °/s, Corner KIAS, Sustained °/s, Best-Sustained KIAS); vmax = KIAS bei 1 G, 10.000 ft
D={'T-15':{'W':(37615,42160),(0,50):(29,337,20,475),(10000,50):(24,360,17,495),(10000,100):(23,385,15,495),(21483,50):(19,383,13,405),'vmax':None},
   'T-16':{'W':(25009,27972),(0,50):(25,392,22,447),(10000,50):(21,409,18,470),(10000,100):(20,434,16,470),(21483,50):(17,436,13,405),'vmax':770},
   'T-18':{'W':(36597,41226),(0,50):(27,365,20,447),(10000,50):(22,385,16,470),(10000,100):(21,409,15,470),(21483,50):(17,426,12,405),'vmax':700}}
conds=[(0,50),(10000,50),(10000,100),(21483,50)]
def model(par,h,W,k):
    SCl,am,T0,lap,SCd,KS,B,Mcr=par
    M,V,q,rho=cas2(k,h); sig=rho/1.225
    Wn=W*LB
    nL=q*SCl*(1-am*M**2)/Wn
    f=1+B*np.clip(M-Mcr,0,None)**2
    T=T0*sig**lap
    ns2=(T-q*SCd*f)*q/KS/Wn**2
    ns=np.sqrt(np.clip(ns2,0,None))
    n_s=np.minimum(np.minimum(ns,nL),9)
    n_i=np.minimum(nL,9)
    w=lambda n: np.degrees(g*np.sqrt(np.clip(n**2-1,0,None))/V)
    return w(n_i), w(n_s), ns
K=np.arange(150,900,1.0)
def feats(par,h,W):
    wi,ws,ns=model(par,h,W,K)
    i=np.argmax(wi); j=np.argmax(ws)
    vm=K[np.where(ns>=1)[0].max()] if (ns>=1).any() else 0
    return wi[i],K[i],ws[j],K[j],vm
def resid(par,d,use):
    r=[]
    for c in use:
        W=d['W'][0 if c[1]==50 else 1]
        wi,ki,ws,ks,vm=feats(par,c[0],W)
        I,KI,S,KSu=d[c]
        r+=[(wi-I)/0.5,(ki-KI)/8,(ws-S)/0.5,(ks-KSu)/15]
    if d['vmax'] and (10000,50) in use:
        r.append((feats(par,10000,d['W'][0])[4]-d['vmax'])/20)
    return np.array(r)
x0=[50,0.3,150e3,0.75,1.0,0.02,30,0.85]
lb=[5,0,20e3,0.4,0.05,1e-4,0,0.7]; ub=[300,0.9,600e3,1.2,10,1,300,1.0]
for name,d in D.items():
    for label,use in [('alle 4 Bedingungen',conds),('Fit nur 10k, Vorhersage 0 ft + 21.5k',[(10000,50),(10000,100)])]:
        best=None
        for s in range(12):
            rng=np.random.default_rng(s); x=np.array(x0)*rng.uniform(.5,1.5,8); x=np.clip(x,lb,ub)
            res=least_squares(resid,x,bounds=(lb,ub),args=(d,use))
            if best is None or res.cost<best.cost: best=res
        print(f'\n{name} | {label}')
        print('  Bedingung      Inst(Daten/Modell)      Sust(Daten/Modell)')
        for c in conds:
            W=d['W'][0 if c[1]==50 else 1]; wi,ki,ws,ks,vm=feats(best.x,c[0],W); I,KI,S,KSu=d[c]
            tag='' if c in use else '  <- Vorhersage'
            print(f'  {c[0]:>5}ft {c[1]:>3}%  {I}@{KI} / {wi:4.1f}@{ki:.0f}    {S}@{KSu} / {ws:4.1f}@{ks:.0f}   vmax {vm:.0f}{tag}')
