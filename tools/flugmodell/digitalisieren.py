"""Liest die Turn-Rate-Kurven aus den VFM-Screenshots ("Aircraft Performance Analysis").

Ablauf je Bild:
1. Achsen (hellgrün) als Geraden finden, Plot grob auf Achsenkoordinaten entzerren (affin).
2. Jede Gitterlinie einzeln fitten (horizontal = 4 °/s, vertikal = 50 KIAS), aus den Schnittpunkten
   eine Homographie bestimmen. Das fängt die VR-Perspektive ab.
3. Markerlinien (senkrecht, Jetfarbe) an Corner- und Sustained-KIAS aus der Tabelle legen den
   KIAS-Nullpunkt fest.
4. Plot in Datenkoordinaten (1 KIAS x 0,05 °/s je Pixel) umrechnen. Je Jet und KIAS-Spalte:
   unterster Farbcluster = Sustained (durchgezogen), oberster = Instant (gestrichelt).

Aufruf: python digitalisieren.py  -> daten/kurven_2026-10.csv und Kontrollbilder in daten/kontrolle/
"""
import csv
import os
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import map_coordinates, median_filter
from scipy.signal import find_peaks

HIER = os.path.dirname(os.path.abspath(__file__))
DATEN = os.path.join(HIER, 'daten')
BILDER = os.path.join(DATEN, 'screens_2026-10')
JETS = ['T-15', 'T-16', 'T-18']
HUE = {'T-15': (15, 45), 'T-16': (195, 232), 'T-18': (300, 340)}
DR = 0.05  # °/s je Zeile im Datenraster


def hsv(rgb):
    a = rgb / 255.0
    mx, mn = a.max(-1), a.min(-1)
    d = mx - mn + 1e-9
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    return h, d / (mx + 1e-9), mx


def achse(ys, xs, waagrecht, zentrum):
    """Längste Gerade in hellgrünen Pixeln per Winkel-Suche, dann Kleinste Quadrate."""
    best = None
    for t in np.radians(np.arange(-5, 5.01, 0.1)):
        p = ys - np.tan(t) * (xs - zentrum) if waagrecht else xs - np.tan(t) * (ys - zentrum)
        hist = np.bincount(np.clip(p, 0, None).astype(int))
        k = hist.argmax()
        if best is None or hist[k] > best[0]:
            best = (hist[k], t, k)
    _, t, k = best
    p = ys - np.tan(t) * (xs - zentrum) if waagrecht else xs - np.tan(t) * (ys - zentrum)
    sel = np.abs(p - k) < 6
    if waagrecht:
        b, a = np.polyfit(xs[sel], ys[sel], 1)   # y = a + b x
    else:
        b, a = np.polyfit(ys[sel], xs[sel], 1)   # x = a + b y
    return a, b


def homographie(src, dst):
    """DLT: dst ~ H @ src (je 2D-Punkte)."""
    A = []
    for (x, y), (u, v) in zip(src, dst):
        A.append([-x, -y, -1, 0, 0, 0, u * x, u * y, u])
        A.append([0, 0, 0, -x, -y, -1, v * x, v * y, v])
    _, _, vt = np.linalg.svd(np.array(A))
    H = vt[-1].reshape(3, 3)
    return H / H[2, 2]


def anwenden(H, x, y):
    w = H[2, 0] * x + H[2, 1] * y + H[2, 2]
    return (H[0, 0] * x + H[0, 1] * y + H[0, 2]) / w, (H[1, 0] * x + H[1, 1] * y + H[1, 2]) / w


def linie_robust(t, p):
    """p = a + b t, mit Ausreißer-Entfernung."""
    sel = np.ones(len(t), bool)
    for _ in range(4):
        b, a = np.polyfit(t[sel], p[sel], 1)
        r = np.abs(p - (a + b * t))
        sel = r < max(1.0, 2.5 * np.median(r[sel]))
    return a, b, sel.sum()


