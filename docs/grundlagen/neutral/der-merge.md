# Der Merge

> Wie du in den Vorbeiflug gehst und was du in den ersten Sekunden danach tust, entscheidet, wer den Kampf offensiv beginnt.

Die meisten Dogfights in VFM beginnen neutral: Ihr fliegt aufeinander zu, passiert euch und dreht. Diesen Moment des Vorbeiflugs nennt man **Merge** (Brevity „Merged“: Freund und Feind am selben Punkt). Begriffe wie Aspect Angle (AA) und Antenna Train Angle (ATA), mit denen du die Lage beschreibst, findest du unter [Relative Geometrie](/grundlagen/geometrie), alle Fachbegriffe im [Glossar](/grundlagen/begriffe).

Am Merge hat noch niemand einen Vorteil. Wer danach als Erster die Nase auf den Gegner bekommt, hat ihn. Dafür brauchst du drei Dinge: die richtige Speed, das richtige Timing für den ersten Turn und eine bewusste Entscheidung, welche Art Kampf du willst.

## Mit welcher Speed in den Merge

Der verbreitete Rat „schnell rein, Mach 0.8 oder mehr“ ist für einen Kurvenkampf falsch. Bei gleichem G wächst dein Wenderadius mit dem Quadrat der Geschwindigkeit (r = V² / (g·√(n²−1)), Herleitung unter [Kurvenphysik](/grundlagen/kurvenphysik)).

::: details Rechnung: Was zu viel Speed kostet
Auf 10.000 ft entsprechen 450 KIAS in VFM grob 500 kt wahrer Geschwindigkeit (TAS, ~12 % über KIAS), also etwa 850 ft/s. Bei 9 G:

r = 850² / (32,2 · √80) ≈ 722.500 / 288 ≈ **2.500 ft**

Mit 600 KIAS (≈ 670 kt TAS ≈ 1.130 ft/s) sind es ≈ 1.276.900 / 288 ≈ **4.400 ft**, also fast der doppelte Radius. Wer mit Corner Speed in den Merge kommt, dreht in deinen Kreis hinein, während du noch in deinem viel größeren Bogen hängst.
:::

Ziel ist ein Band zwischen deiner **Corner Speed** (die niedrigste Speed, bei der du max G ziehen kannst, also maximale Instant Rate) und deiner **Best-Sustained-Speed** (die Speed, bei der du die höchste Turn Rate halten kannst, ohne Energie zu verlieren). Darüber verschenkst du Radius, darunter hast du keine Reserve für den ersten Turn.

| Jet | Corner Speed (10.000 ft) | Best Sustained (10.000 ft) | Merge-Band (Richtwert) |
|---|---|---|---|
| [T-15 Excalibur](/flugzeuge/t15) | ~360–385 KIAS | ~495 KIAS | ~380–450 KIAS |
| [T-16 Falchion](/flugzeuge/t16) | ~409–421 KIAS | ~470 KIAS | ~430–470 KIAS, nie unter ~420 |
| [T-18 Cutlass](/flugzeuge/t18) | ~385–409 KIAS | ~470 KIAS | ~380–420 KIAS, nicht über ~480 |

Daten: Ingame „Aircraft Performance Analysis“, Stand Okt 2026. Die Merge-Bänder sind daraus abgeleitete Richtwerte, im Spiel testen. Details unter [Flugzeugvergleich](/flugzeuge/vergleich). Auf Meereshöhe liegen alle Werte etwas niedriger (z. B. T-15 Corner ~337 KIAS).

::: info IM SPIEL PRÜFEN
- Ob die abgeleiteten Merge-Bänder im echten Kampf passen. Übung dazu: [Corner Speed finden](/grundlagen/uebungen).
:::

## Der Lead Turn

Ein **Lead Turn** heißt: Du beginnst deine Kurve, **bevor** ihr auf gleicher Höhe seid. Du nutzt den seitlichen Abstand (Turning Room) zwischen euren Flugbahnen, um deine Nase schon vor dem Pass Richtung Gegner zu drehen. Nach dem Merge hast du dann Winkel gewonnen, die er erst aufholen muss.

### Das Timing

Es gibt keine feste Sekundenregel. Das Timing hängt vom **seitlichen Abstand** und deinem **eigenen Wenderadius** ab:

- Beobachte die **Sichtlinienrate (LOS-Rate)**: wie schnell der Gegner über deine Haube wandert. Weit draußen bewegt er sich kaum. Kurz vor dem Pass beschleunigt die Bewegung stark.
- Beginne den Lead Turn, wenn diese Bewegung **deutlich zunimmt**. Das ist grob dann der Fall, wenn der seitliche Versatz etwa **einem Wenderadius** entspricht (bei Merge-Speed auf 10.000 ft grob 2.000–3.000 ft, siehe Rechnung oben).
- Lift Vector auf den Gegner bzw. etwas hinter ihn und ziehen.

