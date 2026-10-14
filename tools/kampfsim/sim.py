"""Vektorisierter 1v1-Kampfsimulator für die VFM-Jets (Punktmasse, 3D).

Viele Kämpfe laufen gleichzeitig als Arrays. Jet i kämpft gegen Jet (i + N) mod 2N.
Flugmodell aus tools/flugmodell/daten/modell_original.json (export_original.py): Auftrieb, Widerstand und Schub aus
den Originalkurven des Spiels über α, Mach und Dichte, kalibriert an den eigenen Messungen (kalibrieren.py),
Dichte über der Höhe aus dem Spiel, G-Limit 9.
Dynamik: α folgt dem Kommando mit Verzögerung (G-Aufbau wie gemessen), Lift Vector mit begrenzter Rollrate.
α ist das HUD-α. Schub wirkt entlang der Rumpfachse (T cos α gegen D, T sin α zum Auftrieb).

Annahmen, die nicht gemessen sind, stehen in ANNAHMEN.
Einheiten intern SI (m, m/s, N); Ein- und Ausgabe in ft, KIAS, Grad.
"""
import json
import os
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
MODELL = os.path.join(HIER, '..', 'flugmodell', 'daten', 'modell_original.json')
g, KT, LB, FT, RHO0 = 9.80665, 0.514444, 4.44822, 0.3048, 1.225
UP = np.array([0.0, 0.0, 1.0])

ANNAHMEN = {
    'rollrate_faktor': 1.0,       # Anteil der Spieldaten-Rollrate (325 / 420 / 420 °/s, gedämpft über IAS); nicht gemessen
    'rollrate_fest_dps': 0.0,     # > 0: alle Jets mit dieser festen Rollrate (alte Annahme 180 °/s, für Vergleiche)
    'alpha_tau_s': 0.5,           # α-Verzögerung, mit alpha_rate so gewählt, dass der G-Aufbau zum vollen Zug passt
    'alpha_rate_ab_dps': 25.0,    # Entlasten
    'geschoss_mps': 1030.0,       # Mündungsgeschwindigkeit der Kanone (Spieldaten, in Replays bestätigt)
    'gun_r_min_m': 150.0,
    'gun_r_max_m': 900.0,         # ~3.000 ft
    'ziel_radius_m': 6.0,         # halbe Spannweite als Trefferfenster
    'gun_streuung_deg': 0.3,
    'treffer_s_bis_abschuss': 0.5,
    'fuel_start': 1.0,            # 100 % Fuel
}
# Ranked-Start, gemessen in 71 eigenen 1v1-Replays (alle gleich, Ranked und Casual): 10.000 ft, Mach 0,75
# (246 m/s, im HUD ~427 KIAS), Head-on, 4.000 m Abstand (Merge nach ~8 s), 400 m seitlicher Versatz.
# Voller Tank (keine Fuel-Option in der Lobby, startingFuel = maxFuel). Rundenzeit 8 min.
RANKED = dict(mach=0.75, hoehe_ft=10000.0, abstand_m=4000.0, versatz_m=400.0)
RUNDENZEIT_S = 480.0
# Anstieg des α-Kommandos [°/s], abgestimmt auf die gemessenen G-Verläufe im vollen Zug (siehe kalibrierung.py)
ALPHA_RATE_AUF = {'T-15': 9.0, 'T-16': 6.5, 'T-18': 7.5}
JETS = ['T-15', 'T-16', 'T-18']


def lade_modell(pfad=MODELL):
    return json.load(open(pfad))


