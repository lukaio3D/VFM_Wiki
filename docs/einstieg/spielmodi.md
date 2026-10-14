# Spielmodi

> Welche Modi es gibt, was du in Lobbys einstellst und was die Ranked-Regeln für deine Taktik bedeuten.

## Überblick

| Modus | Wofür |
|---|---|
| **Academy** | Tutorials zu BFM-Grundlagen und zum Visier (Gunsight-Tutorial seit v1.2.8) |
| **Free Flight** | Freies Fliegen ohne Gegner: Jet kennenlernen, Manöver üben |
| **Bots** | Offline oder als Lückenfüller in Lobbys („Fill with bots“) |
| **Custom-Lobbys** | Von Spielern gehostet, freie Regeln, 1v1 bis 4v4 |
| **Ranked** | Elo-Matchmaking, Seasons, Rang-Patches |
| **Replay / Debrief** | 3D-Nachbesprechung deiner Kämpfe |

## Academy, Free Flight und Bots

Mach das **Gunsight-Tutorial** in jedem Fall: Der Gun-Funnel funktioniert anders als ein einfacher Punkt (siehe [HUD](/avionik/hud)).

**Free Flight** ist dein Labor: Wie fühlt sich Corner Speed an, wie viel Energie kostet ein Override, wie schnell bist du nach einem Unload wieder schnell? Übungen: [Trainingsplan](/grundlagen/uebungen).

**Bots** haben keine Schwierigkeitsstufen, sondern ein festes Rating von 1000. Sie sind ein konstanter Sparringspartner für Abläufe (Merge, Lead Turn, Schuss), ersetzen aber keine Menschen, die deine Fehler gezielt ausnutzen.

## Custom-Lobbys

| Einstellung | Optionen |
|---|---|
| **Raketen** | An/aus (aus = Guns-only) und Anzahl |
| **Infinite Ammo** | Unbegrenzte Munition |
| **Head-on Guns** | Frontalschüsse beim Merge erlaubt oder verboten |
| **Merge Safety** | Seit v1.4.1 standardmäßig an |
| **Startdistanz** | Nah oder BVR (Start außerhalb Sichtweite) |
| **Starthöhe** | Optional High-Altitude-Start auf 25.000 ft (seit v1.2.0) |
| **Tageszeit, Map, Runden** | Wählbar; Maps: Mountains, Harbor Island, Desert, Lake Chaka (seit v1.3.0) |

So nutzt du die Lobby fürs Training:

- **Guns-only, Head-on Guns verboten:** reines BFM ohne Abkürzung durch Raketen.
- **Infinite Ammo:** Schießtraining ohne Selbstzerstörungs-Countdown bei leeren Stores (siehe [Waffen](/avionik/waffen)).
- **Nahe Startdistanz:** möglichst viele Merges pro Stunde.
- **25.000 ft:** dünne Luft. Alle Jets drehen schlechter, der Vorsprung der T-16 schrumpft mit der Höhe (siehe [Flugzeugvergleich](/flugzeuge/vergleich)).
- **Tiefe Sonne:** Gegen die Sonne siehst du den Gegner schlecht. Übe das bewusst.

## Ranked

Die Regeln stammen aus Patchnotes; Start, Waffen und Rundendauer aus der Auswertung von 71 eigenen 1v1-Replays (*Replays*, Ranked und Casual starten gleich).

