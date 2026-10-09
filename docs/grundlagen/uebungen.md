# Trainingsplan

> Lesen allein macht dich nicht besser, Fliegen schon. Hier sind konkrete Übungen von der Academy bis zum Lobby-Duell, in sinnvoller Reihenfolge, mit Werten zum Eintragen.

Gute BFM-Piloten trainieren nicht nur „ein paar Runden Ranked“, sondern gezielt: **ein Fokus pro Session, gleiche Bedingungen, danach Debrief.** Dieser Plan führt dich in vier Stufen von „ich kenne meinen Jet“ bis „ich gewinne den Merge gegen Menschen“.

## Grundregeln fürs Training

- **Ein Fokus pro Session**: z. B. nur Lead Turns, nicht alles gleichzeitig.
- **Gleiche Bedingungen**: Miss auf derselben Höhe (10.000 ft, damit du mit den [Ingame-Daten](/flugzeuge/vergleich) vergleichen kannst) und mit ähnlichem Treibstoff. 100 % statt 50 % Fuel kostet etwa 1 °/s Instant und 1–2 °/s Sustained.
- **Aufschreiben**: Werte und Beobachtungen notieren, sonst bleibt nur ein Gefühl.
- **Hard Deck**: Im Training ist 2.000 ft über Grund der Boden. Wer darunter kommt, hat die Übung verloren.
- **Kurze Pulls**: VFM simuliert Greyout und Blackout. Wiederhole Max-G-Übungen lieber kurz und oft.

::: info IM SPIEL PRÜFEN
- Ob du in Free Flight Jet, Höhe und Treibstoffmenge frei wählen kannst.
- In welchem Format das HUD Speed (KIAS?), Höhe und Kurs anzeigt. Für die Rate-Messungen brauchst du eine Kursanzeige oder einen markanten Punkt im Gelände.
:::

## Stufe A: Academy

Fang mit den eingebauten Tutorials an, auch wenn du schon fliegen kannst:

1. **BFM-Tutorials** der Academy komplett durchfliegen.
2. **Gunsight-Tutorial** (seit v1.2.8): Funnel und Boresight-Kreuz verstehen.
3. Steuerung sauber einrichten (Stick-Position, Modus, HOTAS): [Steuerung & Einstellungen](/einstieg/cockpit).

**Ziel**: Du findest im HUD ohne Suchen die AoA-Zahl, den Beschleunigungs-Indikator und den Funnel ([HUD](/avionik/hud)).

## Stufe B: Free Flight, lerne deinen Jet kennen

### B1 Lift-Vector-Drill

Such dir einen Punkt im Gelände (Bergspitze, Insel). Roll so, dass dein **Lift Vector** (die Richtung über dein Kabinendach) genau auf den Punkt zeigt, dann zieh. Wechsle nach links und rechts, über und unter dem Horizont.
**Ziel**: Rollen und Ziehen werden eine flüssige Bewegung, 10 saubere Wiederholungen pro Seite. Wer nicht weiß, wohin er zieht, lernt hier am meisten.

### B2 Corner Speed finden

1. Fliege auf 10.000 ft geradeaus mit 300 KIAS.
2. Roll in die Kurve und zieh **maximal** (bis G-Limit oder AoA-Limit, **ohne** Override) für eine 180°-Kurve. Stoppe die Zeit.
3. Wiederhole das bei 350, 400, 450 und 500 KIAS.
4. Turn Rate = 180° / Zeit. Achte auf HUD-G und AoA: Unter Corner Speed stößt du ans AoA-/Lift-Limit, ehe du 9 G erreichst. Darüber stößt du an die 9-G-Grenze.

**Die Speed mit der kürzesten Zeit ist deine Corner Speed.** Erwartung laut Daten (Stand Dez 2025, 10.000 ft): T-15 ~360–385, T-16 ~409–434, T-18 ~385–409 KIAS.

| Einstieg | 300 | 350 | 400 | 450 | 500 KIAS |
|---|---|---|---|---|---|
| Zeit für 180° | | | | | |
| Rate (°/s) | | | | | |
| Speed nach 180° | | | | | |

### B3 Beschleunigung: Unload vs. 1 G

1. 10.000 ft, 250 KIAS, volle Leistung.
2. **Variante a**: geradeaus mit 1 G bis 450 KIAS, Zeit stoppen.
3. **Variante b**: **unloaded**, also ca. 0–0,5 G mit der Nase leicht unter dem Horizont, bis 450 KIAS. Zeit stoppen und Höhenverlust notieren.
4. Beobachte dabei den **Beschleunigungs-Indikator** im HUD.

