"""Neuer Fit von Schub und Widerstand je Jet aus allen Datenquellen -> daten/modell_v2.json.

modell.py trifft nur den Überschuss T - D. Hier werden Schub und Widerstand getrennt bestimmt:
- Diagramme (27 Bedingungen): Ps = 0 bei der Sustained-Rate.
- Beschleunigungsläufe (10.000 ft): T - D bei 1 G.
- Ausrollen im Leerlauf (10.000 ft): D bei 1 G (Annahme Leerlaufschub ≈ 0).
- Voller Zug ab ~450 KIAS: Energiehöhe über die Zeit bei gemessener G -> Widerstand bei hohem CL.

Modell je Jet (SI-Einheiten, L = n W):
  T(h, M)  = T10(M) * (sigma(h) / sigma(10.000 ft))^x          Nachbrenner
  D        = q SCD0(M) + ks(M) L² / q + kx q SCLm(M) max(0, c - CB)²,   c = L / (q SCLm)
  ks(M)    = exp(a0) (1 + a1 (M - 0,5)²)
  T-18 über α 26°: zusätzlich kst q SCLm (α - 26°) / 9°  (Strömungsabriss)
T10 und SCD0 sind glatte Stützstellen-Kurven über Mach. SCLm(M) ist das Lift-Limit der Diagramme (modell.py).
Im Flug erreichbarer Auftrieb in Abhängigkeit von α: c = ca (α - a0) (aus den Zug-Messungen).

Aufruf: python refit.py
"""
import csv
import json
import os
import numpy as np
from scipy.optimize import least_squares
import modell as M

KT, FT, g, LB, RHO0 = M.KT, M.FT, M.g, M.LB, M.RHO0
DATEN = M.DATEN
MK = M.MK
NK = len(MK)
CB = 0.5                     # ab diesem Anteil am Lift-Limit wächst der Zusatzwiderstand
GEWICHT_VOLL = {'T-15': 42160, 'T-16': 26787, 'T-18': 41226}
AB_LBS_PRO_S = {'T-15': 35.0, 'T-16': 16.3, 'T-18': 35.0}
# Nachbrenner-Sekunden vor Ausrollen bzw. Zug (wie zug_ausrollen.py)
AB_SEK = {'T-15': (6, 18), 'T-16': (8, 17), 'T-18': (10, 19)}
# α am Anschlag ohne Override (gemessen); T-18: G-Maximum bei ~26°, Limiter bei 35°
ALPHA_LIM = {'T-15': 24.5, 'T-16': 23.0, 'T-18': 26.0}
ALPHA_MAX = {'T-15': 24.5, 'T-16': 23.0, 'T-18': 35.0}
ALPHA_STALL = 26.0
# Glättung der Stützstellen und Gewichte der Datenquellen (Summe der Quadrate je Quelle)
GLAETTE = 2.0
GEWICHTE = {'diagramm': 10.0, 'beschl': 1.0, 'ausroll': 1.0, 'zug': 1.0}


def basis():
    daten, tab = M.lade()
    r_par = M.fit_r(daten)
    H, scl = M.fit_lift(daten, tab, r_par)
    return daten, tab, M.Atmosphaere(r_par, H), scl, r_par, H


def lade_csv(pfad, keys):
    zeilen = list(csv.DictReader(open(pfad)))
    f = lambda z, k: float(z[k]) if z.get(k) else np.nan
    out = {}
    for z in zeilen:
        out.setdefault(z['phase'], []).append([f(z, k) for k in keys])
    return {k: np.array(v) for k, v in out.items()}


def fuellen(t, x):
    s = ~np.isnan(x)
    return np.interp(t, t[s], x[s])


