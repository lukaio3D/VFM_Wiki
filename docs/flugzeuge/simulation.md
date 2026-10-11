# Simulation: Stärken, Schwächen, beste Strategien

> Rund 800.000 simulierte Ranked-Kämpfe zwischen Bots, die nur nach der Physik der Jets fliegen. Sie zeigen, **was das Flugmodell begünstigt**, nicht wie gut ein Mensch es umsetzt.

## Was simuliert wurde

- **Flugmodell:** Schub, Widerstand und Auftrieb jedes Jets, gefittet an die Ingame-Diagramme und alle Messflüge (Beschleunigung, Ausrollen, voller Zug). Erster Turn aus 450 KIAS ±3 %, Beschleunigung ±2 %, Energieverlust im vollen Zug ±2 % (Details: `tools/kampfsim/README.md`).
- **Start wie im Ranked:** beide 450 KIAS auf 10.000 ft, Head-on, Merge nach ~5 s (~8.500 ft Abstand), voller Tank, nur Guns. Seitlicher Versatz 500 ft oder 2.000 ft.
- **Strategie** = was der Pilot vor dem Merge festlegt:
  - Drehrichtung am Pass: **hin** (beide hin → Two-Circle), **weg** (→ One-Circle) oder **durch** (Extend).
  - Ebene: steil hoch, hoch, flach oder tief (nose-low).
  - Speed, in der er kämpft: 280, 360, 440 oder 520 KIAS.
  - Pure oder Lag, Merge mit oder ohne Nachbrenner, bei der T-18 α 26° oder 35° beim Kurven.

  Das sind 192 Strategien je Jet (T-18: 384), jede gegen jede.
- **Feste Regeln** für alle Bots: Gun mit Vorhalt, sobald er vor der Nase ist (die T-18 immer bis α 35°), Break Turn, wenn er hinten die Nase auf mir hat, jeder neue Pass beginnt wieder mit dem eigenen ersten Turn, Hard Deck ~3.000 ft. Abschuss nach 0,5 s Treffern; offen nach 150 s.
- **Bewertung:** +1 Abschuss, −1 abgeschossen. Der **Spielwert** ist das Ergebnis, wenn beide Seiten optimal wählen (Nash-Gleichgewicht): 0 heißt ausgeglichen, +0,3 heißt deutlicher Vorteil.

## Ergebnis in einem Satz je Jet

| Jet | Stärke laut Simulation | Schwäche laut Simulation |
|---|---|---|
| **T-15** | Stärkster Jet insgesamt. Gewinnt gegen die T-18 klar, gegen die T-16 knapp. Fast jede vernünftige Strategie funktioniert. | Vertikal und „schnell bleiben“ (520 KIAS) verlieren gegen beide Gegner. |
| **T-16** | Two-Circle bei ~440 KIAS, flach oder nose-low. Schlägt damit die T-18 und hält die T-15 fast ausgeglichen. | Vertikal (−0,3 bis −0,6) und langsamer One-Circle gegen die T-15. |
| **T-18** | Nose-low, 360–440 KIAS, α diszipliniert. Ihre 35° beim Schuss sind gegen die T-15 ~0,1 Spielwert wert. | Unterlegen gegen beide. Hoher Widerstand, gegen die T-15 auch langsam kein Vorteil. |

## Die Paarungen

| Paarung | Spielwert | Spanne in den Robustheitstests |
|---|---|---|
| T-15 gegen T-16 | **+0,08** (fast ausgeglichen) | −0,03 bis +0,10; mit 50 % Fuel +0,32 |
| T-15 gegen T-18 | **+0,29** (T-15 klar vorn) | +0,23 bis +0,50 |
| T-16 gegen T-18 | **+0,17** (T-16 vorn) | +0,13 bis +0,40; mit 50 % Fuel ±0 |
| Spiegelkämpfe | ±0,02 | Kontrolle: muss 0 sein |

Robustheitstests: Rollrate 120 bzw. 270 °/s statt 180, Abschuss erst nach 1 s Treffern, Gun-Reichweite 2.000 statt 3.000 ft, T-16 mit 5 % mehr Schub (so dreht sie im Messflug), 50 % Fuel, T-18 ohne 35° beim Schuss.

### T-15 gegen T-16

| Strategie | T-15 | T-16 |
|---|---|---|
| Two-Circle ~440, nose-low | **+0,03** | −0,09 |
| Two-Circle ~440, flach | −0,03 | **−0,08**, ihre beste |
| Langsamer One-Circle (280) | ±0 | **−0,27** |
| Vertikal (steil hoch) | **−0,25** | **−0,56** |
| Blow-Through, hoch und schnell | −0,27 | – |

