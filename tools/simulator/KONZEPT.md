# BFM-Simulator: Konzept und Auftrag

Stand 2026-10-10. Dieses Dokument ist der Auftrag für die Umsetzung in einer eigenen Session. Es fasst zusammen, was gebaut werden soll, welche Daten es gibt und was vorher am Flugmodell noch zu tun ist. Die Datenherkunft steht in [`../flugmodell/UEBERGABE.md`](../flugmodell/UEBERGABE.md).

## Ziel

Ein interaktiver 3D-Simulator im Browser, der BFM-Situationen der drei VFM-Jets (T-15 Excalibur, T-16 Falchion, T-18 Cutlass) **ohne Echtzeitstress** erfahrbar macht. Der Pilot soll ein mentales Modell aufbauen, das ihm im echten Kampf hilft, schnell die richtige Entscheidung zu treffen.

Nicht das Ziel: ein zweiter Flugsimulator zum Selberfliegen in Echtzeit, ein 6-DOF-Nachbau oder ein Ersatz für VFM.

## Kernidee: einfrieren, entscheiden, vorspulen, vergleichen

1. **Szenario laden**, eingefroren. Zwei Jets mit Position, Speed, Höhe, Flugrichtung, G und Fuel, Typen frei wählbar.
2. **Entscheiden ohne Zeitdruck**: Lift Vector rollen (Querlage relativ zum Gegner), G bzw. α wählen, Schub (Leerlauf, Mil, Nachbrenner), optional Speedbrake.
3. **Vorspulen** um 1–5 s. Beide Jets fliegen, der Gegner nach einer wählbaren Taktik.
4. **Verzweigen und vergleichen**: Mehrere Entscheidungen aus demselben eingefrorenen Zustand nebeneinander als Geisterbahnen. Ergebnis je Zweig: Winkel, Abstand, Energie, Schussgelegenheit für wen.
5. **Lektionen** aus den Wiki-Seiten: Jedes Szenario verlinkt die passende Seite und stellt eine Frage („Was machst du jetzt?“). Die Auflösung zeigt die Musterlösung als Zweig.

### Was sichtbar sein muss

- Flugbahnen beider Jets (Vergangenheit und Vorhersage) als Bänder, die Querlage und G zeigen.
- Lift Vector und **Bewegungsebene** (Plane of Motion) als halbtransparente Scheibe.
- **Kurvenkreise** beider Jets bei aktueller Speed und G; die **Bubble** des Gegners (sein Kurvenkreis, seine 3/9-Linie, Gun-Reichweite als Annahme).
- Nasenrichtung getrennt vom Geschwindigkeitsvektor (α sichtbar machen, wichtig für die T-18).
- Energie: Speed, Höhe, Energiehöhe, Ps als Balken oder Farbe. Ein kleines E-M-Diagramm (Turn Rate über KIAS) mit dem aktuellen Punkt beider Jets.
- Geometrie-Kennzahlen: Range, Aspect Angle, ATA, HCA, Closure, LOS-Rate.
- Kameras: Verfolger, Gegner, Draufsicht, frei; Cockpit-Sicht mit vereinfachtem HUD.

## Flugmodell (Punktmasse mit begrenzter Rollrate)

Zustand je Jet: Position, Geschwindigkeitsvektor, Querlage um den Geschwindigkeitsvektor, Lastvielfaches n, α, Gewicht (Fuel), Schubstufe. Integration mit festem Zeitschritt (z. B. 1/120 s), deterministisch, damit Zweige reproduzierbar sind.

Kräfte:
- **Auftrieb** n·W senkrecht zur Bahn in Richtung Lift Vector. Begrenzt durch das 9-G-Limit und das **Flug-Lift-Limit** (siehe Messungen: ~85–92 % des Diagramm-Lift-Limits ohne Override).
- **Schub** T(h, M, Stufe), **Widerstand** D(h, M, n) = Nullwiderstand + induzierter Widerstand (nichtlinear bei hohem α).
- **Schwerkraft**.
- Dynamik: G-Aufbau zum Höchstwert in ~2–3 s (gemessen), Rollrate (noch nicht gemessen, vorläufig ~180–270 °/s als Annahme, einstellbar).

### Vorhandene Grundlage

