# Begriffe & Definitionen

> Das zentrale Glossar des Wikis: jeder Fachbegriff einmal, kurz und korrekt erklärt.

Die Begriffe sind nach Themen gruppiert und innerhalb jeder Gruppe alphabetisch sortiert. Der Pfeil führt zur Seite mit den Details. Funksprüche stehen am Ende.

## Geometrie & Position

### 3/9-Linie
Die gedachte Linie durch die Flügel des Gegners, von seiner 3- zu seiner 9-Uhr-Position. Hinter ihr bist du im Vorteil, vor ihr kann er dich mit der Nase erreichen. → [Relative Geometrie](/grundlagen/geometrie#die-3-9-linie)

### Aspect Angle (AA)
Am Gegner gemessen: Winkel zwischen seinem Heck und der Sichtlinie zu dir. 0° = genau hinter ihm, 90° = auf seiner 3/9-Linie, 180° = genau vor ihm. → [Relative Geometrie](/grundlagen/geometrie)

### Antenna Train Angle (ATA)
An dir gemessen: Winkel zwischen deiner Nase und der Sichtlinie zum Gegner. 0° = er ist vor deiner Nase, 180° = er ist hinter dir.

### Bewegungsebene (Plane of Motion)
Die Ebene aus Flugrichtung und Lift Vector, in der ein Jet kurvt. Was außerhalb liegt, erreicht er erst nach einer Rolle. → [Relative Geometrie](/grundlagen/geometrie#bewegungsebene-plane-of-motion)

### Bubble
Der Raum rund um den Gegner, in dem er dich mit Nase und Waffen nicht erreicht – vor allem außerhalb seines Kurvenkreises und hinter seiner 3/9-Linie. In der Bubble bleiben heißt sicher sein, etwa in Lag Pursuit außerhalb seines Kreises. Typischer Fehler: zu nah oder zu schnell in seinen Kurvenkreis hineinziehen – damit verlässt du die Bubble, und er bekommt die Nase herum. → [Verfolgungskurven](/grundlagen/verfolgungskurven), [Overshoot](/grundlagen/offensiv/overshoot)

### Closure (Vc)
Die Geschwindigkeit, mit der die Entfernung zum Gegner abnimmt. Zu viel Closure nahe am Gegner führt zum Overshoot.

### Control Zone
Eine Position hinter dem Gegner, aus der du trotz seiner Manöver hinter ihm bleibst. Keine Waffenreichweite, sondern Position. → [Relative Geometrie](/grundlagen/geometrie#control-zone)

### Heading Crossing Angle (HCA)
Der Winkel zwischen den Flugrichtungen beider Jets. 0° = parallel, 180° = gegeneinander. Hohe HCA beim Schuss erlaubt nur einen Snapshot.

### Kurvenkreis (Turn Circle)
Der Kreis, den ein kurvender Jet beschreibt. Bist du in seinem Kreis, kannst du die Nase auf ihn bringen; außerhalb kann er dich wegdrehen.

### LOS / LOS-Rate
Line of Sight ist die Sichtlinie zum Gegner, die LOS-Rate, wie schnell sie sich dreht. Wandert er Richtung deiner Nase, gewinnst du Winkel. → [Relative Geometrie](/grundlagen/geometrie)

### Out of Plane
Manövrieren aus der Bewegungsebene des Gegners heraus (über oder unter ihn). Steuert Closure, nutzt die Schwerkraft und erschwert ihm das Zielen. → [Kurvenphysik](/grundlagen/kurvenphysik#out-of-plane-manovrieren)

### Range
Die Entfernung zum Gegner.

### Six / Uhrzeit-Angaben
Richtungen nach dem Zifferblatt: 12 Uhr = vorne, 6 Uhr („Six“) = hinten, 3 und 9 Uhr = seitlich, dazu „high“ und „low“. „Check Six“ = schau nach hinten.

### Turning Room
Der Platz (seitlich oder vertikal), den du brauchst, um die Nase auf den Gegner zu drehen. Am Merge: Gib ihm keinen, nutz seinen.

### WEZ (Weapons Engagement Zone)
Der Raum, in dem eine Waffe treffen kann, begrenzt durch Reichweite, Off-Boresight-Winkel und Aspect. → [Relative Geometrie](/grundlagen/geometrie#wez-gun-vs-fox-2)

## Flugphysik & Energie

### Anstellwinkel (AoA, α)
Angle of Attack: Winkel zwischen Flügel und anströmender Luft. Mehr AoA gibt mehr Auftrieb, bis zum Stall. Das VFM-HUD zeigt ihn als Zahl.

### AoA-Limiter und Override
Der Limiter begrenzt den Anstellwinkel. Der Override („Cobra-Button“) hebt die Grenze auf, kostet extrem viel Energie; das G-Limit bleibt aktiv. → [Das VFM-Flugmodell](/grundlagen/physik#anstellwinkel-aoa-limiter-und-override)

### Best Sustained Speed
Die Speed mit der höchsten Sustained Turn Rate. Sie liegt meist deutlich über der Corner Speed – nicht verwechseln. → [Energie-Management](/grundlagen/energie-management#corner-speed-vs-best-sustained-speed)

### Buffet
Rütteln des Jets bei hoher Last bzw. hohem AoA durch abreißende Strömung. VFM simuliert es.

### Corner Speed
Die niedrigste Speed, bei der du das G-Limit (9 G) erreichst. Dort hast du die höchste Instant Turn Rate und den kleinsten Radius, verlierst aber schnell Energie. → [Kurvenphysik](/grundlagen/kurvenphysik#corner-speed)

### E-M-Diagramm
Energy-Maneuverability-Diagramm: Turn Rate über Speed mit Lift-Limit, G-Limit und Sustained-Linie (Ps = 0). In VFM heißt es „Aircraft Performance Analysis“. → [Energie-Management](/grundlagen/energie-management#das-leistungsdiagramm-in-vfm-lesen)

### Energiehöhe / Energy State
Gesamtenergie aus Speed und Höhe, ausgedrückt als Höhe: Höhe + V²/(2g). Energy State heißt, wie viel davon du im Vergleich zum Gegner hast.

### G / Lastvielfaches (n)
Auftrieb geteilt durch Gewicht. 1 G = Geradeausflug, 9 G = Grenze in VFM, 0 G = ballistischer Flug.

### Greyout / Blackout
Bei hoher G wird das Bild erst grau, dann schwarz. VFM simuliert beides. → [Golden Rules](/grundlagen/golden-rules#g-awareness-greyout-und-blackout)

### Instantaneous Turn Rate
Die höchste Turn Rate, die du in einem Moment erreichst, auch unter Speedverlust. Maximal bei Corner Speed.

### KIAS / TAS
KIAS ist die angezeigte Speed in Knoten; sie bestimmt, wie viel G du ziehen kannst. TAS ist die wahre Speed durch die Luft, in der Höhe größer als KIAS; Turn Rate und Radius hängen von ihr ab. → [Kurvenphysik](/grundlagen/kurvenphysik#kias-vs-wahre-speed-in-der-hohe)

### Lift-Limit
Die aerodynamische Grenze: Unterhalb der Corner Speed erzeugt der Flügel nicht genug Auftrieb für 9 G. Im E-M-Diagramm die steigende gestrichelte Linie.

### Lift Vector
Der Auftriebsvektor, senkrecht aus den Flügeln Richtung Kabinendach. Wohin er zeigt, dorthin kurvst du, wenn du ziehst. → [Kurvenphysik](/grundlagen/kurvenphysik#der-lift-vector-das-zentrale-konzept)

### Mach / Transsonisch
Mach ist die Speed relativ zur Schallgeschwindigkeit. Im transsonischen Bereich (etwa Mach 0,8–1,2) steigt der Widerstand steil an. → [Das VFM-Flugmodell](/grundlagen/physik#transsonischer-widerstand)

### Ps (Specific Excess Power)
Spezifische Überschussleistung: Ps = V · (T − D) / W. Positiv = Energiegewinn, null = Sustained, negativ = Energieverlust. → [Energie-Management](/grundlagen/energie-management#ps-wie-schnell-du-energie-gewinnst-oder-verlierst)

### Stall
Strömungsabriss oberhalb des kritischen Anstellwinkels: Der Auftrieb bricht ein, der Widerstand steigt stark.

### Sustained Turn Rate
Die Turn Rate, die du ohne Speed- oder Höhenverlust halten kannst (Ps = 0). Immer kleiner als die Instant Rate.

### Turn Radius / Turn Rate
Radius r = V² / (g · √(n² − 1)), Rate ω = g · √(n² − 1) / V. Bei gleicher G wächst der Radius mit V², die Rate sinkt mit 1/V. → [Kurvenphysik](/grundlagen/kurvenphysik)

### Unload
Lift fast auf null nehmen (≈ 0–0,5 G), Nase am oder leicht unter dem Horizont, volle Leistung: maximale Beschleunigung. Nicht mit dem Gegner in Waffenreichweite hinter dir. → [Energie-Management](/grundlagen/energie-management#unload-richtig-gemacht)

## Kampf & Taktik

### Angles Fight / Energy Fight
Zwei Kampftaktiken, keine Flugzeugklassen. Angles Fight: Energie für schnellen Winkelgewinn ausgeben. Energy Fight: Energie aufbauen und halten (oft vertikal), Winkel erst später einlösen.

### Bandit / Bogey
Bandit = als feindlich bestätigter Jet. Bogey = unbekannter Kontakt.

### Engaged Fighter / Supporting Fighter
Teamrollen: Der Engaged Fighter kämpft, der Supporting Fighter sichert und schießt bei Gelegenheit. Die Rollen wechseln dynamisch. → [Team-Taktik](/flugzeuge/team)

### Hard Deck
Vereinbarte Mindesthöhe im Training, in diesem Wiki 2.000 ft über Grund. → [Golden Rules](/grundlagen/golden-rules#hard-deck-2-000-ft)

### Lead Turn
Einen Turn schon vor dem Merge beginnen, um Winkel zu gewinnen. Zu früh = Flight-Path-Overshoot, zu spät = er gewinnt Winkel. → [Der Merge](/grundlagen/neutral/der-merge)

### Merge
Der Moment, in dem die Jets aneinander vorbeifliegen. Im Ranked startet ihr mit ~450 KIAS. → [Der Merge](/grundlagen/neutral/der-merge)

### Offensiv / Neutral / Defensiv
Offensiv: kleine AA und ATA, du sitzt hinter ihm. Defensiv: große AA und ATA, er sitzt hinter dir. Neutral: keiner hat einen klaren Vorteil.

### One-Circle / Two-Circle
One-Circle: Die Jets drehen nach dem Merge entgegengesetzt und liegen auf einem gemeinsamen Kreis – Radius-Kampf. Two-Circle: Beide drehen in dieselbe Richtung, zwei Kreise – Rate-Kampf. → [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle)

### OODA-Loop
Observe – Orient – Decide – Act: der Entscheidungszyklus. Wer ihn schneller durchläuft, zwingt den Gegner zum Reagieren.

### Rate-Jet / Radius-Jet
Rate = hohe Sustained Turn Rate, bevorzugt Two-Circle. Radius = enger Kreis, langsam stark, bevorzugt One-Circle. In VFM: T-16 = Rate-Spezialist, T-18 = Low-Speed-Brawler. → [Flugzeugvergleich](/flugzeuge/vergleich)

### Separation / Extend
Abstand und Speed gewinnen, um den Kampf neu aufzusetzen oder zu verlassen. → [Separation](/grundlagen/defensiv/separation)

## Manöver

### Barrel Roll Attack
Große Rolle aus der Ebene des Gegners bei zu hoher AA oder Closure, um hinter ihn zu fallen. → [Lag Roll & Barrel Roll Attack](/grundlagen/offensiv/lag-roll)

### Break Turn
Sofortiger maximaler Defensivturn: Lift Vector auf den Angreifer, maximale Rate. → [Break Turn](/grundlagen/defensiv/break-turn)

### Climbing Spiral
Steigende Spirale zweier Jets – wer mehr Ps hat, gewinnt. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

### Defensive Spirale
Last-Ditch-Manöver: steil nose-low, unter Last, langsam, um einen Overshoot zu erzwingen. Braucht viel Höhe. → [Spirale](/grundlagen/defensiv/spirale)

### Egg (The Egg)
Die Form einer vertikalen oder schrägen Kurve: oben eng (langsam, Schwerkraft hilft), unten weit. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

### Guns Defense / Jink
Gegen einen Kanonenschuss: unloaden, rollen, mit max G aus der Ebene des Angreifers ziehen, etwa jede Sekunde neu. → [Guns Defense](/grundlagen/defensiv/guns-defense)

### High Yo-Yo
Lift Vector über den Gegner rollen und ziehen: Closure wird in Höhe umgewandelt, die AA sinkt. Gegen Overshoot. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Lag Roll (Lag Displacement Roll)
Rolle über die Oberseite in Richtung seiner Kurve, um aus Lead oder Pure in Lag zu kommen, ohne viel Energie zu verlieren. → [Lag Roll](/grundlagen/offensiv/lag-roll)

### Lead / Pure / Lag Pursuit
Verfolgungskurven nach der Richtung von Nase und Lift Vector: Lead = vor ihn (Closure und AA steigen), Pure = auf ihn, Lag = hinter ihn (Closure und AA sinken). → [Verfolgungskurven](/grundlagen/verfolgungskurven)

### Low Yo-Yo
Lift Vector unter den Gegner, ziehen: Die Schwerkraft hilft bei der Rate, du schneidest seinen Kreis und gewinnst Closure. Kostet Höhe. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Overshoot
Der Angreifer schießt am Gegner vorbei. Flight-Path-Overshoot: Du kreuzt seine Bahn, bleibst aber hinter seiner 3/9-Linie. 3/9-Line-Overshoot: Du bist vor ihm – Rollentausch. → [Overshoot](/grundlagen/offensiv/overshoot)

### Quarter Plane
Abgeschwächter High Yo-Yo mit Lift Vector nur etwas über dem Gegner, um Closure fein zu steuern. → [Yo-Yos](/grundlagen/offensiv/yo-yos)

### Scissors (Flat / Rolling)
Wiederholtes Kreuzen der Flugbahnen. Flat: Gewinnt, wer kontrolliert schneller verlangsamt. Rolling: Gewinnt, wer die Nase schneller über oben/unten bekommt. → [Scissors](/grundlagen/neutral/scissors)

### Slice (Nose-low Turn)
Überbankte Kurve mit Nase unter dem Horizont, nahe max G: Die Schwerkraft hilft bei Rate und Speed, die Höhe sinkt. → [Slice Turn](/grundlagen/defensiv/slice-turn)

### Turn Circle Entry
In den Kurvenkreis des Gegners hineinkommen: in Lag, bis du in seinem Kreis bist, dann Lead. → [Verfolgungskurven](/grundlagen/verfolgungskurven#turn-circle-entry)

### Zoom
Steigflug, bei dem du Speed in Höhe umwandelst. → [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)

## Waffen & Avionik

### Boresight-Kreuz
HUD-Markierung für die Rohrrichtung der Kanone. → [HUD](/avionik/hud)

### Flares
Heiße Täuschkörper gegen IR-Raketen, die einzige Gegenmaßnahme in VFM. → [Gegenmaßnahmen](/avionik/gegenmassnahmen)

### Fox 2 / Heater
Fox 2 = Funkspruch für den Abschuss einer IR-Rakete, Heater = IR-Rakete. VFM hat genau einen Typ. → [Waffen](/avionik/waffen)

### Gun Funnel (EEGS)
Vorhalte-Trichter für die Kanone. Ohne Radar-Lock rechnet er mit einer durchschnittlichen Spannweite, mit Lock liefert das Radar die Entfernung. → [HUD](/avionik/hud)

### MWS (Missile Warning System)
Warnt vor anfliegenden Raketen. → [RWR & MWS](/avionik/rwr)

### Notching
Quer (etwa 90°) zum gegnerischen Radar fliegen, sodass du im Bodenclutter verschwindest. In VFM möglich. → [Radar](/avionik/radar)

### Pipper
Zielpunkt im HUD für die berechnete Auftreffstelle. In VFM arbeitest du mit Gun Funnel und Boresight-Kreuz.

### Radar-Lock
Aufschalten des Radars auf ein Ziel; liefert die Feuerleitlösung für den Funnel. Ausgeschaltetes Radar sieht der gegnerische RWR nicht. → [Radar](/avionik/radar)

### Radar-Modi
Das Wiki nennt SCAN, BST (Boresight) und VERT (vertikaler Scan); die Ingame-Namen sind nicht verifiziert. → [Radar](/avionik/radar)

### RWR (Radar Warning Receiver)
Zeigt an, wenn dich ein gegnerisches Radar erfasst. → [RWR & MWS](/avionik/rwr)

### Snapshot
Schuss mit hoher AA bzw. HCA: Der Gegner läuft durch den Funnel, du feuerst im richtigen Moment, ohne ihn halten zu können. Definiert über die Geometrie, nicht die Entfernung. → [Schusslösung](/grundlagen/offensiv/schussloesung)

### Tracking Shot
Schuss in seiner Ebene mit kleiner AA: Du hältst den Funnel über längere Zeit auf dem Ziel. → [Schusslösung](/grundlagen/offensiv/schussloesung)

### Velocity Vector (Flight Path Marker)
Symbol dafür, wohin der Jet tatsächlich fliegt, nicht wohin die Nase zeigt. → [HUD](/avionik/hud)

### Gibt es in VFM nicht

| Begriff | Bedeutung |
|---|---|
| Fox 1 | Halbaktive Radarrakete |
| Fox 3 | Aktive Radarrakete |
| Chaff | Täuschkörper gegen Radar |
| HMD / Helmvisier | Zielen mit dem Kopf |

## Brevity (Funk)

Kurze, eindeutige Funksprüche für den eingebauten Voice-Chat.

| Funkspruch | Bedeutung |
|---|---|
| **Blind** | Ich sehe meinen Flügelmann nicht. |
| **Break (left/right)** | Sofort maximaler Defensivturn in die genannte Richtung. |
| **Bugout** | Ich verlasse den Kampf endgültig. |
| **Defensive** | Ich bin defensiv. |
| **Engaged** | Ich kämpfe mit dem Gegner. |
| **Extend** | Ich gewinne Abstand und Speed und komme zurück. |
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
| **Visual** | Ich sehe meinen Flügelmann. |

::: tip MERKE
- **Corner Speed ≠ Best Sustained Speed.** Corner = beste Instant Rate, Best Sustained = beste Dauerkurve.
- **Control Zone** ist Position, **WEZ** ist Waffenreichweite.
- **Snapshot vs. Tracking Shot** unterscheidet die Geometrie, nicht die Entfernung.
- **Tally/No Joy** = Gegner, **Visual/Blind** = Freund.
:::

Weiter: [Kurvenphysik](/grundlagen/kurvenphysik)
