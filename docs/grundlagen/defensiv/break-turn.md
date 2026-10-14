# Break Turn

> Die erste Antwort auf einen Angriff: maximal hart in den Gegner hineindrehen, dann in eine Defensivkurve übergehen, die Energie hält.

Der Break ist die härteste Kurve, die dein Jet gerade fliegen kann. Er nimmt dem Angreifer den Winkel für Schuss und Position – und ist teuer. Flieg ihn so lange wie nötig, keine Sekunde länger.

## Wann

- Der Angreifer **kommt in deinen Kurvenkreis** oder ist kurz davor, in Schussposition zu kommen.
- Eine **Rakete ist in der Luft** (dann mit Flares und Idle, siehe [unten](#raketenabwehr-kurzfassung)).

**Zu früh** verschenkt Energie: Er geht einfach in Lag und schneidet in deinen Kreis. **Zu spät** ist schlimmer: Dann hat er den Schuss. Brich ein, wenn er beginnt, Lead auf dich zu ziehen, oder kurz bevor er in Reichweite ist.

## Ausführung

1. **Lift Vector auf den Angreifer.** Kabinendach auf ihn, damit seine AA so schnell wie möglich wächst.
2. **Maximal ziehen**: über Corner Speed bis ans G-Limit (9 G), darunter bis ans AoA-Limit. Bei T-15 und T-16 sitzt der Limiter (HUD-α ~24–25° bzw. ~23°) knapp unter dem Auftriebsmaximum, Knüppel voll ist also richtig. Ausnahme T-18: α ~26° halten, nicht an den 35°-Anschlag (siehe unten).
3. **Kopf drehen, Sicht halten** – du siehst ihn über das Kabinendach.
4. **Leicht nose-low, wenn Höhe da ist.** Das hilft der Rate und bremst den Speedverlust: Übergang zum [Slice Turn](/grundlagen/defensiv/slice-turn).

### Warum nahe Corner Speed

An der [Corner Speed](/grundlagen/kurvenphysik#corner-speed) ist deine Instant Rate maximal. Schneller deckelt das G-Limit die Rate (der Break bremst dich aber schnell herunter), langsamer schaffst du das G nicht mehr.

| 10.000 ft (Diagramm) | Corner Speed | Max Instant Rate dort |
|---|---|---|
| T-15 Excalibur | ~360–385 KIAS | 23–24 °/s |
| T-16 Falchion | ~409–421 KIAS | 20–21 °/s |
| T-18 Cutlass | ~385–409 KIAS | 21–22 °/s |

Spannen jeweils 50 bis 100 % Treibstoff; voller Tank heißt höhere Corner Speed und weniger Rate. Mit fast leerem Tank liegt die Corner Speed rund 25 KIAS tiefer. Im Flug erreichst du die Diagrammwerte ohne Override nicht ganz – laut Spieldaten liegt das Lift-Limit der Diagramme 13–24 % über dem größten Auftrieb, den der Jet im Flug schafft –, und bis die volle G anliegt, vergehen 2–3 s ([Voller Zug](/flugzeuge/vergleich#voller-zug-was-ohne-override-wirklich-geht)).

### Warum der Break so teuer ist

Der Widerstand steigt mit dem Anstellwinkel steil an: Bei α 15° hat der Flügel ~4- bis 12-mal, bei α 25° ~12- bis 34-mal so viel Widerstand wie bei α 0 (*Spieldaten*; T-15 am stärksten, T-18 am wenigsten, die dafür den höchsten Grundwiderstand hat). Deshalb kostet voller Zug so viel Energie, und deshalb lohnt alles, was dich unter dem Anschlag hält, sobald der Break gewirkt hat.

## Danach: die sustained Defensivkurve

Bei Corner Speed und max G verlierst du schnell Speed ([Ps](/grundlagen/energie-management#ps-wie-schnell-du-energie-gewinnst-oder-verlierst) stark negativ). Sobald der Break gewirkt hat – seine AA ist hoch, er hängt in Lag oder kommt nicht in deinen Kreis –, gehst du in die **sustained Defensivkurve**:

- **Last zurücknehmen**, bis die Speed nicht weiter fällt, und **zurück ins Kampfband ~360–440 KIAS** (Ziel: T-15 und T-16 ~400–420, T-18 ~440). Dort gewinnen laut Simulation alle drei Jets am meisten; wer auf ~280 KIAS absinkt, kommt aus dem Loch kaum noch heraus. Best Sustained laut Diagramm liegt höher (10.000 ft: T-15 ~495, T-16 und T-18 ~470 KIAS), aber das Plateau ist flach: Die T-16 dreht bei 420 statt 470 KIAS weniger als 2 % langsamer und fliegt einen ~9 % kleineren Kreis.
- **Volle Leistung**, außer gegen eine IR-Rakete.
- **Weiter beobachten:** Zieht er wieder Lead, wieder hart. Fällt er zurück, Energie halten.

::: tip DAS EIGENTLICHE KÖNNEN
Den Break kann jeder ziehen. Ihn im richtigen Moment wieder zu öffnen, trennt den Verteidiger, der ausblutet, von dem, der neutralisiert.
:::

## Die Jets

- **[T-15](/flugzeuge/t15):** Zieht bei gleicher Speed die meisten G und bricht am härtesten. Sie verliert im vollen Zug aber gut doppelt so schnell Energie wie die T-16 (gemessen; passt zum steilsten Widerstandsanstieg in den Spieldaten): Break kurz halten.
- **[T-16](/flugzeuge/t16):** Verliert im Zug am wenigsten Energie. Ihre Stärke ist die sustained Kurve; Ziel nach dem Break ~420 KIAS (geflogen ~420–440, Simulation). Brich nicht tiefer darunter als nötig.
- **[T-18](/flugzeuge/t18):** Zum Kurven α ~26° halten – dort hat sie die meisten G (gemessen). Die Spieldaten erklären das: Bei allen drei Jets liegt das Auftriebsmaximum bei HUD-α ~27°, darüber fällt der Auftrieb. Bis 35° zieht sie also weniger G bei extremem Widerstand; die vollen 35° nur für den [Snapshot](/grundlagen/begriffe#snapshot).

## Was der Break erreicht – und was nicht

Das Szenario „Bandit an deiner Six“ im 3D-Simulator zeigt es (*Simulation*, T-16 gegen T-16, Start 3.000 ft hinter dir): Mit Break und anschließender Kurve im eigenen Band (~440 KIAS) verweigerst du ihm den Schuss über die ganze Runde. **Umdrehen gelingt aus dieser Lage aber nicht**, und bei Zeitablauf gewinnt im Ranked der Verfolger. Wer stattdessen bei ~360 KIAS nose-low bleibt – für die T-16 unter ihrem Band –, wird nach knapp 3 Minuten getroffen.

- Der Break kauft dir Zeit, keinen Sieg. Gegen einen gleichwertigen Jet, der keinen Fehler macht, bleibst du hinten.
- Umdrehen braucht seinen Fehler: einen [Overshoot](/grundlagen/offensiv/overshoot), zu viel Lead, eine Ebene, die er dir schenkt. Halt die Energie, damit du ihn nutzen kannst.
- Die Bots zielen perfekt, sehen alles und planen nicht voraus. Gegen Menschen ist der Fehler wahrscheinlicher – darauf arbeitest du hin.

**Im 3D-Simulator:** [Defensiv: Bandit an deiner Six](/VFM_Wiki/sim/?szenario=defensiv){target="_self"}.

## Raketenabwehr: Kurzfassung

Nur in Custom-Lobbys mit Raketen; Ranked 1v1 ist Guns-only (*Replays*). Gegen eine IR-Rakete (Fox 2): **Idle + Flares + Break**, praktisch gleichzeitig. Ausführlich: [Gegenmaßnahmen](/avionik/gegenmassnahmen), Warnanzeigen: [RWR & MWS](/avionik/rwr).

1. **Rakete erkennen:** MWS-Warnung, Rauchspur, Funkruf.
2. **Gas auf Idle**, kein Nachbrenner.
3. **Flares in kurzen Gruppen**, nicht als Dauerstrom. Community-Tipp: so rollen, dass die Dispenser zur Rakete zeigen.
4. **Break** gleichzeitig mit den Flares, damit die Rakete stark nachkurven muss; gut getimt schlägt er sie auch kinematisch.
5. **Danach:** volle Leistung, Sicht auf den Schützen, Defensivkurve. Er kommt wahrscheinlich mit der Kanone hinterher.

::: danger KEIN CHAFF
VFM hat nur IR-Raketen. Chaff gibt es nicht und würde gegen einen Wärmesucher auch nichts bringen.
:::

## Typische Fehler

- **Weg vom Angreifer drehen.** Der Break geht in ihn hinein.
- **Den Break nie beenden.** Dann stehst du bald langsam und tief vor einem Angreifer, der Energie gespart hat.
- **Sicht verlieren.** Ein Break, nach dem du nicht weißt, wo er ist, ist nur halb geflogen.

::: info IM SPIEL PRÜFEN
- Ob das Schubniveau die Erfassung durch die Rakete messbar beeinflusst (die Community empfiehlt Idle).
- Wie lange du 9 G halten kannst, bevor Greyout einsetzt ([G-Awareness](/grundlagen/golden-rules#g-awareness-greyout-und-blackout)).
:::

::: tip MERKE
- Lift Vector auf den Angreifer, max ziehen (T-18: α ~26°), Sicht halten.
- Max Instant Rate nahe Corner Speed: T-15 ~360–385, T-16 ~409–421, T-18 ~385–409 KIAS (10.000 ft).
- Break so lange wie nötig, dann sustained Defensivkurve zurück ins Band ~360–440 KIAS.
- Der Break verweigert den Schuss, er dreht den Kampf nicht um. Dafür brauchst du seinen Fehler.
- Gegen IR-Raketen: Break + Flares in kurzen Gruppen + Idle. Kein Chaff, kein Nachbrenner.
:::

Weiter: [Guns Defense](/grundlagen/defensiv/guns-defense)
