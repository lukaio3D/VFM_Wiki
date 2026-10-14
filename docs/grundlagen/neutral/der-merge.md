# Der Merge

> Wie du in den Vorbeiflug gehst und was du in den ersten Sekunden danach tust, entscheidet, wer den Kampf offensiv beginnt.

Die meisten Kämpfe beginnen neutral: Ihr fliegt aufeinander zu, passiert euch (**Merge**) und dreht. Wer danach als Erster die Nase auf den Gegner bekommt, hat ihn. Dafür brauchst du die richtige Speed, das richtige Timing und eine bewusste Wahl, welchen Kampf du willst. Begriffe: [Glossar](/grundlagen/begriffe), Geometrie: [Relative Geometrie](/grundlagen/geometrie).

## Der Ranked-Start

So beginnt jede Runde in allen 71 eigenen 1v1-Replays, Ranked wie Casual (*Replays*, Auswertung mit `tools/replays`):

| | Wert |
|---|---|
| Höhe, Speed | **10.000 ft, Mach 0,75 = im HUD ~427 KIAS** |
| Lage | Head-on, **13.100 ft (4.000 m)** Abstand, **~1.300 ft (400 m)** seitlicher Versatz |
| Merge | nach **~8 s** |
| Tank | voll (die Lobby hat keine Fuel-Option) |
| Waffen | nur Kanone; **kein Schuss vor dem ersten Pass** (Merge Safety) |
| Runde | bis 8 Minuten; Abschuss im Median nach ~2,5 min (146 s), 90 % vor 5 min |

Ältere Wiki-Stände nannten ~450 KIAS, ~8.500 ft und ~5 s bis zum Merge. Das war geschätzt und ist überholt.

## Mit welcher Speed in den Merge

„Schnell rein, Mach 0,8 oder mehr“ ist für einen Kurvenkampf falsch: Der Wenderadius wächst mit dem Quadrat der Speed ([Kurvenphysik](/grundlagen/kurvenphysik)). Bei 9 G auf 10.000 ft sind es mit 450 KIAS rund 2.500 ft, mit 600 KIAS rund 4.400 ft.

Aus den Diagrammen ergibt sich das Band zwischen **Corner Speed** (maximale Instant Rate) und **Best-Sustained-Speed** (höchste Rate ohne Energieverlust). Die Simulation zeigt, bei welcher Speed man **den ganzen Kampf** am besten fliegt:

| Jet (10.000 ft) | Corner Speed | Best Sustained | Kampf-Speed laut *Simulation* |
|---|---|---|---|
| [T-15 Excalibur](/flugzeuge/t15) | ~360–385 KIAS | ~495 KIAS | **~380–420 KIAS** (geflogen ~370–430), nicht über ~440 |
| [T-16 Falchion](/flugzeuge/t16) | ~409–421 KIAS | ~470 KIAS | **~400–420 KIAS** (geflogen ~400–440), nicht über ~440 |
| [T-18 Cutlass](/flugzeuge/t18) | ~385–409 KIAS | ~470 KIAS | **~440 KIAS**, nicht über ~480 |

Corner Speed: 50–100 % Fuel aus den Diagrammen; tiefer liegen alle Werte etwas niedriger (T-15 Corner auf Meereshöhe ~337 KIAS). Daten: [Flugzeugvergleich](/flugzeuge/vergleich), Übung: [Corner Speed finden](/grundlagen/uebungen).