class Atmo:
    """Dichte aus der Spielkurve; KIAS <-> wahre Fahrt wie gemessen (9G-Linie der Diagramme)."""
    def __init__(self, m):
        a = m['atmosphaere']
        self.h_tab, self.sigma_tab = np.array(a['h_m']), np.array(a['sigma'])
        hs = np.array([0.0, 10000.0, 20190.0])
        ra = np.array([a['r'][k][0] for k in ('0', '10000', '20190')])
        self.la = np.polyfit(hs, np.log(ra), 2)
        self.hs, self.b = hs, np.array([a['r'][k][1] for k in ('0', '10000', '20190')])

    def rho(self, h_m):
        return RHO0 * np.interp(h_m, self.h_tab, self.sigma_tab)

    def r(self, h_m, kias):
        hf = h_m / FT
        return np.exp(np.polyval(self.la, hf)) + np.interp(hf, self.hs, self.b) * (kias - 400)

    def kias(self, h_m, V):
        hf = h_m / FT
        a = np.exp(np.polyval(self.la, hf))
        b = np.interp(hf, self.hs, self.b)
        B = a - 400 * b
        c = V / KT
        return 2 * c / (B + np.sqrt(np.maximum(B * B + 4 * b * c, 1e-9)))

    def tas(self, h_m, kias):
        return kias * KT * self.r(h_m, kias)

    @staticmethod
    def schall(h_m):
        return np.sqrt(1.4 * 287.05 * np.maximum(288.15 - 0.0065 * h_m, 216.65))


def _gleich(tab, x0, dx, x):
    """Lineare Interpolation je Zeile in Tabellen mit gleichmäßigem Gitter. tab (J, K), x (J,)."""
    K = tab.shape[1]
    u = np.clip((np.asarray(x, float) - x0) / dx, 0, K - 1 - 1e-9)
    i = u.astype(int)
    f = u - i
    r = np.arange(tab.shape[0])
    return tab[r, i] * (1 - f) + tab[r, i + 1] * f


class Flotte:
    """Modell-Tabellen für J Jets (Typen je Index)."""
    INV = 400   # Stützstellen der Umkehrtabellen

    def __init__(self, m, typen):
        self.typen = list(typen)
        J = len(typen)
        pj = [m['jets'][t] for t in typen]
        f = lambda k: np.array([p[k] for p in pj], float)
        A = np.array(m['alpha'])
        self.a0, self.da = A[0], A[1] - A[0]
        self.m0, self.dm = m['mach'][0], m['mach'][1] - m['mach'][0]
        self.r0, self.dr = m['rho'][0], m['rho'][1] - m['rho'][0]
        self.delta = m['delta_hud_alpha']
        self.SLq, self.SDq, self.mf = f('SLq'), f('SDq'), f('machfaktor')
        self.Tm, self.Td, self.Ta = f('T_mach'), f('T_dichte'), f('T_alpha')
        self.daempfung = f('daempfung')
        self.alpha_lim, self.alpha_max = f('alpha_lim'), f('alpha_max')
        self.stall = self.alpha_max > self.alpha_lim
        self.W_voll, self.W_leer, self.burn = f('W_voll'), f('W_leer'), f('burn')
        self.alpha_rate = np.array([ALPHA_RATE_AUF[t] for t in typen])
        self.roll_max, self.roll_skala = f('rollrate_dps'), f('roll_skala')
        self.di = m['ias_ms'][1] - m['ias_ms'][0]
        # Umkehrtabellen auf dem aufsteigenden Ast (δ .. α beim Auftriebsmaximum)
        k0 = int(round((self.delta - self.a0) / self.da))
        self.L_max, self.alpha_peak = np.zeros(J), np.zeros(J)
        self.inv_L, self.inv_D = np.zeros((J, self.INV + 1)), np.zeros((J, self.INV + 1))
        self.D_min, self.D_peak = np.zeros(J), np.zeros(J)
        for j in range(J):
            k1 = k0 + int(np.argmax(self.SLq[j, k0:]))
            al = A[k0:k1 + 1]
            sl = np.maximum.accumulate(self.SLq[j, k0:k1 + 1])
            sdv = np.maximum.accumulate(self.SDq[j, k0:k1 + 1])
            self.L_max[j], self.alpha_peak[j] = sl[-1], al[-1]
            self.inv_L[j] = np.interp(np.linspace(0, sl[-1], self.INV + 1), sl, al)
            self.D_min[j], self.D_peak[j] = sdv[0], sdv[-1]
            self.inv_D[j] = np.interp(np.linspace(sdv[0], sdv[-1], self.INV + 1), sdv, al)
        self.J = J

    def schub(self, rho, M, alpha):
        """Voller Nachbrenner [N], Schubrichtung = Rumpfachse."""
        return (_gleich(self.Tm, self.m0, self.dm, M) * _gleich(self.Td, self.r0, self.dr, rho)
                * _gleich(self.Ta, self.a0, self.da, alpha))

    def auftrieb(self, q, alpha):
        return q * _gleich(self.SLq, self.a0, self.da, alpha)

    def widerstand(self, q, M, V, masse, alpha):
        return (q * _gleich(self.SDq, self.a0, self.da, alpha) * _gleich(self.mf, self.m0, self.dm, M)
                + masse * self.daempfung * V)

    def alpha_fuer_L(self, L, q):
        """α auf dem aufsteigenden Ast, bei dem der Auftrieb L erreicht wird (darüber: α beim Maximum)."""
        c = np.asarray(L, float) / np.maximum(q, 1.0)
        u = np.clip(np.abs(c) / self.L_max, 0, 1) * self.INV
        a = _gleich(self.inv_L, 0, 1, u)
        return self.delta + np.sign(c) * (a - self.delta)

    def L_fuer_D(self, q, M, V, masse, D):
        """Auftrieb, bei dem der Widerstand D erreicht wird (aufsteigender Ast, ohne Strömungsabriss)."""
        sd = (np.asarray(D, float) - masse * self.daempfung * V) / (
            np.maximum(q, 1.0) * _gleich(self.mf, self.m0, self.dm, M))
        u = np.clip((sd - self.D_min) / (self.D_peak - self.D_min), 0, 1) * self.INV
        return self.auftrieb(q, _gleich(self.inv_D, 0, 1, u))

    def rollrate(self, kias):
        """Größte Rollrate [°/s]: Vorgabe aus den Spieldaten, über IAS gedämpft (IAS hier ≈ KIAS in m/s)."""
        return self.roll_max * _gleich(self.roll_skala, 0.0, self.di, np.asarray(kias, float) * KT)

    def winkel_schub(self, alpha):
        """Winkel zwischen Rumpfachse und Bahn [rad] (Flügel-α)."""
        return np.radians(alpha - self.delta)