Werte gegen die optimale Mischung des Gegners.

- **Wer hochzieht, verliert.** Das gilt für beide Jets und bestätigt die Matchup-Seite: Die T-15 soll gegen die T-16 nicht vertikal gehen, die T-16 erst recht nicht.
- **Die T-16 meidet den One-Circle.** Langsam ist sie der T-15 klar unterlegen.
- **Den Two-Circle verliert die T-15 in der Simulation nicht.** Nose-low ist er für sie sogar leicht positiv. Das ist anders als bisher im Wiki: Ihr Nachteil dort ist klein, und über mehrere Kreise holt ihn die T-16 nicht sicher heraus.
- **Fuel zählt.** Mit halbem Tank wird die T-15 klar besser (+0,32), weil sie relativ mehr Gewicht verliert.

### T-15 gegen T-18

| Strategie | T-15 | T-18 |
|---|---|---|
| Two-Circle ~440, flach oder tief | **+0,25 bis +0,29** | −0,38 (tief) |
| Langsamer One-Circle (280), tief | +0,27 | **−0,44** |
| Blow-Through, tief, dann langsam | +0,22 | – |
| Two-Circle ~360, tief | – | **−0,30**, ihre beste Familie |
| Vertikal | −0,08 | −0,48 |

- **Die T-15 gewinnt fast egal wie**, solange sie nicht vertikal oder auf Speed fliegt.
- **Der langsame One-Circle von unten ist gegen die T-15 die schlechteste T-18-Option.** Bei gleicher niedriger Speed zieht die T-15 mehr G (gemessen: 6,8 gegen 5,7 G bei ~355 KIAS).
- **Die 35°-Nase hilft der T-18 (+0,1), gleicht aber nichts aus.** Ohne sie stünde es +0,42 statt +0,31.

### T-16 gegen T-18

| Strategie | T-16 | T-18 |
|---|---|---|
| Two-Circle ~440, flach oder tief | **+0,17**, ihre beste | −0,21 (tief) |
| Two-Circle ~440, hoch | +0,15 | – |
| One-Circle (280) | −0,02 | −0,19 |
| Vertikal | −0,16 | −0,36 |

- **T-16:** Two-Circle bei ~440 KIAS, flach oder nose-low. Genau der Plan der Matchup-Seite.
- **T-18:** Alle Kreisformen liegen nah beieinander (−0,17 bis −0,27), keine dreht das Matchup. Mit halbem Tank ist es ausgeglichen.

## Was für alle Jets gilt

Gemittelt über alle Gegner-Strategien, in allen Paarungen gleich gerichtet:

1. **Nose-low schlägt flach, flach schlägt hoch, steil hoch ist am schlechtesten.** Im Nose-low-Turn helfen Schwerkraft und Auftrieb gemeinsam, und die Speed bleibt. Gilt nur, solange Höhe da ist: Start auf 10.000 ft, Hard Deck 3.000 ft.
2. **Langsamer kämpfen ist besser als schneller.** 520 KIAS halten ist in jeder Paarung die schlechteste Speed, weil der Bot dafür entlastet und keine Winkel macht. Bei der T-16 ist ~440 so gut wie 280.
3. **Extend am ersten Merge kostet** (−0,1 bis −0,35). Einzige Ausnahme: die T-15 gegen die T-18, dort trägt sie ihr Schub.
4. **Hin oder weg am Pass ist fast egal.** Beides ist deutlich besser als Durchfliegen.
5. **Pure oder Lag macht für Bots keinen Unterschied.** Lag ist ein Werkzeug gegen menschliche Fehler wie Overshoot und Ungeduld. Bots machen diese Fehler nicht.
6. **Nachbrenner bis zum Merge** taucht in vielen der besten Strategien auf, ist aber kein klarer Vorteil.

## Speed nach Fuel

Feineres Raster für T-16 und T-15 (360–500 KIAS in 20er-Schritten, gegen die stärksten Gegner-Strategien, bei 100, 50 und 15 % Fuel):

