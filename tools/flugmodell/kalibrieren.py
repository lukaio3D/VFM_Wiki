"""Kalibriert das Originalmodell (original.py) an den eigenen Messungen -> daten/original_kalibrierung.json.

Aus den Spieldaten kommen Flächen, Profile (Auftrieb und Widerstand über α), Schub über Mach und Dichte,
Massen, Limits und die Dichtekurve. Offen sind nur Faktoren, die im Spielcode stecken. Je Jet:
  KL   Auftrieb      L = KL σ V² SL(α)
  KD   Widerstand    D = KD σ V² SD(α) machDrag(M)
  kB   Dämpfung      a = kB * baseDrag * V (Unity-Rigidbody-Drag, unabhängig von Dichte und Masse)
  kT   Schub         T = kT * Schub aus den Spieldaten (Kontrolle: sollte nahe 1 liegen)
  kS   Widerstandsanstieg jenseits des Auftriebsmaximums (nur T-18, nur er wird dort gemessen; sonst 1)
  δ    HUD-α = Flügel-α + δ (gemeinsam)
Datenquellen wie refit.py: Sustained-Kurven der Diagramme, Beschleunigung, Ausrollen, voller Zug (G über α und
Energieverlust). Danach je Jet das effektive α am Lift-Limit der Diagramme (Instant Turn unterhalb Corner).

Aufruf: python kalibrieren.py
"""
import json

import numpy as np
from scipy.optimize import least_squares

import modell as M
import original as O
import refit as R

G = O.g
DELTA = 2.0          # HUD-α minus Flügel-α, aus dem Lift-Fit über alle Jets (T-15 1,9°, T-18 2,4°)
LEERLAUF = 0.05      # Schubanteil im Leerlauf (minOutput der Spieldaten)


class Modell:
    def __init__(self, jet: O.Jet, atm: O.Atmosphaere, p):
        self.j, self.atm = jet, atm
        self.KL, self.KD, self.kB, self.kT = p[:4]
        self.kS = p[4] if len(p) > 4 else 1.0

    def zustand(self, h_m, V):
        return self.atm.sigma(h_m), V / self.atm.schall(h_m)

    def T(self, s, Mn, alpha, gas=1.0):
        return self.kT * self.j.schub(s, Mn, gas >= 1, alpha) * (1.0 if gas >= 1 else LEERLAUF)

    def L(self, s, V, alpha):
        return self.KL * s * V * V * self.j.SL(alpha)

    def D(self, s, V, alpha, Mn, masse):
        return self.KD * s * V * V * self.j.SD(alpha, self.kS) * self.j.machfaktor(Mn) + self.kB * self.j.base_drag * V * masse

    def alpha_fuer_n(self, n, W, s, V, Mn, amax):
        """α, bei dem L + T sin α = n W (Bisektion bis amax)."""
        lo, hi = np.zeros_like(V), np.full_like(V, amax)
        for _ in range(30):
            a = (lo + hi) / 2
            zu_wenig = self.L(s, V, a) + self.T(s, Mn, a) * np.sin(np.radians(a)) < n * W
            lo, hi = np.where(zu_wenig, a, lo), np.where(zu_wenig, hi, a)
        return (lo + hi) / 2

    def n_sustained(self, h_m, V, W, amax):
        """Größtes n mit T cos α >= D, begrenzt durch amax und 9 G."""
        s, Mn = self.zustand(h_m, V)
        masse = W / G
        lo, hi = np.zeros_like(V), np.full_like(V, amax)
        for _ in range(30):
            a = (lo + hi) / 2
            ok = self.T(s, Mn, a) * np.cos(np.radians(a)) >= self.D(s, V, a, Mn, masse)
            lo, hi = np.where(ok, a, lo), np.where(ok, hi, a)
        n = (self.L(s, V, lo) + self.T(s, Mn, lo) * np.sin(np.radians(lo))) / W
        return np.minimum(n, 9.0)


def daten(jet):
    """Messreihen in SI mit Kräften in kN (refit.py rechnet in N)."""
    d, tab = M.lade()
    r_par = M.fit_r(d)
    H = json.load(open(M.DATEN + '/modell_parameter.json'))['atmosphaere']['H_m']
    atm_alt = M.Atmosphaere(r_par, H)
    tas = lambda h_ft, k: k * O.KT * atm_alt.r(h_ft, k)
    h, k, W, r = M.sus_daten(d, jet, M.HOEHEN)
    sus = (h * O.FT, tas(h, k), W / 1000, r, h, k)
    be = R.beschl_daten(jet, atm_alt)
    au = R.ausroll_daten(jet, atm_alt)
    t, kz, hz, n, al, E, Wz = R.zug_reihe(jet, atm_alt)
    zug = (t, hz * O.FT, tas(hz, kz), n, al - DELTA, E, Wz / 1000)
    inst = M.lade()[0][(jet, 'instant')]
    return dict(sus=sus, be=(be[:, 0] * O.FT, tas(be[:, 0], be[:, 1]), be[:, 2] / 1000, be[:, 3]),
                au=(au[:, 0] * O.FT, tas(au[:, 0], au[:, 1]), au[:, 2] / 1000, au[:, 3]), zug=zug,
                inst=(inst[:, 0] * O.FT, tas(inst[:, 0], inst[:, 1]), inst[:, 2] / 1000, inst[:, 3], inst[:, 4], inst[:, 1]))