def norm(v):
    return np.sqrt(np.einsum('ij,ij->i', v, v))


def einheit(v, ersatz=None):
    n = norm(v)
    out = v / np.maximum(n, 1e-9)[:, None]
    if ersatz is not None:
        out = np.where((n < 1e-6)[:, None], ersatz, out)
    return out


def dot(a, b):
    return np.einsum('ij,ij->i', a, b)


def senkrecht(v, zu):
    """Anteil von v senkrecht zur Einheitsrichtung zu."""
    return v - dot(v, zu)[:, None] * zu


def mit_schwerkraft(l_dir, n, g_s):
    """Lift-Richtung, die bei |L| = n g die Beschleunigung in Richtung l_dir maximiert und die Schwerkraft
    quer zur Bahn ausgleicht (so ist „flach“ wirklich eine Kurve ohne Höhenverlust)."""
    lg = dot(l_dir, g_s)
    a = lg + np.sqrt(np.maximum(lg * lg - dot(g_s, g_s) + (n * g) ** 2, 0))
    return einheit(a[:, None] * l_dir - g_s, l_dir)


def winkel(a, b):
    return np.degrees(np.arccos(np.clip(dot(a, b), -1, 1)))


# ---------------------------------------------------------------- Strategien
# Eine Strategie ist ein Satz Parameter, wie sie ein Pilot vor dem Merge festlegt.
#   wende:  +1 zum Gegner hin (beide hin -> Two-Circle), -1 vom Gegner weg (-> One-Circle), 0 durchfliegen (Extend)
#   ebene:  Neigung des Lift Vectors im ersten Turn [°]; + = nose-high, - = nose-low; im Kampf halb so stark
#   v_ziel: KIAS, die der Pilot im Kampf hält (darüber: ziehen, darunter: entlasten)
#   lag:    Zielpunkt im Kampf [s] hinter dem Gegner (0 = Pure Pursuit)
#   alpha_kampf: α-Grenze beim Kurven (T-18: 26 diszipliniert, 35 voll); für den Schuss gilt immer alpha_max
#   merge_ab: 1 Nachbrenner bis zum Merge (schneller Merge), 0 Startspeed halten
# Jeder weitere Pass (hoher Aspect, Abstand < 1.000 m) beginnt wieder mit dem ersten Turn derselben Strategie.
STRATEGIE_FELDER = ('wende', 'ebene', 'v_ziel', 'lag', 'alpha_kampf', 'merge_ab')


