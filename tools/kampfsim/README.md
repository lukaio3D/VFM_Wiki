# Kampfsimulation (1v1, Guns only)

Rechnet viele Kämpfe der drei VFM-Jets gleichzeitig durch, um Stärken, Schwächen und beste Strategien zu finden. Der interaktive Lern-Simulator ist ein eigenes Projekt (`../simulator/KONZEPT.md`); dieses Werkzeug ist die Batch-Analyse dazu.

## Ablauf

```bash
cd tools/flugmodell && python refit.py      # Flugmodell v2 -> daten/modell_v2.json (~3 min)
cd ../kampfsim
python kalibrierung.py                      # Dynamik gegen die Messflüge prüfen
python turnier.py                           # alle Strategien gegeneinander (~800.000 Kämpfe, ~20 min auf 12 Kernen)
python auswertung.py                        # -> ergebnisse/bericht.md
python varianten.py                         # Empfindlichkeit -> ergebnisse/varianten.md
python bilder.py                            # Beispielkämpfe -> docs/public/images/sim/
python export_web.py                        # Flugmodell für den 3D-Simulator -> app/public/data/
python zeige.py T-15 "weg/flach/280/Pure" T-16 "hin/tief/440/Lag" 150 kampf.png   # einzelner Kampf
```

Benötigt numpy, scipy, matplotlib.

## Flugmodell v2 (`../flugmodell/refit.py`)

Ein gemeinsamer Fit je Jet aus allen Datenquellen: Diagramme (Ps = 0 bei der Sustained-Rate, 27 Bedingungen), Beschleunigungsläufe (T − D bei 1 G), Ausrollen im Leerlauf (D bei 1 G) und voller Zug (Energiehöhe über die Zeit). Damit sind Schub und Widerstand getrennt bestimmt, auch der Widerstand bei hohem α.

| Prüfung | T-15 | T-16 | T-18 |
|---|---|---|---|
| Diagramme 300–550 KIAS, RMS | 0,15–0,28 °/s | 0,34–0,57 °/s | 0,24–0,55 °/s |
| 300 → 500 KIAS (gemessen 8,4 / 11,5 / 12,3 s) | 8,4 s | 11,5 s | 12,6 s |
| Energieverlust im vollen Zug (gemessen) | −2.313 m (−2.338) | −1.704 m (−1.741) | −2.271 m (−2.270) |
| Erster Turn voll, nach 4 / 8 s (gemessen) | 74° / 142° (77 / 146) | 68° / 138° (70 / 141) | α 35°: 67° / 121° (70 / 127) |

Schwachstelle: Die T-16 dreht im Messflug bei ~450 KIAS ~7 % besser als ihr Diagramm (17,6 statt ~16,4 °/s). Das Modell folgt dem Diagramm, unterschätzt die T-16 also eher. `varianten.py` rechnet deshalb auch mit +5 % Schub für die T-16.

## Simulator (`sim.py`)

Punktmasse in 3D: Schub, Widerstand (inkl. hohem α), Auftrieb über α (im Flug ~90 % des Diagramm-Lift-Limits am α-Anschlag, gemessen), 9-G-Limit, Schwerkraft, Fuel-Verbrauch. α folgt dem Kommando verzögert (G-Aufbau wie im Messflug), der Lift Vector mit begrenzter Rollrate. Die T-18 darf beim Schuss bis 35° (Nase ~9° weiter vorn, weniger Auftrieb, Strömungsabriss-Widerstand aus dem Messflug).

**Start (Ranked):** Beide mit 450 KIAS auf 10.000 ft, Head-on, Merge nach ~5 s (~8.500 ft Abstand), seitlicher Versatz 150 m oder 600 m. Voller Tank.

**Pilot (Bot):** Jede Strategie ist ein Satz Entscheidungen vor dem Merge:

| Feld | Werte | Bedeutung |
|---|---|---|
| `wende` | hin / weg / durch | am Pass zum Gegner drehen (beide hin → Two-Circle), weg (→ One-Circle) oder 6 s geradeaus durch (Extend) |
| `ebene` | steil hoch (60°) / hoch (25°) / flach / tief (−30°) | Neigung des Lift Vectors im Turn; im Kampf halb so stark |
| `v_ziel` | 280 / 360 / 440 / 520 KIAS | Speed, auf die der Pilot den Kampf bringt (G nach Speed; 60 kt darüber Leerlauf) |
| `lag` | Pure / Lag | Verfolgung auf kurze Distanz: auf ihn oder 1 s hinter ihn |
| `alpha_kampf` | 26° / 35° (nur T-18) | α beim Kurven; beim Schuss immer bis 35° |
| `merge_ab` | 450 halten / Nachbrenner | Speed bis zum Merge |

