# Spieldaten: Original-Flugmodell aus der VFM-Installation

Stand 2026-10-14, VFM v1.4.2 (Build 24440300). `lesen.py` liest die Parameter der Jets aus den Unity-Assets der lokalen Installation, nur lesend und offline. Die Ausgabe `ausgabe/spieldaten.json` enthält Daten des Spiels und ist gitignored. Ins Repo und ins Wiki gehören nur daraus gewonnene Erkenntnisse, keine Rohtabellen.

```bash
..\flugmodell\.venv\Scripts\python lesen.py                  # -> ausgabe/spieldaten.json
..\flugmodell\.venv\Scripts\python lesen.py --felder Gun     # Feldnamen einer Klasse
```

## Wie das Spiel aufgebaut ist

Unity 6000.2 mit IL2CPP: Der Code liegt kompiliert in `GameAssembly.dll` und wird hier nicht gelesen. Klassen- und Feldnamen stehen in `il2cpp_data/Metadata/global-metadata.dat`. Die Parameter stecken als serialisierte Objekte in `sharedassets*.assets` und `level*`, ohne TypeTrees. Die Feldreihenfolge kommt daher aus den Metadaten, die Typen aus den Rohdaten. Jedes vollständig beschriebene Objekt wird bis zum letzten Byte gelesen.

Interne Namen: Eagle = T-15, Viper = T-16, Hornet = T-18. Das Modell ist ein Flächenmodell wie in VTOL VR (gleicher Entwickler):

| Objekt | Inhalt |
|---|---|
| `JetSpecs` | Leermasse [t], Trägheit, max. Drehraten Pitch/Yaw/Roll, G-Limit über Zeit, Fly-by-Wire-PIDs, Steuerskalierung über IAS, AoA-Limits, Mach-Wellenwiderstand |
| `JetEngineSpecs` | maxThrust [kN], Nachbrenner-Faktor, Schub über Mach und Dichte, Schub über AoA (nur T-18), Drehzahl, Verbrauch |
| `JetController` | Flächen: Name, Fläche, Profil, Lage, Normale; Grundwiderstand `baseDrag`, Speedbrake `brakeDrag` |
| `Aerodynamics` | Profil: Auftriebs- und Widerstandsbeiwert mit Kurven über den Anstellwinkel [°], Buffet |
| `AerodynamicsController` (je Map) | relative Luftdichte über Höhe [m], Verweis auf die allgemeine Mach-Widerstandskurve (`SOCurve` „MachDragCurve“) |
| `FuelTank` | Treibstoffmenge und Dichte [t je Einheit] |
| `Gun` | Mündungsgeschwindigkeit, Kadenz, Streuung, Munition, Geschossmasse, Schaden |

Kurven sind Unity-`AnimationCurve`s: Stützstellen (Zeit, Wert, Steigung ein/aus), dazwischen kubisch Hermite.

## Gegenproben mit den eigenen Messungen

| | Spieldaten | gemessen / gefittet (`../flugmodell`) |
|---|---|---|
| Vollgewicht T-15 / T-16 / T-18 | Leermasse + Treibstoff = 19,15 / 12,14 / 18,70 t | 42.160 / 26.787 / 41.226 lb = 19,12 / 12,15 / 18,70 t |
| Luftdichte 10.000 / 20.190 ft | ≈ 0,69 / 0,48 (Kurve) | 0,694 / 0,478 (aus dem Lift-Limit) |
| T/W mit Nachbrenner, 10.000 ft, ~Mach 0,75 | 1,64 / 1,29 / 1,37 | 1,65 / 1,26 / 1,35 (Ausrollen) |
| Mündungsgeschwindigkeit | 1.030 m/s | 1.030 m/s (Replays) |
| Lift-Limit: Summe Fläche·CL·Kurve am AoA-Limit vs. SCLmax | Faktor 17,2 (T-15) / 16,9 (T-16) / ~19–22 (T-18) | – |

Einheiten: Masse t, Kräfte kN, Höhe m, Geschwindigkeit m/s, Winkel Grad. Der Lift-Faktor ist für T-15 und T-16 gleich, die Kraftformel selbst steht nur im Code. Beim T-18 wirkt zusätzlich etwas AoA-Abhängiges (Schub über AoA, zweites Profil an den Elevons, `aoaEdgeFactor`).

## Offen

- Die Kraftformeln im Spielcode (Skalierung von Auftrieb und Widerstand, Rolle von `aoaEdgeFactor`, G- und AoA-Limiter, Steuerflächen-Ausschläge). Die Faktoren sind an den Messungen kalibriert (`../flugmodell/kalibrieren.py`); beim T-18 wächst der Widerstand jenseits des Auftriebsmaximums schwächer, als die Profile allein ergeben.
- Die Lage im Replay (siehe `../replays/FORMAT.md`). Mit den Lift-Kurven lässt sich der Anstellwinkel aus G, Fahrt, Höhe und Masse zurückrechnen.
- Profile `ViperWingProfile WIP for G-AoA` (sharedassets1) und der Tank/Gun-Satz in sharedassets2 gehören vermutlich zu Tutorial oder Entwicklungsständen.