def strategie_name(s, jet=None):
    w = {1: 'hin', -1: 'weg', 0: 'durch'}[int(s['wende'])]
    e = {60: 'steil hoch', 25: 'hoch', 0: 'flach', -30: 'tief'}.get(int(s['ebene']), f"{s['ebene']:+.0f}°")
    lag = 'Lag' if s['lag'] > 0 else 'Pure'
    a = f", α {s['alpha_kampf']:.0f}°" if jet == 'T-18' else ''
    mg = ', Merge mit AB' if s.get('merge_ab', 0) else ''
    return f"{w}/{e}/{s['v_ziel']:.0f} KIAS/{lag}{a}{mg}"


# ---------------------------------------------------------------- Simulation
def start_geometrie(N, atm, mach=0.75, hoehe_ft=10000.0, abstand_m=4000.0, versatz_m=400.0, hoehe_versatz_m=0.0,
                    kias=None):
    """Ranked-Start (Standardwerte = RANKED): Head-on mit seitlichem Versatz, beide mit Mach (oder kias)."""
    h = hoehe_ft * FT
    if kias is None:
        V = mach * float(atm.schall(np.array(h)))
    else:
        V = float(atm.tas(np.array(h), np.array(kias)))
    abstand = abstand_m
    P = np.zeros((2 * N, 3)); Vv = np.zeros((2 * N, 3))
    P[:N] = [0, -abstand / 2, h]
    P[N:] = [versatz_m, abstand / 2, h + hoehe_versatz_m]
    Vv[:N] = [0, V, 0]
    Vv[N:] = [0, -V, 0]
    return P, Vv


