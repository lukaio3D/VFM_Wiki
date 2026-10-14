"""VFM-Replays lesen (.vrb + .vri) und als Flugbahn mit abgeleiteten Größen ausgeben.

Format (entschlüsselt 2026-10-14 an v1.4.2, Build 24440300, Details in FORMAT.md):
- .vri: JSON mit Spielern (Name, Elo, Jet), Kill-Log, Dauer, Map.
- .vrb: ein LZ4-Block ohne Rahmen. Darin je Spieler ein Track mit ~4,5 Sätzen pro Sekunde:
  Zeitschritt, Positionsänderung, Geschwindigkeitsänderung, Lageänderung (int8-Quaternion-Delta).
  Danach eine Ereignisliste (Geschosse, Treffer).

Einheiten im Replay: Meter, m/s, Unity-Achsen (x rechts, y oben, z vorn; Start auf 3048 m = 10.000 ft).

    python vrb.py                                   # Übersicht über alle eigenen Replays
    python vrb.py replay74                          # ein Replay (Name, Pfad zur .vrb oder .vri)
    python vrb.py replay74 --csv ausgabe/           # je Spieler eine CSV, dazu die Schüsse
    python vrb.py --ordner "F:/.../StreamingAssets/Replays"
"""
import argparse
import json
import os
import struct
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'flugmodell'))
import modell as M  # noqa: E402

g, KT, FT = M.g, M.KT, M.FT
ORDNER = Path(os.environ.get('USERPROFILE', '~')).expanduser() / 'AppData/LocalLow/Boundless Dynamics, LLC/VFM/Replays'
# Jet-Index in .vrb und .vri. Zuordnung aus den Daten geschätzt, siehe FORMAT.md
JETS = {0: 'T-15', 1: 'T-16', 2: 'T-18'}


def lz4_block(src: bytes) -> bytes:
    i, out = 0, bytearray()
    while i < len(src):
        tok = src[i]; i += 1
        n = tok >> 4
        if n == 15:
            while True:
                b = src[i]; i += 1; n += b
                if b != 255:
                    break
        out += src[i:i + n]; i += n
        if i >= len(src):
            break
        off = src[i] | src[i + 1] << 8; i += 2
        n = tok & 15
        if n == 15:
            while True:
                b = src[i]; i += 1; n += b
                if b != 255:
                    break
        n += 4
        if off >= n:
            out += out[-off:len(out) - off + n]
        else:
            for _ in range(n):
                out.append(out[-off])
    return bytes(out)


class Leser:
    def __init__(self, d: bytes):
        self.d, self.p = d, 0

    def __call__(self, fmt: str):
        v = struct.unpack_from('<' + fmt, self.d, self.p)
        self.p += struct.calcsize('<' + fmt)
        return v if len(v) > 1 else v[0]

    def text(self) -> str:
        n = self('i')
        s = self.d[self.p:self.p + n].decode('utf-8', 'replace')
        self.p += n
        return s


def _spur(r: Leser) -> dict:
    sid, team, aktiv, jet = r('ii?i')
    name = r.text()
    anzahl, t0 = r('if')
    pos, vel, q = np.array(r('3f')), np.array(r('3f')), np.array(r('4b'))
    t, P, V, dV, dQ, maske = [t0], [pos], [vel], [np.zeros(3)], [np.zeros(4)], [0]
    for _ in range(anzahl - 1):
        dt, m = r('fB')
        if m & 1:
            pos = pos + r('3f')
        dv = np.array(r('3f')) if m & 2 else np.zeros(3)
        vel = vel + dv
        t.append(t[-1] + dt); P.append(pos); V.append(vel); dV.append(dv); maske.append(m)
        dQ.append(np.array(r('4b')) if m & 4 else np.zeros(4))
    return dict(id=sid, team=team, aktiv=aktiv, jet=JETS.get(jet, str(jet)), jet_idx=jet, name=name, q0=q,
                t=np.array(t), pos=np.array(P), vel=np.array(V), dv=np.array(dV), dq=np.array(dQ), maske=np.array(maske))