def gitter(gex, off, U, V):
    """Gitterlinien im affin entzerrten Raster finden und einzeln fitten."""
    prof_v = np.median(gex[:, off + 40:off + 600], axis=1)
    pk = find_peaks(prof_v, distance=40, prominence=0.4)[0] - off
    pk = pk[(pk > 20) & (pk < V - 30)]
    sv = np.median(np.diff(pk))
    prof_u = np.median(gex[off + 30:off + 450, :], axis=0)
    pku = find_peaks(prof_u, distance=30, prominence=0.4)[0] - off
    pku = pku[pku > 20]
    su = np.median(np.diff(pku))
    # zusammenhängende Folge gleichmäßiger Abstände behalten
    pku = pku[np.abs((pku - pku[0]) / su - np.round((pku - pku[0]) / su)) < 0.2]
    pk = pk[np.abs(pk / sv - np.round(pk / sv)) < 0.2]
    hor, ver = {}, {}
    umax, vmax = pku.max() + 5, pk.max() + 5
    for v0 in pk:
        k = int(round(v0 / sv))
        ts, ps = [], []
        for u in range(30, int(umax), 12):
            st = gex[off + int(v0) - 8:off + int(v0) + 9, off + u:off + u + 12]
            prof = np.median(st, axis=1)
            if prof.max() - np.median(prof) > 2:
                ts.append(u + 6); ps.append(v0 - 8 + np.argmax(prof))
        if len(ts) > 8:
            hor[k] = linie_robust(np.array(ts, float), np.array(ps, float))
    hor[0] = None  # x-Achse kommt aus der Achsen-Geraden (v = 0)
    for u0 in pku:
        j = int(round((u0 - pku[0]) / su))
        ts, ps = [], []
        for v in range(15, int(vmax), 12):
            st = gex[off + v:off + v + 12, off + int(u0) - 8:off + int(u0) + 9]
            prof = np.median(st, axis=0)
            if prof.max() - np.median(prof) > 2:
                ts.append(v + 6); ps.append(u0 - 8 + np.argmax(prof))
        if len(ts) > 8:
            ver[j] = linie_robust(np.array(ts, float), np.array(ps, float))
    return hor, ver, pku[0], su, sv