class Polare:
    """Schub und Widerstand eines Jets aus dem Parametervektor."""
    def __init__(self, p, scl_par, atm):
        self.x, self.a0, self.a1, self.kx, self.kst = p[0], p[1], p[2], p[3], p[4]
        self.lnT = p[5:5 + NK]
        self.lnD = p[5 + NK:5 + 2 * NK]
        self.scl_par, self.atm = scl_par, atm
        self.sig10 = atm.rho(10000) / RHO0

    def schub(self, h, Mach):
        return 1e5 * np.exp(np.interp(Mach, MK, self.lnT)) * (self.atm.rho(h) / RHO0 / self.sig10) ** self.x

    def scd0(self, Mach):
        return np.exp(np.interp(Mach, MK, self.lnD))

    def ks(self, Mach):
        return np.exp(self.a0) * (1 + self.a1 * (Mach - 0.5) ** 2)

    def widerstand(self, q, Mach, L, alpha_ueber=0.0):
        sclm = M.scl(self.scl_par, Mach)
        c = L / (q * sclm)
        return (q * self.scd0(Mach) + self.ks(Mach) * L ** 2 / q
                + self.kx * q * sclm * np.clip(c - CB, 0, None) ** 2
                + self.kst * q * sclm * np.clip(alpha_ueber, 0, None) / 9.0)

    def n_sustained(self, h, k, W):
        """Lastvielfaches mit T = D (ohne Strömungsabriss), begrenzt auf Lift-Limit der Diagramme und 9 G."""
        V, q, Mach = self.atm.zustand(h, k)
        T = self.schub(h, Mach)
        sclm = M.scl(self.scl_par, Mach)
        ks = self.ks(Mach)
        rest = np.clip(T - q * self.scd0(Mach), 0, None)
        L1 = np.sqrt(rest * q / ks)
        # Bereich c > CB: quadratische Gleichung in c
        A = ks * q * sclm ** 2 + self.kx * q * sclm
        B = -2 * self.kx * q * sclm * CB
        C = self.kx * q * sclm * CB ** 2 - rest
        c2 = (-B + np.sqrt(np.clip(B ** 2 - 4 * A * C, 0, None))) / (2 * A)
        L = np.where(L1 <= CB * q * sclm, L1, c2 * q * sclm)
        return np.minimum(np.minimum(L, q * sclm) / W, 9.0), V


def beschl_daten(jet, atm):
    pfad = os.path.join(DATEN, f'messflug_{jet.lower().replace("-", "")}_2026-10-10.csv')
    mess = lade_csv(pfad, ('t_s', 'kias', 'mach', 'hoehe_ft'))
    pts, ab = [], 0.0
    for ph, d in mess.items():
        t, k, h = d[:, 0], d[:, 1], d[:, 3]
        if ph.startswith('lauf'):
            V = k * KT * atm.r(h, k)
            for i in range(3, len(t) - 2):
                dVdt = (V[i + 1] - V[i - 1]) / (t[i + 1] - t[i - 1])
                dhdt = (h[i + 1] - h[i - 1]) * FT / (t[i + 1] - t[i - 1])
                W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * (ab + t[i] - t[0])) * LB
                pts.append((h[i], k[i], W, (dVdt * V[i] / g + dhdt) / V[i]))
        ab += t[-1] - t[0]
    return np.array(pts)


def zug_daten(jet):
    pfad = os.path.join(DATEN, f'zug_{jet.lower().replace("-", "")}_2026-10-10.csv')
    return lade_csv(pfad, ('t_s', 'kias', 'mach', 'hoehe_ft', 'g', 'rate_dps', 'alpha'))


def ausroll_daten(jet, atm):
    d = zug_daten(jet)['ausrollen']
    t, k, h = d[:, 0], d[:, 1], fuellen(d[:, 0], d[:, 3])
    W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * AB_SEK[jet][0]) * LB
    V = k * KT * atm.r(h, k)
    pts = []
    for i in range(1, len(t) - 1, 2):
        dVdt = (V[i + 1] - V[i - 1]) / (t[i + 1] - t[i - 1])
        dhdt = (h[i + 1] - h[i - 1]) * FT / (t[i + 1] - t[i - 1])
        pts.append((h[i], k[i], W, -(dVdt * V[i] / g + dhdt) / V[i]))
    return np.array(pts)