| Timing | Folge |
|---|---|
| **Zu früh** | Du drehst über seine Flugbahn hinweg (Flight-Path-Overshoot) oder verbrauchst den Turning Room, bevor er dir nützt. Er dreht hinter dir ein. |
| **Zu spät** | Er beginnt zuerst und gewinnt die Winkel. |
| **Richtig** | Du kommst mit der Nase vor ihm herum und bist nach dem Pass vorn im Kreis. |

::: tip VFM: Wer gewinnt den ersten Turn?
Den ersten Turn entscheidet die **Instant Rate**. Laut Daten hat die T-15 die beste Instant Rate und die niedrigste Corner Speed. Bei gleich gutem Timing gewinnt die T-15 den Lead Turn gegen beide anderen Jets. Als T-16 oder T-18 gegen eine T-15 solltest du deshalb nicht darauf setzen, ihn zu überdrehen. Verweigere ihm stattdessen den Turning Room (nächster Abschnitt) oder wähle einen Flow, der ihm nicht liegt ([One-/Two-Circle](/grundlagen/neutral/one-two-circle)).
:::

## Dem Gegner den Turning Room verweigern

Seitlicher Abstand beim Pass ist Turning Room für **beide**. Wenn du merkst, dass der Gegner einen Versatz aufbaut, um einen Lead Turn zu fliegen:

- Dreh deine Nase leicht **auf ihn zu** und verkleinere den Versatz. Je enger der Pass, desto weniger Raum hat er für einen Lead Turn.
- Nimm ihm die Ebene: Ein Pass mit Höhenunterschied, bei dem du über oder unter ihm durchgehst, macht seine horizontale Vorbereitung weniger wert.
- Kollisionsgefahr und Head-on-Schüsse beachten (siehe Lobby-Einstellungen unten). Mit eingeschalteten Raketen bzw. Head-on-Guns ist ein Pass direkt auf der Nase des Gegners auch eine Schussgelegenheit für ihn.

## Der erste Zug nach dem Pass

Nach dem Pass musst du sofort entscheiden, **in welche Ebene** du drehst. Das ist eine Lift-Vector-Entscheidung: Wohin dein Lift Vector zeigt, dorthin geht die Kurve.

| Zug | Lift Vector | Was er bringt | Was er kostet | Passt zu |
|---|---|---|---|---|
| **Level** | waagerecht auf den Gegner | einfach, berechenbar, volle Rate in der Ebene | keine Hilfe durch Schwerkraft, Energie geht nur über Speed verloren | Rate-Duell ([Two-Circle](/grundlagen/neutral/one-two-circle)) |
| **Nose-high** (schräg nach oben) | über dem Horizont | Speed wird zu Höhe statt zu verpuffen; oben dreht es sich enger | du wirst langsam; der Gegner kann unter dir abkürzen | Jets mit viel Schub (T-15) |
| **Nose-low** (schräg nach unten) | unter dem Horizont | Schwerkraft hilft bei Rate, Speed bleibt eher erhalten | du verlierst Höhe | Speed halten (T-16), tief kämpfen |
| **Slice** | deutlich unter dem Horizont, nahe max G | höchste Rate am Merge ohne Speedverlust | kostet Höhe und damit Gesamtenergie; siehe [Slice Turn](/grundlagen/defensiv/slice-turn) | schneller erster Turn, tief |
| **Pitch-back** | fast senkrecht nach oben, oben auf den Gegner rollen | dreht über die Vertikale um, nimmt die Höhe mit | braucht genug Speed beim Einstieg; oben bist du langsam | T-15, siehe [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf) |

::: warning Höhe ist begrenzt
Slice und Nose-low tauschen Höhe gegen Speed. 3.000 ft Höhe bringen allein durch die Schwerkraft nur etwa +77 kt (mit Schub mehr). Wer schon tief ist, kann nicht unendlich slicen. Im Training gilt ein [Hard Deck](/grundlagen/begriffe) von 2.000 ft über Grund.
:::

## Den Turn des Banditen lesen

Lose Sight, Lose Fight: Behalte den Gegner durch den Pass hindurch im Blick (Tally) und schau ihm über die Schulter nach. In den ersten zwei Sekunden nach dem Pass liest du ab:

1. **Drehrichtung**: Dreht er in dieselbe Richtung wie du (beide zueinander oder beide weg), wird es **Two-Circle**. Dreht einer hin und einer weg, wird es **One-Circle**. Was das heißt: [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle).
2. **Ebene**: Geht seine Nase hoch, runter oder bleibt sie am Horizont? Nose-high heißt, er spart Energie in Höhe. Nose-low heißt, er will schnell bleiben oder schnell drehen.
3. **Planform**: Siehst du seine Oberseite (Draufsicht auf die Tragflächen), zeigt sein Lift Vector auf dich. Er zieht in deine Richtung.
4. **Nasen-Rate**: Wie schnell wandert seine Nase? Dreht er deutlich schneller als du, verliere keine Zeit mit einem Rate-Duell, das du nicht gewinnst.

Je früher du das erkennst, desto früher kannst du gegensteuern: Ebene wechseln, beim nächsten Pass die Drehrichtung ändern oder aussteigen.

## Blow-Through und Extension

Nicht jeder Merge muss mit einem Turn enden. Beim **Blow-Through** fliegst du ohne Turn durch den Merge und baust Abstand auf (**Extend**), um später unter besseren Bedingungen wieder anzugreifen.

**Wann:**
- Der Gegner hat den Lead Turn klar gewonnen und du würdest im Turn sofort defensiv.
- Dein Jet verliert den Flow, den der Gegner gerade anbietet, und du kannst ihn nicht anders verweigern.
- Du bist zu langsam für dein Merge-Band und brauchst erst Energie.

**Wie:**
- Unload: Lift nahe null (ca. 0–0,5 G), Nase am oder leicht unter dem Horizont, volle Leistung.
- Geradeaus weg vom Gegner und nicht zu früh wieder eindrehen, denn du brauchst genug Abstand für einen neuen, neutralen Merge.
- Mit eingeschalteten Raketen ist das riskant: Du zeigst ihm dein Heck. In der Community wird außerdem berichtet, dass die IR-Rakete auch frontal trifft. Flares bereithalten, siehe [Gegenmaßnahmen](/avionik/gegenmassnahmen).

Ausführlich: [Separation](/grundlagen/defensiv/separation).

## VFM: Lobby-Einstellungen rund um den Merge

| Einstellung | Was du weißt | Bedeutung für den Merge |
|---|---|---|
| **Merge Safety** | seit v1.4.1 standardmäßig an | beeinflusst den ersten Merge, Details siehe unten |
| **Head-on Guns** | in Custom-Lobbys erlaubt/verboten | erlaubt: Ein Pass auf der Nase des Gegners ist eine Schussgelegenheit für beide. Verboten: Du kannst enger passen, um ihm Turning Room zu nehmen. |
| **Startdistanz** | nah oder BVR | nah: Ihr startet kurz vor dem Merge, die Merge-Speed kommt aus dem Start. BVR: Du hast Zeit, Speed und Höhe einzustellen und Versatz aufzubauen. |
| **Raketen** | an/aus, Anzahl einstellbar | aus (Guns-only): reiner Kanonenkampf, Extend ist sicherer. An: Fox 2 kann den Kampf schon vor oder kurz nach dem Merge entscheiden. |

::: info IM SPIEL PRÜFEN
- Was **Merge Safety** genau bewirkt (z. B. ob Schüsse oder Kollisionen beim ersten Pass unterdrückt werden und wie lange).
- Was **Head-on Guns verboten** technisch heißt: Ist der Schuss gesperrt oder zählt der Treffer nur nicht?
- Mit welcher Speed und Höhe die Startdistanz „nah“ beginnt und ob der seitliche Versatz fest ist.
:::

::: warning Ranked
Eine Runde dauert 8 Minuten. Läuft die Zeit im 1v1 ab, gewinnt der **Verfolger** (seit v1.2.2). Ein endloses neutrales Kreisen ist also kein Unentschieden. Wer in der letzten Minute hinten sitzt, gewinnt. Ranked 1v1 wird als Guns-only berichtet.
:::

::: tip MERKE
- Komm mit Corner- bis Best-Sustained-Speed in den Merge (Richtwerte bei 10.000 ft: T-15 ~380–450, T-16 ~430–470, T-18 ~380–420 KIAS), nicht mit Mach 0.8+.
- Starte den Lead Turn, wenn die Sichtlinienrate deutlich steigt, grob bei einem Wenderadius seitlichem Versatz.
- Verweigere dem Gegner Turning Room, vor allem gegen eine T-15, die den ersten Turn per Instant Rate gewinnt.
- Lies nach dem Pass Drehrichtung, Ebene und Planform des Gegners und entscheide dann bewusst.
- Ein Blow-Through ist keine Niederlage, wenn der Turn dich defensiv machen würde.
:::

Weiter: [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle)
