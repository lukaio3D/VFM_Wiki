# Begriffe & Definitionen

> Das zentrale Glossar des Wikis: jeder Fachbegriff einmal, kurz und korrekt erklärt.

Die Begriffe sind nach Themen gruppiert und innerhalb jeder Gruppe alphabetisch sortiert. Wo es eine ausführliche Seite gibt, ist sie verlinkt. Funksprüche (Brevity) stehen gesammelt am Ende.

## Geometrie & Position

### 3/9-Linie
Die gedachte Linie durch die Flügel des Gegners, von seiner 3- zu seiner 9-Uhr-Position. Teilt den Raum in **vor ihm** und **hinter ihm**. Hinter seiner 3/9-Linie bist du im Vorteil. → [Relative Geometrie](/grundlagen/geometrie#die-3-9-linie)

### Aspect Angle (AA)
Gemessen am Gegner: Winkel zwischen seinem Heck und der Sichtlinie zu dir. 0° = du bist genau hinter ihm, 90° = auf seiner 3/9-Linie, 180° = genau vor ihm. Sagt, **wo du relativ zu ihm stehst**.

### Antenna Train Angle (ATA)
Gemessen an dir: Winkel zwischen deiner Nase und der Sichtlinie zum Gegner. 0° = er ist vor deiner Nase, 180° = er ist hinter dir. Sagt, **wohin du relativ zu ihm zeigst**.

### Bewegungsebene (Plane of Motion)
Die Ebene, in der ein Jet kurvt – aufgespannt von Flugrichtung und Lift Vector. Was außerhalb seiner Ebene liegt, kann er erst nach einer Rolle erreichen. → [Relative Geometrie](/grundlagen/geometrie#bewegungsebene-plane-of-motion)

### Bubble
Der Raum rund um den Gegner, in dem er dich mit Nase und Waffen nicht erreicht – vor allem außerhalb seines Kurvenkreises und hinter seiner 3/9-Linie. Wer in Lag Pursuit außerhalb seines Kreises bleibt, ist „außerhalb der Bubble“: Er kann nicht nachdrehen, ohne dir Winkel zu schenken. Typischer Fehler: zu nah oder zu schnell herein, in seinen Kreis hinein – dann ist man in der Bubble und er bekommt die Nase herum. → [Verfolgungskurven](/grundlagen/verfolgungskurven), [Overshoot](/grundlagen/offensiv/overshoot)

### Closure (Vc)
Die Geschwindigkeit, mit der die Entfernung zum Gegner abnimmt. Zu viel Closure nahe am Gegner führt zum Overshoot.

### Control Zone
Eine geometrische Position hinter dem Gegner, aus der du trotz seiner Manöver hinter ihm bleiben kannst. Richtwert: etwa 30–60° AA und einige tausend Fuß Range, abhängig von Jets und Speed – im Spiel testen. **Keine Waffenreichweite**, sondern Position. → [Relative Geometrie](/grundlagen/geometrie#control-zone)

### Heading Crossing Angle (HCA)
Der Winkel zwischen den Flugrichtungen beider Jets. 0° = parallel in dieselbe Richtung, 180° = gegeneinander. Hohe HCA beim Schuss = nur Snapshot möglich.

### Kurvenkreis (Turn Circle)
Der Kreis, den ein kurvender Jet beschreibt. Bist du **in** seinem Kreis, kannst du die Nase auf ihn bringen; bist du außerhalb, kann er dich wegdrehen.

### LOS / LOS-Rate
**Line of Sight**: die Sichtlinie zum Gegner. Die **LOS-Rate** ist, wie schnell sie sich dreht. Wandert der Gegner Richtung deiner Nase, gewinnst du Winkel; wandert er nach hinten, verlierst du. Vor dem Merge das Signal für den Lead Turn.

### Out of Plane
Manövrieren aus der Bewegungsebene des Gegners heraus (über oder unter ihn). Steuert Closure, nutzt die Schwerkraft und erschwert ihm das Zielen. → [Kurvenphysik](/grundlagen/kurvenphysik#out-of-plane-manovrieren)

### Range
Die Entfernung zum Gegner.

### Six / Uhrzeit-Angaben
Richtungen relativ zum eigenen Jet nach dem Zifferblatt: 12 Uhr = vorne, 6 Uhr ("Six") = hinten, 3 und 9 Uhr = seitlich. Dazu "high" und "low" für über und unter dir. "Check Six" = schau nach hinten.

### Turning Room
Der Platz (seitlich oder vertikal), den du brauchst, um deine Nase auf den Gegner zu drehen. Am Merge: Gib ihm keinen, nutz seinen.

### WEZ (Weapons Engagement Zone)
Der Raum, in dem eine Waffe treffen kann: begrenzt durch Mindest- und Maximalreichweite, Off-Boresight-Winkel und Aspect. → [Relative Geometrie](/grundlagen/geometrie#wez-gun-vs-fox-2)

## Flugphysik & Energie

### Anstellwinkel (AoA)
Angle of Attack: Winkel zwischen Flügel und anströmender Luft. Mehr AoA = mehr Auftrieb, bis zum Stall. Das VFM-HUD zeigt seit v1.2.0 eine AoA-Zahl.

### AoA-Limiter und Override
Der Limiter begrenzt den Anstellwinkel. Der Override-Button ("Cobra-Button") hebt die Grenze auf und gibt sofortige Nasen-Autorität darüber hinaus – kostet extrem viel Energie. Das G-Limit bleibt aktiv. → [Das VFM-Flugmodell](/grundlagen/physik#anstellwinkel-aoa-limiter-und-override)

### Best Sustained Speed
Die Speed mit der höchsten Sustained Turn Rate. Liegt meist über der Corner Speed – in VFM bei ~450–500 KIAS, in großer Höhe (20.190 ft) bei ~410–425 KIAS (je nach Jet und Fuel). **Nicht mit der Corner Speed verwechseln.**

### Buffet
Rütteln des Jets bei hoher Last bzw. hohem AoA durch abreißende, turbulente Strömung. VFM simuliert Buffeting.

### Corner Speed
Die **niedrigste Speed, bei der du das G-Limit (9 G) erreichst**. Dort hast du die maximale Instant Turn Rate und den kleinsten Radius bei 9 G – verlierst aber schnell Energie. VFM (10.000 ft, 50 % Fuel, Stand Okt 2026): T-15 ~360, T-16 ~409, T-18 ~385 KIAS. → [Kurvenphysik](/grundlagen/kurvenphysik#corner-speed)

### E-M-Diagramm
Energy-Maneuverability-Diagramm: Turn Rate über Speed mit Lift-Limit, G-Limit und Sustained-Linie (Ps = 0). In VFM als "Aircraft Performance Analysis" im Spiel. → [Energie-Management](/grundlagen/energie-management#das-leistungsdiagramm-in-vfm-lesen)

### Energiehöhe / Energy State
Gesamtenergie aus Speed und Höhe, umgerechnet in eine Höhe: Höhe + V²/(2g). "Energy State" beschreibt, wie viel davon du im Vergleich zum Gegner hast.

### G / Lastvielfaches (n)
Auftrieb geteilt durch Gewicht. 1 G = Geradeausflug, 9 G = Grenze in VFM, 0 G = ballistischer Flug.

### Greyout / Blackout
Bei hoher G wird das Bild erst grau (Greyout), dann schwarz (Blackout). VFM simuliert beides; Schwellen und Zeitverhalten im Spiel prüfen.

### Instantaneous Turn Rate
Die höchste Turn Rate, die du in einem Moment erreichen kannst – auch wenn du dabei Speed verlierst. Maximal bei Corner Speed.

### KIAS / TAS
**KIAS**: angezeigte Speed in Knoten. Bestimmt Auftrieb und G-Verfügbarkeit. **TAS**: wahre Speed durch die Luft. In der Höhe ist TAS größer als KIAS (in VFM 10.000 ft: ~12 %, 20.190 ft: ~28 %). Turn Rate und Radius hängen von der TAS ab.

### Lift-Limit
Die aerodynamische Grenze: Unterhalb der Corner Speed kann der Flügel nicht genug Auftrieb für 9 G erzeugen. Im E-M-Diagramm die steigende gestrichelte Linie.

### Lift Vector
Der Auftriebsvektor – zeigt senkrecht aus den Flügeln Richtung Kabinendach. **Wohin er zeigt, dorthin kurvst du, wenn du ziehst.** Jedes Manöver ist: Lift Vector platzieren, dann ziehen. → [Kurvenphysik](/grundlagen/kurvenphysik#der-lift-vector-das-zentrale-konzept)

### Mach / Transsonisch
Mach = Speed relativ zur Schallgeschwindigkeit (Meereshöhe ~661 kt). Transsonisch = etwa Mach 0,8–1,2. Dort steigt der Widerstandsbeiwert steil an und hat um Mach 1 sein Maximum; die Widerstandskraft steigt darüber weiter. → [Das VFM-Flugmodell](/grundlagen/physik#transsonischer-widerstand)

### Ps (Specific Excess Power)
Spezifische Überschussleistung: Ps = V · (T − D) / W. Positiv = du gewinnst Energie, null = du hältst sie (Sustained), negativ = du verlierst sie. → [Energie-Management](/grundlagen/energie-management#ps-wie-schnell-du-energie-gewinnst-oder-verlierst)

### Stall
Strömungsabriss oberhalb des kritischen Anstellwinkels: Der Auftrieb bricht ein, der Widerstand steigt stark.

### Sustained Turn Rate
Die Turn Rate, die du **ohne Speed- oder Höhenverlust** halten kannst (Ps = 0). Immer kleiner als die Instant Rate.

### Turn Radius
Der Radius deines Kurvenkreises: r = V² / (g · √(n² − 1)). Bei gleicher G wächst er mit dem Quadrat der Speed.

### Turn Rate
Wie viel Grad pro Sekunde deine Flugrichtung sich ändert: ω = g · √(n² − 1) / V.

### Unload
Lift fast auf null nehmen (**≈ 0 bis 0,5 G**), Nase am oder leicht unter dem Horizont, volle Leistung – maximale Beschleunigung. Bei 0 G ist die Bahn ballistisch. Nicht mit dem Gegner in Waffenreichweite hinter dir. → [Energie-Management](/grundlagen/energie-management#unload-richtig-gemacht)

## Kampf & Taktik

### Angles Fight / Energy Fight
Zwei **Kampftaktiken**, keine Flugzeugklassen. Angles Fight: Energie für schnellen Winkelgewinn ausgeben. Energy Fight: Energie aufbauen und halten (oft vertikal), Winkel erst später einlösen.

### Bandit / Bogey
**Bandit** = als feindlich bestätigter Jet. **Bogey** = unbekannter Kontakt.

### Engaged Fighter / Supporting Fighter
Rollen im Team: Der **Engaged Fighter** kämpft mit dem Gegner, der **Supporting Fighter** sichert, schaut nach weiteren Gegnern und schießt, wenn sich die Chance ergibt. Die Rollen wechseln dynamisch – sie hängen nicht an Lead oder Wingman. → [Team-Taktik](/flugzeuge/team)

### Hard Deck
Vereinbarte Mindesthöhe im Training. In diesem Wiki: **2.000 ft über Grund**. Darunter wird nicht gekämpft. Ein echtes Hard Deck im Spiel ist nicht bekannt. → [Golden Rules](/grundlagen/golden-rules#hard-deck-2-000-ft)

### Lead Turn
Einen Turn schon **vor** dem Merge beginnen, um Winkel zu gewinnen. Timing über den seitlichen Abstand und die LOS-Rate (grob bei ~1 Wenderadius Versatz). Zu früh = Flight-Path-Overshoot, zu spät = Gegner gewinnt Winkel. → [Der Merge](/grundlagen/neutral/der-merge)

### Merge
Der Moment, in dem die Jets aneinander vorbeifliegen. Ideal mit Corner- bis Best-Sustained-Speed. Richtwerte für VFM (10.000 ft, im Spiel testen): T-15 ~380–450, T-16 ~430–470, T-18 ~380–420 KIAS. → [Der Merge](/grundlagen/neutral/der-merge)

### Offensiv / Neutral / Defensiv
Offensiv: kleine AA und ATA – du sitzt hinter ihm. Defensiv: große AA und ATA – er sitzt hinter dir. Neutral: keiner hat einen klaren Vorteil.

### One-Circle / Two-Circle
**One-Circle**: Die Jets drehen nach dem Merge in **entgegengesetzter** Richtung und liegen auf einem gemeinsamen Kreis – Radius-Kampf, wird langsam. **Two-Circle**: Beide drehen in **dieselbe** Richtung, zwei Kreise, nose-to-tail – Rate-Kampf. → [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle)

### OODA-Loop
Observe – Orient – Decide – Act: der Entscheidungszyklus. Wer ihn schneller durchläuft als der Gegner, zwingt ihn zum Reagieren.

### Rate-Jet / Radius-Jet
Beschreibung der Stärke eines Jets: **Rate** = hohe Sustained Turn Rate (bevorzugt Two-Circle). **Radius** = enger Kreis, langsam stark (bevorzugt One-Circle). In VFM: T-16 = Rate-Spezialist, T-18 = Radius/Low-Speed-Design, T-15 = Energie/Allround. → [Flugzeugvergleich](/flugzeuge/vergleich)

### Separation / Extend
Abstand und Speed gewinnen, um den Kampf neu aufzusetzen oder ihn zu verlassen. → [Separation](/grundlagen/defensiv/separation)

## Manöver

### Barrel Roll Attack
Große Rolle **aus der Ebene** des Gegners bei zu hoher AA oder Closure (z. B. beim Eintritt mit hoher Aspect), um hinter ihn zu fallen. Nicht mit dem Lag Roll verwechseln. → [Lag Roll & Barrel Roll Attack](/grundlagen/offensiv/lag-roll)

### Break Turn
Sofortiger maximaler Defensivturn: Lift Vector auf den Angreifer, max Instant Rate nahe Corner Speed, dann Übergang in die Defensivkurve. → [Break Turn](/grundlagen/defensiv/break-turn)

### Climbing Spiral
Steigende Spirale zweier Jets – ein Energie-Wettbewerb: Wer mehr Ps hat, gewinnt. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

### Defensive Spirale
Last-Ditch-Manöver: steil nose-low, unter Last, langsam, um einen Overshoot zu erzwingen oder den Angreifer zuerst Richtung Boden zu zwingen. Braucht viel Höhe. → [Spirale](/grundlagen/defensiv/spirale)

### Egg (The Egg)
Die Form einer vertikalen oder schrägen Kurve: oben enger (langsamer, Schwerkraft hilft), unten weiter. Keine Steigspirale. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

### Guns Defense / Jink
Gegen einen Kanonenschuss: wiederholt unloaden, rollen und mit max G **aus der Ebene** des Angreifers ziehen, Ebene etwa jede Sekunde wechseln. → [Guns Defense](/grundlagen/defensiv/guns-defense)

### High Yo-Yo
Lift Vector **über** den Gegner rollen und ziehen: Closure und Speed werden in Höhe umgewandelt, die AA sinkt. Dann Lift Vector zurück auf ihn rollen und ziehen. Gegen Overshoot. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Lag Roll (Lag Displacement Roll)
Rolle über die Oberseite in Richtung **seiner** Kurve, um aus Lead oder Pure in Lag zu kommen und AA sowie Closure abzubauen, ohne viel Energie zu verlieren. → [Lag Roll](/grundlagen/offensiv/lag-roll)

### Lead / Pure / Lag Pursuit
Verfolgungskurven, definiert über Nase und Lift Vector relativ zum Gegner: **Lead** = vor ihn (Closure und AA steigen), **Pure** = auf ihn, **Lag** = hinter ihn (Closure und AA sinken). → [Verfolgungskurven](/grundlagen/verfolgungskurven)

### Low Yo-Yo
Überbanken, Lift Vector **unter** den Gegner, ziehen: Die Schwerkraft hilft bei der Rate, du schneidest seinen Kreis und gewinnst Closure. Kostet Höhe. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Overshoot
Der Angreifer schießt am Gegner vorbei. **Flight-Path-Overshoot**: Du kreuzt seine Flugbahn hinter ihm, verlierst Winkelvorteil, bist aber noch hinter seiner 3/9-Linie. **3/9-Line-Overshoot**: Du schießt an seiner 3/9-Linie vorbei und bist vor ihm – Rollentausch. → [Overshoot](/grundlagen/offensiv/overshoot)

### Quarter Plane
Abgeschwächter High Yo-Yo mit kleinerem Out-of-Plane-Anteil (Lift Vector nur etwas über dem Gegner), um Closure fein zu steuern. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Scissors (Flat / Rolling)
Wiederholtes Kreuzen der Flugbahnen. **Flat Scissors**: Gewinnt, wer schneller verlangsamt, dabei Kontrolle behält und die Umkehr gut timet. **Rolling Scissors**: Gewinnt, wer die Nase schneller über oben/unten bekommt. Neutrales Szenario. → [Scissors](/grundlagen/neutral/scissors)

### Slice (Nose-low Turn)
Überbankte Kurve mit Nase unter dem Horizont, nahe max G: Die Schwerkraft hilft bei der Rate und hält die Speed, die Höhe sinkt. → [Slice Turn](/grundlagen/defensiv/slice-turn)

### Turn Circle Entry
In den Kurvenkreis des Gegners hineinkommen: **in Lag, bis du in seinem Kreis bist, dann Lead.** → [Verfolgungskurven](/grundlagen/verfolgungskurven#turn-circle-entry)

### Zoom
Steigflug, bei dem du Speed in Höhe umwandelst. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

## Waffen & Avionik

### Boresight-Kreuz
Markierung im HUD für die Rohrrichtung der Kanone (seit v1.3.1). → [HUD](/avionik/hud)

### Flares
Heiße Täuschkörper gegen IR-Raketen. Die einzige Gegenmaßnahme in VFM. → [Gegenmaßnahmen](/avionik/gegenmassnahmen)

### Fox 2 / Heater
Fox 2 = Funkspruch für den Abschuss einer IR-Rakete. "Heater" = IR-Rakete. VFM hat genau einen Typ IR-Rakete; der Ingame-Name ist hier nicht verifiziert. → [Waffen](/avionik/waffen)

### Gun Funnel (EEGS)
Vorhalte-Trichter für die Kanone, bei allen Jets. Ohne Radar-Lock rechnet er mit einer durchschnittlichen Spannweite (seit v1.2.8); mit Lock liefert das Radar die Feuerleitlösung. → [HUD](/avionik/hud)

### MWS (Missile Warning System)
Warnt vor anfliegenden Raketen. Darstellung im Spiel prüfen. → [RWR & MWS](/avionik/rwr)

### Notching
Quer (etwa 90°) zum gegnerischen Radar fliegen, sodass du für sein Radar im Bodenclutter verschwindest. In VFM möglich (v1.2.0). → [Radar](/avionik/radar)

### Pipper
Zielpunkt im HUD für die berechnete Auftreffstelle. In VFM arbeitest du mit Gun Funnel und Boresight-Kreuz.

### Radar-Lock
Aufschalten des Radars auf ein Ziel. Liefert die Feuerleitlösung für den Funnel. Das Radar lässt sich ausschalten – dann bekommt der gegnerische RWR nichts. → [Radar](/avionik/radar)

### Radar-Modi
Das Wiki nennt SCAN, BST (Boresight) und VERT (vertikaler Scan). Die genauen Ingame-Namen sind nicht offiziell verifiziert – im Spiel prüfen. → [Radar](/avionik/radar)

### RWR (Radar Warning Receiver)
Zeigt an, wenn dich ein gegnerisches Radar erfasst. → [RWR & MWS](/avionik/rwr)

### Snapshot
Schuss mit **hoher AA bzw. HCA**: Der Gegner läuft durch den Funnel, du feuerst im richtigen Moment. Kein Halten auf dem Ziel möglich. Wird nach der Geometrie definiert, nicht nach der Entfernung. → [Schusslösung](/grundlagen/offensiv/schussloesung)

### Tracking Shot
Schuss **in seiner Ebene** mit kleiner AA: Du hältst den Funnel über längere Zeit auf dem Ziel. → [Schusslösung](/grundlagen/offensiv/schussloesung)

### Velocity Vector (Flight Path Marker)
Symbol, das zeigt, wohin der Jet tatsächlich fliegt – nicht, wohin die Nase zeigt. Ob und wie das VFM-HUD ihn darstellt: [HUD](/avionik/hud).

### Gibt es in VFM nicht

| Begriff | Bedeutung | In VFM |
|---|---|---|
| Fox 1 | Halbaktive Radarrakete | gibt es nicht |
| Fox 3 | Aktive Radarrakete | gibt es nicht |
| Chaff | Täuschkörper gegen Radar | gibt es nicht |
| HMD / Helmvisier | Zielen mit dem Kopf | gibt es nicht |

## Brevity (Funk)

Kurze, eindeutige Funksprüche für den eingebauten Voice-Chat.

| Funkspruch | Bedeutung |
|---|---|
| **Blind** | Ich sehe meinen Flügelmann/Freund nicht. |
| **Break (left/right)** | Sofort maximaler Defensivturn in die genannte Richtung. |
| **Bugout** | Ich verlasse den Kampf endgültig. |
| **Defensive** | Ich bin defensiv. |
| **Engaged** | Ich kämpfe mit dem Gegner / greife an. |
| **Extend** | Ich gewinne Abstand und Speed und komme später zurück. |
| **Fox 2** | IR-Rakete abgefeuert. |
| **Guns** | Schuss mit der Kanone. |
| **Knock it off** | Übung sofort abbrechen. |
| **Merged** | Freund und Feind sind am selben Punkt. |
| **Naked** | Nichts auf dem RWR. |
| **No Joy** | Ich sehe den Gegner nicht. |
| **Padlocked** | Ich kann den Blick nicht vom Gegner nehmen. |
| **Press** | (vom Supporting Fighter) Setz deinen Angriff fort. |
| **Separate** | Ich verlasse den Kampf. |
| **Spike** | RWR-Warnung: Ich werde vom Radar erfasst. |
| **Splash** | Abschuss. |
| **Tally** | Ich sehe den Gegner. |
| **Visual** | Ich sehe meinen Flügelmann/Freund. |

::: tip MERKE
- **Corner Speed ≠ Best Sustained Speed.** Corner = beste Instant Rate, Best Sustained = beste Dauerkurve.
- **Control Zone** ist Position, **WEZ** ist Waffenreichweite.
- **Snapshot vs. Tracking Shot** unterscheidet die Geometrie (AA, Ebene), nicht die Entfernung.
- **Unload** = ≈ 0–0,5 G, nicht negativ drücken.
- **Tally/No Joy** = Gegner, **Visual/Blind** = Freund.
:::

Weiter: [Kurvenphysik](/grundlagen/kurvenphysik)