| Regel | Stand |
|---|---|
| **Matchmaking** | Elo, Seasons seit Februar 2026, Rang-Patches bis zu „Ace“-Rängen, Hall of Fame (Top 10 der letzten Season) |
| **Match** | Bis zu 3 Runden (laut Spiel-Log) |
| **Rundenzeit** | 8 Minuten |
| **Zeitablauf im 1v1** | Der **Verfolger gewinnt** (seit v1.2.2) |
| **Waffen im 1v1** | **Guns-only:** 63 Kanonen-Abschüsse, 9 Abstürze, keine Raketen (*Replays*) |
| **Start** | 10.000 ft, Mach 0,75 (im HUD ~427 KIAS), Head-on, 13.100 ft (4.000 m) Abstand, ~1.300 ft (400 m) seitlicher Versatz, Merge nach ~8 s (*Replays*) |
| **Fuel** | Voller Tank: Die Lobby hat keine Fuel-Option, der Tank startet laut *Spieldaten* voll |
| **Erster Pass** | Kein Schuss vor dem ersten Pass (Merge Safety; 0 von 7.314 Schüssen). Danach sind Schüsse auf der Nase möglich: 14 % aller Schüsse fallen bei fast frontalem Aspect |
| **Dauer bis zum Abschuss** | Median **146 s**, 90 % unter 301 s, längste 334 s (*Replays*) |

Ältere Wiki-Stände nannten ~450 KIAS, ~8.500 ft Abstand und ~5 s bis zum Merge. Das war geschätzt und ist überholt.

### Was das taktisch bedeutet

- **~427 KIAS am Start** liegt nahe bis über der Diagramm-Corner-Speed aller drei Jets (im Flug erreicht aus dieser Speed nur die T-15 sicher 9 G) und schon im Band, in dem laut [Simulation](/flugzeuge/simulation) alle drei am besten kämpfen: **Two-Circle bei ~440 KIAS, nose-low oder flach – nur nicht steil hoch.** Der erste Turn ist fast ausgeglichen; die T-15 gewinnt ihn knapp. Messung: [Der erste Turn (gemessen)](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen), Pläne je Paarung: [Merge-Strategien für Ranked](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias).
- **Nachbrenner bis zum Merge** bringt dich auf ~605 (T-15), ~550 (T-16) bzw. ~535 KIAS (T-18) (*Modell*), weit über dein Kampfband. In der Simulation ist das kein klarer Vorteil.
- **Die Hälfte der Runden ist nach ~2,5 Minuten entschieden, 90 % nach 5 Minuten.** In den eigenen Replays kam keine Runde an die 8 Minuten heran. Plane deshalb nicht auf den Zeitablauf, sondern darauf, deinen ersten Vorteil umzusetzen.
- **~12 % der Runden enden mit einem Absturz.** Nose-low ist eine der stärksten Ebenen, aber ab 10.000 ft ist der Boden nach wenigen Kreisen nah. Höhe im Blick behalten.
- **Die Timeout-Regel belohnt Position, nicht Energie.** Bist du kurz vor Ablauf offensiv, sichere die Position: in Lag bleiben, keinen Overshoot riskieren. **Defensiv kurz vor Ablauf?** Dann musst du die Rollen umdrehen; Durchhalten verliert.
- **Guns-only:** Flares und Raketenabwehr spielen keine Rolle, es zählen Merge, Kurvenkampf, Energie und Zielen. Nach dem ersten Pass kann ein Pass auf der Nase eine Schussgelegenheit sein.

::: info IM SPIEL PRÜFEN
- Wie bestimmt das Spiel bei Zeitablauf den „Verfolger“ (Position, Aspect, Distanz)?
- Unterdrückt Merge Safety auch Kollisionen, und bis wann genau gilt sie? (Dass vor dem ersten Pass kein Schuss fällt, ist aus den Replays belegt.)
- Wie wird ein Match aus bis zu 3 Runden gewertet (Best-of-3?), und gilt der Start für jede Runde gleich?
:::

## Replay und Debrief

Der 3D-Debrief-Raum (ähnlich Tacview) zeigt beide Flugbahnen frei drehbar, einen **Specific-Energy-Graph** (Höhe + Speed über die Zeit, seit v1.2.0) und eine **S-Cam** aus dem Cockpit mit HUD. Geh ihn in dieser Reihenfolge durch:

