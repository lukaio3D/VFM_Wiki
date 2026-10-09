# Spielmodi

> Welche Modi es gibt, welche Einstellungen du in Lobbys hast und was die Ranked-Regeln für deine Taktik bedeuten.

## Überblick

| Modus | Wofür |
|---|---|
| **Academy** | Tutorials zu BFM-Grundlagen und zum Visier (Gunsight-Tutorial seit v1.2.8) |
| **Free Flight** | Freies Fliegen ohne Gegner – Flugzeug kennenlernen, Manöver üben |
| **Bots** | Offline gegen Bots oder in Lobbys mit "Fill with bots" auffüllen |
| **Custom-Lobbys** | Von Spielern gehostete Matches mit frei wählbaren Regeln, 1v1 bis 4v4 |
| **Ranked** | Wertungsspiele mit Elo-Matchmaking, Seasons und Rang-Patches |
| **Replay / Debrief** | 3D-Nachbesprechung deiner Kämpfe |

## Academy und Free Flight

Die **Academy** bringt dir die Grundmanöver und das Visier bei. Mach das Gunsight-Tutorial in jedem Fall: Der Gun-Funnel funktioniert anders als ein einfacher Punkt (siehe [HUD](/avionik/hud)).

**Free Flight** ist dein Labor. Hier lernst du ohne Druck, wie sich dein Jet bei Corner Speed anfühlt, wie viel Energie ein Override kostet und wie schnell du nach einem Unload wieder Speed hast. Konkrete Übungen: [Übungen](/grundlagen/uebungen).

## Bots

- Bots gibt es offline und als Lückenfüller in Lobbys ("Fill with bots").
- Es gibt **keine Schwierigkeitsstufen**. Bots haben ein festes Rating von 1000.

**Was das für dich heißt:** Bots sind ein konstanter Sparringspartner. Gut, um Abläufe zu wiederholen (Merge, Lead Turn, Schuss). Sie ersetzen aber keine Menschen: Menschen nutzen deine Fehler gezielt aus und reagieren auf dein Verhalten.

::: info IM SPIEL PRÜFEN
- Welche Jets fliegen Bots, und kannst du ihnen einen Jet zuweisen?
- Setzen Bots Raketen, Flares und den AoA-Override ein?
:::

## Custom-Lobbys

Lobbys werden von Spielern gehostet (Host/Non-Host). Teams von 1v1 bis 4v4, Lücken auf Wunsch mit Bots.

| Einstellung | Optionen / Bedeutung |
|---|---|
| **Raketen** | An/aus (aus = Guns-only) und Anzahl |
| **Infinite Ammo** | Unbegrenzte Munition |
| **Head-on Guns** | Erlaubt oder verboten (Schüsse frontal beim Merge) |
| **Merge Safety** | Seit v1.4.1 standardmäßig an |
| **Startdistanz** | Nah oder BVR (Start außerhalb Sichtweite) |
| **Starthöhe** | Optionaler High-Altitude-Start auf 25.000 ft (seit v1.2.0) |
| **Tageszeit** | Wählbar |
| **Map** | Mountains, Harbor Island, Desert, Lake Chaka (seit v1.3.0) |
| **Runden zum Sieg** | Wählbar |

::: info IM SPIEL PRÜFEN
- Was genau macht "Merge Safety"? (Verhindert sie Kollisionen am Merge oder Schüsse vor dem ersten Passieren?)
- Ist die Flare-Anzahl einstellbar?
- Wo genau wird der High-Altitude-Start gewählt (Lobby-Einstellung oder anderer Ort)?
- Welche Startdistanzen gibt es genau, und wie weit ist "nah"?
:::

### Lobby-Einstellungen gezielt fürs Training nutzen

- **Guns-only + Head-on Guns verboten:** reines BFM. Du lernst Geometrie und Energie, ohne dass ein Raketenschuss den Kampf abkürzt.
- **Infinite Ammo:** Schießtraining. Du kannst den Funnel ausprobieren, ohne den Selbstzerstörungs-Countdown bei leeren Stores zu riskieren (siehe [Waffen](/avionik/waffen)).
- **Nahe Startdistanz:** maximal viele Merges pro Stunde.
- **High-Altitude-Start (25.000 ft):** Kämpfe in dünner Luft. Alle Jets drehen dort schlechter, die T-15 verliert relativ am wenigsten (siehe [Flugzeugvergleich](/flugzeuge/vergleich)).
- **Tageszeit:** Gegen die Sonne ist ein Gegner schwer zu sehen. Übe bewusst Kämpfe mit tiefstehender Sonne.

