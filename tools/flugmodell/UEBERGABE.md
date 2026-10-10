# Übergabe: Flugmodell, Replays, 3D-Lehre

Stand 2026-10-10. Diese Datei ist der Einstieg für die Weiterarbeit, auch auf dem Windows-PC, auf dem VFM installiert ist.

## Ziel

1. VFM-Flugmodell nachbauen und an die Spieldaten kalibrieren.
2. Echte Kämpfe aus VFM-Replays auswerten.
3. BFM-Situationen interaktiv in 3D zeigen: Szenario einfrieren, Lift Vector und G wählen, vorspulen, Alternativen vergleichen. Ziel ist ein mentales Modell ohne Echtzeitstress.
4. Strategien je Jet-Paarung per Simulation prüfen.

## Dateien

| Datei | Inhalt |
|---|---|
| `daten/screens_2026-10/` | 9 Screenshots der Ingame-„Aircraft Performance Analysis“ (0 / 10.000 / 20.190 ft × 0 / ~50 / 100 % Fuel), aufgenommen Oktober 2026 |
| `daten/tabellen_2026-10.csv` | Tabellenwerte aus den Screenshots (Gewicht, Instant, Sustained, Min Radius) |
| `digitalisieren.py` | liest die Kurven aus den Screenshots → `daten/kurven_2026-10.csv`, Kontrollbilder in `daten/kontrolle/` |
| `modell.py` | fittet das Flugmodell, Kreuzvalidierung, → `daten/modell_parameter.json`, `daten/kontrolle/modell_fit.png` |
| `messflug.py` | wertet aus Videos abgelesene Messflüge aus (Beschleunigung → Schub-Maßstab, Kurve → Validierung) |

## Was bisher feststeht

**Digitalisierung:** Achsen und jede Gitterlinie werden einzeln gefittet; eine Homographie fängt die VR-Perspektive ab (Rest ~1 px). Die erste vertikale Gitterlinie liegt bei 200 KIAS, die Markerlinien treffen die Tabellen-KIAS auf ±2 KIAS. Gitter: 4 °/s bzw. 50 KIAS je Linie.

**Spiel-Atmosphäre (aus den Daten, nicht ISA):**
- Wahre Fahrt / KIAS, gemessen an der 9G-Linie (ω = g·√80 / V): 0,994 (0 ft), 1,115 (10.000 ft), 1,276 (20.190 ft). Echte Standardatmosphäre: 1,15 / 1,31 (CAS).
- Das Lift-Limit (n·W / q) fällt bei allen drei Jets im selben Verhältnis mit der Höhe. Erklärt durch die Dichte ρ = ρ0 · exp(−h / 8.340 m): 0,694 auf 10.000 ft, 0,478 auf 20.190 ft (ISA: 0,738 / 0,543).
- Die Schallgeschwindigkeit im Spiel ist unbekannt; das Modell nimmt ISA-Temperatur an.

**Struktur des Flugmodells (modellfrei bestätigt):**
- n_sustained · Gewicht ist bei gleicher Höhe und KIAS über alle Fuel-Stände konstant (< 1 %). Daraus folgt: Schub ist gewichtsunabhängig, und der induzierte Widerstand wächst mit (n·W)².
- Corner = genau 9 G (Min Radius passt zu V²/(g·√80)).

**Modell (`modell.py`):** Punktmasse; Lift-Limit S·CLmax(M) quadratisch in Mach; Schub = t0 · σ^x · τ(M); Nullwiderstand cd0(M); τ und cd0 stückweise linear über Mach (Stützstellen alle 0,1 Mach, geglättet). Die Sustained-Kurven von VFM haben Knicke und Plateaus, eine geschlossene Formel reicht nicht.

| | RMS-Fehler Sustained, 300–550 KIAS |
|---|---|
| Fit auf allen Höhen | 0,10–0,17 °/s (T-15, T-16), 0,14–0,56 °/s (T-18) |
| Vorhersage einer weggelassenen Höhe | 0,23–0,37 °/s (T-15, T-16), 0,49–1,12 °/s (T-18) |
| Corner Speed | ±4 KIAS (T-16 einmal 8,5) |

