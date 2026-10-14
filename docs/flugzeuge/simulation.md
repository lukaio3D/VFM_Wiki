# Simulation: Stärken, Schwächen, beste Strategien

> Rund 405.000 simulierte Ranked-Kämpfe zwischen Bots, die nur nach der Physik der Jets fliegen. Sie zeigen, **was das Flugmodell begünstigt**, nicht wie gut ein Mensch es umsetzt.

## Was simuliert wurde

- **Flugmodell:** die Originalkurven des Spiels. Auftrieb und Widerstand jedes Jets über den Anstellwinkel kommen aus seinen Flächen und Profilen, der Schub über Mach und Luftdichte aus den Triebwerksdaten. Nur die Umrechnungsfaktoren aus dem Spielcode sind an den Messflügen kalibriert. Ergebnis: Schub auf 2–4 % wie im Spiel, Ingame-Diagramme auf 0,2–1,0 °/s, Energieverlust im vollen Zug auf wenige Meter (Details: `tools/kampfsim/README.md`).
- **Rollrate:** jeder Jet mit seiner Vorgabe aus den Spieldaten (T-15 325 °/s, T-16 und T-18 420 °/s), über die Fahrt gedämpft; im Kampfband ~310 bzw. ~395 °/s. Ob die Jets das im Flug erreichen, ist **nicht gemessen** – und genau davon hängt ein Teil der Ergebnisse ab ([siehe unten](#die-rollrate-entscheidet-mit)).
- **Start wie im Ranked**, gemessen in 71 eigenen 1v1-Replays: beide auf 10.000 ft mit Mach 0,75 (im HUD ~427 KIAS), Head-on, 13.100 ft Abstand, ~1.300 ft seitlicher Versatz, Merge nach ~8 s. Voller Tank, nur Guns, kein Schuss vor dem ersten Pass (Merge Safety).
- **Strategie** = was der Pilot vor dem Merge festlegt:
  - Drehrichtung am Pass: **hin** (beide hin → Two-Circle), **weg** (→ One-Circle) oder **durch** (Extend).
  - Ebene: steil hoch, hoch, flach oder tief (nose-low).
  - Speed, in der er kämpft: 280, 360, 440 oder 520 KIAS.
  - Pure oder Lag, Merge mit oder ohne Nachbrenner, bei der T-18 α 26° oder 35° beim Kurven.

  Das sind 192 Strategien je Jet (T-18: 384), jede gegen jede.
- **Feste Regeln** für alle Bots: Gun mit Vorhalt, sobald er vor der Nase ist (die T-18 immer bis α 35°), Break Turn, wenn er hinten die Nase auf mir hat, jeder neue Pass beginnt wieder mit dem eigenen ersten Turn, unter ~3.000 ft ziehen die Bots hoch (eigene Regel, das Spiel hat kein Hard Deck). Abschuss nach 0,5 s Treffern. Eine Runde dauert wie im Ranked bis zu 8 Minuten.
- **Bewertung:** +1 Abschuss, −1 abgeschossen, 0 offen nach 8 Minuten (54–83 % der Kämpfe enden mit Abschuss). Der **Spielwert** ist das Ergebnis, wenn beide Seiten optimal wählen (Nash-Gleichgewicht): 0 heißt ausgeglichen, +0,3 heißt deutlicher Vorteil.

::: tip NEU (Oktober 2026)
Die Seite ist mit dem Originalmodell des Spiels, dem echten Ranked-Start und den Rollraten aus den Spieldaten neu gerechnet. Bisher galten ein angepasstes Modell, 450 KIAS, ~5 s bis zum Merge, ein Abbruch nach 150 s und 180 °/s Rollrate für alle. Stabil geblieben: die T-15 ist der stärkste Jet, **~440 KIAS ist für alle die beste Kampf-Speed**, Two-Circle schlägt One-Circle, steil hoch verliert. Neu: **Langsam kämpfen (280 KIAS) ist nicht mehr gut**, und **T-16 gegen T-18 ist fast ausgeglichen**, solange die Jets so schnell rollen, wie die Spieldaten vorgeben.
:::

## Ergebnis in einem Satz je Jet

| Jet | Stärke laut Simulation | Schwäche laut Simulation |
|---|---|---|
| **T-15** | Stärkster Jet, gewinnt gegen beide. Am besten im Two-Circle bei ~440 KIAS (tief, flach oder leicht hoch), wo sie mehr G zieht und den kleineren Kreis fliegt. | Langsamer One-Circle (280) halbiert ihren Vorteil, schnell und hoch durchfliegen (520) verliert ihn fast ganz. |
| **T-16** | Two-Circle bei ~440 KIAS, flach, nose-low oder leicht hoch. Gegen die T-18 knapp vorn, bei langsamerem Rollen klar. | Gegen die T-15 unterlegen (−0,41). Steil hoch (−0,5) und langsam (360 und darunter) verlieren deutlich. |
| **T-18** | Durchfliegen, abtauchen und mit ~440 KIAS zurückkommen, oder Two-Circle bei ~440. Ihre 35° sind gegen die T-15 ~0,2 Spielwert wert. Profitiert am meisten von schnellem Rollen. | Gegen die T-15 unterlegen (−0,20). Langsamer One-Circle verliert. |

## Die Paarungen

| Paarung | Spielwert | Spanne in den Robustheitstests |
|---|---|---|
| T-15 gegen T-16 | **+0,41** (T-15 klar vorn) | +0,20 bis +0,46; vorn in jeder Variante |
| T-15 gegen T-18 | **+0,20** (T-15 vorn) | +0,09 bis klar T-15; je langsamer die Jets rollen, desto deutlicher |
| T-16 gegen T-18 | **+0,03** (fast ausgeglichen) | +0,04 bis klar T-16; je langsamer die Jets rollen, desto deutlicher |
| Spiegelkämpfe | −0,02 bis 0,00 | Kontrolle: muss 0 sein |

Robustheitstests: Rollrate × 0,75 und × 0,5, alle Jets 180 °/s (alte Annahme), Abschuss erst nach 1 s Treffern, Gun-Reichweite 2.000 statt 3.000 ft, T-16 mit 5 % mehr Schub, 50 % Fuel, T-18 ohne 35° beim Schuss. Gerechnet mit den je 16 stärksten Strategien, daher streuen die Werte um etwa ±0,1 bis ±0,2.

### Die Rollrate entscheidet mit

| Paarung | Basis, volles Turnier | Basis, Teilrechnung | × 0,75 | alle 180 °/s | × 0,5 |
|---|---|---|---|---|---|
| T-15 gegen T-16 | +0,41 | +0,40 | +0,38 | +0,23 | +0,20 |
| T-15 gegen T-18 | +0,20 | +0,24 | +0,50 | +0,56 | klar T-15 |
| T-16 gegen T-18 | **+0,03** | +0,08 | +0,36 | +0,65 | klar T-16 |

**Je schneller die Jets wirklich rollen, desto besser für die T-18.** Schnelles Rollen hilft dem Verteidiger und dem, der mit der Nase den Schuss erzwingt; beides ist ihre Stärke. Die Spalten ab „Teilrechnung“ sind mit den je 16 stärksten Strategien gerechnet und liegen deshalb etwas anders als das volle Turnier. Das volle Turnier mit 180 °/s für alle (der bisherige Stand) ergab +0,27 / +0,39 / +0,28. Die × 0,75-Spalte entspricht der Lesart, dass die Dämpfungskurve der Spieldaten in Knoten statt m/s geht. Welche Spalte stimmt, zeigt nur ein Messflug: [Rollrate messen (M6)](/grundlagen/uebungen#b2-eigenen-jet-vermessen).

Mit schnellem Rollen enden außerdem weniger Kämpfe mit Abschuss (T-16 gegen T-18: 58 % statt 81 %): Verteidigen wird leichter.

In den Tabellen unten steht je Strategie der Wert **gegen ein breites Feld** (alle Strategien des Gegners, beste Variante der Familie). Er trennt die Strategien deutlicher als der Spielwert, bei dem viele gleich gut sind.

### T-15 gegen T-16

| Strategie | T-15 | T-16 |
|---|---|---|
| Two-Circle ~440, nose-low | **+0,76** | +0,19 |
| Two-Circle ~440, flach | +0,67 | **+0,21**, ihre beste |
| Two-Circle ~440, leicht hoch | **+0,77** | +0,19 |
| Two-Circle ~360, nose-low | +0,65 | −0,19 |
| Durchfliegen, nose-low, ~440 | +0,64 | +0,20 |
| Langsamer One-Circle (280), nose-low | +0,29 | −0,42 |
| Vertikal (steil hoch, 440) | +0,58 | **−0,47** |
| Durchfliegen, hoch und schnell (520) | +0,14 | −0,55 |

- **Die T-15 gewinnt den Two-Circle bei ~440 KIAS.** Die T-16 hat im Band 440–500 KIAS 1–2 °/s mehr Rate, die T-15 aber bei gleicher Speed mehr G und den kleineren Radius. Über eine Runde von bis zu 8 Minuten setzt sich das durch.
- **Die T-16 muss ihre Speed halten.** Bei ~360 ist sie schon im Nachteil, langsamer verliert sie klar.
- **Steil hoch kostet beide**, die T-16 viel mehr.

### T-15 gegen T-18

| Strategie | T-15 | T-18 |
|---|---|---|
| Two-Circle ~440, leicht hoch | **+0,71** | +0,09 |
| Two-Circle ~440, flach | +0,63 | +0,15 |
| Two-Circle ~440, nose-low | +0,62 | +0,08 |
| Durchfliegen, nose-low, ~440 | +0,64 | **+0,30**, ihre beste |
| Langsamer One-Circle (280), nose-low | +0,11 | −0,35 |
| Vertikal (steil hoch, 440) | +0,58 | −0,01 |

- **Die T-15 gewinnt mit fast allem bei ~440 KIAS.** Langsam (280) verschenkt ihren Vorteil fast ganz.
- **Die T-18 sollte durchfliegen und abtauchen**, wenn sie die Wahl hat, und mit Speed zurückkommen; im langsamen One-Circle verliert sie.
- **Die 35°-Nase ist ~0,2 Spielwert wert.** Ohne sie stünde es +0,39 statt +0,20.

### T-16 gegen T-18

| Strategie | T-16 | T-18 |
|---|---|---|
| Two-Circle ~440, leicht hoch | **+0,55** | +0,30 |
| Two-Circle ~440, flach | +0,52 | +0,19 |
| Two-Circle ~440, nose-low | +0,47 | +0,16 |
| Durchfliegen, nose-low, ~440 | +0,49 | **+0,35**, ihre beste |
| Two-Circle ~360, nose-low | +0,20 | +0,18 |
| Langsamer One-Circle (280) | −0,38 | −0,09 |
| Vertikal (steil hoch, 440) | +0,26 | +0,15 |

- **Knapp.** Beide gewinnen bei ~440 KIAS am meisten, und bei den Rollraten der Spieldaten hebt sich das fast auf. Mit langsamerem Rollen liegt die T-16 klar vorn.
- **Die T-16 bleibt in ihrem Band**; unter ~360 KIAS verliert sie gegen die T-18.
- **Die 35° der T-18** sind hier ~0,08 wert.

## Was für alle Jets gilt

Gemittelt über alle Gegner-Strategien:

1. **~440 KIAS ist die beste Kampf-Speed für jeden Jet.** 360 ist gut, 280 und 520 verlieren in jeder Paarung. Das Originalmodell kostet im harten Zug viel Energie: Wer langsam kämpft, kommt aus dem Loch nicht mehr heraus; wer schnell bleiben will, entlastet und macht keine Winkel.
2. **Two-Circle schlägt One-Circle.** Am Pass zum Gegner hin drehen ist in fast allen Paarungen die beste Drehrichtung, Wegdrehen die schlechteste. **Durchfliegen** und mit ~440 KIAS wieder einsteigen ist dagegen kein Nachteil mehr; für die T-18 ist es oft die beste Wahl.
3. **Steil hoch ist die schlechteste Ebene.** Zwischen nose-low, flach und leicht hoch ist der Unterschied bei ~440 KIAS klein. Nose-low ist klar besser nur, wenn die Jets langsamer rollen als die Spieldaten vorgeben.
4. **Pure oder Lag macht für Bots wenig Unterschied**, Lag ist leicht besser. Lag ist vor allem ein Werkzeug gegen menschliche Fehler wie Overshoot und Ungeduld.
5. **Nachbrenner bis zum Merge** taucht in vielen der besten Strategien auf, ist aber kein klarer Vorteil.

## Speed nach Fuel

Feineres Raster für T-16 und T-15 (360–500 KIAS in 20er-Schritten, gegen die stärksten Gegner-Strategien, bei 100, 50 und 15 % Fuel):

- **T-16:** am besten mit einer Ziel-Speed von **~400–420 KIAS** (geflogen ~400–440), mit wenig Fuel ebenso. Über ~440 KIAS fällt es gegen alle drei Jets ab. Ihr Sustained-Optimum auf 10.000 ft liegt bei ~460–470 KIAS; das Plateau ist flach, bei 420 gibt sie nur ~0,2–0,3 °/s her und fliegt einen ~9 % kleineren Kreis. Mittel über alle Gegner und Fuel-Stände: Ziel 420 → +0,20, 440 → −0,08, 470 → −0,25. Details: [T-16, Kampf-Speed](/flugzeuge/t16#kampf-speed-420-statt-470-kias).
- **T-15:** am besten mit einer Ziel-Speed von **~380–420 KIAS** (geflogen ~370–430). Über ~440 KIAS fällt es gegen T-15 und T-16 ab.

Wie sich die Paarungen mit sinkendem Fuel verschieben, ist aus diesen Rechnungen nicht sicher abzulesen: Das Speed-Raster optimiert nur eine Seite.

## AoA-Override (Annahme)

Das maximale α im Override ist nicht gemessen (angenommen: T-15 ~50°, T-16 ~32°, T-18 ~80°); Auftrieb und Widerstand dort kommen aus den Originalkurven. Als Gewohnheit schadet Override mehr, als er nützt. Gerechnet über 360 Kämpfe je Paarung gegen die stärksten Gegner: T-18 gegen T-15 −0,41 statt −0,24, gegen T-16 −0,38 statt −0,12. Im Override-Szenario des [3D-Simulators](/VFM_Wiki/sim/?szenario=t18-override){target="_self"} verliert die T-18 mit Override 7 von 9 Varianten, ohne gewinnt sie 5 von 9. Ein Messflug ([B2, M5](/grundlagen/uebungen#b2-eigenen-jet-vermessen)) würde die Annahme ersetzen.

## Simulation und Praxis

Abgleich mit Erfahrungen aus dem Ranked (Top-10-Spieler, vor allem T-16):

| Erfahrung | Simulation | Erklärung |
|---|---|---|
| T-16 gewinnt mit Two-Circle in Lag (Top 10) | **bestätigt** (beste T-16-Familie in jeder Paarung) | – |
| T-15 verliert gegen abtauchende T-16, wenn sie hochzieht | **teilweise**: Steil hoch kostet die T-15 einen Teil ihres Vorteils, sie bleibt aber vorn | Ein Bot schießt sofort, wenn die Lage kippt. Menschen verlieren oben zusätzlich durch Ungeduld. |
| T-15 verliert gegen T-18 in Lag bei ~450 KIAS | Simulation: T-15 vorn | Bei ~450 drehen beide gleich schnell; in Lag fliegt man den größeren Kreis. Ein Bot schaltet sofort auf den Schuss um, ein Mensch bleibt oft zu lange in Lag. |
| T-18 ist mit engen Kreisen nose-low stark | **teilweise**: gegen die T-16 fast ausgeglichen, gegen die T-15 unterlegen; der langsame Kreis selbst verliert | Bots zielen perfekt und reagieren sofort. Die T-18 lebt von Snapshots und von schnellem Rollen; gegen Menschen, die ihr in den langsamen Kreis folgen, ist sie stärker als gegen Bots. |
| T-15 Energy Fight ist frustrierend | **bestätigt**: Steil hoch und Speed verlieren | Die T-15 gewinnt mit Kraft im Two-Circle bei ~440, nicht mit Energie-Taktik. Einschränkung: Bots planen nicht über mehrere Pässe, ein echter Energy Fight ist für sie zu schwer. |

## Grenzen

- **Bots sind keine Menschen.** Sie sehen alles, zielen perfekt, kennen keinen Stress und keine Täuschung, planen aber auch nicht voraus.
- **Nicht gemessen:** Rollrate im Flug (siehe oben, entscheidet mit), Kanone (Reichweite, Treffer bis Abschuss), Verhalten unter ~280 KIAS und über 20.000 ft. Die Kraftformeln im Spielcode sind nicht gelesen, nur kalibriert.
- **Schüsse** sind wie im Spiel erst nach dem ersten Pass erlaubt, danach auch auf der Nase; ein Teil der Abschüsse fällt dort, wo einer schon mehr Winkel hat.
- **Steigen:** Bots, die hoch kämpfen, steigen in langen Kämpfen bis zur eigenen Decke (~22.000 ft). Darüber reichen die Daten nicht.
- **Nur der Ranked-Start** mit vollem Tank. Höher (wo die T-16 schwächer wird) und mit wenig Fuel kann es anders aussehen.

::: details Beispielkämpfe (je die beste Strategie gegen ein breites Feld)
Einzelne Kämpfe können anders ausgehen als der Durchschnitt.

![T-15 gegen T-16: Beide drehen bei ~440 KIAS im Two-Circle und steigen dabei bis ~20.000 ft; nach 8 Minuten ist der Kampf offen](/images/sim/t15_vs_t16.png)
![T-15 gegen T-18: Die T-18 fliegt mit Nachbrenner durch und taucht ab, die T-15 bleibt bei ~440 KIAS dran und schießt nach gut 2 Minuten](/images/sim/t15_vs_t18.png)
![T-16 gegen T-18: Die T-18 fliegt durch, kommt mit Speed zurück und trifft die T-16 nach 45 s](/images/sim/t16_vs_t18.png)
:::

::: tip MERKE
- **~440 KIAS** ist für alle die beste Kampf-Speed. Nicht langsam machen (280), nicht schnell bleiben (520).
- Two-Circle schlägt One-Circle. Steil hoch verliert in jeder Paarung; nose-low, flach oder leicht hoch liegen nah beieinander.
- T-15 vor T-16 und T-18. T-16 gegen T-18 ist fast ausgeglichen – wie sehr, hängt an der Rollrate, die noch niemand gemessen hat.
- Die T-16 hält ihr Band (Ziel ~400–420 KIAS) und geht nie steil hoch.
:::

Selbst ansehen: [3D-Simulator](/VFM_Wiki/sim/){target="_self"} · Weiter: [Flugzeugvergleich](/flugzeuge/vergleich) · [Merge-Strategien für Ranked](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias)
