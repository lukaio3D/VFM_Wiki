"""Original-Flugmodell aus der lokalen VFM-Installation lesen (nur lesend, offline).

Liest die serialisierten Unity-Objekte (ScriptableObjects und Komponenten) aus den .assets-Dateien und
schreibt sie als JSON nach ausgabe/spieldaten.json. Die Ausgabe enthält Daten des Spiels und bleibt lokal
(gitignored), ins Repo und ins Wiki gehören nur daraus gewonnene Erkenntnisse.

    python lesen.py                       # alles lesen -> ausgabe/spieldaten.json, Kurzfassung ausgeben
    python lesen.py --felder JetSpecs     # Feldnamen einer Klasse aus global-metadata.dat (zum Erkunden)

Die Feldreihenfolgen unten stammen aus global-metadata.dat (IL2CPP, Version 31), die Typen aus den Rohdaten.
Gelesen und geprüft an v1.4.2 (Build 24440300): jedes Objekt wird bis zum letzten Byte gelesen, sonst Fehler.
Nach einem Spiel-Update kann sich das Layout ändern; dann meldet das Skript, welches Objekt nicht aufgeht.

Benötigt: pip install UnityPy numpy
"""
import argparse
import json
import os
import struct
from pathlib import Path

import UnityPy

HIER = Path(__file__).resolve().parent
SPIEL = Path(os.environ.get('VFM_PFAD', r'F:\SteamLibrary\steamapps\common\Virtual Fighter Maneuvers')) / 'VFM_Data'
JETS = {'Eagle': 'T-15', 'Viper': 'T-16', 'Hornet': 'T-18'}   # interne Namen


class Leser:
    def __init__(self, raw: bytes):
        self.r, self.p = raw, 0

    def f(self):
        v = struct.unpack_from('<f', self.r, self.p)[0]; self.p += 4; return v

    def i(self):
        v = struct.unpack_from('<i', self.r, self.p)[0]; self.p += 4; return v

    def b(self):  # bool, auf 4 Byte ausgerichtet
        v = self.r[self.p]; self.p += 4; return bool(v)

    def v2(self): return [self.f(), self.f()]
    def v3(self): return [self.f(), self.f(), self.f()]

    def s(self):
        n = self.i(); t = self.r[self.p:self.p + n].decode('utf-8', 'replace'); self.p += (n + 3) & ~3; return t

    def pptr(self):
        fid = self.i(); pid = struct.unpack_from('<q', self.r, self.p)[0]; self.p += 8; return [fid, pid]

    def c(self):
        """AnimationCurve: Stützstellen (Zeit, Wert, Steigung ein, Steigung aus), Hermite-interpoliert."""
        n = self.i()
        if not 0 <= n < 1000:
            raise ValueError(f'Kurve mit {n} Punkten bei Byte {self.p - 4}')
        k = [struct.unpack_from('<4fi2f', self.r, self.p + 28 * j)[:4] for j in range(n)]
        self.p += 28 * n + 12   # dazu PreInfinity, PostInfinity, RotationOrder
        return [list(x) for x in k]

    def kopf(self):  # MonoBehaviour: m_GameObject, m_Enabled, m_Script, m_Name
        self.pptr(); self.b(); self.pptr(); return self.s()


def pid(n):
    return lambda d: [d.f() for _ in range(n)]


def liste(fn):
    return lambda d: [fn(d) for _ in range(d.i())]


def fluegel(d):
    return dict(name=d.s(), flaeche=d.f(), omnidirektional=d.b(), profil=d.pptr(), position=d.v3(), normale=d.v3(),
                stumm=d.b(), buffet_versatz=d.f())