**Energie-Maßstab (aus den Diagrammen nicht bestimmbar) – T-15 gemessen:** Beschleunigungsläufe im Quest-Video (`daten/messflug_t15_2026-10-10.csv`, ausgewertet mit `messflug.py`), 10.000 ft, 100 % Fuel, Nachbrenner:
- 300 → 550 KIAS mit ~23–24 kt/s (KIAS) bzw. ~26–27 kt/s wahre Fahrt, leicht steigend; zwei Läufe fast deckungsgleich.
- Schubüberschuss bei 1 G: (T − D)/W = 1,33–1,44 von Mach 0,54 bis 0,95. Kalibriert: **T/W ≈ 1,75** (Meereshöhe, M 0,4, 50 % Fuel). Das Modell trifft die Läufe danach auf 4 % RMS; es unterschätzt den Überschuss nahe Mach 0,9 etwas (gemeinsamer Fit von Diagrammen und Beschleunigung würde das verbessern).
- Unabhängige Prüfung durch eine Kurve (447 KIAS, ~7 G, ~15 °/s, 16 s): Modell-Sustained 7,07 G, geflogen 6,93 G bei leichtem Energieverlust → Modell ~2 % optimistisch.
- Nebenbefunde: Schallgeschwindigkeit im Spiel auf ~10.000 ft ≈ 630 kt (ISA 638); die HUD-Drehrate passt zu g·√(n²−1)/V mit der Modell-Atmosphäre auf 2 %.
- HUD (T-15): oben links G und Drehrate °/s, darunter Speed (KIAS), Mach und α; rechts Höhe; „BRAKE“ unten rechts bei ausgefahrener Speedbrake. Fuel Flow im Cockpit (Nachbrenner ~115.000–140.000 PPH).
- **T-16 und T-18 fehlen noch** (gleiches Protokoll: 10.000 ft, Vollgas ab ~250 KIAS bis ~550, Kopf so, dass das HUD komplett im Bild ist; Kurve mit Blick durchs HUD).

**Datenstand vs. Wiki:** T-15 und T-18 zeigen exakt dieselben Werte wie die Wiki-Screenshots von Dez 2025. Die T-16 ist durch −20 % Treibstoffgewicht leichter (50 %: 24.417 statt 25.009 lbs) und etwas besser (Meereshöhe 50 %: 26 °/s @ 378 statt 25 @ 392, Min Radius 1.428 statt 1.524 ft). Die Wiki-Angabe „vor v1.1“ stimmt vermutlich nicht.

**Was weiter fehlt:** Rollrate, G-Onset, Verhalten unter ~170 KIAS, Override und Post-Stall, Speedbrake, Greyout, Raketen- und Gun-Ballistik.

**Replays:** VFM hat eine Replay-Szene mit S-Cam. Die Patch Notes zu v1.2.8 nennen „AoA desync in replays reduziert“, das spricht für aufgezeichnete Flugzustände. Ein Export (Tacview/ACMI), ein dokumentiertes Format oder Mod-Support ist nicht bekannt. Engine: Unity.

## Nächste Schritte auf dem Windows-PC

1. **Installation ansehen** (nur lesen, nichts verändern):
   - Steam-Ordner finden: `Steam\steamapps\common\Virtual Fighter Maneuvers\` (Name prüfen).
   - Mono oder IL2CPP? `*_Data\Managed\Assembly-CSharp.dll` heißt Mono (Code mit ILSpy lesbar), `GameAssembly.dll` heißt IL2CPP (deutlich schwerer).
   - Lesbare Konfigurationsdateien (`.json`, `.xml`, `.txt`, `.ini`, `StreamingAssets\`)? Flugzeugparameter stecken bei Unity meist binär in `*.assets`.
   - Falls Parameter lesbar sind: mit `modell.py` vergleichen (Atmosphäre, Schubkurve über Mach, CLmax).
2. **Replays finden:** typischerweise `%USERPROFILE%\AppData\LocalLow\<Firma>\<Spiel>\` oder `Documents\`. Größe, Endung, erste Bytes (Hexdump): Text, JSON, gzip/zlib oder eigenes Binärformat?
3. **Format entschlüsseln:** einen kurzen, bekannten Flug aufnehmen (30 s geradeaus mit Vollgas, dann ein 9-G-Kreis) und schauen, welche Werte sich wie ändern. Derselbe Flug liefert gleich die fehlende Beschleunigungsmessung.
4. **Regeln:** Vor dem Auslesen von Spieldateien die EULA prüfen. Nur offline arbeiten, nie etwas ins laufende Spiel injizieren (Ranked, möglicher Anti-Cheat).

## Setup

```bash
cd tools/flugmodell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python digitalisieren.py
.venv\Scripts\python modell.py
```