**Lektion**: Ohne Lift sinkt der induzierte Widerstand, und du beschleunigst deutlich schneller. Das ist dein wichtigstes Werkzeug, um nach einem harten Turn wieder ins Speedband zu kommen. Vergleiche die Jets: Die Schub-Balken lassen T-15 > T-18 > T-16 erwarten.

### B4 Best Sustained Turn

1. 10.000 ft, volle Leistung, Kurve bei ~470 KIAS (T-15: ~495).
2. Dosier das G so, dass die Speed **konstant** bleibt. Das ist deine Sustained Turn.
3. Stopp die Zeit für 360°. Wiederhole das bei 400 und 550 KIAS.

**Lektion**: Du spürst, wo dein Jet Rate halten kann und wo er sie verliert. Die T-16 sollte im Band 420–500 KIAS 1–2 °/s vorn sein, die T-15 über ~500 KIAS, und die T-18 bricht über ~480 KIAS ein.

### B5 Vertikal-Tests

Looping-Einstiegsspeed, Speed oben am Scheitel und Zoom-Höhe von 450 auf 200 KIAS, für jeden Jet. Tabelle und Ablauf: [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf).

### B6 Die T-18-Hypothese testen

Der Entwickler beschreibt die T-18 als High-AoA-/Low-Speed-Jet. Ihre vermutete Stärke liegt **unter** den Ingame-Diagrammen (unter ~170–200 KIAS), wo es keine Daten gibt. Teste das:

1. T-18, 10.000 ft, 50 % Fuel (falls einstellbar), geradeaus mit **200 KIAS**.
2. Zieh maximal für 180°: einmal **mit** AoA-Limiter, einmal **mit Override**. Notiere die Zeit und die Speed danach.
3. **Reversal-Test**: Bei 150–200 KIAS schnell von einer Kurve in die Gegenkurve rollen. Wie schnell kommt der Jet herum, und bleibt er kontrollierbar?
4. Dasselbe mit der **T-15** (und der T-16) unter identischen Bedingungen.

| Bei 200 KIAS | T-15 | T-16 | T-18 |
|---|---|---|---|
| 180° mit Limiter (s) | | | |
| 180° mit Override (s) | | | |
| Speed danach | | | |
| Reversal-Gefühl | | | |

Dreht die T-18 hier klar schneller oder enger, ist die Hypothese gestützt, und das ist ihr Terrain in [Scissors](/grundlagen/neutral/scissors) und im langsamen One-Circle. Teil deine Ergebnisse mit der Community.

## Stufe C: Gegen Bots

Bots gibt es offline und in Lobbys („Fill with bots“). Sie haben **keine Schwierigkeitsstufe** (Bot-Rating 1000). Sie sind gute, konstante Sparringspartner, aber keine Menschen. Lern keine Tricks, die nur gegen Bots funktionieren.

**Setups**: Startdistanz **nah** für schnelle neutrale Merges, **BVR**, wenn du Speed und Versatz vor dem Merge selbst einstellen willst.

::: info IM SPIEL PRÜFEN
- Ob Lobby oder Offline-Modus offensive oder defensive Startpositionen gegen Bots anbieten. Falls nicht, beginnen alle Bot-Drills neutral.
- Ob Bots in Free Flight verfügbar sind.
:::

| Drill | Aufgabe | Erfolgskriterium |
|---|---|---|
| **C1 Merge-Speed** | 10 Merges, jedes Mal im eigenen [Merge-Band](/grundlagen/neutral/der-merge) ankommen | im Replay 8 von 10 im Band |
| **C2 Lead Turn** | 10 Merges, nur der erste Turn zählt | nach 90° bist du öfter vorn als er |
| **C3 Flow** | Fliege den Flow aus der [Flow-Tabelle](/grundlagen/neutral/one-two-circle) gegen jeden Bot-Jet, je 5 Kämpfe | du erkennst nach dem Pass sofort, ob One- oder Two-Circle entsteht |
| **C4 Guns** | Guns-only, Infinite Ammo: nur Tracking Shots aus dem Rear Quarter | Treffer ohne Overshoot ([Schusslösung](/grundlagen/offensiv/schussloesung)) |
| **C5 Raketenabwehr** | Raketen an: Break, Flares, Gas auf Idle | jede Rakete überlebt ([Break Turn](/grundlagen/defensiv/break-turn)) |
| **C6 Schlechtes Matchup** | Fliege bewusst dein schwierigstes Matchup | du hältst dein Speedband trotz Druck |