1. **Energie-Graph:** Wo hast du Energie verloren, ohne Winkel zu gewinnen?
2. **Draufsicht beim Merge:** Wer hat wann gedreht, wer hat den ersten Winkel gewonnen? Hin zum Gegner (Two-Circle) oder weg (One-Circle)?
3. **Speed im Kampf:** Warst du im Band (~380–440 KIAS) oder deutlich darunter bzw. darüber?
4. **S-Cam beim Schuss:** Wo lag der Gegner im Funnel?
5. **Rollentausch:** An welcher Stelle ist der Kampf gekippt, und was hättest du dort anders machen können?

### Die Replay-Dateien

| Was | Wo / wie |
|---|---|
| **Speicherort** | `%USERPROFILE%\AppData\LocalLow\Boundless Dynamics, LLC\VFM\Replays\` |
| **Dateien** | Je Replay zwei: `replayNN.vri` (Spieler, Elo, Jets, Abschüsse, Dauer, Map) und `replayNN.vrb` (Flugbahnen beider Jets mit ~4–5 Werten pro Sekunde, Schüsse, Treffer) |
| **Umfang** | Ein Replay enthält nur die **letzte Runde** des Matches: Die Kills und Deaths in der `.vri` zählen das ganze Match, das Log darin aber nur einen Abschuss |
| **Lehr-Replays** | Im Spielordner unter `VFM_Data\StreamingAssets\Replays` liegen drei Replays des Entwicklers: `simple1c`, `simple2c` und `sus2reversal1to2`. Nach den Namen vermutlich Beispiele zu One- und Two-Circle (*Hypothese*). |

**Selbst auswerten:** Das Skript `tools/replays/vrb.py` im [Wiki-Repo](https://github.com/lukaio3D/VFM_Wiki/tree/main/tools/replays) liest beide Dateien (Python mit numpy und scipy). Ohne Argument zeigt es eine Übersicht aller eigenen Replays, mit Namen ein einzelnes (Flugbahn, KIAS, G, Ps, Schüsse), mit `--csv` exportiert es je Spieler eine Tabelle, mit `--ordner` liest es einen anderen Ordner, etwa die Lehr-Replays. Was die Dateien nicht verraten: den Anstellwinkel (das Lage-Feld ist noch nicht entschlüsselt). Übung dazu: [Trainingsplan, Replay und Debrief](/grundlagen/uebungen#replay-und-debrief).

::: info IM SPIEL PRÜFEN
- Lassen sich die Lehr-Replays im Debrief-Raum des Spiels öffnen?
:::

## Voice-Chat

Eingebauter Voice-Chat mit **Push-to-Talk**. Im Teamkampf nutzt du kurze Brevity-Calls wie „Tally“, „No Joy“, „Engaged“, „Defensive“ (siehe [Begriffe](/grundlagen/begriffe) und [Team-Taktik](/flugzeuge/team)).

::: tip MERKE
- Erst Academy (inkl. Gunsight-Tutorial) und Free Flight; Bots haben ein festes Rating von 1000.
- Lobbys gezielt fürs Training einstellen: Guns-only, Infinite Ammo, nahe Startdistanz.
- Ranked 1v1: Guns-only, voller Tank, Start auf 10.000 ft mit ~427 KIAS, 13.100 ft Abstand, Merge nach ~8 s, kein Schuss vor dem ersten Pass.
- Runden dauern bis zum Abschuss meist unter 5 Minuten (Median 146 s); bei Zeitablauf (8 min) gewinnt der Verfolger.
- Offensiv kurz vor Ablauf: Position sichern. Defensiv: Rollen umdrehen.
- Nach jedem Kampf in den Debrief: Energie-Graph und Merge-Geometrie zuerst. Replays liegen unter `AppData\LocalLow\…\VFM\Replays` und lassen sich mit `vrb.py` auswerten.
:::

Weiter: [Golden Rules](/grundlagen/golden-rules)