SCHEMAS = {
    'JetSpecs': [('mass', 'f'), ('angularInertia', 'v3'), ('angularDrag', 'f'), ('useCustomMachWaveDrag', 'b'),
                 ('customMachWaveDrag', 'c'), ('gLimitCurve', 'c'), ('pyrRates', 'v3'), ('pitchPid', pid(5)),
                 ('yawPid', pid(5)), ('rollPid', pid(5)), ('controlInputScaleOverIAS', 'c'),
                 ('controlOutputScaleOverIAS', 'c'), ('aoaEdgeFactor', 'f'), ('aoaEdgeFactor2', 'f'), ('aoaLimit1', 'f'),
                 ('aoaLimit2', 'f'), ('useAoAGLimiter', 'b'), ('aoaGLimiterCurve', 'c')],
    'Aerodynamics': [('liftCoefficient', 'f'), ('liftCurve', 'c'), ('dragCoefficient', 'f'), ('dragCurve', 'c'),
                     ('buffetCurve', 'c'), ('buffetMagnitude', 'f'), ('buffetTimeFactor', 'f'), ('perpLiftVector', 'b'),
                     ('mirroredCurves', 'b')],
    'JetEngineSpecs': [('rotorMass', 'f'), ('rotorDrag', 'f'), ('maxTorque', 'f'), ('torqueRpmCurve', 'c'),
                       ('torqueAirDensityCurve', 'c'), ('maxThrust', 'f'), ('thrustMachCurve', 'c'),
                       ('thrustDensityCurve', 'c'), ('abThrustMul', 'f'), ('abDrainMul', 'f'),
                       ('normThrustToTempCurve', 'c'), ('tempLerpRate', 'f'), ('thrustFuelRatio', 'f'), ('minOutput', 'f'),
                       ('throttleRPMCurve', 'c'), ('governorPID', pid(7)), ('useThrustAoACurve', 'b'),
                       ('thrustAoACurve', 'c'), ('nozzleThrustFactorRange', 'v2'), ('normNozzleMoveSpeed', 'f'),
                       ('throttleToNozzlePosition', 'c')],
    'SOCurve': [('curve', 'c')],
    'FuelTank': [('baseMass', 'f'), ('startingFuel', 'f'), ('maxFuel', 'f'), ('fuelDensity', 'f'), ('_unbekannt', 'f')],
    'AerodynamicsController': [('wingAero', 'pptr'), ('atmosDensityCurve', 'c'), ('defaultDragMachCurve', 'pptr')],
    # JetController: nur der vordere Teil bis zu den Flügeln ist sicher zugeordnet
    'JetController': [('flightInfo', 'pptr'), ('jetSync', 'pptr'), ('inputSync', 'pptr'), ('startSpeed', 'f'),
                      ('jetSpecs', 'pptr'), ('collisionSphereRadius', 'f'), ('collisionSphereScale', 'v3'),
                      ('health', 'pptr'), ('outputs', liste(Leser.pptr)), ('jetEngine', 'pptr'), ('pitchPid', pid(7)),
                      ('yawPid', pid(7)), ('rollPid', pid(7)), ('baseDrag', 'f'), ('brakeDrag', 'f'),
                      ('brakeDeployRate', 'f')],
    'Gun': [('flightInfo', 'pptr'), ('actor', 'pptr'), ('muzzleVelocity', 'f'), ('rateOfFire', 'f'), ('inaccuracy', 'f'),
            ('inaccuracyPower', 'f'), ('maxAmmo', 'i'), ('ammo', 'i'), ('ammoMass', 'f'), ('damage', 'f')],
}
# Diese Klassen haben hinten Felder, die das Schema nicht abdeckt
TEILWEISE = {'AerodynamicsController', 'JetController', 'Gun'}


def dekodieren(raw, klasse):
    d = Leser(raw)
    out = {'_name': d.kopf()}
    for name, typ in SCHEMAS[klasse]:
        out[name] = typ(d) if callable(typ) else getattr(d, typ)()
    if klasse == 'JetController':
        out['fluegel'] = fluegel_suchen(raw)
    rest = len(raw) - d.p
    if rest and klasse not in TEILWEISE:
        raise ValueError(f'{klasse} {out["_name"]!r}: {rest} Bytes übrig, Layout passt nicht')
    return out


def fluegel_suchen(raw):
    """Flügel-Einträge (Name, Fläche, ..., Profil-Verweis mit fileID 0) im JetController finden."""
    gefunden = []
    for k in range(0, len(raw) - 68, 4):
        n = struct.unpack_from('<i', raw, k)[0]
        if not 3 <= n <= 24 or not all(32 <= c < 127 for c in raw[k + 4:k + 4 + n]):
            continue
        d = Leser(raw); d.p = k
        try:
            w = fluegel(d)
        except struct.error:
            continue
        if w['profil'][0] == 0 and w['profil'][1] > 0 and 0.05 < w['flaeche'] < 20 and abs(sum(x * x for x in w['normale']) - 1) < 0.2:
            w['_byte'] = k
            gefunden.append(w)
    return gefunden


