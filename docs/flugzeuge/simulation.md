# Simulation: Stärken, Schwächen, beste Strategien

> Rund 405.000 simulierte Ranked-Kämpfe zwischen Bots, die nur nach der Physik der Jets fliegen. Sie zeigen, **was das Flugmodell begünstigt**, nicht wie gut ein Mensch es umsetzt.

## Was simuliert wurde

- **Flugmodell:** die Originalkurven des Spiels. Auftrieb und Widerstand jedes Jets über den Anstellwinkel kommen aus seinen Flächen und Profilen, der Schub über Mach und Luftdichte aus den Triebwerksdaten. Nur die Umrechnungsfaktoren aus dem Spielcode sind an den Messflügen kalibriert. Ergebnis: Schub auf 2–4 % wie im Spiel, Ingame-Diagramme auf 0,2–1,0 °/s, Energieverlust im vollen Zug auf wenige Meter (Details: `tools/kampfsim/README.md`).
- **Start wie im Ranked**, gemessen in 71 eigenen 1v1-Replays: beide auf 10.000 ft mit Mach 0,75 (im HUD ~427 KIAS), Head-on, 13.100 ft Abstand, ~1.300 ft seitlicher Versatz, Merge nach ~8 s. Voller Tank, nur Guns, kein Schuss vor dem ersten Pass (Merge Safety).
- **Strategie** = was der Pilot vor dem Merge festlegt:
  - Drehrichtung am Pass: **hin** (beide hin → Two-Circle), **weg** (→ One-Circle) oder **durch** (Extend).
  - Ebene: steil hoch, hoch, flach oder tief (nose-low).
  - Speed, in der er kämpft: 280, 360, 440 oder 520 KIAS.
  - Pure oder Lag, Merge mit oder ohne Nachbrenner, bei der T-18 α 26° oder 35° beim Kurven.

  Das sind 192 Strategien je Jet (T-18: 384), jede gegen jede.
- **Feste Regeln** für alle Bots: Gun mit Vorhalt, sobald er vor der Nase ist (die T-18 immer bis α 35°), Break Turn, wenn er hinten die Nase auf mir hat, jeder neue Pass beginnt wieder mit dem eigenen ersten Turn, unter ~3.000 ft ziehen die Bots hoch (eigene Regel, das Spiel hat kein Hard Deck). Abschuss nach 0,5 s Treffern. Eine Runde dauert wie im Ranked bis zu 8 Minuten.
- **Bewertung:** +1 Abschuss, −1 abgeschossen, 0 offen nach 8 Minuten (75–92 % der Kämpfe enden mit Abschuss). Der **Spielwert** ist das Ergebnis, wenn beide Seiten optimal wählen (Nash-Gleichgewicht): 0 heißt ausgeglichen, +0,3 heißt deutlicher Vorteil.

::: tip NEU (Oktober 2026)
Die Seite ist mit dem Originalmodell des Spiels und dem echten Ranked-Start neu gerechnet. Bisher galten ein angepasstes Modell, 450 KIAS, ~5 s bis zum Merge und ein Abbruch nach 150 s. Die Rangfolge der Jets und „nose-low schlägt hoch“ bleiben. Neu: Die T-15 liegt gegen beide deutlich vorn, und **langsam kämpfen (280 KIAS) ist nicht mehr gut**. Am besten ist für alle drei Jets der Two-Circle bei ~360–440 KIAS.
:::

## Ergebnis in einem Satz je Jet

| Jet | Stärke laut Simulation | Schwäche laut Simulation |
|---|---|---|
| **T-15** | Stärkster Jet. Gewinnt gegen beide klar. Am besten im Two-Circle nose-low bei ~360–440 KIAS, wo sie mehr G zieht. | Schnell durchfliegen und hochziehen (−0,3 gegen ein breites Feld der T-16); vertikal halbiert ihren Vorteil. |
| **T-16** | Two-Circle bei ~440 KIAS, flach oder nose-low. Schlägt damit die T-18 klar. | Gegen die T-15 unterlegen (−0,27). Vertikal (−0,5 bis −0,6) und langsamer One-Circle verlieren. |
| **T-18** | Two-Circle nose-low bei ~440 KIAS. Ihre 35° sind ~0,1 Spielwert wert. | Unterlegen gegen beide. Gegen die T-15 hat sie keine Strategie, die ein breites Feld schlägt. |