- **T-16:** am besten bei geflogenen **~420–450 KIAS**, mit wenig Fuel ~410–440. Über ~480 KIAS verliert sie gegen alle drei Jets deutlich. Ihr Sustained-Optimum auf 10.000 ft liegt bei ~460 KIAS; im Kampf lohnt der untere Rand des Plateaus. Details: [T-16, Speed nach Fuel und Höhe](/flugzeuge/t16#speed-nach-fuel-und-hohe).
- **T-15:** am besten bei geflogenen **~380–440 KIAS**, mit wenig Fuel ~360–400. Mit sinkendem Fuel wird sie gegen die T-16 deutlich stärker, weil sie relativ mehr Gewicht verliert.

## AoA-Override (Annahme)

Override ist nicht gemessen. Mit geschätzten Werten (maximales α T-15 ~50°, T-16 ~32°, T-18 ~80°; darüber Auftrieb und Widerstand wie eine flache Platte) schadet Override als Gewohnheit mehr, als er nützt. Gerechnet über 360 Kämpfe je Paarung: T-18 gegen T-15 −0,57 statt −0,41, gegen T-16 −0,30 statt −0,23. Ein gezielter Snapshot kann trotzdem den Kampf entscheiden, wie das Override-Szenario im [3D-Simulator](/VFM_Wiki/sim/){target="_self"} zeigt. Ein Messflug ([B2, M5](/grundlagen/uebungen#b2-eigenen-jet-vermessen)) würde die Annahmen ersetzen.

## Simulation und Praxis

Abgleich mit Erfahrungen aus dem Ranked (Top-10-Spieler, vor allem T-16):

| Erfahrung | Simulation | Erklärung |
|---|---|---|
| T-16 gewinnt mit Two-Circle in Lag (Top 10) | **bestätigt** (beste T-16-Strategie gegen T-16 und T-18) | – |
| T-15 verliert gegen abtauchende T-16, wenn sie hochzieht | **bestätigt** | – |
| T-15 verliert gegen T-18 in Lag bei ~450 KIAS | Simulation: T-15 klar vorn | Bei ~450 drehen beide gleich schnell; in Lag fliegt man den größeren Kreis. Ein Bot schaltet sofort auf den Schuss um, ein Mensch bleibt oft zu lange in Lag. |
| T-18 ist mit engen Kreisen nose-low stark | Simulation: T-18 schwächster Jet | Bots zielen perfekt und reagieren sofort. Die T-18 lebt von Snapshots gegen Menschen, die ihre Nase unterschätzen, und von Gegnern, die ihr in den langsamen Kreis folgen. |
| T-15 Energy Fight ist frustrierend | **bestätigt**: Vertikal und Speed verlieren | Die T-15 gewinnt mit Kraft im langsamen oder nose-low Kreis, nicht mit Energie-Taktik. Einschränkung: Bots planen nicht über mehrere Pässe, ein echter Energy Fight ist für sie zu schwer. |

## Grenzen

- **Bots sind keine Menschen.** Sie sehen alles, zielen perfekt, kennen keinen Stress und keine Täuschung, planen aber auch nicht voraus.
- **Nicht gemessen:** Rollrate, Kanone (Reichweite, Treffer bis Abschuss), Verhalten unter ~280 KIAS und über 20.000 ft. Die Robustheitstests zeigen, dass sich die Rangfolge der Jets dadurch nicht ändert.
- **Head-on-Schüsse** sind ab dem zweiten Pass erlaubt; ein Teil der Abschüsse fällt dort, wo einer schon mehr Winkel hat.
- **Nur der Ranked-Start auf 10.000 ft** mit vollem Tank. Höher (wo die T-16 schwächer wird) und mit wenig Fuel kann es anders aussehen.

::: details Beispielkämpfe (beste Strategien beider Seiten)
![T-15 gegen T-16](/images/sim/t15_vs_t16.png)
![T-15 gegen T-18](/images/sim/t15_vs_t18.png)
![T-16 gegen T-18: Two-Circle, die T-16 dreht mit ~7,7 G gegen ~7,1 G und bekommt am zweiten Pass die Nase zuerst herum](/images/sim/t16_vs_t18.png)
:::

::: tip MERKE
- Nose-low und eher langsam: In allen Paarungen der Grundsatz mit dem größten Effekt.
- Vertikal und „schnell bleiben“ verlieren in jeder Paarung.
- T-15 > T-16 ≈ knapp > T-18. Die T-18 braucht menschliche Fehler des Gegners.
- Die T-16 bleibt im Two-Circle bei ~440 KIAS und geht nie hoch.
:::

Selbst ansehen: [3D-Simulator](/VFM_Wiki/sim/){target="_self"} · Weiter: [Flugzeugvergleich](/flugzeuge/vergleich) · [Merge-Strategien für Ranked](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias)
