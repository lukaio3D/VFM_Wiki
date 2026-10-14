"""Unbekanntes Replay-Format untersuchen.

Nimmt eine Datei, entpackt sie wenn nötig und sucht nach der typischen Struktur einer
Flugaufzeichnung: Datensätze fester Länge (Frames) mit float32-Feldern. Gibt je Feld
Wertebereich, Glätte und Verdacht aus (Zeit, Position, Quaternion, Geschwindigkeit).

    python format.py replay.bin                     # Überblick
    python format.py replay.bin --csv felder.csv    # beste Struktur als Tabelle exportieren
    python format.py replay.bin --stride 96 --offset 40
    python format.py a.bin b.bin                    # zwei Aufnahmen: gemeinsamer Kopf, Größen

Erkennt nur Formate mit festen Frame-Längen. Delta- oder Varint-Kodierung (z. B. Protobuf,
Netzwerk-Snapshots) zeigt sich als hohe Entropie ohne klare Periode; dann helfen die
Bezeichner aus erkunden.ps1 -Bezeichner weiter.
"""

import argparse
import bz2
import gzip
import lzma
import re
import sys
import zlib
from pathlib import Path

import numpy as np


def entpacken(roh: bytes) -> tuple[bytes, str]:
    versuche = [
        ("gzip", lambda b: gzip.decompress(b)),
        ("zlib", lambda b: zlib.decompress(b)),
        ("deflate roh", lambda b: zlib.decompress(b, -15)),
        ("xz/lzma", lambda b: lzma.decompress(b)),
        ("bzip2", lambda b: bz2.decompress(b)),
    ]
    try:
        import zstandard

        versuche.append(("zstd", lambda b: zstandard.ZstdDecompressor().decompressobj().decompress(b)))
    except ImportError:
        pass
    try:
        import lz4.frame

        versuche.append(("lz4", lambda b: lz4.frame.decompress(b)))
    except ImportError:
        pass
    for name, f in versuche:
        try:
            daten = f(roh)
            if len(daten) > len(roh) // 2:
                return daten, name
        except Exception:
            pass
    # Komprimierter Block hinter einem Kopf? Erste 4 KB nach zlib/gzip-Signaturen absuchen.
    for m in re.finditer(rb"\x1f\x8b\x08|\x78[\x01\x5e\x9c\xda]", roh[:4096]):
        try:
            d = zlib.decompressobj(31 if roh[m.start()] == 0x1F else 15)
            daten = d.decompress(roh[m.start():])
            if len(daten) > 1024:
                return daten, f"{'gzip' if roh[m.start()] == 0x1F else 'zlib'} ab Byte {m.start()}"
        except Exception:
            pass
    return roh, "keine"


def entropie(b: bytes) -> float:
    if not b:
        return 0.0
    z = np.bincount(np.frombuffer(b, np.uint8), minlength=256) / len(b)
    z = z[z > 0]
    return float(-(z * np.log2(z)).sum())


def zeichenketten(b: bytes, n: int = 40) -> list[str]:
    asc = [m.group().decode() for m in re.finditer(rb"[ -~]{6,}", b)]
    u16 = [m.group().decode("utf-16le") for m in re.finditer(rb"(?:[ -~]\x00){6,}", b)]
    gesehen, aus = set(), []
    for s in asc + u16:
        if s not in gesehen:
            gesehen.add(s)
            aus.append(s)
    return aus[:n]