## Die Paarungen

| Paarung | Spielwert | Spanne in den Robustheitstests |
|---|---|---|
| T-15 gegen T-16 | **+0,27** (T-15 deutlich vorn) | 0,00 bis +0,33; mit 5 % mehr Schub für die T-16 ausgeglichen, mit 50 % Fuel +0,16 |
| T-15 gegen T-18 | **+0,39** (T-15 klar vorn) | 0,00 bis +0,71; empfindlich auf die Rollrate (270 °/s: ausgeglichen, 120 °/s: +0,71) |
| T-16 gegen T-18 | **+0,28** (T-16 vorn) | +0,19 bis +0,63 |
| Spiegelkämpfe | −0,05 bis −0,01 | Kontrolle: muss 0 sein |

Robustheitstests: Rollrate 120 bzw. 270 °/s statt 180, Abschuss erst nach 1 s Treffern, Gun-Reichweite 2.000 statt 3.000 ft, T-16 mit 5 % mehr Schub, 50 % Fuel, T-18 ohne 35° beim Schuss. Gerechnet mit den je 16 stärksten Strategien, daher streuen die Werte um etwa ±0,1 bis ±0,2.

In den Tabellen unten steht je Strategie der Wert **gegen ein breites Feld** (alle Strategien des Gegners, beste Variante der Familie). Er trennt die Strategien deutlicher als der Spielwert, bei dem viele gleich gut sind.

### T-15 gegen T-16

| Strategie | T-15 | T-16 |
|---|---|---|
| Two-Circle ~440, nose-low | **+0,88** | +0,48 |
| Two-Circle ~440, flach | +0,76 | **+0,54**, ihre beste |
| Two-Circle ~360, nose-low | +0,85 | +0,02 |
| Langsamer One-Circle (280), nose-low | +0,43 | −0,20 |
| Vertikal (steil hoch, 440) | +0,47 | **−0,49** |
| Durchfliegen, hoch und schnell (520) | −0,31 | −0,76 |

- **Die T-15 gewinnt den Two-Circle.** Die T-16 hat im Band 440–500 KIAS 1–2 °/s mehr Rate, die T-15 aber bei gleicher Speed mehr G und den kleineren Radius. Über eine Runde von bis zu 8 Minuten setzt sich das in der Simulation durch.
- **Die T-16 muss ihre Speed halten.** Bei ~360 ist sie gegen die T-15 nur noch ausgeglichen, langsamer verliert sie.
- **Hochziehen kostet beide**, die T-16 viel mehr.
- **Fuel:** Mit halbem Tank wird die T-16 relativ besser (+0,16 statt +0,33 in der Teilrechnung).

### T-15 gegen T-18

| Strategie | T-15 | T-18 |
|---|---|---|
| Two-Circle ~440, nose-low | **+0,86** | +0,04 |
| Two-Circle ~440, flach | +0,79 | +0,08 |
| Two-Circle ~360, nose-low | +0,86 | −0,17 |
| Durchfliegen, nose-low, dann ~360 | +0,70 | **+0,09**, ihre beste Familie |
| Langsamer One-Circle (280), nose-low | +0,49 | −0,19 |
| Vertikal (steil hoch, 440) | +0,53 | −0,20 |

- **Die T-15 gewinnt mit fast allem**, am klarsten im Two-Circle bei 360–440 KIAS.
- **Der langsame One-Circle ist für keine Seite gut.** Bei 280 KIAS verlieren beide zu viel Energie.
- **Die 35°-Nase hilft der T-18 (+0,1), gleicht aber nichts aus.** Ohne sie stünde es +0,49 statt +0,39.

### T-16 gegen T-18

| Strategie | T-16 | T-18 |
|---|---|---|
| Two-Circle ~440, flach | **+0,85** | +0,36 |
| Two-Circle ~440, nose-low | +0,83 | **+0,42**, ihre beste |
| Two-Circle ~360, nose-low | +0,71 | +0,33 |
| Langsamer One-Circle (280) | +0,21 | +0,05 |
| Vertikal (steil hoch, 440) | +0,20 | −0,14 |