## Ranked

| Regel | Stand |
|---|---|
| **Matchmaking** | Elo-basiert |
| **Seasons** | Seit Februar 2026 |
| **Rang-Patches** | Abzeichen für deinen Rang, inkl. "Ace"-Rängen für Top-Spieler |
| **Hall of Fame** | Top 10 der letzten Season |
| **Rundenzeit** | 8 Minuten |
| **Zeitablauf im 1v1** | Der **Verfolger gewinnt** (seit v1.2.2) |
| **Waffen im 1v1** | Laut Community-Berichten Guns-only |

::: info IM SPIEL PRÜFEN
- Namen und Elo-Grenzen der Rang-Patches.
- Ist Ranked 1v1 tatsächlich Guns-only? Gibt es Ranked-Modi mit mehr als zwei Spielern?
- Wie entscheidet das Spiel bei Zeitablauf, wer "Verfolger" ist (Position hinter dem Gegner, Aspect, Distanz)?
:::

### Was die Ranked-Regeln taktisch bedeuten

- **Die Timeout-Regel belohnt offensive Position.** Wenn die Zeit knapp wird, zählt nicht, wer mehr Energie hat, sondern wer hinten sitzt. Bist du kurz vor Ablauf offensiv, ist Kontrolle wichtiger als ein riskanter Schuss: in Lag bleiben, Overshoot vermeiden, hinter ihm bleiben.
- **Defensiv kurz vor Ablauf?** Dann musst du die Rollen umdrehen, nicht nur überleben. Ein reines "Durchhalten" verliert.
- **Kein Neutral-Stillstand.** Ein langer neutraler Kampf ohne Fortschritt endet bei Zeitablauf nicht automatisch zu deinen Gunsten. Plane den Kampf so, dass du rechtzeitig einen Vorteil umsetzt.
- **Guns-only (falls bestätigt):** Flares und Raketenabwehr spielen keine Rolle. Es zählen Merge, Kurvenkampf, Energie und Zielen.

Siehe auch: [Golden Rules](/grundlagen/golden-rules), [Offensiv-Manöver](/grundlagen/offensiv-manoever).

## Replay und Debrief-Raum

Nach dem Kampf kannst du ihn im 3D-Debrief-Raum ansehen (ähnlich wie Tacview):

- **3D-Replay** beider Flugbahnen, frei drehbar
- **Specific-Energy-Graph** (seit v1.2.0): zeigt die Energie (Höhe + Geschwindigkeit) über die Zeit
- **S-Cam** mit HUD-Modus: Kampf aus der Cockpit-Perspektive inklusive HUD

So nutzt du den Debrief:

1. **Energie-Graph:** An welcher Stelle hast du Energie verloren, ohne Winkel zu gewinnen? Das ist dein wichtigster Lernpunkt.
2. **Draufsicht beim Merge:** Wann hast du den Turn begonnen, wann er? Wer hat den ersten Winkel gewonnen?
3. **S-Cam beim Schuss:** Wo lag der Gegner im Funnel, als du geschossen hast?
4. **Moment des Rollentauschs:** Suche die Stelle, an der der Kampf gekippt ist – und was du dort hättest anders machen können.

Ein strukturierter Plan dazu steht in [Übungen](/grundlagen/uebungen).

## Voice-Chat

VFM hat einen eingebauten Voice-Chat mit **Push-to-Talk**. Im Teamkampf ist er dein wichtigstes Werkzeug: kurze, klare Brevity-Calls wie "Tally", "No Joy", "Engaged", "Defensive" (siehe [Begriffe](/grundlagen/begriffe) und [Team-Taktik](/flugzeuge/team)).

::: tip MERKE
- Academy (inkl. Gunsight-Tutorial) und Free Flight zuerst; Bots haben keine Schwierigkeitsstufe (Rating 1000).
- Lobbys: Raketen an/aus und Anzahl, Infinite Ammo, Head-on Guns, Merge Safety, Startdistanz, Höhe, Tageszeit, Map, Runden.
- Ranked: Elo, Seasons, 8-Minuten-Runden – im 1v1 gewinnt bei Zeitablauf der Verfolger.
- Wer offensiv ist, sichert die Position; wer defensiv ist, muss die Rollen umdrehen.
- Nach jedem Kampf den Debrief öffnen: Energie-Graph und Merge-Geometrie zuerst.
:::

Weiter: [Golden Rules](/grundlagen/golden-rules)