`tools/flugmodell/modell.py` (Python) mit Parametern in `daten/modell_parameter.json`:
- **Spiel-Atmosphäre**: Dichte ρ = ρ0·exp(−h / 8.340 m); wahre Fahrt / KIAS ≈ 1,00 / 1,115 / 1,276 auf 0 / 10.000 / 20.190 ft. Schallgeschwindigkeit ~630 kt auf 10.000 ft (ISA 638).
- **Lift-Limit** S·CLmax(M) je Jet, aus den Diagrammen (Corner ±4 KIAS).
- **Sustained-Kurven** aller 27 Bedingungen auf ~0,1–0,5 °/s getroffen (300–550 KIAS).
- **Maßstab** `MASSSTAB_C` je Jet aus den Beschleunigungsläufen: Der Überschuss T − D bei 1 G stimmt.

### Muss vor dem Simulator neu gefittet werden

Die Aufteilung in Schub und Widerstand im Modell ist **falsch** (nur T − D stimmt), und der Widerstand bei hohem α fehlt. Für einen Lernsimulator ist das kritisch, weil harte Züge sonst viel zu „billig“ wirken (Energieverlust im vollen Zug bei der T-18 ~4-fach unterschätzt).

Neuer gemeinsamer Fit je Jet aus allen Datenquellen:

| Quelle | Datei | liefert |
|---|---|---|
| Ingame-Diagramme, 9 Bedingungen | `daten/kurven_2026-10.csv`, `daten/tabellen_2026-10.csv` | Ps = 0 bei n_sustained(KIAS, h, W); Lift-Limit |
| Beschleunigungsläufe 10.000 ft, voll | `daten/messflug_t1x_2026-10-10.csv` | T − D bei 1 G über Mach 0,5–1,0 |
| Ausrollen im Leerlauf | `daten/zug_t1x_2026-10-10.csv` (Phase `ausrollen`) | D bei 1 G über Mach 0,6–0,96 (Leerlaufschub ≈ 0) |
| Voller Zug ab ~450 KIAS | `daten/zug_t1x_2026-10-10.csv` (Phase `zug`) | erreichte G, α, Energieverlust bei hohem CL |
| Sustained-Kurve ~450 KIAS | `daten/messflug_t1x_2026-10-10.csv` (Phase `kurve`) | Validierung (Modell traf ±2–3 %) |

Vorschlag für die Struktur: T(M) und CD0(M) als glatte Stützstellen-Kurven über Mach, induzierter Widerstand K(M)·CL² plus ein Zusatzterm oberhalb eines α bzw. CL der Bestform (Post-CLmax-Widerstand); Flug-Lift-Limit als eigene Kurve CLmax_flug(M) bzw. α-Limit je Jet. Schubhöhenabhängigkeit σ^x aus den Diagrammen.

### Messwerte (alle 10.000 ft, voller Tank, nur Guns)

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| 300 → 500 KIAS mit Nachbrenner | ~8,4 s | ~11,5 s | ~12,3 s |
| (T − D)/W bei 1 G, 300–500 KIAS | ~1,40 | ~1,02 | ~0,95 |
| D/W bei 1 G im Leerlauf, 350–550 KIAS | 0,18–0,35 | 0,18–0,35 | 0,33–0,60 |
| T/W mit Nachbrenner (abgeleitet) | ~1,65 | ~1,26 | ~1,35 |
| Sustained bei ~450 KIAS (geflogen) | 7,0 G / 15,4 °/s | 7,9 G / 17,6 °/s | 7,0 G / 15,6 °/s |
| Voller Zug ab ~450 KIAS: Höchst-G | 9,1 G nach ~2 s | 8,4 G nach ~3 s | 8,7 G nach ~3 s |
| α am Anschlag (ohne Override) | ~24–25° | ~23° | bis 35° (G-Maximum bei ~26°) |
| G unterhalb Höchst-G / Diagramm-Lift-Limit | ~0,90 | ~0,92 | ~0,85 |
| Ps im vollen Zug (Ø ab Höchst-G) | −990 ft/s | −430 ft/s | −1.540 ft/s |
| Fuel Flow mit Nachbrenner | ~115.000–140.000 PPH | ~58.700 PPH | nicht abgelesen |

### Abnahmetests für das Modell