## Stufe D: Lobby mit Partner

Mit einem Partner kannst du die klassischen BFM-Setups fliegen, mit denen echte Piloten trainieren. Custom-Lobby, Push-to-Talk-Voice-Chat, abwechselnd die Rollen tauschen.

**Lobby**: Guns-only (Raketen aus), Infinite Ammo, Startdistanz BVR (gibt Zeit zum Aufstellen). Die Position fliegt ihr nach dem Start selbst an.
**Funk**: „Fight's on“ startet, „Knock it off“ bricht ab (Hard Deck verletzt, Tally verloren, Setup falsch).

### D1 Offensive / Defensive Perch

- **Aufstellung**: Der Verteidiger fliegt geradeaus, gleichmäßig, mit vereinbarter Speed (z. B. ~400 KIAS). Der Angreifer sitzt **3.000–6.000 ft** hinter ihm, etwa 30–45° seitlich versetzt, leicht überhöht.
- **Fight's on**: Der Verteidiger macht einen Break Turn in den Angreifer.
- **Angreifer-Ziel**: Turn Circle Entry in Lag, Control Zone halten, kein Overshoot, Guns ([Offensiv-Manöver](/grundlagen/offensiv-manoever)).
- **Verteidiger-Ziel**: Schusslösung verweigern, Overshoot erzwingen, neutralisieren oder sauber separieren ([Defensiv-Manöver](/grundlagen/defensiv-manoever)).
- **Steigerung**: Erst 6.000 ft (mehr Zeit), dann 3.000 ft (mehr Overshoot-Gefahr).

Die Abstände sind Richtwerte aus dem realen BFM-Training. Wo du die Entfernung zum Gegner ablesen kannst (Radar-Lock, HUD), findest du unter [Radar](/avionik/radar) und [HUD](/avionik/hud).

### D2 Butterfly (High Aspect / Neutral)

- **Aufstellung**: Nebeneinander (line abreast), gleiche Höhe und Speed, etwa 1–1,5 NM Abstand.
- **Call „Turn away“**: Beide drehen 45° auseinander und fliegen ein Stück geradeaus.
- **Call „Turn in“**: Beide drehen zueinander, es folgt ein Merge mit Versatz.
- **Fokus**: Merge-Speed, Lead-Turn-Timing, Flow-Wahl, den Turn des Gegners lesen ([Der Merge](/grundlagen/neutral/der-merge)).

### D3 Matchup-Abend

Fliegt alle Paarungen eurer Jets aus beiden Cockpits, je 3 Kämpfe, dann wechseln. Davor die passende Matchup-Seite lesen: [T-15 vs T-16](/flugzeuge/matchups/t15-vs-t16), [T-15 vs T-18](/flugzeuge/matchups/t15-vs-t18), [T-16 vs T-18](/flugzeuge/matchups/t16-vs-t18).

## Replay und Debrief

VFM hat einen 3D-Replay-/Debrief-Raum mit **Specific-Energy-Graph** und einer S-Cam mit HUD-Modus. Nutze ihn nach jeder Session, mindestens für die Kämpfe, die du verloren hast.

**Worauf du achtest:**

1. **Merge**: Welche Speed hattest du beim Pass? Wie groß war der seitliche Versatz? Wer hat zuerst gedreht, und welcher Flow ist entstanden?
2. **Energie-Graph**: Wo fällt deine Energie steil ab? Meist ist das ein Max-G-Pull weit über Corner Speed oder eine lange Kurve außerhalb deines Bands. Vergleiche das mit der Kurve des Gegners: Wer hatte bei jedem Pass mehr Energie?
3. **Der erste Nachteil**: Spul zu dem Moment zurück, in dem du zum ersten Mal schlechter standest. Welche Entscheidung kam direkt davor?
4. **Lift Vector**: Hast du dorthin gezogen, wo du hinwolltest, oder nur „irgendwie hart“?
5. **Schüsse** (S-Cam im HUD-Modus): War der Gegner im Funnel? Zu früh oder zu spät geschossen?
6. **Hard Deck**: Wie tief bist du gekommen?

**Debrief in drei Sätzen**: Was ist passiert? Warum? Was mache ich beim nächsten Mal anders? Schreib den dritten Satz auf und mach ihn zum Fokus der nächsten Session.

## Wochenplan (Beispiel)