**Im Ranked kommst du mit ~427 KIAS schon im richtigen Band an.** Mit Nachbrenner bis zum Merge wären es ~605 (T-15), ~550 (T-16) bzw. ~535 KIAS (T-18) (*Modell*); einen klaren Vorteil bringt das in der Simulation nicht. Zu langsam (~280 KIAS) und zu schnell (~520 KIAS) verlieren dort für jeden Jet ([Simulation](/flugzeuge/simulation#was-fur-alle-jets-gilt)).

## Der Lead Turn

Beim **Lead Turn** beginnst du deine Kurve, **bevor** ihr auf gleicher Höhe seid. Du nutzt den seitlichen Versatz (Turning Room), um die Nase schon vor dem Pass herumzubringen, und hast nach dem Merge Winkel, die er erst aufholen muss.

Eine feste Sekundenregel gibt es nicht. Beginne, wenn die **Sichtlinienrate** deutlich zunimmt, der Gegner also plötzlich schnell über die Haube wandert. Dann ist der Versatz grob ein Wenderadius (auf 10.000 ft etwa 2.000–3.000 ft). Lift Vector auf ihn oder knapp hinter ihn und ziehen.

| Timing | Folge |
|---|---|
| **zu früh** | Du schießt über seine Flugbahn hinaus (Flight-Path-Overshoot), er dreht hinter dir ein. |
| **zu spät** | Er beginnt zuerst und gewinnt die Winkel. |
| **richtig** | Du kommst mit der Nase vor ihm herum und bist nach dem Pass vorn. |

**Im Ranked** liegt der Versatz bei nur ~1.300 ft, also etwa einem halben Wenderadius, und beide haben denselben. Ein großer Lead Turn ist daraus nicht drin, und mehr Versatz aufzubauen kostet Zeit, die er nutzt, um ihn wieder wegzunehmen. Wichtiger ist, den ersten Turn richtig zu fliegen (nächster Abschnitt).

## Der erste Turn aus 450 KIAS (gemessen)

Wie viel Winkel bringt der erste Turn nach dem Pass, und was kostet er? Dazu gibt es eine Messung und eine Modellrechnung. Ergebnis vorweg: **Voll ziehen gewinnt ein paar Grad und kostet viel Speed.** Der Kampf wird danach im Band entschieden.

### Gemessen (ab 450 KIAS)

Messflüge auf 10.000 ft, voller Tank, HUD-Werte, gezählt ab einer Drehrate über 10 °/s. Sie starten bei 450 KIAS, also etwas schneller als der Ranked-Start (~427):

| | nach 4 s | nach 8 s | Speed nach 8 s |
|---|---|---|---|
| **T-15** voller Zug | **77°** | **146°** | ~286 KIAS |
| **T-16** voller Zug | 70° | 141° | ~365 KIAS |
| T-18 voller Zug (überzogen, α bis 35°) | 70° | 127° | ~281 KIAS |
| **T-18 mit α ~26°** (geschätzt) | ~73° | **≥ ~138°** | > 281 KIAS |
| T-15 Sustained (~7 G, 15,4 °/s) | 62° | 123° | ~450 KIAS |
| **T-16 Sustained** (~7,9 G, 17,6 °/s) | 70° | **141°** | **~450 KIAS** |
| T-18 Sustained (~7 G, 15,6 °/s) | 62° | 125° | ~450 KIAS |

Bei T-15 und T-16 stoppt der AoA-Limiter am Optimum, Knüppel voll ist dort die beste Kurve. Bei der T-18 lässt er bis 35° zu, ihr voller Zug ist **überzogen**. Einschränkung: ein Messflug je Jet, jeweils mit leichtem Sinkflug (~600–900 ft); die T-18-Zeile mit α ~26° ist aus den Messdaten geschätzt.

### Modell (echter Ranked-Start)

Dieselbe Frage im Originalmodell, aus dem echten Ranked-Start, gezählt **8 s ab Beginn des Zugs** (also inklusive der 2–3 s, bis die G anliegen):

| Jet | voller Zug | Sustained |
|---|---|---|
| **T-15** | **131°**, ~276 KIAS | 111°, ~451 KIAS |
| **T-16** | 126°, ~368 KIAS | 114°, **~449 KIAS** |
| **T-18** | α ~26°: **123°**, ~330 KIAS · α 35°: 108°, ~282 KIAS | – |

Die Winkel liegen niedriger als gemessen, weil das Modell ab Zugbeginn zählt und bei ~427 statt 450 KIAS startet. Beide Quellen stimmen in der Richtung überein: Die T-15 gewinnt den ersten Turn mit vollem Zug und ist danach langsam; die T-18 dreht mit α ~26° klar besser als mit 35°. Ein Unterschied: Gemessen bringt der volle Zug der T-16 nach 8 s keinen Winkel mehr, im Modell ~12°. Er kostet in beiden Fällen ~80–85 KIAS.

### Was daraus folgt

- **Der Instant-Vorteil aus den Diagrammen ist aus dem Ranked-Start klein.** Die G brauchen 2–3 s, T-16 und T-18 erreichen keine 9 G. Die Diagramm-Instant-Rate zählt erst nahe Corner Speed.
- **T-15:** gewinnt den ersten Turn (gemessen ~5° gegen die T-16, ~8° gegen eine sauber geflogene T-18; im Modell gegen eine sustained fliegende T-16 ~17°), landet voll gezogen aber bei ~280 KIAS. Das ist laut Simulation eine schwache Kampf-Speed. Voll ziehen nur, solange es dir einen Schuss bringt, dann zurück ins Band ~380–420 (nose-low hilft).
- **T-16:** dreht ihn **sustained** und bleibt bei ~440–450 KIAS. Der volle Zug bringt höchstens ~12° und kostet ~85 KIAS.
- **T-18:** fliegt ihn mit **α ~26°**. Voll durchgezogen verliert sie ihn (gemessen 127° gegen 141° der T-16; im Modell mit 35° nur 108° statt 123° mit 26°). Die vollen 35° sind für den Snapshot: Die Nase zeigt dann ~10° weiter in die Kurve als die Flugbahn.

**Im 3D-Simulator:** [Erster Turn aus dem Ranked-Start, mit Haltepunkt am Merge](/VFM_Wiki/sim/?szenario=erster-turn){target="_self"}.

## Merge-Strategien für Ranked (Start ~430 KIAS) {#merge-strategien-fur-ranked-start-450-kias}

Die Matrix folgt der [Simulation](/flugzeuge/simulation) (~405.000 Bot-Kämpfe, Originalmodell, echter Ranked-Start, Rollraten aus den Spieldaten). Zahlen in Klammern: Wert der Strategie gegen ein breites Feld des Gegners (+1 = immer gewonnen, −1 = immer verloren).

| Du fliegst | gegen T-15 | gegen T-16 | gegen T-18 |
|---|---|---|---|
| **T-15** | Spiegelkampf: Two-Circle nose-low bei ~380–420 KIAS. Wer unnötig voll zieht oder schnell bleibt (520 KIAS), verliert. Nicht steil hoch. | **Am Pass zu ihr hin, Two-Circle bei ~400–440, nose-low, flach oder leicht hoch** (+0,67 bis +0,77): Du ziehst bei gleicher Speed mehr G und fliegst den kleineren Kreis. Geht sie nose-low: **mitgehen, nicht steil hochziehen** (+0,58). Langsamer One-Circle (+0,29) ist schwächer, schnell bleiben (520) am schwächsten. | **Two-Circle bei ~400–440, flach, nose-low oder leicht hoch** (+0,62 bis +0,71). Fliegt sie durch und taucht ab: sofort zu ihr hin, nose-low. Nicht in Lag warten (siehe unten), nicht langsam (280: +0,11) und nicht schnell kämpfen. Achte auf ihren Snapshot. |
| **T-16** | Du bist unterlegen (−0,41). **Two-Circle bei ~440, flach** (+0,21) oder nose-low (+0,19); durchfliegen und tief mit ~440 wieder einsteigen geht auch (+0,20). Speed halten: bei ~360 schon im Minus (−0,19). Zieht sie hoch: **nose-low weiterkreisen**, nie hinterher. Steil hoch verliert (−0,47). | Spiegelkampf: erster Turn sustained, Two-Circle bei ~400–420 KIAS, flach oder nose-low. Mit sinkendem Fuel nicht schneller werden: bei 15 % Fuel schlägt 420 KIAS 470 deutlich. | Fast ausgeglichen (+0,03). **Two-Circle bei ~440, leicht hoch, flach oder nose-low** (+0,47 bis +0,55), oder durchfliegen und tief wieder einsteigen (+0,49). Erster Turn sustained. Dreht sie weg und taucht ab: in der [Bubble](/grundlagen/begriffe#bubble) bleiben (außerhalb ihres Kreises), nie langsam werden. Vorsicht vor ihrem Snapshot. |
| **T-18** | Schwerste Paarung (−0,20). Am besten **durchfliegen, abtauchen, mit ~440 wieder einsteigen** (+0,30) oder **flacher Two-Circle bei ~440** (+0,15). Langsamer One-Circle ist schwach (−0,35). 35° für den Snapshot: Sie sind hier ~0,2 Spielwert wert. | Fast ausgeglichen. **Durchfliegen, abtauchen, mit ~440 wieder einsteigen** (+0,35, deine beste Familie) oder **Two-Circle bei ~440**, leicht hoch (+0,30), flach oder nose-low (+0,16 bis +0,19). Erster Turn mit α ~26°. Nicht langsam machen: Der langsame One-Circle bringt −0,09. Snapshot mit vollem α. | Spiegelkampf: Two-Circle bei ~440 oder durchfliegen und tief wieder einsteigen. Wer α diszipliniert fliegt (~26° zum Kurven, 35° nur für den Schuss), behält die Energie. |

::: info SIMULATION
**~440 KIAS ist für alle drei Jets die beste Kampf-Speed.** Am Pass zum Gegner hin drehen (Two-Circle) schlägt Wegdrehen (One-Circle). Durchfliegen und mit ~440 KIAS wieder einsteigen ist in Ordnung; teuer wird es erst, wenn du dabei Speed verlierst. Nose-low, flach und leicht hoch (~25°) liegen nah beieinander, steil hoch ist am schlechtesten. Pure oder Lag ist für Bots fast egal, Nachbrenner bis zum Merge kein klarer Vorteil.

Gerechnet mit den Rollraten aus den Spieldaten. **Je schneller die Jets wirklich rollen, desto besser für die T-18:** Mit der früheren Annahme 180 °/s für alle stand T-16 gegen T-18 bei +0,28, jetzt bei +0,03; T-15 gegen T-18 bei +0,39, jetzt bei +0,20. Die T-15 bleibt in jeder Variante vorn. Die Rollrate im Flug ist nicht gemessen ([Pitch- und Rollrate](/grundlagen/physik#pitch-und-rollrate)).

Damit gelten die älteren Spielpläne „T-15: langsamen One-Circle erzwingen oder schnell (> 500) kämpfen“ und „T-18: Kampf langsam machen, One-Circle von unten“ nicht mehr. Sie kamen aus den Diagrammen, die nur zeigen, wer in welchem Band dauerhaft schneller dreht. Warum der ganze Kampf anders ausgeht: [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle#flow-wahl-in-vfm). Grenzen: Bots zielen perfekt, sehen alles und planen nicht voraus.
:::

::: details Warum die T-15 bei ~450 KIAS nicht in Lag hinter der T-18 warten sollte
Bei ~450 KIAS drehen beide dauerhaft gleich schnell (15,4 gegen 15,6 °/s, *gemessen*). In Lag fliegst du außen den größeren Kreis und fällst zurück, und sie bekommt mit α bis 35° die Nase weiter herum. In der Simulation gewinnt die T-15 den Two-Circle trotzdem klar, weil ein Bot sofort auf den Schuss umschaltet, sobald der Gegner vor der Nase ist. Menschen bleiben oft zu lange in Lag. Also: nose-low im Band bleiben und die Nase auf sie bringen, sobald der Schuss kommt.
:::

::: details Warum die T-15 gegen eine abtauchende T-16 nicht hochziehen sollte
Zieht die T-15 hoch und die T-16 nose-low herum, entsteht ein vertikaler Two-Circle. Die T-15 verliert im harten Zug Energie ~2,3-mal so schnell (*gemessen*). Die T-16 tauscht Höhe gegen Speed, bleibt bei ~450 KIAS und dreht dort ~2 °/s schneller. Nach einem Kreis ist sie unten, schnell und vorn, du oben und langsam. In der Simulation kostet steiles Hochziehen die T-15 einen Teil ihres Vorteils (+0,58 statt +0,76 nose-low); im 3D-Szenario bleibt der Kampf dann in 7 von 9 Varianten offen, nose-low gewinnt sie 6 von 9. Gegenmittel: Nase auch runter, auf ihrer Höhe bleiben und im Two-Circle bei ~380–420 KIAS weiterkreisen ([Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)).
:::

## Dem Gegner den Turning Room verweigern

Seitlicher Abstand beim Pass ist Turning Room für **beide**. Baut der Gegner Versatz für einen Lead Turn auf:

- Dreh die Nase leicht **auf ihn zu** und verkleinere den Versatz. Je enger der Pass, desto weniger Raum für seinen Lead Turn.
- Geh über oder unter ihm durch. Ein Höhenunterschied entwertet seine horizontale Vorbereitung.
- Mit Head-on Guns ist ein Pass auf seiner Nase auch seine Schussgelegenheit. Im Ranked gilt das erst ab dem zweiten Pass (Merge Safety, siehe unten).

## Der erste Zug nach dem Pass

Nach dem Pass entscheidest du sofort, **in welche Ebene** du drehst. Wohin dein Lift Vector zeigt, dorthin geht die Kurve.

| Zug | Lift Vector | Wirkung | in VFM (*Simulation*) |
|---|---|---|---|
| **Nose-low** | schräg nach unten | Schwerkraft hilft, Speed bleibt; kostet Höhe | **gut für alle Jets**, bei ~440 KIAS etwa gleichauf mit flach und leicht hoch |
| **Level** | waagerecht | volle Rate in der Ebene, berechenbar | gut, Rate-Duell ([Two-Circle](/grundlagen/neutral/one-two-circle)) |
| **Nose-high** | schräg nach oben | Speed wird zu Höhe, oben dreht es enger; du wirst langsam | leicht hoch (~25°) bei ~440 KIAS kein Nachteil; nur bei langsamem Rollen schlechter als flach |
| **[Slice](/grundlagen/defensiv/slice-turn)** | deutlich unter dem Horizont, nahe max G | höchste Rate ohne Speedverlust; kostet Höhe | schneller erster Turn, wenn Höhe da ist |
| **Pitch-back** | fast senkrecht hoch, oben auf ihn rollen | dreht über die Vertikale; braucht Einstiegsspeed | **klar am schlechtesten**, auch für die T-15 ([Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)) |

**Nose-low oder flach, leicht hoch geht auch – nur nicht steil hoch.** Mit den Rollraten aus den Spieldaten liegen tief, flach und leicht hoch bei ~440 KIAS in der Simulation nah beieinander; die alte Reihenfolge nose-low > flach > hoch zeigt sich deutlich nur, wenn die Jets langsam rollen. Steil hoch ist in allen Paarungen klar schlechter. Im Nose-low-Turn arbeiten Auftrieb und Schwerkraft zusammen, und die Speed bleibt im Band.

::: warning Höhe ist begrenzt
Slice und Nose-low tauschen Höhe gegen Speed. 3.000 ft bringen allein durch die Schwerkraft nur grob 60–80 kt. Wer schon tief ist, kann nicht beliebig slicen. Im Training gilt das [Hard Deck](/grundlagen/golden-rules#hard-deck-2-000-ft) von 2.000 ft. Auch die Simulation (Start 10.000 ft, Hard Deck ~3.000 ft) bestätigt nose-low nur, solange Höhe da ist.
:::

**Im 3D-Simulator:** [Nose-low gegen nose-high](/VFM_Wiki/sim/?szenario=nose-low){target="_self"}.

## Den Turn des Banditen lesen

Behalte den Gegner durch den Pass im Blick (Lose Sight, Lose Fight). In den ersten zwei Sekunden liest du ab:

1. **Drehrichtung:** Drehen beide zueinander oder beide weg, wird es **Two-Circle**. Dreht einer hin und einer weg, wird es **One-Circle** ([One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle)).
2. **Ebene:** Nose-high heißt, er speichert Energie in Höhe. Nose-low heißt, er will schnell bleiben oder schnell drehen.
3. **Planform:** Siehst du seine Oberseite, zeigt sein Lift Vector auf dich.
4. **Nasen-Rate:** Dreht er deutlich schneller als du, lass dich nicht auf ein Rate-Duell ein, das du nicht gewinnst.

Gefällt dir nicht, was du siehst: Ebene wechseln, beim nächsten Pass die Drehrichtung ändern oder aussteigen.

## Blow-Through und Extension

Nicht jeder Merge endet in einem Turn. Beim **Blow-Through** fliegst du ohne Turn durch und baust Abstand auf (**Extend**), um später unter besseren Bedingungen neu anzugreifen.

- **Wann:** Er hat den Lead Turn klar gewonnen, er bietet einen Flow an, den dein Jet verliert, oder du bist unter deinem Band.
- **Wie:** Unload (ca. 0–0,5 G), Nase am oder knapp unter dem Horizont, volle Leistung, geradeaus weg und nicht zu früh wieder eindrehen.
- **Grenze:** Extend funktioniert nur, solange seine Nase von dir weg zeigt, etwa weil er noch in seiner Kurve gebunden ist. Selbst die T-15 hat nach 5 s erst ~200 ft mehr Abstand. Im Ranked kostet Abstand außerdem Zeit, siehe [Separation](/grundlagen/defensiv/separation#vfm-separation-im-ranked-1v1-hat-einen-preis).

**Am ersten Merge** ist in der Simulation das Wegdrehen (One-Circle) die schlechteste Drehrichtung. Durchfliegen und mit ~440 KIAS nose-low wieder einsteigen ist in Ordnung, für die T-18 sogar ihre beste Familie (siehe Matrix). Teuer wird der Extend, wenn du dabei Speed verlierst oder zu lange geradeaus fliegst: Wer sofort dreht, bekommt die Winkel, der Abstand reicht nicht.

**Im 3D-Simulator:** [Extend gegen einen Gegner, der sofort dreht](/VFM_Wiki/sim/?szenario=extend-merge){target="_self"} (6 s geradeaus, während der Gegner sofort dreht).

## VFM: Lobby-Einstellungen und Ranked

| Einstellung | Bedeutung für den Merge |
|---|---|
| **Merge Safety** (seit v1.4.1 standardmäßig an) | In 7.314 Schüssen aus eigenen Ranked-Replays fiel keiner vor dem ersten Pass. Danach sind Schüsse auf der Nase möglich (14 % aller Schüsse bei fast frontalem Aspect, 160–180°). |
| **Head-on Guns** | erlaubt: Ein Pass auf der Nase ist eine Schussgelegenheit für beide. Verboten: Du kannst enger passen und ihm Turning Room nehmen. |
| **Startdistanz** | nah: Merge-Speed kommt aus dem Start. BVR: Zeit, Speed, Höhe und Versatz selbst einzustellen. |
| **Raketen** | aus: reiner Kanonenkampf, Extend ist sicherer. An: Fox 2 kann vor oder kurz nach dem Merge entscheiden. |

::: warning Ranked
Eine Runde dauert 8 Minuten. Läuft die Zeit ab, gewinnt der **Verfolger** (seit v1.2.2). Endloses neutrales Kreisen ist also kein Unentschieden: Wer in der letzten Minute hinten sitzt, gewinnt. In den eigenen Replays fiel die Entscheidung aber meist früh (Median 146 s, längste Runde 334 s). Ranked 1v1 ist Guns-only: 63 Abschüsse mit der Kanone, keiner mit Raketen, dazu 9 Abstürze (~12 % der Runden).
:::

::: info IM SPIEL PRÜFEN
- Ob **Merge Safety** auch Kollisionen beim ersten Pass unterdrückt und bis wann sie gilt.
- Was **Head-on Guns verboten** technisch heißt: Ist der Schuss gesperrt oder zählt der Treffer nur nicht? (Das Spiel meldet „Head-on gunshot blocked!“.)
:::

::: tip MERKE
- Im Ranked kommst du mit ~427 KIAS schon im richtigen Band an; Nachbrenner bis zum Merge bringt keinen klaren Vorteil.
- Am Pass **zu ihm hin** drehen (Two-Circle) bei ~440 KIAS, nose-low oder flach (leicht hoch geht auch). Nicht wegdrehen; durchfliegen und mit ~440 wieder einsteigen ist in Ordnung.
- Erster Turn: T-16 sustained, T-18 mit α ~26°, die T-15 gewinnt ihn mit vollem Zug, muss danach aber zurück ins Band.
- Nicht langsam machen (280) und nicht schnell bleiben (520); nicht steil hochziehen.
- Lies nach dem Pass Drehrichtung, Ebene und Planform des Gegners, dann entscheide.
:::

Weiter: [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle)
