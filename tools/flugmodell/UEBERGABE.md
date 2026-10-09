# Übergabe: Flugmodell, Replays, 3D-Lehre

Stand 2026-10-09, aus einer Claude-Code-Session auf dem Mac. Diese Datei ist der Einstieg für die Weiterarbeit auf dem Windows-PC, auf dem VFM installiert ist.

## Ziel

1. VFM-Flugmodell nachbauen und an die Spieldaten kalibrieren.
2. Echte Kämpfe aus VFM-Replays auswerten.
3. BFM-Situationen interaktiv in 3D zeigen: Szenario einfrieren, Lift Vector und G wählen, vorspulen, Alternativen vergleichen. Ziel ist ein mentales Modell ohne Echtzeitstress.
4. Strategien je Jet-Paarung per Simulation prüfen.

## Was bisher feststeht

**Modell-Fit (`fit.py`):** Ein Punktmassen-Modell mit 8 Parametern je Jet (Lift-Limit mit Mach-Abfall, Schub mit Höhen-Lapse, Widerstandspolare mit transsonischem Anstieg) trifft die Tabellenwerte der Ingame-Analyse aus allen vier Bedingungen auf etwa ±0,5 °/s und ±10 KIAS Corner Speed.

- Fittet man nur auf 10.000 ft, extrapoliert das Modell schlecht auf 0 ft und 21.500 ft (T-16 auf 21.500 ft völlig daneben). Mit vier Tabellenwerten je Bedingung ist es unterbestimmt.
- Die vollen Sustained-Kurven in den Screenshots (`docs/public/images/img4–7.jpg`) würden das lösen. Das automatische Digitalisieren ist noch offen: Die Kurvenfarben liegen bei Hue ~20–40 (T-15), ~210–230 (T-16) und ~300–330 (T-18). Die senkrechten Markerlinien sind zu blass für einfache Schwellwerte.
- 6-DOF ist nicht nötig. Für BFM reicht eine Punktmasse plus begrenzte Rollrate für den Lift Vector.

**Was in den Daten fehlt:** Rollrate, G-Onset, Verhalten unter ~170 KIAS, Override und Post-Stall, Beschleunigung und Steigen, Speedbrake, Greyout, Raketen- und Gun-Ballistik. Außerdem sind alle Daten von vor Patch v1.1; aktuell ist v1.4.2.

**Replays:** VFM hat eine Replay-Szene mit S-Cam. Die Patch Notes zu v1.2.8 nennen „AoA desync in replays reduziert“, das spricht für aufgezeichnete Flugzustände statt Video. Ein Export (Tacview/ACMI), ein dokumentiertes Format oder Mod-Support ist nicht bekannt. Engine: Unity.

## Nächste Schritte auf dem Windows-PC

1. **Installation ansehen** (nur lesen, nichts verändern):
   - Steam-Ordner finden: `Steam\steamapps\common\Virtual Fighter Maneuvers\` (Name prüfen).
   - Mono oder IL2CPP? `*_Data\Managed\Assembly-CSharp.dll` heißt Mono (Code mit ILSpy lesbar), `GameAssembly.dll` heißt IL2CPP (deutlich schwerer).
   - Liegen lesbare Konfigurationsdateien herum (`.json`, `.xml`, `.txt`, `.ini`, `StreamingAssets\`)? Flugzeugparameter stecken bei Unity meist binär in `*.assets` oder Asset-Bundles, nicht als Klartext.
2. **Replays finden:** typischerweise `%USERPROFILE%\AppData\LocalLow\<Firma>\<Spiel>\` oder `Documents\`. Dateigröße, Endung und die ersten Bytes (Hexdump) anschauen. Ist es Text, JSON, komprimiert (gzip/zlib) oder ein eigenes Binärformat?
3. **Format entschlüsseln:** einen bekannten, kurzen Kampf aufnehmen (z. B. 30 s geradeaus, dann ein 9-G-Kreis) und schauen, welche Werte sich wie ändern.
4. **Regeln:** Vor dem Auslesen von Spieldateien die EULA prüfen. Nur offline arbeiten, nie etwas ins laufende Spiel injizieren (Ranked, möglicher Anti-Cheat). Alternativ beim Entwickler (Boundless Dynamics) nach einem Tacview-Export fragen.

## Setup

```bash
cd tools/flugmodell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python fit.py
```