def lesen(spiel: Path):
    env = UnityPy.load(str(spiel))
    skripte, namen = {}, {}
    for o in env.objects:
        if o.type.name == 'MonoScript':
            s = o.read()
            skripte[(o.assets_file.name, o.path_id)] = s.m_ClassName
    daten = {k: [] for k in SCHEMAS}
    for o in env.objects:
        if o.type.name != 'MonoBehaviour':
            continue
        mb = o.read(check_read=False)
        try:
            sk = mb.m_Script.deref()
            klasse = skripte.get((sk.assets_file.name, sk.path_id))
        except Exception:  # noqa: BLE001
            continue
        namen[(o.assets_file.name, o.path_id)] = mb.m_Name
        if klasse in SCHEMAS:
            x = dekodieren(o.get_raw_data(), klasse)
            x['_datei'], x['_id'] = o.assets_file.name, o.path_id
            daten[klasse].append(x)
    # Profil-Verweise der Flügel auflösen
    for jc in daten['JetController']:
        for w in jc['fluegel']:
            w['profil'] = namen.get((jc['_datei'], w['profil'][1]), w['profil'])
        jc['jetSpecs'] = namen.get((jc['_datei'], jc['jetSpecs'][1]), jc['jetSpecs'])
    return daten


def kurzfassung(daten):
    specs = {x['_name']: x for x in daten['JetSpecs']}
    motoren = {x['_name']: x for x in daten['JetEngineSpecs']}
    tanks = sorted(daten['FuelTank'], key=lambda x: (x['_datei'], x['_id']))
    for intern, jet in JETS.items():
        s, m = specs.get(f'{intern}Specs'), motoren.get(f'{intern}EngineSpecs')
        if not s:
            continue
        jc = next((j for j in daten['JetController'] if j['jetSpecs'] == f'{intern}Specs'), None)
        print(f"{jet} ({intern}): Leermasse {s['mass']} t, Drehraten P/Y/R {s['pyrRates']} °/s, "
              f"AoA-Limits {s['aoaLimit1']}° / {s['aoaLimit2']}°, G-Limit {s['gLimitCurve'][0][1]}")
        if m:
            print(f"    Schub {m['maxThrust']:.1f} kN × Nachbrenner {m['abThrustMul']:.3f}, Schub über Mach max "
                  f"{max(k[1] for k in m['thrustMachCurve']):.2f}")
        if jc:
            print(f"    baseDrag {jc['baseDrag']:.3g}, brakeDrag {jc['brakeDrag']:.3g}, Flügel: "
                  + ', '.join(f"{w['name']} {w['flaeche']:.2f} ({w['profil']})" for w in jc['fluegel']))
    print('Tanks:', ', '.join(f"{t['maxFuel']:.0f} × {t['fuelDensity']:.3g} t" for t in tanks))


def felder(klasse):
    """Feldnamen einer Klasse aus global-metadata.dat (v31). Typen stehen nur in GameAssembly.dll."""
    d = (SPIEL / 'il2cpp_data/Metadata/global-metadata.dat').read_bytes()
    h = struct.unpack_from('<64i', d, 8)
    so, fo, (to, ts) = h[4], h[22], (h[38], h[39])
    s = lambda i: d[so + i:d.index(b'\0', so + i)].decode('utf-8', 'replace')
    for k in range(ts // 88):
        v = struct.unpack_from('<16i8H2I', d, to + 88 * k)
        if s(v[0]) == klasse:
            namen = [s(struct.unpack_from('<i', d, fo + 12 * (v[8] + j))[0]) for j in range(v[18])]
            print(f"{s(v[1])}.{klasse}: {', '.join(namen)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--spiel', type=Path, default=SPIEL)
    ap.add_argument('--felder', metavar='KLASSE')
    a = ap.parse_args()
    if a.felder:
        felder(a.felder)
        return
    daten = lesen(a.spiel)
    ziel = HIER / 'ausgabe' / 'spieldaten.json'
    ziel.parent.mkdir(exist_ok=True)
    ziel.write_text(json.dumps(daten, indent=1, ensure_ascii=False), encoding='utf-8')
    kurzfassung(daten)
    print(f'-> {ziel}')


if __name__ == '__main__':
    main()
