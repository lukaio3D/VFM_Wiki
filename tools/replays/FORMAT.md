# VFM-Replayformat (.vri / .vrb)

Entschlüsselt am 2026-10-14 an VFM v1.4.2 (Steam-Build 24440300, Unity 6000.2, IL2CPP) aus den Dateien allein, ohne den Spielcode zu lesen. Leser: [`vrb.py`](vrb.py).

## Wo die Dateien liegen

| Ort | Inhalt |
|---|---|
| `%USERPROFILE%\AppData\LocalLow\Boundless Dynamics, LLC\VFM\Replays\` | eigene Matches `replay.vr?`, `replay1.vr?` … (Stand: 76 Matches von Feb. bis Okt. 2026, ~7 h Flugzeit) |
| `<Steam>\steamapps\common\Virtual Fighter Maneuvers\VFM_Data\StreamingAssets\Replays\` | drei Lehr-Replays vom Entwickler (BahamutoD gegen Bots): `simple1c`, `simple2c`, `sus2reversal1to2` |
| `…\VFM\Player.log` | Unity-Log, für Replays nichts Brauchbares |

Die `.vtr`- und `.cfg`-Dateien unter `Boundless Dynamics, LLC\VTOLVR` gehören zu VTOL VR (gleicher Entwickler), nicht zu VFM.

## .vri – Metadaten (JSON, UTF-8)

`name`, `s_timeRecorded` (Ortszeit des Rechners), `duration` [s], `players[]` (`name`, `elo`, `rank`, `kills`, `deaths`, `team`, `vehicle`), `logEvents[]` (`time`, `message`: Start, Kills mit Waffe, Absturz, Ende), `mpState`, `playersPerTeam`, `mapIdx`, `metadataVersion`, `matchLog`.

Jet-Index (`vehicle` hier, `jet` in der .vrb): **0 = T-15, 1 = T-16, 2 = T-18**. Aus den Daten bestimmt: Index 0 hat den größten Schubüberschuss und erreicht Mach 1,37, Index 2 kommt nie über Mach 0,98.

## .vrb – Flugdaten

Die ganze Datei ist **ein LZ4-Block** (Rohformat, ohne Frame-Header und ohne Längenangabe). Entpackt ~1,1-fach, also kaum Redundanz. Danach Little Endian, Strings als `int32 Länge + UTF-8`.

```
int32   version            = 1
int32   anzahlSpieler
Spieler[anzahlSpieler]
int32   0                  (unbekannt, bisher immer 0)
int32   anzahlEreignisse
Ereignis[anzahlEreignisse]
```

### Spieler

```
int32   id                 Reihenfolge kann von der .vri abweichen, Zuordnung über den Namen
int32   team
bool    (1 Byte, bisher immer 1)
int32   jet                0 T-15, 1 T-16, 2 T-18
string  name
int32   anzahlSaetze       inklusive Startzustand
float   t0                 = 0
float3  position           Startposition [m]
float3  geschwindigkeit    Startgeschwindigkeit [m/s]
int8[4] lage               Quaternion x, y, z, w × 127
Satz[anzahlSaetze - 1]
```

Unity-Achsen: x rechts, y oben (Höhe), z vorn. 1v1-Start: (∓200, 3048, ±2000) m, also 10.000 ft und 4 km Abstand, Kurs aufeinander zu mit 246 m/s.

### Satz (~4,5 pro Sekunde, Zeitschritt 0,19–0,23 s, selten bis 0,9 s)

```
float   dt                 Zeit seit dem letzten Satz [s]
uint8   maske
float3  dPosition          wenn maske & 1   Positionsänderung [m]
float3  dGeschwindigkeit   wenn maske & 2   Geschwindigkeitsänderung [m/s]
int8[4] dLage              wenn maske & 4   Änderung der Lage-Quaternion × 127
```

Fehlt ein Feld, ist die Änderung null. Position und Geschwindigkeit ergeben sich durch Aufsummieren und sind exakt (Korrelation von dGeschwindigkeit mit der Ableitung der Positionen: 0,998). Ein Track endet beim Tod (meist ~5 s nach dem Kill) oder mit dem Match.

**Offen: dLage.** Über die ersten ~30 Sätze stimmt die aufsummierte Lage mit der physikalisch geschätzten überein (Nase entlang der Bahn, Hochachse in Auftriebsrichtung), danach driftet die Summe weg und ihre Norm verlässt 127. Wie das Spiel daraus die Lage rekonstruiert, ist ungeklärt. Für BFM-Auswertungen reicht vorerst die Schätzung aus Bahn und Auftriebsrichtung; der Anstellwinkel fehlt damit.

### Ereignis

```
uint8   art
float   t
int8    k                  Bedeutung je Art
```

| art | Rest | Bedeutung |
|---|---|---|
| 3 | `float3 p0, float3 v0, int32 zahl, float3 p1, float3 v1, float t1` | Geschoss (Gun): Start und Ende mit Zeit. Mündungsgeschwindigkeit ~1.030 m/s relativ zum Schützen, nach ~6 s noch ~560 m/s. Der Schütze ergibt sich aus der Nähe zu p0, `k` ist nicht die Spieler-id. |
| 2 | `float3 p, int8[4] lage` | Objekt mit Position, tritt bei Treffern auf |
| 5 | `int32 wert` | unbekannt, wenige pro Match |

## Was sich daraus ableiten lässt (`vrb.py`)

Höhe, wahre Fahrt, KIAS und Mach (Spiel-Atmosphäre aus `../flugmodell/modell_parameter.json`), Last senkrecht zur Bahn (≈ HUD-G), Drehrate, spezifische Überschussleistung Ps, Kurs und Steigwinkel. Beschleunigungen sind Rückwärtsdifferenzen über einen Satz (~0,22 s) und glätten kurze Spitzen.

Der Track des aufnehmenden Spielers ist glatt, der des Gegners verrauscht (vermutlich Netzwerk-Replikation, G schwankt um ±1,5). Für den Gegner vor dem Auswerten glätten.

Nicht enthalten: Treibstoff, Schubhebel, Anstellwinkel, Stick, Raketen (bisher nur Gun-Kills in den Proben).
