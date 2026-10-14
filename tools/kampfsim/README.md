# Kampfsimulation (1v1, Guns only)

Rechnet viele Kämpfe der drei VFM-Jets gleichzeitig durch, um Stärken, Schwächen und beste Strategien zu finden. Der interaktive Lern-Simulator ist ein eigenes Projekt (`../simulator/KONZEPT.md`); dieses Werkzeug ist die Batch-Analyse dazu.

## Ablauf

```bash
cd tools/spieldaten && python lesen.py      # nur auf dem PC mit VFM: Originaldaten -> ausgabe/ (lokal)
cd ../flugmodell
python kalibrieren.py                       # Faktoren an den Messungen -> daten/original_kalibrierung.json
python export_original.py                   # Modelltabellen -> daten/modell_original.json
cd ../kampfsim
python kalibrierung.py                      # Dynamik gegen die Messflüge prüfen
python turnier.py                           # alle Strategien gegeneinander (~405.000 Kämpfe bis 8 min Kampfzeit)
python auswertung.py                        # -> ergebnisse/bericht.md
python varianten.py                         # Empfindlichkeit -> ergebnisse/varianten.md
python bilder.py                            # Beispielkämpfe -> docs/public/images/sim/
python export_web.py                        # Flugmodell für den 3D-Simulator -> app/public/data/
python zeige.py T-15 "weg/flach/280/Pure" T-16 "hin/tief/440/Lag" 150 kampf.png   # einzelner Kampf
```

Benötigt numpy, scipy, matplotlib. Ohne VFM-Installation laufen alle Schritte ab `kalibrierung.py` mit der vorhandenen `daten/modell_original.json`.

## Flugmodell: Originalkurven (`../flugmodell/original.py`, seit 2026-10-14)

Auftrieb und Widerstand über α kommen aus den Flächen und Profilkurven des Spiels, der Schub über Mach, Dichte und α aus den Triebwerksdaten, die Dichte über der Höhe aus der Spielkurve, die Massen aus Leermasse und Tank (`../spieldaten/README.md`). Offen sind nur Faktoren aus dem Spielcode; `kalibrieren.py` legt sie je Jet an allen Messquellen fest (Diagramme, Beschleunigung, Ausrollen, voller Zug): Auftrieb KL, Widerstand KD, Geschwindigkeitsdämpfung kB (`baseDrag` als Unity-Rigidbody-Drag), Schub kT und beim T-18 der Widerstandsanstieg jenseits des Auftriebsmaximums kS. HUD-α = Flügel-α + 2°. Der Schub wirkt entlang der Rumpfachse.

| Prüfung | T-15 | T-16 | T-18 |
|---|---|---|---|
| Schubfaktor kT (1 = Spieldaten unverändert) | 0,98 | 0,98 | 0,96 |
| Diagramme 300–550 KIAS, RMS | 0,22–0,40 °/s | 0,47–1,03 °/s | 0,28–0,38 °/s |
| 300 → 500 KIAS (gemessen 8,4 / 11,5 / 12,3 s) | 8,4 s | 12,1 s | 13,2 s |
| Energieverlust im vollen Zug, Abweichung am Ende | −16 m | +3 m | +2 m |
| Erster Turn voll, nach 4 / 8 s (gemessen) | 75° / 141° (77 / 146) | 70° / 139° (70 / 141) | α 35°: 67° / 118° (70 / 127) |

Das Lift-Limit der Ingame-Diagramme liegt 13–24 % über dem größten Auftrieb, der im Flug ohne Override erreicht wird (gemessen 85–92 %). Das Modell fliegt mit dem Auftrieb im Flug. Das alte Modell v2 (`../flugmodell/refit.py`, freie Stützstellen über Mach) bleibt zum Vergleich erhalten.

## Ranked-Start (`sim.RANKED`)

