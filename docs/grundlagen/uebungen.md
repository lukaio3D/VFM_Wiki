# Trainingsplan

> Lesen allein macht dich nicht besser, Fliegen schon. Konkrete Übungen von der Academy bis zum Lobby-Duell, in sinnvoller Reihenfolge.

Trainier gezielt statt „ein paar Runden Ranked“. Der Plan führt in vier Stufen von „ich kenne meinen Jet“ bis „ich gewinne den Merge gegen Menschen“, dazu die Auswertung deiner Replays.

## Grundregeln

- **Ein Fokus pro Session**, z. B. nur Lead Turns.
- **Gleiche Bedingungen:** 10.000 ft und voller Tank, wie im Ranked (Start mit ~427 KIAS) und in den [Referenzmessungen](/flugzeuge/vergleich). Treibstoff verändert die Werte deutlich (voll → leer bis zu +4 °/s Sustained).
- **Aufschreiben**, sonst bleibt nur ein Gefühl.
- **Hard Deck** 2.000 ft über Grund: Wer darunter kommt, hat die Übung verloren ([Golden Rules](/grundlagen/golden-rules#hard-deck-2-000-ft)). Im Ranked enden ~12 % der Runden mit einem Absturz.
- **Kurze Pulls:** VFM simuliert Greyout und Blackout. Max-G-Übungen lieber kurz und oft.

## Stufe A: Academy

1. **BFM-Tutorials** der Academy komplett durchfliegen, auch wenn du schon fliegen kannst.
2. **Gunsight-Tutorial**: Funnel und Boresight-Kreuz verstehen.
3. Steuerung einrichten: [Steuerung & Einstellungen](/einstieg/cockpit).

**Ziel:** Du findest im [HUD](/avionik/hud) ohne Suchen Speed, G, Drehrate, AoA, Beschleunigungs-Indikator und Funnel.

## Stufe B: Free Flight, lerne deinen Jet kennen

### B1 Lift-Vector-Drill

Such dir einen Punkt im Gelände. Roll so, dass dein **Lift Vector** (die Richtung über dein Kabinendach) genau auf den Punkt zeigt, dann zieh. Wechsle links und rechts, über und unter dem Horizont.
**Ziel:** Rollen und Ziehen werden eine Bewegung, 10 saubere Wiederholungen pro Seite.

### B2 Eigenen Jet vermessen

**Aufbau:** Free Flight, 10.000 ft, voller Tank, nur Guns. Nimm jeden Flug als Video auf und halte den Kopf so, dass **das HUD vollständig im Bild** ist. Danach liest du die Werte Sekunde für Sekunde aus dem Video ab. Jeden Flug zweimal fliegen.

| Flug | So fliegst du ihn | Das liest du ab |
|---|---|---|
| **M1 Beschleunigung** | Geradeaus mit 300 KIAS, Höhe halten, Nachbrenner rein, bis 500 KIAS | Zeit von 300 auf 500 KIAS |
| **M2 Ausrollen** | Von ~550 KIAS geradeaus, Gas auf Leerlauf, **ohne Speedbrake**, Höhe halten, bis ~350 KIAS | Speedverlust in kt/s bei ~450 KIAS |
| **M3 Sustained-Kurve** | Kurve bei ~450 KIAS mit Nachbrenner, G so dosieren, dass Speed und Höhe konstant bleiben. Blick geradeaus durchs HUD, nicht in die Kurve | G und Drehrate |
| **M4 Voller Zug** | Aus ~450 KIAS Knüppel voll ziehen und halten, ohne Override | Zeit bis zur Höchst-G, Höchst-G, α am Anschlag, Winkel und Speed nach 4 und 8 s |
| **M5 Override-Zug** | Wie M4, aber mit AoA-Override, einmal aus ~450 und einmal aus ~300 KIAS, ~4 s halten | Höchstes α, G und KIAS jede halbe Sekunde, Speed nach 2 und 4 s |
| **M6 Rollrate** *(neu)* | Aus ~400 KIAS geradeaus, Knüppel voll zur Seite, zwei volle Rollen; je einmal links und rechts | Zeit für 360° (Videobilder zählen) |
| **M7 Speedbrake** *(neu)* | Wie M2, aber mit ausgefahrener Speedbrake | Speedverlust bei ~450 KIAS, Unterschied zu M2 |

**Auswertung:** M1 zeigt, wie schnell du nach einem Turn wieder ins Band kommst; M2 zusammen mit M1 trennt Schub und Widerstand; M3 ist deine dauerhafte Rate im Ranked-Startbereich; M4 zeigt, was der erste Turn bringt und was er kostet; M5 ersetzt die Annahmen zum Override im [3D-Simulator](/VFM_Wiki/sim/){target="_self"}. M6 und M7 sind bisher von niemandem gemessen: Die Spieldaten nennen als Vorgabe des Fly-by-Wire 325 °/s Roll für die T-15 und 420 °/s für T-16 und T-18, ob der Jet das im Flug schafft, ist offen ([Pitch- und Rollrate](/grundlagen/physik#pitch-und-rollrate)). Die Rollrate entscheidet laut [Simulation](/flugzeuge/simulation#die-paarungen) besonders T-15 gegen T-18. Referenzwerte: [Beschleunigung (gemessen)](/flugzeuge/vergleich#beschleunigung-gemessen), [Schub und Widerstand getrennt](/flugzeuge/vergleich#schub-und-widerstand-getrennt), [Voller Zug](/flugzeuge/vergleich#voller-zug-was-ohne-override-wirklich-geht), [Der erste Turn (gemessen)](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen). Variante: M3 bei 420 und 520 KIAS wiederholen, dann siehst du, wie flach das Plateau deines Jets ist.

| | M1: 300 → 500 KIAS (s) | M2: Verlust bei 450 (kt/s) | M3: G / °/s | M4: Höchst-G / α | M6: s für 360° |
|---|---|---|---|---|---|
| Lauf 1 | | | | | |
| Lauf 2 | | | | | |

::: info SCHON GEKLÄRT, NICHT MEHR MESSEN
- **Ranked-Start:** 10.000 ft, Mach 0,75 (~427 KIAS), Head-on, 13.100 ft Abstand, ~1.300 ft Versatz, Merge nach ~8 s (*Replays*, siehe [Spielmodi](/einstieg/spielmodi#ranked)).
- **Fuel beim Start:** voller Tank (*Spieldaten*).
- **Gewichte:** leer 15,0 / 10,0 / 14,5 t, voll 19,15 / 12,14 / 18,70 t (T-15 / T-16 / T-18, *Spieldaten*, wie in den Diagrammen).
- **Kanone:** 1.030 m/s Mündungsgeschwindigkeit, 100 Schuss/s (*Spieldaten*, siehe [Waffen](/avionik/waffen#bordkanone)).
- **Schub/Gewicht und G-Limit:** Die Spieldaten bestätigen die Messflüge (1,64 / 1,29 / 1,37; 9 G für alle).
:::

### B3 Corner Speed finden

1. 10.000 ft, geradeaus mit 300 KIAS.
2. Für 180° **maximal** ziehen (bis G- oder AoA-Limit, **ohne** Override). Drehrate im HUD ablesen oder die Zeit stoppen (Rate = 180° / Zeit).
3. Wiederholen bei 350, 400, 450 und 500 KIAS.

**Die Speed mit der höchsten Rate ist deine Corner Speed.** Darunter stößt du ans AoA-Limit, ehe du 9 G erreichst, darüber an die 9 G. Erwartung laut Diagramm (10.000 ft): T-15 ~360–385, T-16 ~409–421, T-18 ~385–409 KIAS. Für 9 G musst du wegen des G-Aufbaus deutlich über Corner Speed anfangen zu ziehen. Die T-18 dabei mit α ~26° fliegen, nicht 35°: Über HUD-α ~27° fällt bei allen Jets der Auftrieb (*Spieldaten*).

| Einstieg | 300 | 350 | 400 | 450 | 500 KIAS |
|---|---|---|---|---|---|
| Rate (°/s) | | | | | |
| Speed nach 180° | | | | | |

### B4 Unload vs. 1 G

1. 10.000 ft, 250 KIAS, volle Leistung.
2. **a:** geradeaus mit 1 G bis 450 KIAS, Zeit stoppen.
3. **b:** **unloaded** (ca. 0–0,5 G, Nase leicht unter dem Horizont) bis 450 KIAS, Zeit und Höhenverlust notieren.

**Lektion:** Ohne Lift sinkt der induzierte Widerstand, du beschleunigst deutlich schneller. Das ist dein Werkzeug, um nach einem harten Turn zurück ins Band zu kommen ([Unload richtig gemacht](/grundlagen/energie-management#unload-richtig-gemacht)).

### B5 Vertikal-Tests

Für jeden Jet unter gleichen Bedingungen ([Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)):

1. **Looping:** Mit welcher Einstiegsspeed kommst du mit max G kontrolliert über den Scheitel, und wie schnell bist du oben? Einmal mit, einmal ohne Override.
2. **Zoom:** Von 450 KIAS mit ~60° Steigwinkel hoch, bis 200 KIAS. Höhengewinn notieren.

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| Min. Einstiegsspeed Looping (max G) | | | |
| Speed oben am Scheitel | | | |
| Höhengewinn Zoom 450 → 200 KIAS | | | |

Die Werte brauchst du, um die Vertikale zu verstehen, nicht um sie zu suchen: In der [Simulation](/flugzeuge/simulation#was-fur-alle-jets-gilt) verliert „steil hoch“ in jeder Paarung.

### B6 Die T-18-Hypothese testen

Ihre vermutete Stärke liegt unter dem gemessenen Bereich (unter ~280 KIAS, hoher AoA, Override). Flieg bei ~200 KIAS mit T-18, T-15 und T-16 je eine 180°-Kurve mit Limiter und eine mit Override, dazu schnelle Reversals. Ablauf und Tabelle: [T-18, Hypothese testen](/flugzeuge/t18#hypothese-testen). Die Simulation spricht bisher dagegen: Der langsame One-Circle (280 KIAS) ist dort auch für die T-18 schwach, weil hoher α sehr viel Energie kostet. Unter ~280 KIAS ist das Modell aber nicht geprüft. Dreht die T-18 dort klar schneller, ist das ihr Terrain in [Scissors](/grundlagen/neutral/scissors).

### B7 Unter dem Anschlag fliegen

1. 10.000 ft, ~430 KIAS, Nachbrenner.
2. **a:** 180° mit Knüppel voll (Limiter, T-18 α ~26°). Zeit und Speed am Ende notieren.
3. **b:** 180° mit 4–6° weniger α als bei a (HUD ablesen). Zeit und Speed notieren.

**Lektion:** Der Widerstand steigt mit α steil, der Auftrieb in der Nähe des Maximums kaum noch (*Spieldaten*). Erwartung: Bei b brauchst du etwas länger, bist am Ende aber deutlich schneller und noch im Band. Im Kampf ist das meist der bessere Tausch, außer für einen Schuss. Gemessen ist das noch nicht; trag deine Werte ein.

| | Zeit für 180° | Speed danach |
|---|---|---|
| a: voll | | |
| b: unter dem Anschlag | | |

## Stufe C: Gegen Bots

Bots gibt es offline und in Lobbys („Fill with bots“), ohne Schwierigkeitsstufe (Bot-Rating 1000). Sie sind konstante Sparringspartner, aber keine Menschen: Lern keine Tricks, die nur gegen Bots funktionieren. Startdistanz **nah** für schnelle Merges, **BVR**, wenn du Speed und Versatz selbst einstellen willst.

| Drill | Aufgabe | Erfolgskriterium |
|---|---|---|
| **C1 Speed halten** | 10 Merges ohne Nachbrenner-Exzess; nach dem ersten Turn im Kampfband bleiben: ~360–440 KIAS, T-16 ~420–440 | im Replay 8 von 10 nach dem ersten Turn im Band |
| **C2 Erster Turn** | 10 Merges aus ~430 KIAS, nur der erste Turn zählt: T-16 sustained, T-18 mit α ~26°, T-15 voll nur, bis der Winkel da ist, dann zurück ins Band ([Szene im 3D-Simulator](/VFM_Wiki/sim/?szenario=erster-turn){target="_self"}) | nach 90° bist du öfter vorn als er, ohne unnötig Speed zu verlieren |
| **C3 Two-Circle nose-low** | am Pass zum Gegner hin drehen, Nase leicht unter dem Horizont, je 5 Kämpfe gegen jeden Bot-Jet ([Two-Circle](/VFM_Wiki/sim/?szenario=t16-two-circle){target="_self"}, [Nose-low](/VFM_Wiki/sim/?szenario=nose-low){target="_self"}) | du drehst in jedem Pass hin, bleibst im Band und über dem Hard Deck |
| **C4 Guns** | Guns-only, Infinite Ammo, Tracking Shots aus dem Rear Quarter | Treffer ohne Overshoot ([Schusslösung](/grundlagen/offensiv/schussloesung)) |
| **C5 Raketenabwehr** | Raketen an: Break, Flares, Gas auf Idle (nur für Lobbys mit Raketen; Ranked 1v1 ist Guns-only) | jede Rakete überlebt ([Break Turn](/grundlagen/defensiv/break-turn)) |
| **C6 Schlechtes Matchup** | bewusst dein schwierigstes Matchup | du hältst dein Speedband trotz Druck |

Warum C1 und C3 so aussehen: In ~405.000 simulierten Ranked-Kämpfen ist der **Two-Circle bei ~360–440 KIAS, nose-low oder flach,** für alle drei Jets die beste Familie; langsam (280) und schnell (520) verlieren ([Simulation](/flugzeuge/simulation)).

::: info IM SPIEL PRÜFEN
- Ob Lobby oder Offline-Modus offensive oder defensive Startpositionen gegen Bots anbieten (sonst beginnen alle Bot-Drills neutral).
- Ob Bots in Free Flight verfügbar sind.
- Ob die nahe Startdistanz in Custom-Lobbys dieselbe Geometrie hat wie der Ranked-Start.
:::

## Stufe D: Lobby mit Partner

Custom-Lobby, Push-to-Talk, Rollen abwechselnd tauschen. **Lobby:** Guns-only, Infinite Ammo, Startdistanz BVR; die Position fliegt ihr nach dem Start selbst an. **Funk:** „Fight's on“ startet, „Knock it off“ bricht ab.

### D1 Offensive / Defensive Perch

- **Aufstellung:** Der Verteidiger fliegt geradeaus mit vereinbarter Speed (z. B. ~400 KIAS). Der Angreifer sitzt **3.000–6.000 ft** dahinter, 30–45° seitlich, leicht überhöht.
- **Fight's on:** Der Verteidiger breakt in den Angreifer.
- **Angreifer:** Turn Circle Entry in Lag, Control Zone halten, kein Overshoot, Guns ([Offensiv-Manöver](/grundlagen/offensiv-manoever)). 3.000 ft sind ~0,75 s Geschossflugzeit: Vorhalt über den Funnel.
- **Verteidiger:** Schusslösung verweigern, Overshoot erzwingen, neutralisieren oder separieren ([Defensiv-Manöver](/grundlagen/defensiv-manoever)).
- **Steigerung:** erst 6.000 ft, dann 3.000 ft. Entfernung ablesen: [Radar](/avionik/radar), [HUD](/avionik/hud).

### D2 Butterfly (neutral)

- **Aufstellung:** nebeneinander, gleiche Höhe und Speed, 1–1,5 NM Abstand.
- **„Turn away“:** beide drehen 45° auseinander und fliegen ein Stück geradeaus. **„Turn in“:** beide drehen zueinander, es folgt ein Merge mit Versatz.
- **Ranked-Variante:** 10.000 ft, ~427 KIAS, Head-on mit ~1.300 ft Versatz, ohne Nachbrenner bis zum Merge.
- **Fokus:** Lead-Turn-Timing, Drehrichtung am Pass, den Turn des Gegners lesen ([Der Merge](/grundlagen/neutral/der-merge)).

### D3 Matchup-Abend

Alle Paarungen aus beiden Cockpits, je 3 Kämpfe. Vorher die Matchup-Seite lesen: [T-15 vs T-16](/flugzeuge/matchups/t15-vs-t16), [T-15 vs T-18](/flugzeuge/matchups/t15-vs-t18), [T-16 vs T-18](/flugzeuge/matchups/t16-vs-t18). Fliegt jede Paarung einmal mit dem Plan der Simulation (Two-Circle bei ~360–440 KIAS, nose-low) und einmal mit eurem gewohnten Plan, dann vergleicht ihr im Replay.

## Replay und Debrief

VFM hat einen 3D-Replay-Raum mit **Specific-Energy-Graph** und einer S-Cam mit HUD-Modus. Nutze ihn nach jeder Session, mindestens für verlorene Kämpfe:

1. **Merge:** Speed beim Pass, seitlicher Versatz, wer zuerst gedreht hat, welcher Flow entstand.
2. **Energie-Graph:** Wo fällt deine Energie steil ab? Meist ein voller Zug am Anschlag oder eine lange Kurve außerhalb deines Bands. Wer hatte bei jedem Pass mehr Energie?
3. **Erster Nachteil:** Zurückspulen zum Moment, in dem du zum ersten Mal schlechter standest. Welche Entscheidung kam davor?
4. **Lift Vector:** Hast du dorthin gezogen, wo du hinwolltest?
5. **Schüsse** (S-Cam, HUD-Modus): War er im Funnel? Zu früh oder zu spät?

**Debrief in drei Sätzen:** Was ist passiert? Warum? Was mache ich nächstes Mal anders? Der dritte Satz ist der Fokus der nächsten Session.

### E1 Eigene Replays auswerten

Für Zahlen statt Eindrücke: Das Skript `tools/replays/vrb.py` aus dem [Wiki-Repo](https://github.com/lukaio3D/VFM_Wiki/tree/main/tools/replays) liest deine Replays (Speicherort und Dateien: [Spielmodi, Replay und Debrief](/einstieg/spielmodi#replay-und-debrief)) und gibt Flugbahn, KIAS, G, Ps und Schüsse aus, mit `--csv` als Tabelle.

1. **Übersicht:** `python vrb.py` listet alle eigenen Replays mit Datum, Dauer, Jets, Elo und Abschüssen. Wie lange dauern deine Runden im Vergleich zum Median von 146 s (*Replays*)? Wie oft stürzt du ab?
2. **Ein Replay:** `python vrb.py replayNN` zeigt KIAS- und Höhenbereich, höchste G und die Zeit über 7 G. Viel Zeit über 7 G heißt meist: zu oft am Anschlag.
3. **Kampf-Speed** (`--csv`, Spalte `kias`): Wie viel Zeit verbringst du im Band ~360–440 KIAS, wie viel darunter? Langsam kämpfen (~280 KIAS) ist laut Simulation ein Loch, aus dem du schwer herauskommst.
4. **Erster Turn:** KIAS, G (`n`) und Ps (`ps_fts`) in den ersten 20 s. Hast du bis zum Merge Nachbrenner gegeben? Wie schnell warst du nach dem ersten Turn?
5. **Höhe** (`hoehe_ft`): Tiefster Punkt der Runde. Wie nah warst du am Boden?
6. **Schüsse** (Geschoss-CSV): Wann hast du geschossen, und wie weit war der Gegner weg? Viele Schüsse aus großer Entfernung sind verschenkte Gelegenheiten.

Vergleiche mit 5–10 Runden desselben Matchups. Zum Abgleich eignen sich die drei Lehr-Replays des Entwicklers im Spielordner (`--ordner` auf `VFM_Data\StreamingAssets\Replays`). Den Anstellwinkel zeigen die Dateien nicht.

## Wochenplan (Beispiel)

| Tag | Session (30–45 min) | Fokus |
|---|---|---|
| 1 | Free Flight | B1 Lift Vector + B2, B3 oder B7 |
| 2 | Bots | C1/C2 Speed halten und erster Turn, danach Replay |
| 3 | Pause oder Lesen | eine Grundlagen-Seite zum Fehler aus dem Debrief |
| 4 | Lobby mit Partner | D1 Perch (beide Rollen) |
| 5 | Bots oder Lobby | C3 Two-Circle / D3 Matchup |
| 6 | Ranked oder freie Lobby | anwenden, danach 2 verlorene Kämpfe im Replay |
| 7 | Pause oder E1 | die Runden der Woche mit `vrb.py` auswerten |

Regelmäßigkeit schlägt Länge. Nach einem Balance-Patch B2 und B3 neu fliegen.

## Selbstcheck

Wo du „noch nicht“ sagst, lies die Seite und mach die Übung.

- **Flugphysik:** Ich kenne Corner Speed, Sustained Rate und Beschleunigung meines Jets aus eigener Messung (B2, B3), fliege unter dem Anschlag (B7) und unloade bewusst (B4). → [Energie-Management](/grundlagen/energie-management)
- **Geometrie:** Ich schätze Aspect Angle und Closure ein und wähle Lead, Pure oder Lag bewusst. → [Verfolgungskurven](/grundlagen/verfolgungskurven)
- **Offensiv:** Ich komme aus dem Perch in die Control Zone, ohne zu überschießen. → [Offensiv-Manöver](/grundlagen/offensiv-manoever)
- **Defensiv:** Ich breake auf Call sofort richtig und weiß, wann Separation geht. → [Defensiv-Manöver](/grundlagen/defensiv-manoever)
- **Neutral:** Ich drehe am Pass zum Gegner hin, bleibe nose-low oder flach im Band ~360–440 KIAS und weiß aus meinen Replays, wo ich wirklich lande. → [Der Merge](/grundlagen/neutral/der-merge), [Simulation](/flugzeuge/simulation)

::: tip MERKE
- Erst den eigenen Jet vermessen (B2, B3), dann kämpfen. Rollrate und Speedbrake (M6, M7) sind noch offen.
- Ein Fokus pro Session, gleiche Bedingungen wie im Ranked (10.000 ft, voller Tank, ~427 KIAS), Werte aufschreiben.
- Trainiere den Two-Circle bei ~360–440 KIAS, nose-low oder flach, und flieg knapp unter dem Anschlag.
- Bots für Wiederholung, Partner für klassische Setups, Ranked zum Anwenden.
- Jede Session endet im Replay: Energie-Graph lesen, ersten Nachteil finden, einen Satz für das nächste Mal. Zahlen liefert `vrb.py`.
- Nach Balance-Patches neu messen.
:::

Weiter: [Flugzeugvergleich](/flugzeuge/vergleich)