def zug_reihe(jet, atm):
    """Voller Zug: Zeit, KIAS, Höhe, G, α, Energiehöhe [m]."""
    d = zug_daten(jet)['zug']
    t = d[:, 0]
    k, h = d[:, 1], fuellen(t, d[:, 3])
    n, al = fuellen(t, d[:, 4]), fuellen(t, d[:, 6])
    V = k * KT * atm.r(h, k)
    E = h * FT + V ** 2 / (2 * g)
    W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * AB_SEK[jet][1]) * LB
    return t, k, h, n, al, E, W


def zug_energie(pol, reihe, atm, ueber=0.0):
    """Energiehöhe über die Zeit mit gemessener G (Integration in 0,05-s-Schritten) und gemessener Speed als Startwert."""
    t, k, h, n, al, E, W = reihe
    ts = np.arange(t[0], t[-1] + 1e-9, 0.05)
    Em, Es = E[0], [E[0]]
    for i in range(1, len(ts)):
        tm = ts[i - 1]
        kk, hh = np.interp(tm, t, k), np.interp(tm, t, h)
        V, q, Mach = atm.zustand(hh, kk)
        L = np.interp(tm, t, n) * W
        a_ue = np.interp(tm, t, al) - ALPHA_STALL if ueber else 0.0
        Em += (pol.schub(hh, Mach) - pol.widerstand(q, Mach, L, a_ue)) * V / W * 0.05
        Es.append(Em)
    return np.interp(t, ts, np.array(Es))


def fit_jet(jet, daten, atm, scl_par, kx_fest=None):
    sus = M.sus_daten(daten, jet, M.HOEHEN)
    be = beschl_daten(jet, atm)
    au = ausroll_daten(jet, atm)
    reihe = zug_reihe(jet, atm)
    ueber = jet == 'T-18'

    def polare(p):
        if kx_fest is not None:
            p = p.copy(); p[3] = kx_fest
        return Polare(p, scl_par, atm)

    def res(p):
        pol = polare(p)
        h, k, W, r = sus
        n, V = pol.n_sustained(h, k, W)
        e1 = (M.rate(n, V) - r) / 0.5
        hb, kb, Wb, tdb = be.T
        Vb, qb, Mb = atm.zustand(hb, kb)
        e2 = ((pol.schub(hb, Mb) - pol.widerstand(qb, Mb, Wb)) / Wb - tdb) / 0.04
        ha, ka, Wa, da = au.T
        Va, qa, Ma = atm.zustand(ha, ka)
        e3 = (pol.widerstand(qa, Ma, Wa) / Wa - da) / 0.03
        e4 = (zug_energie(pol, reihe, atm, ueber) - reihe[5]) / 15.0
        krumm = np.concatenate([np.diff(p[5:5 + NK], 2), np.diff(p[5 + NK:], 2)]) * GLAETTE
        teile = [(e1, 'diagramm'), (e2, 'beschl'), (e3, 'ausroll'), (e4, 'zug')]
        return np.concatenate([e * np.sqrt(GEWICHTE[w] / len(e)) for e, w in teile] + [krumm])

    W0 = GEWICHT_VOLL[jet] * LB
    x0 = np.concatenate([[0.8, np.log(2e-3), 0.0, 0.5, 0.5],
                         np.log(np.full(NK, 1.3 * W0 / 1e5)), np.log(np.full(NK, 1.5))])
    lb = np.concatenate([[0.2, np.log(2e-4), -3, 0.0, 0.0], np.full(2 * NK, -8)])
    ub = np.concatenate([[1.6, np.log(2e-2), 8, 20.0, 20.0], np.full(2 * NK, 8)])
    if not ueber:
        x0[4], lb[4], ub[4] = 0.0, 0.0, 1e-9
    sol = least_squares(res, x0, bounds=(lb, ub), loss='soft_l1', f_scale=1.0)
    p = sol.x.copy()
    if kx_fest is not None:
        p[3] = kx_fest
    return p


