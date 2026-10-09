# Break Turn

> Die erste Antwort auf einen Angriff: maximal hart in den Gegner hineindrehen, dann in eine Defensivkurve übergehen, die Energie hält.

Der Break ist die härteste Kurve, die dein Jet in diesem Moment fliegen kann. Er hat ein einziges Ziel: dem Angreifer den Winkel zu nehmen, den er für Schuss und Position braucht. Er ist teuer. Deshalb fliegst du ihn so lange wie nötig und keine Sekunde länger.

## Wann

- Der Angreifer **kommt in deinen Kurvenkreis** oder ist kurz davor, in Schussposition zu kommen.
- Eine **Rakete ist in der Luft** (dann mit Flares und Idle, siehe [unten](#raketenabwehr-kurzfassung)).
- Ruf im Team: "Break left/right" heißt sofort maximaler Defensivturn in diese Richtung.

**Zu früh** ist ein Fehler: Wenn er noch weit weg ist, geht er einfach in Lag, schneidet in deinen Kreis, und du hast Energie verschenkt. **Zu spät** ist schlimmer: Dann hat er den Schuss. Brich ein, wenn er beginnt, Lead auf dich zu ziehen, oder kurz bevor er in Reichweite ist.

## Ausführung

1. **Lift Vector auf den Angreifer.** Roll so, dass dein Kabinendach auf ihn zeigt. Damit drehst du direkt in ihn hinein, und seine AA (Aspect Angle) wächst so schnell wie möglich.
2. **Maximal ziehen.** Bis an das Limit, das gerade gilt: über Corner Speed das G-Limit (9 G), unter Corner Speed das AoA-Limit (Buffet spürbar). Das ist deine **maximale Instant Rate**.
3. **Kopf drehen, Sicht halten.** Du ziehst in ihn hinein, also siehst du ihn über das Kabinendach.
4. **Leicht nose-low, wenn Höhe da ist.** Lift Vector etwas unter den Horizont hilft der Rate und bremst den Speedverlust. Das ist der Übergang zum [Slice Turn](/grundlagen/defensiv/slice-turn).

### Warum nahe Corner Speed

[Corner Speed](/grundlagen/begriffe) ist die niedrigste Geschwindigkeit, bei der du das volle G erreichst. Dort ist deine Instant Rate maximal (ω = g·√(n²−1)/V, siehe [Kurvenphysik](/grundlagen/kurvenphysik)):

- **Schneller als Corner:** Das G-Limit deckelt die Last, die Rate sinkt mit wachsendem V. Der Break bremst dich aber schnell herunter.
- **Langsamer als Corner:** Du schaffst das G nicht mehr, die Rate fällt mit jedem Knoten weniger weiter ab.

| Jet | Corner Speed (10.000 ft, Stand Dez 2025) | Max Instant Rate dort |
|---|---|---|
| T-15 Excalibur | ~360–385 KIAS | 23–24 °/s |
| T-16 Falchion | ~409–434 KIAS | 20–21 °/s |
| T-18 Cutlass | ~385–409 KIAS | 21–22 °/s |

Spanne jeweils 100 % bis 50 % Treibstoff. Daten vor Patch v1.1. Die T-15 hat seitdem 3 % Lift verloren (Instant Rate etwas niedriger). Details auf der [Vergleichsseite](/flugzeuge/vergleich).

## Danach: die sustained Defensivkurve

Bei Corner Speed und max G ist dein Ps (spezifische Überschussleistung, siehe [Energie-Management](/grundlagen/energie-management)) stark negativ: Du verlierst schnell Speed. Den Break kannst du nicht lange halten. Sobald er seinen Zweck erfüllt hat, gehst du über in die **sustained Defensivkurve**:

- **Wann umschalten:** Wenn der Angreifer nicht mehr in Schussposition kommen kann, weil seine AA hoch ist, er in Lag hängt oder nicht in deinen Kreis kommt.
- **Wie:** Last so weit zurücknehmen, dass deine Speed nicht weiter fällt. Ziel ist dein Best-Sustained-Bereich (VFM-Daten: ~470–495 KIAS je Jet), mindestens aber nicht weiter unter Corner Speed.
- **Weiter beobachten:** Zieht er wieder Lead und kommt rein: wieder hart. Fällt er in Lag zurück: Energie halten.
- **Kein Leerlauf:** Volle Leistung in der Defensivkurve, außer gegen eine IR-Rakete (siehe unten).

| Jet | Best Sustained (10.000 ft, Stand Dez 2025) | Sustained Rate dort |
|---|---|---|
| T-15 | ~495 KIAS | 15–17 °/s |
| T-16 | ~470 KIAS | 16–18 °/s |
| T-18 | ~470 KIAS | 15–16 °/s |

::: tip DAS EIGENTLICHE KÖNNEN
Den Break kann jeder ziehen. Den Moment zu erwischen, in dem du ihn wieder öffnest, ohne dass der Angreifer es ausnutzen kann, ist der Unterschied zwischen einem Verteidiger, der langsam ausblutet, und einem, der neutralisiert.
:::

## Raketenabwehr: Kurzfassung

Gegen eine IR-Rakete (Fox 2) gilt: **Idle + Flares + Break**, praktisch gleichzeitig. Die vollständige Beschreibung steht unter [Gegenmaßnahmen](/avionik/gegenmassnahmen), die Warnanzeigen unter [RWR & MWS](/avionik/rwr).

1. **Rakete erkennen:** MWS-Warnung, Rauchspur, Funkruf.
2. **Gas auf Idle.** Kein Nachbrenner, keine volle Leistung: Gegen einen Wärmesucher machst du dich damit nur heller.
3. **Flares in kurzen Gruppen**, nicht als Dauerstrom. Community-Tipp: so rollen, dass die Dispenser zur Rakete zeigen.
4. **Break**, praktisch gleichzeitig mit den Flares, damit die Rakete möglichst stark nachkurven muss. Ein gut getimter Break kann eine Rakete auch rein kinematisch schlagen: Wenn sie ihre Energie verbraucht hat, kann sie deine Kurve nicht mehr mitgehen.
5. **Nach dem Vorbeiflug der Rakete:** wieder volle Leistung, Sicht auf den Schützen, zurück in die Defensivkurve. Er kommt wahrscheinlich mit der Kanone hinterher.

::: danger KEIN CHAFF
VFM hat nur IR-Raketen. Chaff gibt es nicht und würde gegen einen Wärmesucher auch nichts bringen.
:::

::: info IM SPIEL PRÜFEN
- Ob dein Throttle einen Nachbrenner-Bereich hat und wie er angezeigt wird.
- Ob das Schubniveau die Erfassung durch die Rakete messbar beeinflusst (die Community empfiehlt Idle).
- Wie MWS und Rakete im Cockpit dargestellt werden (Richtung, Entfernung, Ton).
:::

## Typische Fehler

- **Weg vom Angreifer drehen.** Der Break geht in ihn hinein. Wegdrehen gibt ihm einen Schuss von hinten.
- **Den Break nie beenden.** Wer nach dem überstandenen Angriff weiter Max-G zieht, steht kurz darauf langsam und tief vor einem Angreifer, der Energie gespart hat.
- **Zu früh brechen.** Gegen einen Angreifer, der noch weit draußen ist, verbrennt das nur Energie.
- **Nachbrenner gegen eine IR-Rakete.** Gegen Wärmesucher: Idle.
- **Sicht verlieren.** Ein Break, nach dem du nicht weißt, wo er ist, ist nur halb geflogen.

::: info IM SPIEL PRÜFEN
- Wie VFM Greyout/Blackout modelliert (Reviews berichten davon). Wie lange du 9 G halten kannst, bevor dir die Sicht wegbricht.
:::

::: tip MERKE
- Lift Vector auf den Angreifer, max ziehen, Sicht halten.
- Max Instant Rate liegt nahe Corner Speed: T-15 ~360–385, T-16 ~409–434, T-18 ~385–409 KIAS (10.000 ft).
- Break so lange wie nötig, dann in die sustained Defensivkurve und Energie halten.
- Gegen IR-Raketen: Break + Flares in kurzen Gruppen + Idle. Kein Chaff, kein Nachbrenner.
:::

Weiter: [Guns Defense](/grundlagen/defensiv/guns-defense)