Feste Regeln für alle: Gun-Modus (Nase auf den Vorhaltepunkt) unter ~4.900 ft, wenn er vor der Nase ist; Break Turn, wenn er hinter der 3/9-Linie die Nase auf mir hat; jeder neue Pass beginnt wieder mit dem eigenen ersten Turn; Bodenabstand ≥ ~3.000 ft, Decke ~22.000 ft.

**Abschuss:** 0,5 s Treffer insgesamt. Treffer, wenn die Nase innerhalb von max(Zielgröße 6 m, 0,3°) auf dem Vorhaltepunkt liegt (Geschoss 1.000 m/s, mit Ziel-Beschleunigung und Geschossfall), zwischen 150 und 900 m.

## Nicht gemessene Annahmen (in `sim.ANNAHMEN`)

Rollrate (180 °/s), Kanone (Reichweite, Geschwindigkeit, Treffer bis Abschuss), Verhalten über 20.190 ft und unter ~280 KIAS, Leerlaufschub ≈ 0, keine Speedbrake. `varianten.py` prüft, ob die Ergebnisse davon abhängen.

## Grenzen

Bots sind keine Menschen: Sie sehen alles, zielen perfekt und reagieren sofort, aber ohne Plan über den nächsten Pass hinaus und ohne Täuschung. Die Ergebnisse zeigen, **was die Physik der Jets begünstigt**: welche Ebene, welches Speedband, welcher Kreis. Wie gut ein Mensch das umsetzt, ist eine andere Frage.

## Weitere Werkzeuge

- `speedband.py T-16` – feines Speed-Raster (360–500 KIAS) je Fuel-Stand gegen die stärksten Gegner-Strategien.
- `export_web.py` – schreibt das Flugmodell nach `app/public/data/` für den 3D-Simulator.
- `test/vergleich.mjs` – prüft die JS-Portierung (`app/src/sim/physik.js`) gegen `sim.py` (720 Kämpfe, 97 % gleicher Ausgang; Abweichungen sind numerisches Chaos in langen Kämpfen). `test/faelle.json` ist eine Zufallsstichprobe aus `turnier.strategien` mit den Python-Ergebnissen.

## 3D-Simulator (eigene App)

Der Simulator ist eine eigene Vite-App in `app/` (Vue 3, Three.js), veröffentlicht neben dem Wiki unter `/VFM_Wiki/sim/`. Lokal startet `npm run dev` im Hauptordner beides; der Wiki-Server (Port 5180) reicht `/VFM_Wiki/sim/` an den App-Server (Port 5181) weiter, also alles unter http://127.0.0.1:5180/VFM_Wiki/. Szenen öffnen per `/VFM_Wiki/sim/?szenario=<id>`. `app/src/App.vue` ist die Oberfläche (Layout nach Konzept v2), die Module unter `app/src/sim/`:

- `physik.js` – Portierung von `sim.py` für einen Kampf, dazu eigene Startlagen (`geo.start`, `geo.imKampf`) und **AoA-Override** (Annahmen: maximales α T-15 50°, T-16 32°, T-18 80°; jenseits von 35° Auftrieb und Widerstand wie eine flache Platte).
- `modelle.js` – Low-Poly-Modelle der drei Jets im gleichen Maßstab (Maße nach den Vorbildern angenommen).
- `analyse.js` – die drei Probleme (Winkel, Aspect, Abstand/Closure) mit Lösung, Kurvenkreis, Ps.
- `hud.js` – HUD der Cockpit-Ansicht.
- `editor.js` – Vorlagen für eigene Szenarien und die Suche nach den besten Strategien (eigene Kandidaten gegen die Antworten des Bandits, im Browser).
- `szenarien.js` – Lern-Szenarien mit Kategorie, Haltepunkt-Frage und Wiki-Link.

Das Flugmodell kommt aus `app/public/data/modell.json` (`python export_web.py`).