def lift_alpha(jet, atm, scl_par):
    """c = L / (q SCLm) über α aus dem vollen Zug (nur α bis 26°), linear: c = ca (α - a0)."""
    t, k, h, n, al, E, W = zug_reihe(jet, atm)
    V, q, Mach = atm.zustand(h, k)
    c = n * W / (q * M.scl(scl_par, Mach))
    s = al <= ALPHA_STALL
    ca, b = np.polyfit(al[s], c[s], 1)
    out = {'ca': float(ca), 'a0': float(-b / ca)}
    if jet == 'T-18':   # Anteil am Lift-Limit bei 35°
        out['c35'] = float(np.mean(c[al >= 34]))
    return out, (al, c)


def pruefe(jet, pol, atm, scl_par):
    """Abnahmetests aus tools/simulator/KONZEPT.md, gerechnet mit dem neuen Modell."""
    out = {}
    # 1. Beschleunigung 300 -> 500 KIAS, 10.000 ft, 1 G, voller Tank
    W = GEWICHT_VOLL[jet] * LB
    k, t = 300.0, 0.0
    while k < 500:
        V, q, Mach = atm.zustand(10000, k)
        a = (pol.schub(10000, Mach) - pol.widerstand(q, Mach, W)) / W * g
        V2 = V + a * 0.05
        k = V2 / (KT * atm.r(10000, k))
        t += 0.05
        W -= AB_LBS_PRO_S[jet] * LB * 0.05
    out['beschl_300_500_s'] = round(t, 1)
    # 2. Ausrollen 550 -> 350 KIAS im Leerlauf
    W = (GEWICHT_VOLL[jet] - AB_LBS_PRO_S[jet] * AB_SEK[jet][0]) * LB
    k, t = 550.0, 0.0
    while k > 350:
        V, q, Mach = atm.zustand(10000, k)
        V2 = V - pol.widerstand(q, Mach, W) / W * g * 0.05
        k = V2 / (KT * atm.r(10000, k))
        t += 0.05
    out['ausroll_550_350_s'] = round(t, 1)
    # 3. Sustained bei 450 KIAS
    n, V = pol.n_sustained(10000.0, 450.0, (GEWICHT_VOLL[jet] - 600) * LB)
    out['sustained_450'] = (round(float(n), 2), round(float(M.rate(n, V)), 1))
    return out