def _ereignisse(r: Leser) -> dict:
    _, n = r('ii')
    schuesse, typ2, typ5 = [], [], []
    for _ in range(n):
        art, t, k = r('Bfb')
        if art == 3:    # Geschoss: Start (Position, Geschwindigkeit), Zahl, Ende (Position, Geschwindigkeit, Zeit)
            p0, v0, z, p1, v1, t1 = r('3f'), r('3f'), r('i'), r('3f'), r('3f'), r('f')
            schuesse.append((t, k, *p0, *v0, z, *p1, *v1, t1))
        elif art == 2:  # Objekt mit Position und Lage, tritt um Treffer herum auf
            typ2.append((t, k, *r('3f'), *r('4b')))
        elif art == 5:
            typ5.append((t, k, r('i')))
        else:
            raise ValueError(f'unbekannter Ereignistyp {art} bei Byte {r.p - 6}')
    return dict(schuesse=np.array(schuesse).reshape(-1, 16), typ2=np.array(typ2).reshape(-1, 9),
                typ5=np.array(typ5).reshape(-1, 3))


def lesen(pfad) -> dict:
    pfad = Path(pfad)
    if not pfad.suffix:
        pfad = (pfad if pfad.parent != Path('.') else ORDNER / pfad).with_suffix('.vrb')
    vrb, vri = pfad.with_suffix('.vrb'), pfad.with_suffix('.vri')
    meta = json.loads(vri.read_text(encoding='utf-8-sig')) if vri.exists() else {}
    r = Leser(lz4_block(vrb.read_bytes()))
    version, n = r('ii')
    if version != 1:
        print(f'Warnung: Formatversion {version}, gelesen wird Version 1', file=sys.stderr)
    spieler = [_spur(r) for _ in range(n)]
    ereignisse = _ereignisse(r)
    if r.p != len(r.d):
        print(f'Warnung: {len(r.d) - r.p} Bytes am Ende nicht gelesen', file=sys.stderr)
    for s in spieler:
        s.update(abgeleitet(s))
        m = next((p for p in meta.get('players', []) if p['name'] == s['name']), {})
        s.update(elo=m.get('elo'), kills=m.get('kills'), deaths=m.get('deaths'))
    return dict(name=vrb.stem, meta=meta, spieler=spieler, ereignisse=ereignisse)


_atm = None


def atmosphaere():
    global _atm
    if _atm is None:
        p = json.load(open(Path(M.DATEN) / 'modell_parameter.json'))['atmosphaere']
        _atm = M.Atmosphaere({int(h): v for h, v in p['r'].items()}, p['H_m'])
    return _atm


def abgeleitet(s: dict) -> dict:
    """Fahrt, Höhe, Last und Energie je Satz. Beschleunigung = dv / dt des Satzes (Rückwärtsdifferenz)."""
    t, V, dv = s['t'], s['vel'], s['dv']
    dt = np.diff(t, prepend=t[0] - 1)
    a = dv / np.maximum(dt, 1e-3)[:, None]
    spez = a + [0, g, 0]                                   # spezifische Kraft: Auftrieb + (Schub - Widerstand)
    v = np.linalg.norm(V, axis=1)
    e = V / v[:, None]
    laengs = (spez * e).sum(1)
    quer = spez - laengs[:, None] * e
    h_ft = s['pos'][:, 1] / FT
    tas = v / KT
    atm = atmosphaere()
    kias = tas / atm.r(h_ft, tas / atm.r(h_ft, 400))
    return dict(dt=dt, hoehe_ft=h_ft, tas_kt=tas, kias=kias, mach=v / M.schall(h_ft),
                n=np.linalg.norm(quer, axis=1) / g,           # Last senkrecht zur Bahn (≈ HUD-G)
                ps_fts=v * laengs / g / FT,                     # spezifische Überschussleistung
                kurs=np.degrees(np.arctan2(V[:, 0], V[:, 2])) % 360,
                steig=np.degrees(np.arcsin(np.clip(V[:, 1] / v, -1, 1))),
                rate_dps=np.degrees(np.linalg.norm(quer, axis=1) / v))


SPALTEN = ['t', 'x', 'y', 'z', 'vx', 'vy', 'vz', 'hoehe_ft', 'tas_kt', 'kias', 'mach', 'n', 'rate_dps', 'ps_fts',
           'kurs', 'steig', 'dqx', 'dqy', 'dqz', 'dqw', 'maske']