Aus 71 eigenen 1v1-Replays (`../replays/vrb.py`), in allen gleich: 10.000 ft, Mach 0,75 (246 m/s, im HUD ~427 KIAS), Head-on, 4.000 m Abstand, 400 m seitlicher Versatz, Merge nach ~8 s. Voller Tank (keine Fuel-Option in der Lobby, `startingFuel = maxFuel`). Kein Schuss vor dem ersten Pass (Merge Safety), danach sind Schüsse auf der Nase möglich. Rundenzeit 8 Minuten: Ein Kampf ist erst nach 480 s offen; in den Replays fiel der Abschuss im Median nach 146 s, spätestens nach 334 s.

## Nicht gemessene Annahmen (in `sim.ANNAHMEN`)

Rollrate (180 °/s), Kanone (Reichweite, Treffer bis Abschuss; die Mündungsgeschwindigkeit 1.030 m/s stammt aus den Spieldaten), Verhalten über 20.190 ft und unter ~280 KIAS, Leerlaufschub 0 im Simulator (Kalibrierung: 5 % laut minOutput), keine Speedbrake. `varianten.py` prüft, ob die Ergebnisse davon abhängen.

## Grenzen

Bots sind keine Menschen: Sie sehen alles, zielen perfekt und reagieren sofort, aber ohne Plan über den nächsten Pass hinaus und ohne Täuschung. Die Ergebnisse zeigen, **was die Physik der Jets begünstigt**: welche Ebene, welches Speedband, welcher Kreis. Wie gut ein Mensch das umsetzt, ist eine andere Frage.

## Weitere Werkzeuge

- `speedband.py T-16` – feines Speed-Raster (360–500 KIAS) je Fuel-Stand gegen die stärksten Gegner-Strategien.
- `export_web.py` – schreibt das Flugmodell nach `app/public/data/` für den 3D-Simulator.
- `test/vergleich.mjs` – prüft die JS-Portierung (`app/src/sim/physik.js`) gegen `sim.py` (720 Kämpfe, 95 % gleicher Ausgang; die Verläufe sind Schritt für Schritt gleich, Abweichungen sind numerisches Chaos in langen Kämpfen). `test/faelle.json` ist eine Zufallsstichprobe aus `turnier.strategien` mit den Python-Ergebnissen (neu gerechnet mit dem Originalmodell).

## 3D-Simulator (eigene App)

Der Simulator ist eine eigene Vite-App in `app/` (Vue 3, Three.js), veröffentlicht neben dem Wiki unter `/VFM_Wiki/sim/`. Lokal startet `npm run dev` im Hauptordner beides; der Wiki-Server (Port 5180) reicht `/VFM_Wiki/sim/` an den App-Server (Port 5181) weiter, also alles unter http://127.0.0.1:5180/VFM_Wiki/. Szenen öffnen per `/VFM_Wiki/sim/?szenario=<id>`. `app/src/App.vue` ist die Oberfläche (Layout nach Konzept v2), die Module unter `app/src/sim/`:

- `physik.js` – Portierung von `sim.py` für einen Kampf, dazu eigene Startlagen (`geo.start`, `geo.imKampf`) und **AoA-Override** (Annahmen: maximales α T-15 50°, T-16 32°, T-18 80°; Auftrieb und Widerstand dort aus den Originalkurven).
- `modelle.js` – Low-Poly-Modelle der drei Jets im gleichen Maßstab (Maße nach den Vorbildern angenommen).
- `lage.js` – die drei Probleme (Winkel, Aspect, Abstand/Closure) mit Lösung, Kurvenkreis, Ps.
- `hud.js` – HUD der Cockpit-Ansicht.
- `editor.js` – Vorlagen für eigene Szenarien und die Suche nach den besten Strategien (eigene Kandidaten gegen die Antworten des Bandits, im Browser).
- `szenarien.js` – Lern-Szenarien mit Kategorie, Haltepunkt-Frage und Wiki-Link.

Das Flugmodell kommt aus `app/public/data/modell.json` (`python export_web.py`).