def digitalisiere(bild, tabelle):
    rgb = np.asarray(Image.open(os.path.join(BILDER, bild + '.jpg')).convert('RGB')).astype(float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    hell = (G > 95) & (R < 75) & (B < 75)
    ys, xs = np.nonzero(hell[700:1000, 1000:1990]); ys = ys + 700; xs = xs + 1000
    ax_a, ax_b = achse(ys, xs, True, 1500)
    ys, xs = np.nonzero(hell[250:1000, 1000:1300]); ys = ys + 250; xs = xs + 1000
    ay_a, ay_b = achse(ys, xs, False, 600)
    y0 = (ax_a + ax_b * ay_a) / (1 - ax_b * ay_b)
    x0 = ay_a + ay_b * y0
    ex = np.array([1, ax_b]) / np.hypot(1, ax_b)
    ey = np.array([-ay_b, -1]) / np.hypot(1, ay_b)
    aff = lambda u, v: (x0 + u * ex[0] + v * ey[0], y0 + u * ex[1] + v * ey[1])

    off, U, V = 10, 960, 700
    uu, vv = np.meshgrid(np.arange(-off, U), np.arange(-off, V))
    px, py = aff(uu, vv)
    warp = np.stack([map_coordinates(rgb[..., c], [py, px], order=1) for c in range(3)], -1)
    gex = warp[..., 1] - 0.5 * (warp[..., 0] + warp[..., 2])
    hor, ver, u_first, su, sv = gitter(gex, off, U, V)

    # Schnittpunkte Gitter (j, k) -> affine Koordinaten (u, v); x-Achse ist v = 0
    src, dst = [], []
    for k, hl in hor.items():
        for j, vl in ver.items():
            a2, b2, _ = vl                   # u = a2 + b2 v
            if hl is None:
                v = 0.0
            else:
                a1, b1, _ = hl               # v = a1 + b1 u
                v = (a1 + b1 * a2) / (1 - b1 * b2)
            u = a2 + b2 * v
            src.append((j, k)); dst.append((u, v))
    src, dst = np.array(src, float), np.array(dst, float)
    sel = np.ones(len(src), bool)            # robust: Schnittpunkte falsch erkannter Linien verwerfen
    for _ in range(5):
        Hgu = homographie(src[sel], dst[sel])    # Gitter -> affin
        gu = np.array(anwenden(Hgu, src[:, 0], src[:, 1])).T
        res = np.sqrt(((gu - dst) ** 2).sum(1))
        sel = res < max(1.5, 3 * np.median(res[sel]))
    gitter_rest = res[sel].max()
    n_schnitt = (sel.sum(), len(sel))

    # Datenraster: Spalte = KIAS (relativ zur ersten Gitterlinie), Zeile = Rate
    kias_rel = np.arange(-120, 50 * (max(ver) + 1) + 1, 1.0)
    rate = np.arange(0, 33, DR)
    KK, RR = np.meshgrid(kias_rel, rate)
    gu_, gv_ = anwenden(Hgu, KK / 50, RR / 4)
    ix, iy = aff(gu_, gv_)
    dat = np.stack([map_coordinates(rgb[..., c], [iy, ix], order=1) for c in range(3)], -1)
    h, s, v = hsv(dat)

    # Marker: in 0,5..5 °/s fast durchgehend farbig
    band = slice(int(0.5 / DR), int(5 / DR))
    farbig = (s[band] > 0.35) & (v[band] > 0.22) & ~((h[band] > 85) & (h[band] < 160))
    cols = np.nonzero(farbig.mean(0) > 0.8)[0]
    gruppen = np.split(cols, np.nonzero(np.diff(cols) > 2)[0] + 1) if len(cols) else []
    marker = [kias_rel[g].mean() for g in gruppen if len(g)]
    soll = sorted({tabelle[j][f] for j in JETS for f in ('corner_kias', 'sustained_kias')})
    # Nullpunkt: KIAS = K0 + kias_rel; K0 so, dass Marker die Sollwerte treffen
    best = None
    for K0 in np.arange(0, 400, 0.5):
        f = sum(min(min(abs(K0 + m - s_) for m in marker), 10) for s_ in soll)
        if best is None or f < best[0]:
            best = (f, K0)
    K0 = best[1]
    assert abs(K0 - 200) < 5, f'erste Gitterlinie bei {K0} KIAS statt 200'
    K0 = 200.0                               # Gitterlinien liegen auf 50er-KIAS; Marker = Kontrolle
    rest = [round(min(abs(K0 + m - s_) for m in marker), 1) for s_ in soll]

    punkte = []
    for jet in JETS:
        lo, hi = HUE[jet]
        m = (h >= lo) & (h <= hi) & (s > 0.45) & (v > 0.35)
        for ci, kr in enumerate(kias_rel):
            if any(abs(kr - mk) <= 3 for mk in marker):
                continue
            col = np.nonzero(m[3:, ci])[0] + 3
            if len(col) == 0:
                continue
            grp = np.split(col, np.nonzero(np.diff(col) > 4)[0] + 1)
            zent = [g.mean() * DR for g in grp]
            punkte.append((jet, 'sustained', K0 + kr, zent[0]))
            if len(zent) > 1:
                punkte.append((jet, 'instant', K0 + kr, zent[-1]))

    def bildpunkt(kias, r):
        gu_, gv_ = anwenden(Hgu, (kias - K0) / 50, r / 4)
        return aff(gu_, gv_)

    info = dict(marker_rest=rest, gitter_rest=gitter_rest, K0=best[1], n_h=len(hor), n_v=len(ver), n_schnitt=n_schnitt)
    return punkte, info, bildpunkt


def glaette(punkte):
    """Ausreißer je Jet/Kurve entfernen (Verdeckung durch andere Kurven).

    Sustained wird als stetige Kurve verfolgt: ein Punkt zählt nur, wenn er vom zuletzt akzeptierten
    Punkt um höchstens 0,8 °/s + 0,08 °/s je KIAS Abstand abweicht. Sonst springt man auf die
    gestrichelte 9G-Linie, wo die durchgezogene Kurve verdeckt ist oder schon auf der Achse liegt.
    Erreicht die Kurve die Achse (< 0,5 °/s), endet sie dort.
    """
    out = []
    for jet in JETS:
        for art in ['sustained', 'instant']:
            p = sorted([q for q in punkte if q[0] == jet and q[1] == art], key=lambda q: q[2])
            if len(p) < 9:
                continue
            r = np.array([q[3] for q in p])
            med = median_filter(r, size=15, mode='nearest')
            p = [q for q, rr, mm in zip(p, r, med) if abs(rr - mm) < 0.4]
            if art == 'sustained':
                ok, letzt = [], None
                for q in p:
                    if letzt is not None and letzt[3] < 0.5:
                        break                    # Kurve ist auf der Achse angekommen: Ende
                    if letzt is None or abs(q[3] - letzt[3]) <= min(0.8 + 0.08 * (q[2] - letzt[2]), 3):
                        ok.append(q); letzt = q
                p = ok
            out += p
    return out


def main():
    tab = {}
    with open(os.path.join(DATEN, 'tabellen_2026-10.csv')) as f:
        for r in csv.DictReader(f):
            tab.setdefault(r['bild'], {})[r['jet']] = {k: float(v) for k, v in r.items() if k not in ('bild', 'jet')}
    os.makedirs(os.path.join(DATEN, 'kontrolle'), exist_ok=True)
    zeilen = []
    for bild in sorted(tab):
        punkte, info, bildpunkt = digitalisiere(bild, tab[bild])
        punkte = glaette(punkte)
        print(f"{bild}: Gitter {info['n_h']}x{info['n_v']} Linien, {info['n_schnitt'][0]}/{info['n_schnitt'][1]} Schnittpunkte, Rest max {info['gitter_rest']:.2f} px, "
              f"Marker-Fit {info['K0']:.1f}, Marker-Rest (KIAS) {[float(x) for x in info['marker_rest']]}, {len(punkte)} Punkte")
        im = Image.open(os.path.join(BILDER, bild + '.jpg')).convert('RGB')
        d = ImageDraw.Draw(im)
        for jet, art, k, r in punkte[::3]:
            x, y = bildpunkt(k, r)
            d.point((x, y), fill=(255, 255, 255) if art == 'sustained' else (255, 255, 0))
        for kias in range(150, 1000, 50):   # Soll-Gitter zur Kontrolle
            pts = [bildpunkt(kias, r) for r in (0, 32)]
            d.line(pts, fill=(255, 0, 0))
        for r in range(0, 33, 4):
            pts = [bildpunkt(k, r) for k in (150, 950)]
            d.line(pts, fill=(255, 0, 0))
        im.crop((1000, 230, 2000, 1000)).save(os.path.join(DATEN, 'kontrolle', bild + '.png'))
        for jet, art, k, r in punkte:
            t = tab[bild][jet]
            zeilen.append([bild, int(t['hoehe_ft']), int(t['fuel_pct']), jet, int(t['gewicht_lbs']), art,
                           round(k, 1), round(r, 3)])
    with open(os.path.join(DATEN, 'kurven_2026-10.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['bild', 'hoehe_ft', 'fuel_pct', 'jet', 'gewicht_lbs', 'kurve', 'kias', 'rate_dps'])
        w.writerows(zeilen)


if __name__ == '__main__':
    main()