- **T-16:** Two-Circle bei ~440 KIAS, flach oder nose-low. Genau der Plan der Matchup-Seite.
- **T-18:** Auch für sie ist der Two-Circle bei ~440 die beste Familie, nicht der langsame Kreis. Ihre 35° sind hier ~0,06 wert.

## Was für alle Jets gilt

Gemittelt über alle Gegner-Strategien, in allen Paarungen gleich gerichtet:

1. **Two-Circle bei ~360–440 KIAS ist die beste Familie für jeden Jet.** Am Pass zum Gegner hin drehen schlägt Wegdrehen (One-Circle) und Durchfliegen deutlich.
2. **Nose-low schlägt flach, flach schlägt hoch, steil hoch ist am schlechtesten.** Im Nose-low-Turn helfen Schwerkraft und Auftrieb gemeinsam, und die Speed bleibt. Gilt nur, solange Höhe da ist: Start auf 10.000 ft, Hard Deck 3.000 ft.
3. **Nicht langsam machen und nicht schnell bleiben.** 440 und 360 KIAS sind am besten, 280 klar schlechter, 520 am schlechtesten. Das Originalmodell kostet im harten Zug mehr Energie als das alte Modell; wer langsam kämpft, kommt aus dem Loch nicht mehr heraus.
4. **Extend am ersten Merge kostet** (in allen Paarungen die schlechteste Drehrichtung).
5. **Pure oder Lag macht für Bots wenig Unterschied**, Lag ist leicht besser. Lag ist vor allem ein Werkzeug gegen menschliche Fehler wie Overshoot und Ungeduld.
6. **Nachbrenner bis zum Merge** taucht in vielen der besten Strategien auf, ist aber kein klarer Vorteil.

## Speed nach Fuel

Feineres Raster für T-16 und T-15 (360–500 KIAS in 20er-Schritten, gegen die stärksten Gegner-Strategien, bei 100, 50 und 15 % Fuel):