def simuliere(m, typ_a, typ_b, strat_a, strat_b, geo, t_max=RUNDENZEIT_S, dt=0.04, spur_alle=0.0, aenderung=None):
    """N Kämpfe gleichzeitig. strat_a/strat_b: dict Feld -> Array (N,). Rückgabe dict mit Ergebnis-Arrays.
    aenderung: abweichende ANNAHMEN für Empfindlichkeitstests, dazu 'schub_<Jet>' als Faktor auf den Schub."""
    AN = dict(ANNAHMEN, **(aenderung or {}))
    atm = Atmo(m)
    N = len(strat_a['wende'])
    typen = [typ_a] * N + [typ_b] * N
    fl = Flotte(m, typen)
    schub_f = np.array([AN.get(f'schub_{t}', 1.0) for t in typen])
    fl.alpha_max = np.array([AN.get(f'alpha_max_{t}', a) for t, a in zip(typen, fl.alpha_max)])
    J = 2 * N
    opp = np.concatenate([np.arange(N, J), np.arange(N)])
    S = {k: np.concatenate([np.asarray(strat_a[k], float), np.asarray(strat_b[k], float)]) for k in STRATEGIE_FELDER}

    P, V = start_geometrie(N, atm, **geo)
    W = fl.W_leer + (fl.W_voll - fl.W_leer) * AN['fuel_start']
    kias_start = atm.kias(P[:, 2], norm(V))
    l = np.tile(UP, (J, 1))                    # Lift Vector (Einheit, senkrecht zu v)
    alpha = np.full(J, 2.0)
    A_prev = np.zeros((J, 3))
    phase = np.zeros(J, int)                   # 0 vor dem Merge, 1 erster Turn / Extend, 2 Kampf
    t_phase = np.zeros(J)
    N_ebene = np.zeros((J, 3))
    dir_prev = None
    t_cpa_alt = np.zeros(J)
    gas = np.ones(J)
    dfire_prev = None
    treffer = np.zeros(J)
    offensiv = np.zeros(J)
    tot = np.zeros(J, bool)
    t_tot = np.full(J, np.inf)
    absturz = np.zeros(J, bool)
    u = AN['geschoss_mps']
    spur = []
    n_akt = np.ones(J)
    min_v = np.full(J, np.inf)
    kias_sum = np.zeros(J); kias_n = np.zeros(J)

    schritte = int(round(t_max / dt))
    for it in range(schritte):
        t = it * dt
        lebt = ~tot & ~tot[opp]
        if not lebt.any():
            break
        h = P[:, 2]
        Vm = np.maximum(norm(V), 20.0)
        vh = einheit(V, np.array([0.0, 1.0, 0.0]))
        rho = atm.rho(h)
        q = 0.5 * rho * Vm * Vm
        M = Vm / atm.schall(h)
        kias = atm.kias(h, Vm)
        min_v = np.minimum(min_v, np.where(lebt, kias, np.inf))
        im_kampf = lebt & (phase == 2)
        kias_sum += kias * im_kampf; kias_n += im_kampf
        T = fl.schub(rho, M, alpha) * schub_f
        mass = W / g

        # Geometrie zum Gegner
        rel = P[opp] - P
        R = norm(rel)
        los = rel / R[:, None]
        nose = vh * np.cos(np.radians(alpha))[:, None] + l * np.sin(np.radians(alpha))[:, None]
        ata = winkel(vh, los)
        ata_nose = winkel(nose, los)
        aa = winkel(vh[opp], los)               # Aspect: 0 = ich bin an seiner Six
        relv = V[opp] - V
        t_cpa = -dot(rel, relv) / np.maximum(dot(relv, relv), 1e-6)

        # Schusslösung (Vorhalt mit Flugzeit, Ziel-Beschleunigung, Geschoss fällt mit g)
        a_rel = A_prev[opp] + np.array([0, 0, g])
        tf = R / u
        for _ in range(2):
            pt = rel + relv * tf[:, None] + 0.5 * a_rel * (tf * tf)[:, None]
            tf = norm(pt) / u
        d_fire = einheit(pt)
        fehler = winkel(nose, d_fire)
        fenster = np.maximum(np.degrees(np.arctan(AN['ziel_radius_m'] / R)), AN['gun_streuung_deg'])
        im_schuss = (lebt & (phase >= 1) & (phase[opp] >= 1) & (R > AN['gun_r_min_m'])
                     & (R < AN['gun_r_max_m']) & (fehler < fenster))
        treffer += im_schuss * dt
        neu_tot = lebt[opp] & (treffer[opp] >= AN['treffer_s_bis_abschuss']) & ~tot
        offensiv += (lebt & (ata < 45) & (aa < 60) & (R < 1800)) * dt

        # Phasen
        neuer_pass = (phase == 2) & (t_cpa < 0) & (t_cpa_alt >= 0) & (R < 1000) & (aa > 60) & (ata > 60)
        t_cpa_alt = t_cpa
        geht = ((phase == 0) & ((t_cpa < 0.3) | (R < 300))) | neuer_pass
        if geht.any():
            seite = senkrecht(rel, vh); seite[:, 2] = 0
            seite = einheit(seite, np.array([1.0, 0, 0])) * np.where(S['wende'] < 0, -1.0, 1.0)[:, None]
            e = np.radians(S['ebene'])
            l0 = einheit(senkrecht(seite * np.cos(e)[:, None] + UP * np.sin(e)[:, None], vh))
            N_ebene = np.where(geht[:, None], np.cross(vh, l0), N_ebene)
            phase = np.where(geht, 1, phase); t_phase = np.where(geht, 0.0, t_phase)
        t_phase += dt
        extend = (phase == 1) & (S['wende'] == 0)
        weiter = (phase == 1) & (((S['wende'] != 0) & (((ata < 75) & (t_phase > 2)) | (t_phase > 20)))
                                 | (extend & (t_phase > 6)))
        phase = np.where(weiter, 2, phase)

        # Steuerung: gewünschte Richtung des Lift Vectors und Lastvielfaches
        up_s = einheit(senkrecht(np.tile(UP, (J, 1)), vh), l)
        g_s = senkrecht(np.tile([0, 0, -g], (J, 1)), vh)
        sin_gam = vh[:, 2]

        # Speed-Regler: G so, dass die Speed zum Ziel läuft
        dVdt = np.clip(0.3 * (S['v_ziel'] - kias), -40, 40) * KT * atm.r(h, kias)
        D_req = T - mass * (dVdt + g * sin_gam)
        n_speed = np.clip(fl.L_fuer_D(q, M, Vm, mass, D_req) / W, 0.5, 9.0)

        # Kampf: Verfolgung (Pure / Lag) mit Ebenen-Neigung
        # Lag nur auf kurze Distanz (Überschießen vermeiden); weiter weg Pure, um aufzuschließen
        lag_eff = S['lag'] * np.clip((2000 - R) / 800, 0, 1)
        ziel = P[opp] - V[opp] * lag_eff[:, None]
        dir_ = einheit(ziel - P)
        if dir_prev is None:
            dir_prev = dir_.copy()
        Om = np.cross(dir_prev, dir_) / dt
        dir_prev = dir_
        e_s = senkrecht(dir_, vh)
        th = np.arcsin(np.clip(norm(e_s), 0, 1))
        th = np.where(dot(dir_, vh) < 0, np.pi - th, th)
        e_hat = einheit(e_s, l)
        a_des = np.cross(Om, V) + (1.5 * th * Vm)[:, None] * e_hat
        bias = np.radians(S['ebene'] * 0.5)
        L_vec = a_des - g_s
        n_pur = norm(L_vec) / g
        l_kampf = einheit(einheit(L_vec, l) + up_s * np.tan(bias)[:, None])
        n_kampf = np.minimum(n_speed, n_pur)

        # Guns: Nase auf den Vorhaltepunkt
        gun = (phase >= 1) & (R < 1500) & (ata_nose < 30) & (dot(los, vh) > 0)
        if dfire_prev is None:
            dfire_prev = d_fire.copy()
        Om_g = np.cross(dfire_prev, d_fire) / dt
        dfire_prev = d_fire
        e_g = senkrecht(d_fire - nose, vh)
        th_g = np.radians(fehler)
        a_g = np.cross(Om_g, V) + (2.0 * th_g * Vm)[:, None] * einheit(e_g, l)
        Lg = a_g - g_s
        l_gun, n_gun = einheit(Lg, l), norm(Lg) / g

        # Verteidigung: er hat die Nase auf mir und ist hinter meiner 3/9-Linie -> Break Turn
        bedroht = (phase >= 1) & (R < 1500) & (ata_nose[opp] < 30) & (ata > 90)
        l_def = mit_schwerkraft(einheit(senkrecht(los, vh), l), np.full(J, 8.0), g_s)

        # erster Turn in fester Ebene
        l_turn = mit_schwerkraft(einheit(np.cross(N_ebene, vh), l), n_akt, g_s)

        l_soll = np.where((phase == 0)[:, None], up_s, l_turn)
        n_soll = np.where(phase == 0, 1.0, n_speed)
        l_soll = np.where(extend[:, None], up_s, l_soll)
        n_soll = np.where(extend, np.clip(-g_s[:, 2] / g, 0.5, 1.0), n_soll)
        k2 = phase == 2
        l_soll = np.where(k2[:, None], l_kampf, l_soll); n_soll = np.where(k2, n_kampf, n_soll)
        l_soll = np.where(bedroht[:, None], l_def, l_soll); n_soll = np.where(bedroht, 9.0, n_soll)
        l_soll = np.where(gun[:, None], l_gun, l_soll); n_soll = np.where(gun, n_gun, n_soll)

        # Boden: wenn die Höhe in 4 s unter 3.000 ft läge, hochziehen
        w_b = np.clip((900 - (h + 4 * V[:, 2])) / 600, 0, 1) * (sin_gam < 0.1)
        l_soll = einheit(l_soll * (1 - w_b)[:, None] + up_s * w_b[:, None], l)
        n_soll = np.maximum(n_soll, w_b * 9.0)
        # Decke: über ~22.000 ft Nase runter (Daten reichen bis 20.190 ft)
        w_c = np.clip((h + 4 * V[:, 2] - 6700) / 600, 0, 1) * (sin_gam > -0.1)
        l_soll = einheit(l_soll * (1 - w_c)[:, None] - up_s * w_c[:, None], l)
        n_soll = np.maximum(n_soll, w_c * 4.0)

        # α-Kommando aus n_soll; Grenze: beim Kurven alpha_kampf, beim Schuss alpha_max
        a_grenze = np.where(gun, fl.alpha_max, np.minimum(S['alpha_kampf'], fl.alpha_max))
        a_grenze = np.minimum(a_grenze, np.where(fl.stall, 35.0, fl.alpha_lim))
        a_cmd = fl.alpha_fuer_L(n_soll * W, q)
        bis_lim = np.minimum(a_grenze, fl.alpha_lim)
        a_cmd = np.where(a_cmd > bis_lim, np.where((n_soll >= 8.99) | gun, a_grenze, bis_lim), a_cmd)
        a_cmd = np.clip(a_cmd, -5, a_grenze)
        da = (a_cmd - alpha) / AN['alpha_tau_s']
        alpha = alpha + np.clip(da, -AN['alpha_rate_ab_dps'], fl.alpha_rate) * dt

        # Auftrieb, 9-G-Limiter
        L = fl.auftrieb(q, alpha)
        L = np.minimum(L, 9.0 * W)
        alpha = np.where(L >= 9.0 * W - 1, np.minimum(alpha, fl.alpha_fuer_L(9.0 * W, q)), alpha)
        n_akt = L / W

        # Rollen: l dreht um vh Richtung l_soll, begrenzt
        ls = einheit(senkrecht(l_soll, vh), l)
        sinp = dot(np.cross(l, ls), vh)
        cosp = dot(l, ls)
        roll = np.radians(AN['rollrate_fest_dps'] if AN['rollrate_fest_dps'] > 0
                          else fl.rollrate(kias) * AN['rollrate_faktor']) * dt
        phi = np.clip(np.arctan2(sinp, cosp), -roll, roll)
        l = l * np.cos(phi)[:, None] + np.cross(vh, l) * np.sin(phi)[:, None]

        # Bewegung
        D = fl.widerstand(q, M, Vm, mass, alpha)
        # Schub: vor dem Merge Startspeed halten oder Nachbrenner; im Kampf Leerlauf, wenn weit über Ziel-Speed
        T_halten = np.clip(D + mass * (0.5 * (kias_start - kias) * KT + g * sin_gam), 0, T)
        gas = np.where(phase == 0, np.where(S['merge_ab'] > 0, 1.0, T_halten / T),
                       np.where(extend | (kias < S['v_ziel'] + 60), 1.0, 0.0))
        T = T * gas
        ws = fl.winkel_schub(alpha)
        A = (((T * np.cos(ws) - D) / mass)[:, None] * vh + ((L + T * np.sin(ws)) / mass)[:, None] * l
             + np.array([0, 0, -g]))
        A = np.where(lebt[:, None], A, 0)
        V = V + A * dt
        P = P + V * dt
        W = np.maximum(W - fl.burn * gas * dt * lebt, fl.W_leer)
        vh2 = einheit(V)
        l = einheit(senkrecht(l, vh2), up_s)
        A_prev = A

        crash = lebt & (P[:, 2] <= 0)
        absturz |= crash
        tot_neu = neu_tot | crash
        t_tot = np.where(tot_neu & ~tot, t + dt, t_tot)
        tot |= tot_neu

        if spur_alle and it % int(round(spur_alle / dt)) == 0:
            spur.append(dict(t=t, P=P.copy(), kias=kias.copy(), n=n_akt.copy(), alpha=alpha.copy(),
                             phase=phase.copy(), gun=gun.copy(), bedroht=bedroht.copy(), treffer=treffer.copy()))

    # Ergebnis aus Sicht von A: +1 A gewinnt, -1 B gewinnt, 0 offen (gleichzeitig = 0)
    ta, tb = t_tot[:N], t_tot[N:]
    erg = np.where(tb < ta, 1, np.where(ta < tb, -1, 0))
    return dict(ergebnis=erg, t_a=ta, t_b=tb, absturz_a=absturz[:N], absturz_b=absturz[N:],
                offensiv_a=offensiv[:N], offensiv_b=offensiv[N:], treffer_a=treffer[:N], treffer_b=treffer[N:],
                min_kias_a=min_v[:N], min_kias_b=min_v[N:], kias_a=(kias_sum / np.maximum(kias_n, 1))[:N],
                kias_b=(kias_sum / np.maximum(kias_n, 1))[N:], spur=spur)
