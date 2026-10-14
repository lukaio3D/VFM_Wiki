"""Tabellen des Originalmodells für Kampfsimulator und 3D-App -> daten/modell_original.json.

Aus original.py (Spieldaten) und daten/original_kalibrierung.json (kalibrieren.py). Alles in SI (N, Pa, m, m/s):
  L = q * SLq(α),  D = q * SDq(α) * machfaktor(M) + Masse * daempfung * V,
  T = T_mach(M) * T_dichte(rho) * T_alpha(α)   (voller Nachbrenner),  q = 0,5 rho V²,  rho = 1,225 * sigma(h)
α ist das HUD-α (Flügel-α + delta). Gemessene Größen bleiben gemessen: α-Grenzen im Flug, Verbrauch.

Aufruf: python export_original.py   (braucht tools/spieldaten/ausgabe/spieldaten.json)
"""
import json

import numpy as np

import original as O

RHO0 = 1.225
ZIEL = O.HIER / 'daten' / 'modell_original.json'
# gemessen (refit.py): α am Anschlag ohne Override im HUD; T-18 nutzt bis 35°
ALPHA_LIM = {'T-15': 24.5, 'T-16': 23.0, 'T-18': 26.0}
ALPHA_MAX = {'T-15': 24.5, 'T-16': 23.0, 'T-18': 35.0}
AB_LBS_PRO_S = {'T-15': 35.0, 'T-16': 16.3, 'T-18': 35.0}


def runden(x, n=5):
    return [float(f'{v:.{n}g}') for v in np.asarray(x, float)]


def main():
    sd = O.lade_spieldaten()
    kal = json.loads(O.KALIBRIERUNG.read_text())
    atm = O.Atmosphaere(sd)
    alt = json.load(open(O.HIER / 'daten' / 'modell_parameter.json'))['atmosphaere']
    delta = kal['delta_hud_alpha']
    A = np.arange(-10.0, 90.01, 0.5)
    MG = np.arange(0.0, 3.001, 0.05)
    RG = np.arange(0.0, 1.401, 0.02)
    HG = np.arange(0.0, 20000.1, 250.0)
    IG = np.arange(0.0, 450.1, 10.0)   # IAS [m/s] für die Steuerdämpfung
    out = {'quelle': 'Originalkurven aus der VFM-Installation (v1.4.2), kalibriert mit kalibrieren.py',
           'atmosphaere': {'r': alt['r'], 'H_m': alt['H_m'], 'h_m': runden(HG), 'sigma': runden(atm.sigma(HG))},
           'alpha': runden(A), 'mach': runden(MG), 'rho': runden(RG), 'ias_ms': runden(IG), 'delta_hud_alpha': delta, 'jets': {}}
    for t in O.JETS:
        k = kal['jets'][t]
        j = O.Jet(t, sd, {'KL': k['KL'], 'KD': k['KD'], 'KB': 1.0})
        aw = A - delta
        f = 2000.0 / RHO0
        out['jets'][t] = {
            'SLq': runden(f * k['KL'] * j.SL(aw)), 'SDq': runden(f * k['KD'] * j.SD(aw, k.get('kS', 1.0))),
            'machfaktor': runden(j.machfaktor(MG)),
            'T_mach': runden(1000 * k['kT'] * j.T_max * j.ab * j.thrust_mach(MG)),
            'T_dichte': runden(j.thrust_dichte(RG)),
            'T_alpha': runden(j.thrust_aoa(np.abs(aw)) if j.thrust_aoa else np.ones_like(A)),
            'daempfung': k['kB'] * j.base_drag,
            'W_leer': j.gewicht(0.0) * 1000, 'W_voll': j.gewicht(1.0) * 1000,
            'burn': AB_LBS_PRO_S[t] * O.LB,
            'alpha_lim': ALPHA_LIM[t], 'alpha_max': ALPHA_MAX[t],
            'alpha_limiter_spiel': j.alpha_lim + delta, 'alpha_limit2_spiel': j.alpha_lim2 + delta,
            'drehraten_pyr': j.pyr, 'diagramm_lift_faktor': k['diagramm_lift_faktor'],
            # Rollrate = Vorgabe aus den Spieldaten × Dämpfung über IAS (Achse als m/s angenommen)
            'rollrate_dps': j.pyr[2], 'roll_skala': runden(j.steuer_skala(IG)),
        }
    ZIEL.write_text(json.dumps(out), encoding='utf-8')
    print(f'-> {ZIEL} ({ZIEL.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