- **T-16:** am besten mit einer Ziel-Speed von **~420 KIAS** (geflogen ~420–440), mit wenig Fuel ebenso. Über ~460 KIAS verliert sie gegen alle drei Jets deutlich. Ihr Sustained-Optimum auf 10.000 ft liegt bei ~460–470 KIAS; das Plateau ist flach, bei 420 gibt sie nur ~0,2–0,3 °/s her und fliegt einen ~9 % kleineren Kreis. Mittel über alle Gegner und Fuel-Stände: Ziel 420 → +0,25, 470 → −0,20. Details: [T-16, Speed nach Fuel und Höhe](/flugzeuge/t16#speed-nach-fuel-und-hohe).
- **T-15:** am besten mit einer Ziel-Speed von **~400–420 KIAS** (geflogen ~385–420), mit wenig Fuel ähnlich. Über ~460 KIAS verliert sie gegen T-15 und T-16 deutlich; gegen die T-18 gewinnt sie in jedem Band.

Wie sich die Paarungen mit sinkendem Fuel verschieben, ist aus diesen Rechnungen nicht sicher abzulesen: Das Speed-Raster optimiert nur eine Seite, und die Robustheitstests mit halbem Tank zeigen teils das Gegenteil.

## AoA-Override (Annahme)

Das maximale α im Override ist nicht gemessen (angenommen: T-15 ~50°, T-16 ~32°, T-18 ~80°); Auftrieb und Widerstand dort kommen aus den Originalkurven. Als Gewohnheit schadet Override mehr, als er nützt. Gerechnet über 360 Kämpfe je Paarung gegen die stärksten Gegner: T-18 gegen T-15 −0,76 statt −0,54, gegen T-16 −0,66 statt −0,39. Ein gezielter Snapshot kann trotzdem den Kampf entscheiden, wie das Override-Szenario im [3D-Simulator](/VFM_Wiki/sim/?szenario=t18-override){target="_self"} zeigt. Ein Messflug ([B2, M5](/grundlagen/uebungen#b2-eigenen-jet-vermessen)) würde die Annahme ersetzen.

## Simulation und Praxis

Abgleich mit Erfahrungen aus dem Ranked (Top-10-Spieler, vor allem T-16):

| Erfahrung | Simulation | Erklärung |
|---|---|---|
| T-16 gewinnt mit Two-Circle in Lag (Top 10) | **bestätigt** (beste T-16-Familie gegen T-16 und T-18) | – |
| T-15 verliert gegen abtauchende T-16, wenn sie hochzieht | **teilweise**: Hochziehen kostet die T-15 die Hälfte ihres Vorteils, sie bleibt aber knapp vorn | Ein Bot schießt sofort, wenn die Lage kippt. Menschen verlieren oben zusätzlich durch Ungeduld. |
| T-15 verliert gegen T-18 in Lag bei ~450 KIAS | Simulation: T-15 klar vorn | Bei ~450 drehen beide gleich schnell; in Lag fliegt man den größeren Kreis. Ein Bot schaltet sofort auf den Schuss um, ein Mensch bleibt oft zu lange in Lag. |
| T-18 ist mit engen Kreisen nose-low stark | Simulation: T-18 schwächster Jet | Bots zielen perfekt und reagieren sofort. Die T-18 lebt von Snapshots gegen Menschen, die ihre Nase unterschätzen, und von Gegnern, die ihr in den langsamen Kreis folgen. |
| T-15 Energy Fight ist frustrierend | **bestätigt**: Vertikal und Speed verlieren | Die T-15 gewinnt mit Kraft im Two-Circle nose-low, nicht mit Energie-Taktik. Einschränkung: Bots planen nicht über mehrere Pässe, ein echter Energy Fight ist für sie zu schwer. |

## Grenzen

- **Bots sind keine Menschen.** Sie sehen alles, zielen perfekt, kennen keinen Stress und keine Täuschung, planen aber auch nicht voraus.
- **Nicht gemessen:** Rollrate, Kanone (Reichweite, Treffer bis Abschuss), Verhalten unter ~280 KIAS und über 20.000 ft. Die Kraftformeln im Spielcode sind nicht gelesen, nur kalibriert.
- **Rollrate:** Die Bots rollen alle mit 180 °/s. Laut Spieldaten rollen T-16 und T-18 bis 420 °/s, die T-15 nur bis 325 °/s (Vorgabe, im Flug nicht gemessen). Die Rollrate ändert gegen die T-18 viel (siehe Robustheitstests); der Vorsprung der T-15 könnte kleiner sein.
- **Schüsse** sind wie im Spiel erst nach dem ersten Pass erlaubt, danach auch auf der Nase; ein Teil der Abschüsse fällt dort, wo einer schon mehr Winkel hat.
- **Nur der Ranked-Start** mit vollem Tank. Höher (wo die T-16 schwächer wird) und mit wenig Fuel kann es anders aussehen.

::: details Beispielkämpfe (je die beste Strategie gegen ein breites Feld)
Einzelne Kämpfe können anders ausgehen als der Durchschnitt.

![T-15 gegen T-16: Two-Circle bei ~440 KIAS über fast 5 Minuten; in diesem Kampf trifft die T-16 zuerst](/images/sim/t15_vs_t16.png)
![T-15 gegen T-18: Die T-18 fliegt durch und taucht ab, die T-15 dreht sofort nose-low herum und schießt nach 25 s](/images/sim/t15_vs_t18.png)
![T-16 gegen T-18: Two-Circle, die T-16 hält ~440 KIAS und mehr G und trifft nach 3 Minuten](/images/sim/t16_vs_t18.png)
:::

::: tip MERKE
- Two-Circle bei ~360–440 KIAS, nose-low oder flach: für alle drei Jets die beste Familie.
- Nicht langsam machen (280) und nicht schnell bleiben (520). Vertikal verliert in jeder Paarung.
- T-15 > T-16 > T-18, jeweils deutlich. Die T-18 braucht menschliche Fehler des Gegners.
- Die T-16 hält ihr Band (~400–440 KIAS) und geht nie hoch.
:::

Selbst ansehen: [3D-Simulator](/VFM_Wiki/sim/){target="_self"} · Weiter: [Flugzeugvergleich](/flugzeuge/vergleich) · [Merge-Strategien für Ranked](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias)