Pass den Plan an deine Zeit an. Wichtiger als die Länge ist die Regelmäßigkeit.

| Tag | Session (30–45 min) | Fokus |
|---|---|---|
| 1 | Free Flight | B1 Lift Vector + B2/B3 (eine Messreihe) |
| 2 | Bots | C1/C2 Merge-Speed und Lead Turn, danach Replay |
| 3 | Pause oder Lesen | eine Grundlagen-Seite, passend zum Fehler aus dem Debrief |
| 4 | Lobby mit Partner | D1 Perch (beide Rollen) |
| 5 | Bots oder Lobby | C3 Flow / D3 Matchup |
| 6 | Ranked oder freie Lobby | anwenden, danach 2 verlorene Kämpfe im Replay analysieren |
| 7 | Pause | |

Nach etwa vier Wochen: B2–B4 noch einmal messen, vor allem nach einem Balance-Patch.

## Selbstcheck pro Lernstufe

Geh die Liste ehrlich durch. Wo du „noch nicht“ sagst, lies die Seite und mach die passende Übung.

**Stufe 0: Grundlagen**
- Ich kenne die [Golden Rules](/grundlagen/golden-rules) und halte Tally durch den Merge.
- Ich benutze die Begriffe und Brevity-Calls aus dem [Glossar](/grundlagen/begriffe) richtig.

**Stufe 1: Flugphysik**
- Ich kenne die Corner Speed und die Best-Sustained-Speed meines Jets, und zwar **gemessen** (B2, B4). → [Kurvenphysik](/grundlagen/kurvenphysik)
- Ich unloade bewusst, um zu beschleunigen (B3), und kann ein E-M-Diagramm lesen. → [Energie-Management](/grundlagen/energie-management)
- Ich weiß, was das VFM-Flugmodell simuliert. → [Flugmodell](/grundlagen/physik)

**Stufe 2: Geometrie**
- Ich schätze Aspect Angle, 3/9-Linie und Closure im Kampf ein. → [Relative Geometrie](/grundlagen/geometrie)
- Ich wähle Lead, Pure oder Lag bewusst. → [Verfolgungskurven](/grundlagen/verfolgungskurven)

**Stufe 3: Offensiv**
- Ich komme aus einem Perch in die Control Zone, ohne zu überschießen. → [Offensiv-Manöver](/grundlagen/offensiv-manoever), [Yo-Yos](/grundlagen/offensiv/yo-yos), [Lag Roll](/grundlagen/offensiv/lag-roll)
- Ich erkenne Flight-Path- und 3/9-Overshoot. → [Overshoot](/grundlagen/offensiv/overshoot)
- Ich unterscheide Snapshot und Tracking Shot. → [Schusslösung](/grundlagen/offensiv/schussloesung)

**Stufe 4: Defensiv**
- Ich breake auf Call sofort richtig. → [Break Turn](/grundlagen/defensiv/break-turn)
- Ich jinke gegen Guns, ohne langsam zu werden. → [Guns Defense](/grundlagen/defensiv/guns-defense)
- Ich kenne Slice, Spirale und den richtigen Moment für Separation. → [Slice Turn](/grundlagen/defensiv/slice-turn), [Spirale](/grundlagen/defensiv/spirale), [Separation](/grundlagen/defensiv/separation)

**Stufe 5: Neutral**
- Ich komme im Merge-Band an und time den Lead Turn über die Sichtlinienrate. → [Der Merge](/grundlagen/neutral/der-merge)
- Ich wähle den Flow passend zum Matchup und erkenne sofort, welcher entstanden ist. → [One-/Two-Circle](/grundlagen/neutral/one-two-circle)
- Ich erkenne Scissors früh und weiß, ob mein Jet sie gewinnt. → [Scissors](/grundlagen/neutral/scissors)
- Ich setze Vertikale und schräge Kurven gezielt zur Speed-Regelung ein. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

**Stufe 6: Training**
- Ich trainiere mit Fokus und mache nach jeder Session ein Debrief im Replay.

::: tip MERKE
- Erst den eigenen Jet vermessen (Corner, Sustained, Beschleunigung), dann kämpfen.
- Ein Fokus pro Session, gleiche Bedingungen, Werte aufschreiben.
- Bots für Wiederholung, Partner für klassische Setups, Ranked zum Anwenden.
- Jede Session endet im Replay: Energie-Graph lesen, ersten Nachteil finden, einen Satz für das nächste Mal.
- Nach Balance-Patches neu messen und die Daten nicht blind glauben.
:::