def perioden(b: bytes, max_stride: int = 1024, top: int = 6) -> list[tuple[int, float]]:
    """Anteil gleicher Bytes im Abstand s. Feste Frame-Länge -> Spitze bei s und Vielfachen."""
    a = np.frombuffer(b[: 4_000_000], np.uint8)
    werte = []
    for s in range(4, min(max_stride, len(a) // 4)):
        werte.append((s, float(np.mean(a[:-s] == a[s:]))))
    if not werte:
        return []
    basis = np.median([w for _, w in werte])
    # Grundperiode bevorzugen: Vielfache einer starken Periode abwerten
    werte.sort(key=lambda x: -x[1])
    aus = []
    for s, w in werte:
        if any(s % t == 0 and w <= wt * 1.02 for t, wt in aus):
            continue
        aus.append((s, w))
        if len(aus) >= top:
            break
    return [(s, w / basis if basis > 0 else w) for s, w in aus]


def felder(b: bytes, stride: int, offset: int) -> tuple[np.ndarray, np.ndarray]:
    n = (len(b) - offset) // stride
    roh = np.frombuffer(b[offset: offset + n * stride], np.uint8).reshape(n, stride)
    nf = stride // 4
    f32 = roh[:, : nf * 4].copy().view("<f4").reshape(n, nf)
    i32 = roh[:, : nf * 4].copy().view("<i4").reshape(n, nf)
    return f32, i32


def bewertung(f32: np.ndarray) -> float:
    """Wie sehr sieht das nach Zeitreihen aus: plausible Floats, die sich glatt ändern."""
    with np.errstate(all="ignore"):
        ok = np.isfinite(f32) & ((np.abs(f32) < 1e7) & ((np.abs(f32) > 1e-6) | (f32 == 0)))
        d = np.abs(np.diff(f32, axis=0))
        skala = np.nanpercentile(np.abs(f32), 90, axis=0) + 1e-9
        glatt = np.nanmedian(d / skala, axis=0) < 0.05
    return float(ok.mean() + glatt.mean())


def beste_lage(b: bytes, stride: int) -> int:
    kopf = min(len(b) // 2, 8192)
    beste, wert = 0, -1.0
    for off in range(0, min(kopf, stride * 2), 1 if stride < 64 else 2):
        f32, _ = felder(b, stride, off)
        if len(f32) < 20:
            continue
        w = bewertung(f32[: 5000])
        if w > wert:
            beste, wert = off, w
    return beste


def verdacht(f32: np.ndarray, j: int) -> str:
    x = f32[:, j]
    with np.errstate(all="ignore"):
        if not np.all(np.isfinite(x)) or np.nanmax(np.abs(x)) > 1e7:
            return ""
        d = np.diff(x)
        if len(d) and np.all(d >= 0) and np.ptp(x) > 0:
            gleich = np.std(d) / (np.mean(d) + 1e-12) < 0.2
            return "Zeit? (steigt" + (", gleichmäßig" if gleich else "") + f", Schritt {np.median(d):.4g})"
        if j + 3 < f32.shape[1]:
            q = f32[:, j: j + 4]
            if np.all(np.isfinite(q)):
                norm = np.sqrt((q * q).sum(axis=1))
                if np.abs(norm - 1).max() < 1e-3:
                    return "Quaternion? (Felder j..j+3, Norm 1)"
        if j + 2 < f32.shape[1]:
            v = f32[:, j: j + 3]
            if np.all(np.isfinite(v)):
                norm = np.sqrt((v * v).sum(axis=1))
                if np.abs(norm - 1).max() < 1e-3:
                    return "Richtungsvektor? (j..j+2, Norm 1)"
        if np.ptp(x) == 0:
            return "konstant"
        if np.nanmax(np.abs(x)) > 500 and np.nanmedian(np.abs(d)) < 0.01 * np.ptp(x):
            return "Position/Höhe? (groß, glatt)"
    return ""


def bericht(pfad: Path, stride: int | None, offset: int | None, csv: Path | None):
    roh = pfad.read_bytes()
    daten, art = entpacken(roh)
    print(f"# {pfad.name}: {len(roh):,} B, entpackt: {art} -> {len(daten):,} B")
    print(f"Entropie {entropie(daten[:1_000_000]):.2f} bit/Byte (roh {entropie(roh[:1_000_000]):.2f})")
    print(f"Kopf: {daten[:48].hex(' ')}")
    s = zeichenketten(daten)
    if s:
        print("Zeichenketten:", " | ".join(s))
    p = perioden(daten)
    print("Perioden (Frame-Länge?, Stärke über Median):", ", ".join(f"{a} B x{w:.2f}" for a, w in p))
    if stride is None:
        if not p:
            return
        stride = p[0][0]
    if offset is None:
        offset = beste_lage(daten, stride)
    f32, i32 = felder(daten, stride, offset)
    print(f"\n## Struktur: Frame {stride} B ab Byte {offset} -> {len(f32):,} Frames")
    print(f"{'Feld':>5} {'Byte':>5} {'min':>12} {'max':>12} {'Mittel':>12} {'Std':>11}  int32-Bereich           Verdacht")
    for j in range(f32.shape[1]):
        x = f32[:, j]
        fin = x[np.isfinite(x)]
        if len(fin):
            st = f"{fin.min():12.5g} {fin.max():12.5g} {fin.mean():12.5g} {fin.std():11.4g}"
        else:
            st = f"{'nan':>12} " * 3 + f"{'':>11}"
        ii = i32[:, j]
        print(f"{j:5d} {offset + 4 * j:5d} {st}  {ii.min():>10d}..{ii.max():<11d} {verdacht(f32, j)}")
    if csv:
        np.savetxt(csv, f32, delimiter=";", fmt="%.6g", header=";".join(f"f{j}" for j in range(f32.shape[1])), comments="")
        print(f"\nTabelle -> {csv}")


def vergleich(pfade: list[Path]):
    daten = [entpacken(p.read_bytes())[0] for p in pfade]
    gemeinsam = 0
    while gemeinsam < min(map(len, daten)) and len({d[gemeinsam] for d in daten}) == 1:
        gemeinsam += 1
    print(f"Gemeinsamer Anfang: {gemeinsam} B  ({daten[0][:gemeinsam][:64].hex(' ')})")
    for p, d in zip(pfade, daten):
        print(f"- {p.name}: {len(d):,} B entpackt")
    g = [len(d) for d in daten]
    if len(g) == 2 and g[0] != g[1]:
        diff = abs(g[0] - g[1])
        teiler = [s for s in range(8, 1025) if diff % s == 0]
        print(f"Größendifferenz {diff:,} B, teilbar durch (Kandidaten Frame-Länge): {teiler[:20]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dateien", nargs="+", type=Path)
    ap.add_argument("--stride", type=int)
    ap.add_argument("--offset", type=int)
    ap.add_argument("--csv", type=Path)
    a = ap.parse_args()
    if len(a.dateien) > 1:
        vergleich(a.dateien)
        print()
    for p in a.dateien:
        bericht(p, a.stride, a.offset, a.csv if len(a.dateien) == 1 else None)
        print()


if __name__ == "__main__":
    main()