Der Simulator rechnet diese Flüge nach und muss sie innerhalb der Toleranz treffen (automatisierte Tests):
1. Sustained-Kurven der 27 Diagramm-Bedingungen: ±0,5 °/s im Band 300–550 KIAS.
2. Beschleunigungsläufe: Zeit 300 → 500 KIAS ±5 %.
3. Ausrollen: Speedverlauf 550 → 350 KIAS ±10 %.
4. Voller Zug ab 450 KIAS: Höchst-G ±0,3 G, Speed nach 5 s ±15 KIAS.
5. Sustained-Kurve bei ~450 KIAS: G ±3 %.

## Gegner-Taktiken (für das Vorspulen)

Einfache, nachvollziehbare Regeln reichen für die Lehre: Pure / Lead / Lag Pursuit auf den Spieler; Break Turn bei Bedrohung; Sustained-Kurve (Ps = 0); Max-Rate-Kurve; Extend mit Unload; Vertikal hoch / Slice nach unten. Später: Suchverfahren über diese Bausteine (z. B. Minimax über 1-s-Entscheidungen), um die beste Antwort pro Szenario vorzuschlagen und Matchups systematisch zu vergleichen.

## Szenarien für den Start

Jedes Szenario ist eine kleine JSON-Datei (Zustand beider Jets, Gegner-Taktik, Frage, Musterlösung, Wiki-Link). Erste Auswahl, abgeleitet aus den Wiki-Seiten:

1. **Overshoot droht** → High Yo-Yo statt weiterziehen (`grundlagen/offensiv/yo-yos.md`, `overshoot.md`).
2. **Lag Pursuit außerhalb der Bubble** (T-16 gegen T-18): Wer zu nah hineinzieht, gibt der T-18 die Nase (`grundlagen/verfolgungskurven.md`).
3. **Merge-Speed**: derselbe Merge mit 380, 450 und 550 KIAS nebeneinander (`grundlagen/neutral/der-merge.md`).
4. **One- vs. Two-Circle** je Paarung (`grundlagen/neutral/one-two-circle.md`).
5. **T-15 Energy Fight**: Extend direkt nach dem Merge vs. Extend aus dem Kreis heraus; Abstand und Speed-Vorsprung über die Zeit (`flugzeuge/t15.md#energy-fight-geht-das-mit-der-t-15`).
6. **T-18 Nasenautorität**: Zug mit α 26° vs. 35° – G, Nasenrichtung, Energie (`flugzeuge/vergleich.md#voller-zug-was-ohne-override-wirklich-geht`).
7. **Break Turn und Guns Defense**: Out-of-Plane gegen einen Tracking Shot (`grundlagen/defensiv/`).
8. **Slice Turn**: nose-low Rate gegen Energie (`grundlagen/defensiv/slice-turn.md`).

## Technik (Vorschlag)

- **TypeScript + Three.js**, gebaut mit Vite. Einbindung ins Wiki als Vue-Komponente (VitePress kann Vue-Komponenten in Markdown-Seiten einbetten), damit jede Wiki-Seite ihr Szenario direkt zeigen kann. Alternativ eine eigene Seite unter `docs/simulator/`.
- Physik in einem reinen TS-Modul ohne Three.js-Abhängigkeit (testbar mit Vitest, auch serverseitig für Batch-Analysen).
- Modellparameter als JSON aus `tools/flugmodell/` exportieren; das Python-Modell bleibt die Kalibrier-Werkstatt.
- Mobil und VR sind kein Startziel; Desktop-Browser zuerst.

## Später: echte Kämpfe

Replays aus VFM als Szenarioquelle: Format ist unbekannt (Unity, Replays enthalten offenbar Flugzustände). Wege: Replay-Dateien auf dem Windows-PC untersuchen, beim Entwickler einen Tacview-/ACMI-Export anfragen, oder Situationen aus dem Video nachstellen (HUD ablesen wie bei den Messflügen). Siehe `tools/flugmodell/UEBERGABE.md`.

## Offene Datenlücken

Rollrate je Jet; Override (α, G, Energie); Verhalten unter ~280 KIAS (Messung endet dort); Leerlaufschub; Speedbrake-Wirkung; andere Höhen als 10.000 ft für die Messflüge; Gun-Reichweite und Streuung; Greyout-Modell.