def tabelle(s: dict) -> np.ndarray:
    return np.column_stack([s['t'], s['pos'], s['vel'], s['hoehe_ft'], s['tas_kt'], s['kias'], s['mach'], s['n'],
                            s['rate_dps'], s['ps_fts'], s['kurs'], s['steig'], s['dq'], s['maske']])


def zusammenfassung(rp: dict):
    m = rp['meta']
    print(f"# {rp['name']}  {m.get('s_timeRecorded', '')}  Map {m.get('mapIdx')}  {m.get('duration', 0):.1f} s")
    for e in m.get('logEvents', []):
        print(f"    {e['time']:7.2f}  {e['message']}")
    for s in rp['spieler']:
        n = s['n'][1:]
        print(f"  {s['name'][:20]:20} {s['jet']:5} Team {s['team']}  Elo {s['elo']}  {len(s['t'])} Sätze, "
              f"{s['t'][-1]:.1f} s | KIAS {s['kias'].min():.0f}–{s['kias'].max():.0f}, "
              f"Höhe {s['hoehe_ft'].min():,.0f}–{s['hoehe_ft'].max():,.0f} ft, G max {n.max():.1f}, "
              f"Zeit > 7 G {np.sum(s['dt'][1:][n > 7]):.0f} s")
    sch = rp['ereignisse']['schuesse']
    print(f"  {len(sch)} Geschosse, {len(rp['ereignisse']['typ2'])} Typ-2-, {len(rp['ereignisse']['typ5'])} Typ-5-Ereignisse")


def uebersicht(ordner: Path):
    dateien = sorted(ordner.glob('*.vrb'), key=lambda p: p.stat().st_mtime)
    print(f"{len(dateien)} Replays in {ordner}\n")
    print(f"{'Replay':12} {'Datum':19} {'Map':>3} {'Dauer':>6}  Spieler (Jet, Elo, K/D)")
    jets, fehler = {}, 0
    for p in dateien:
        try:
            rp = lesen(p)
        except Exception as e:  # noqa: BLE001
            fehler += 1
            print(f"{p.stem:12} FEHLER {e}")
            continue
        m = rp['meta']
        teile = [f"{s['name'][:16]} ({s['jet']}, {s['elo']}, {s['kills']}/{s['deaths']})" for s in rp['spieler']]
        print(f"{p.stem:12} {m.get('s_timeRecorded', '')[:19]:19} {m.get('mapIdx', ''):>3} {m.get('duration', 0):6.0f}  "
              + ' vs '.join(teile))
        for s in rp['spieler']:
            jets[s['jet']] = jets.get(s['jet'], 0) + s['t'][-1]
    print(f"\nFlugzeit je Jet: " + ', '.join(f"{j} {t / 60:.0f} min" for j, t in sorted(jets.items()))
          + (f"; {fehler} Dateien nicht lesbar" if fehler else ''))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('replay', nargs='?')
    ap.add_argument('--ordner', type=Path, default=ORDNER)
    ap.add_argument('--csv', type=Path)
    a = ap.parse_args()
    if not a.replay:
        uebersicht(a.ordner)
        return
    p = Path(a.replay)
    rp = lesen(p if p.suffix or p.parent != Path('.') else a.ordner / p)
    zusammenfassung(rp)
    if a.csv:
        a.csv.mkdir(parents=True, exist_ok=True)
        for s in rp['spieler']:
            ziel = a.csv / f"{rp['name']}_{s['id']}_{s['jet']}.csv"
            np.savetxt(ziel, tabelle(s), delimiter=';', fmt='%.6g', header=';'.join(SPALTEN), comments='')
            print(f"  -> {ziel}")
        sch = rp['ereignisse']['schuesse']
        if len(sch):
            ziel = a.csv / f"{rp['name']}_geschosse.csv"
            np.savetxt(ziel, sch, delimiter=';', fmt='%.6g', comments='',
                       header='t;k;x0;y0;z0;vx0;vy0;vz0;zahl;x1;y1;z1;vx1;vy1;vz1;t1')
            print(f"  -> {ziel}")


if __name__ == '__main__':
    main()