def main():
    daten, tab, atm, scl, r_par, H = basis()
    erg = {'atmosphaere': {'H_m': H, 'r': {str(h): r_par[h] for h in M.HOEHEN}}, 'mach_stuetz': MK.tolist(),
           'cb': CB, 'alpha_stall': ALPHA_STALL, 'jets': {}}
    pars, pols = {}, {}
    for jet in ['T-15', 'T-16', 'T-18']:
        kx = None
        if jet == 'T-18':   # kx aus T-15/T-16 übernommen, Zug der T-18 ist überzogen (α bis 35°)
            kx = float(np.mean([pars['T-15'][3], pars['T-16'][3]]))
        p = fit_jet(jet, daten, atm, scl[jet], kx)
        pars[jet] = p
        pol = Polare(p, scl[jet], atm)
        pols[jet] = pol
        la, _ = lift_alpha(jet, atm, scl[jet])
        erg['jets'][jet] = {
            'SCLmax_m2': scl[jet], 'x': p[0], 'a0': p[1], 'a1': p[2], 'kx': p[3], 'kst': p[4],
            'ln_T10': p[5:5 + NK].tolist(), 'ln_SCD0': p[5 + NK:].tolist(),
            'lift_alpha': la, 'alpha_lim': ALPHA_LIM[jet], 'alpha_max': ALPHA_MAX[jet],
            'gewicht_voll_lbs': GEWICHT_VOLL[jet], 'ab_lbs_pro_s': AB_LBS_PRO_S[jet]}

        # Bericht
        h, k, W, r = M.sus_daten(daten, jet, M.HOEHEN)
        n, V = pol.n_sustained(h, k, W)
        e = M.rate(n, V) - r
        band = (k >= 300) & (k <= 550)
        print(f'\n{jet}: x={p[0]:.2f}  ks={np.exp(p[1]):.2e} (1{p[2]:+.2f}(M-0,5)²)  kx={p[3]:.2f}  kst={p[4]:.2f}')
        for hh in M.HOEHEN:
            s = band & (h == hh)
            print(f'  Diagramm {hh:>5} ft, 300–550 KIAS: RMS {np.sqrt(np.mean(e[s] ** 2)):.2f} °/s, '
                  f'max {np.max(np.abs(e[s])):.2f}')
        be = beschl_daten(jet, atm)
        Vb, qb, Mb = atm.zustand(be[:, 0], be[:, 1])
        tdm = (pol.schub(be[:, 0], Mb) - pol.widerstand(qb, Mb, be[:, 2])) / be[:, 2]
        print(f'  (T-D)/W Beschleunigung: RMS {np.sqrt(np.mean((tdm - be[:, 3]) ** 2)):.3f} '
              f'(Mittel gemessen {np.mean(be[:, 3]):.2f})')
        au = ausroll_daten(jet, atm)
        Va, qa, Ma = atm.zustand(au[:, 0], au[:, 1])
        dm = pol.widerstand(qa, Ma, au[:, 2]) / au[:, 2]
        print(f'  D/W Ausrollen: RMS {np.sqrt(np.mean((dm - au[:, 3]) ** 2)):.3f} (gemessen {au[:, 3].min():.2f}–{au[:, 3].max():.2f})')
        reihe = zug_reihe(jet, atm)
        Ez = zug_energie(pol, reihe, atm, jet == 'T-18')
        print(f'  Zug: Energiehöhe Ende gemessen {reihe[5][-1] - reihe[5][0]:+.0f} m, Modell {Ez[-1] - reihe[5][0]:+.0f} m')
        for M_ in (0.5, 0.7, 0.8, 0.9, 1.0, 1.2):
            q = 0.5 * atm.rho(10000) * (M_ * M.schall(10000)) ** 2
            W0 = GEWICHT_VOLL[jet] * LB
            print(f'    M {M_:.1f}: T/W {pol.schub(10000, M_) / W0:.2f}  D0/W {q * pol.scd0(M_) / W0:.2f}')
        print(f'  lift(α): {la}')
        print(f'  Abnahme: {pruefe(jet, pol, atm, scl[jet])}')
    with open(os.path.join(DATEN, 'modell_v2.json'), 'w') as f:
        json.dump(erg, f, indent=1, default=float)
    kontrollplot(daten, atm, scl, pols)


def kontrollplot(daten, atm, scl, pols):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(3, 4, figsize=(19, 11))
    for i, jet in enumerate(['T-15', 'T-16', 'T-18']):
        pol = pols[jet]
        for j, hh in enumerate(M.HOEHEN):
            a = ax[i, j]
            h, k, W, r = M.sus_daten(daten, jet, [hh])
            for c, Wu in enumerate(np.unique(W)):
                s = W == Wu
                a.plot(k[s], r[s], '.', ms=2, color=f'C{c}')
                kk = np.arange(180, k.max() + 1, 2.0)
                n, V = pol.n_sustained(hh + 0 * kk, kk, Wu + 0 * kk)
                a.plot(kk, M.rate(n, V), 'k-', lw=0.7)
            a.set_title(f'{jet} {hh} ft (Punkte Diagramm, Linie Modell v2)', fontsize=9)
            a.set_ylim(0, 26); a.grid(alpha=0.3)
        a = ax[i, 3]
        t, k, h, n, al, E, W = reihe = zug_reihe(jet, atm)
        a.plot(t - t[0], E - E[0], 'o', label='Energiehöhe gemessen [m]')
        a.plot(t - t[0], zug_energie(pol, reihe, atm, jet == 'T-18') - E[0], '-', label='Modell v2')
        a.set_title(f'{jet} voller Zug ab ~450 KIAS', fontsize=9); a.grid(alpha=0.3); a.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(DATEN, 'kontrolle', 'modell_v2_fit.png'), dpi=75)


if __name__ == '__main__':
    main()