def zug_energie(m, zug):
    t, h, V, n, al, E, W = zug
    ts = np.arange(t[0], t[-1] + 1e-9, 0.05)
    Em, Es = E[0], [E[0]]
    for i in range(1, len(ts)):
        tm = ts[i - 1]
        hh, VV, a = np.interp(tm, t, h), np.interp(tm, t, V), np.interp(tm, t, al)
        s, Mn = m.zustand(hh, VV)
        Em += (m.T(s, Mn, a) * np.cos(np.radians(a)) - m.D(s, VV, a, Mn, W / G)) * VV / W * 0.05
        Es.append(Em)
    return np.interp(t, ts, np.array(Es))


def fehler(m, dd, amax):
    h, V, W, r, _, _ = dd['sus']
    n = m.n_sustained(h, V, W, amax)
    e1 = (M.rate(n, V) - r) / 0.5
    hb, Vb, Wb, tdb = dd['be']
    s, Mn = m.zustand(hb, Vb)
    ab = m.alpha_fuer_n(1.0, Wb, s, Vb, Mn, amax)
    e2 = ((m.T(s, Mn, ab) - m.D(s, Vb, ab, Mn, Wb / G)) / Wb - tdb) / 0.04
    ha, Va, Wa, da = dd['au']
    s, Mn = m.zustand(ha, Va)
    aa = m.alpha_fuer_n(1.0, Wa, s, Va, Mn, amax)
    e3 = ((m.D(s, Va, aa, Mn, Wa / G) - m.T(s, Mn, aa, gas=0)) / Wa - da) / 0.03
    t, hz, Vz, nz, alz, E, Wz = dd['zug']
    s, Mn = m.zustand(hz, Vz)
    nm = (m.L(s, Vz, alz) + m.T(s, Mn, alz) * np.sin(np.radians(alz))) / Wz
    e4 = np.log(nm / nz) / 0.04
    e5 = (zug_energie(m, dd['zug']) - E) / 15.0
    return [e1, e2, e3, e4, e5]


def fit(jet, atm, sd):
    j = O.Jet(jet, sd, {'KL': 1, 'KD': 1, 'KB': 1})
    dd = daten(jet)
    amax = j.alpha_lim

    def res(p):
        return np.concatenate([e / np.sqrt(len(e)) for e in fehler(Modell(j, atm, p), dd, amax)])

    x0, lo, hi = [0.009, 0.009, 1.0, 1.0], [1e-4, 1e-4, 0, 0.5], [0.1, 0.1, 5, 1.5]
    if jet == 'T-18':
        x0, lo, hi = x0 + [0.5], lo + [0.0], hi + [1.5]
    sol = least_squares(res, x0, bounds=(lo, hi), loss='soft_l1')
    m = Modell(j, atm, sol.x)
    # Lift-Limit der Diagramme (Instant unterhalb Corner) im Verhältnis zum größten Auftrieb des Modells
    h, V, W, w, corner, kias = dd['inst']
    sel = (kias < corner - 15) & (kias > 150)
    s, Mn = m.zustand(h[sel], V[sel])
    n = np.sqrt((w[sel] * V[sel] / G) ** 2 + 1)
    L_max = m.KL * s * V[sel] ** 2 * j.SL_tab[(j.alpha_tab >= 0) & (j.alpha_tab <= j.alpha_lim2)].max()
    return m, dd, float(np.median(n * W[sel] / L_max))


def bericht(jet, m, dd, a_inst):
    e = fehler(m, dd, m.j.alpha_lim)
    h, V, W, r, hft, kias = dd['sus']
    n = m.n_sustained(h, V, W, m.j.alpha_lim)
    d = M.rate(n, V) - r
    band = (kias >= 300) & (kias <= 550)
    zeilen = [f"{jet}: KL {m.KL:.5f}  KD {m.KD:.5f}  kB {m.kB:.2f}  kT {m.kT:.3f}  kS {m.kS:.2f}  | Lift-Limit der Diagramme = "
              f"{a_inst:.2f} × größter Auftrieb im Flug"]
    for hh in M.HOEHEN:
        s = band & (hft == hh)
        zeilen.append(f"    Sustained {hh:>5} ft, 300–550 KIAS: RMS {np.sqrt(np.mean(d[s] ** 2)):.2f} °/s, max {np.abs(d[s]).max():.2f}")
    zeilen.append(f"    (T-D)/W Beschleunigung RMS {np.sqrt(np.mean((e[1] * 0.04) ** 2)):.3f} | D/W Ausrollen RMS "
                  f"{np.sqrt(np.mean((e[2] * 0.03) ** 2)):.3f} | G im Zug RMS {100 * np.sqrt(np.mean((e[3] * 0.04) ** 2)):.1f} % | "
                  f"Energiehöhe Zug Ende {e[4][-1] * 15:+.0f} m")
    return zeilen


def main():
    sd = O.lade_spieldaten()
    atm = O.Atmosphaere(sd)
    out = {'delta_hud_alpha': DELTA, 'leerlauf': LEERLAUF, 'jets': {}}
    for jet in O.JETS:
        m, dd, a_inst = fit(jet, atm, sd)
        print('\n'.join(bericht(jet, m, dd, a_inst)))
        out['jets'][jet] = {'KL': m.KL, 'KD': m.KD, 'kB': m.kB, 'kT': m.kT, 'kS': m.kS, 'diagramm_lift_faktor': a_inst}
    with open(O.KALIBRIERUNG, 'w') as f:
        json.dump(out, f, indent=1)
    print(f'-> {O.KALIBRIERUNG}')


if __name__ == '__main__':
    main()
