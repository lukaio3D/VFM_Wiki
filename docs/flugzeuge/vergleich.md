# Performance-Daten & Vergleich

> Alle Leistungsdaten der drei Jets an einem Ort: Diagramme, Messflüge, Spieldaten und was sie für deinen Kampf bedeuten.

::: info DATENSTAND
- **Diagramme:** Ingame-Ansicht „Aircraft Performance Analysis“, aufgenommen im Oktober 2026 (v1.4.2) in neun Bedingungen (0 / 10.000 / 20.190 ft × 0 / 50 / 100 % Fuel). T-15 und T-18 zeigen exakt dieselben Werte wie im Dezember 2025, die T-16 ist durch v1.4.1 minimal besser ([Patch-Historie](#patch-historie)).
- **Messflüge:** Oktober 2026, 10.000 ft, voller Tank, nur Guns, Werte aus dem HUD-Video.
- **Spieldaten:** Oktober 2026, aus den Dateien der VFM-Installation gelesen (Massen, Schub über Mach, Auftrieb und Widerstand über α, Drehraten-Vorgaben, Kanone). Hier stehen nur Einzelwerte und qualitative Aussagen, keine Rohkurven.
- **Replays:** 71 eigene 1v1-Replays (Ranked und Casual), Oktober 2026: Startbedingungen, Schüsse, Abschüsse.
- **Simulation:** ~405.000 Bot-Kämpfe mit dem Originalmodell, dem echten Ranked-Start und den Rollraten aus den Spieldaten ([Simulation](/flugzeuge/simulation)).
- **Info-Karten:** Dezember 2025.

Kennzeichnung im ganzen Wiki: *Diagramm* (Ingame-Analyse), *gemessen* (Messflug), *Spieldaten*, *Replays*, *Simulation*, *Modell* (aus Diagrammen und Messungen gerechnet), *geschätzt*, *Hypothese*.
:::

## Die drei Jets in einem Satz

Es gibt kein Stein-Schere-Papier. Die **Diagramme** zeigen, wer in welchem Speedband dauerhaft schneller dreht; die **Simulation** zeigt, was im ganzen Kampf gewinnt. Beides steht unten getrennt ([Diagramm und Simulation](#diagramm-und-simulation)).

| Jet | Charakter | Spielplan (laut Simulation) |
|---|---|---|
| **[T-15 Excalibur](/flugzeuge/t15)** | Stärkster Jet: meiste G bei gleicher Speed, kleinster Radius, ~40 % mehr Beschleunigung, höchste Top-Speed. Rollt am langsamsten (*Spieldaten*). Bestraft unnötige Vollzüge. | Two-Circle bei ~380–420 KIAS, nose-low oder flach, mit G statt mit Rate gewinnen. Nicht steil hoch, nicht schnell bleiben. |
| **[T-16 Falchion](/flugzeuge/t16)** | Rate-Spezialist: leichtester Jet, beste Sustained Rate bei ~420–500 KIAS, verliert im Zug am wenigsten Energie | Two-Circle bei ~400–420 KIAS, flach oder nose-low. Nie steil hoch, nie langsam, nicht schneller als ~440. |
| **[T-18 Cutlass](/flugzeuge/t18)** | Nasenautorität (α bis 35°), höchster Widerstand, über ~510 KIAS schwach | Durchfliegen und nose-low mit ~440 KIAS wieder einsteigen oder Two-Circle bei ~440, α ~26° zum Kurven, 35° für den Snapshot. Den Kampf nicht langsam machen. |

Rangfolge in der Simulation: **T-15 vorn** (+0,41 gegen die T-16, +0,20 gegen die T-18), **T-16 gegen T-18 praktisch ausgeglichen** (+0,03). Je schneller die Jets wirklich rollen, desto besser für die T-18; die Rollrate ist nicht gemessen. Rollen sie langsamer als die Spieldaten vorgeben, schlägt die T-16 die T-18 klar (Details: [Simulation](/flugzeuge/simulation#die-paarungen)).

Die Duelle: [T-15 vs T-16](/flugzeuge/matchups/t15-vs-t16) · [T-15 vs T-18](/flugzeuge/matchups/t15-vs-t18) · [T-16 vs T-18](/flugzeuge/matchups/t16-vs-t18) · [Team-Taktik](/flugzeuge/team)

## Die Rohdaten

Alle Geschwindigkeiten in **KIAS**. Instant kostet Energie, Sustained nicht. Begriffe: [Begriffe](/grundlagen/begriffe), Physik: [Kurvenphysik](/grundlagen/kurvenphysik).

### Referenz: 10.000 ft, 50 % Treibstoff

| | T-15 Excalibur | T-16 Falchion | T-18 Cutlass |
|---|---|---|---|
| Gewicht | 37.615 lbs | 24.417 lbs | 36.597 lbs |
| Max Instant | **24 °/s** @ 360 KIAS | 21 °/s @ 409 KIAS | 22 °/s @ 385 KIAS |
| Max Sustained | 17 °/s @ 495 KIAS | **18 °/s** @ 470 KIAS | 16 °/s @ 470 KIAS |
| Min Radius | **1.644 ft** | 2.099 ft | 1.899 ft |
| Top-Speed (Sustained 0) | über Diagrammrand (> 885) | ~835 KIAS | ~720 KIAS |

![Performance-Analyse 10.000 ft, 50 % Treibstoff](/images/perf/10000ft_050.jpg)
*10.000 ft, 50 % Treibstoff. Orange = T-15, Blau = T-16, Magenta = T-18.*

### Alle neun Bedingungen

Je Zelle: Max Instant in °/s (bei KIAS) · Max Sustained in °/s (bei KIAS) · Min Radius in ft. Fett = bester Wert der Zeile.

**Meereshöhe (0 ft)**

| Fuel | T-15 Excalibur | T-16 Falchion | T-18 Cutlass |
|---|---|---|---|
| 0 % | **31** (310) · 22 (434) · **974** | 27 (365) · **24** (406) · 1.304 | 28 (337) · 23 (420) · 1.155 |
| 50 % | **29** (337) · 20 (475) · **1.138** | 26 (378) · **22** (447) · 1.428 | 27 (365) · 20 (447) · 1.313 |
| 100 % | **27** (351) · 18 (516) · **1.255** | 24 (406) · **20** (475) · 1.621 | 25 (378) · 18 (447) · 1.465 |

**10.000 ft**

| Fuel | T-15 Excalibur | T-16 Falchion | T-18 Cutlass |
|---|---|---|---|
| 0 % | **26** (336) · 19 (458) · **1.433** | 22 (385) · **20** (446) · 1.894 | 24 (360) · 19 (458) · 1.667 |
| 50 % | **24** (360) · 17 (495) · **1.644** | 21 (409) · **18** (470) · 2.099 | 22 (385) · 16 (470) · 1.899 |
| 100 % | **23** (385) · 15 (495) · **1.851** | 20 (421) · **16** (470) · 2.275 | 21 (409) · 15 (470) · 2.123 |

**20.190 ft**

| Fuel | T-15 Excalibur | T-16 Falchion | T-18 Cutlass |
|---|---|---|---|
| 0 % | **21** (359) · **15** (412) · **2.107** | 18 (412) · **15** (423) · 2.807 | 19 (380) · **15** (423) · 2.427 |
| 49 % | **20** (380) · 13 (412) · **2.387** | 18 (434) · **14** (423) · 3.073 | 18 (412) · 13 (423) · 2.816 |
| 100 % | **19** (402) · **12** (412) · **2.681** | 17 (445) · **12** (423) · 3.261 | 17 (434) · 11 (423) · 3.131 |

**Gewichte (0 / 50 / 100 % Fuel):** T-15 33.069 / 37.615 / 42.160 lbs, T-16 22.046 / 24.417 / 26.787 lbs, T-18 31.967 / 36.597 / 41.226 lbs. Die Spieldaten bestätigen sie (leer 15,0 / 10,0 / 14,5 t, voll 19,15 / 12,14 / 18,70 t). Auf 20.190 ft stand der Regler bei 49 %.

::: details Die neun Diagramme
Orange = T-15, Blau = T-16, Magenta = T-18. Auffällig: Auf 0 ft, 50 % ist der Sustained-Vorsprung der T-16 am größten (22 vs 20 °/s); auf 20.190 ft hält die T-15 bis ~600 KIAS ein flaches Plateau bei ~12 °/s.

![Performance-Analyse 0 ft, 0 %](/images/perf/00000ft_000.jpg)
*0 ft, 0 %*

![Performance-Analyse 0 ft, 50 %](/images/perf/00000ft_050.jpg)
*0 ft, 50 %*

![Performance-Analyse 0 ft, 100 %](/images/perf/00000ft_100.jpg)
*0 ft, 100 %*

![Performance-Analyse 10.000 ft, 0 %](/images/perf/10000ft_000.jpg)
*10.000 ft, 0 %*

![Performance-Analyse 10.000 ft, 50 %](/images/perf/10000ft_050.jpg)
*10.000 ft, 50 %*

![Performance-Analyse 10.000 ft, 100 %](/images/perf/10000ft_100.jpg)
*10.000 ft, 100 %*

![Performance-Analyse 20.190 ft, 0 %](/images/perf/20190ft_000.jpg)
*20.190 ft, 0 %*

![Performance-Analyse 20.190 ft, 49 %](/images/perf/20190ft_049.jpg)
*20.190 ft, 49 %*

![Performance-Analyse 20.190 ft, 100 %](/images/perf/20190ft_100.jpg)
*20.190 ft, 100 %*
:::

::: tip PLAUSIBILITÄTS-CHECK
„Min Radius“ ist der Radius am Corner-Punkt (Instant): Alle 27 Werte erfüllen exakt r = V² / (g · √80), also 9 G (G-Limit 9 laut Spieldaten bei allen Jets). Daraus folgt die wahre Fahrt in VFM: auf 10.000 ft ~12 % über KIAS, auf 20.190 ft ~28 % (Standardatmosphäre: 16 % bzw. ~36 %). Die Spieldaten bestätigen die Luftdichte dahinter: 69 % auf 10.000 ft, 48 % auf 20.190 ft (Standard 74 / 54 %). Details: [Die Atmosphäre in VFM](/grundlagen/physik#die-atmosphare-in-vfm).
:::

## Das Diagramm lesen

Das Diagramm zeigt **Turn Rate (°/s) über KIAS**, die x-Achse beginnt erst bei ~170–200 KIAS. Jede Linie ist ein Jet.

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Schema eines Turn-Rate-Diagramms: gestrichelte Lift-Limit-Linie steigt bis zum Corner-Punkt, danach fällt die gestrichelte 9G-Linie; darunter die durchgezogene Sustained-Kurve mit Best-Sustained-Punkt; zwei gepunktete Strahlen aus dem Ursprung zeigen Linien gleichen Radius">
<line x1="50" y1="260" x2="500" y2="260" stroke="currentColor" stroke-width="1.5"/>
<line x1="50" y1="260" x2="50" y2="15" stroke="currentColor" stroke-width="1.5"/>
<text x="56" y="18" font-size="12" fill="currentColor">Turn Rate (°/s)</text>
<text x="500" y="292" font-size="12" fill="currentColor" text-anchor="end">KIAS</text>
<line x1="50" y1="260" x2="265" y2="38" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="2 4"/>
<line x1="50" y1="260" x2="490" y2="46" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="2 4"/>
<text x="262" y="30" font-size="12" fill="currentColor" text-anchor="end">kleiner Radius</text>
<text x="490" y="36" font-size="12" fill="currentColor" text-anchor="end">größerer Radius</text>
<polyline points="132,195 248,56" fill="none" stroke="var(--vp-c-text-2)" stroke-width="2" stroke-dasharray="6 4"/>
<polyline points="248,56 270,76 298,97 325,113 380,138 435,155 490,168" fill="none" stroke="var(--vp-c-text-2)" stroke-width="2" stroke-dasharray="6 4"/>
<polyline points="149,192 193,158 243,137 287,129 322,127 358,136 402,158 446,200 474,260" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<circle cx="248" cy="56" r="4.5" fill="var(--vp-c-danger-1)"/>
<circle cx="322" cy="127" r="4.5" fill="var(--vp-c-brand-1)"/>
<circle cx="474" cy="260" r="4" fill="var(--vp-c-brand-1)"/>
<text x="256" y="64" font-size="12" fill="currentColor">Corner Speed</text>
<text x="212" y="112" font-size="12" fill="currentColor">Lift-Limit</text>
<text x="425" y="140" font-size="12" fill="currentColor">9G-Limit</text>
<text x="322" y="152" font-size="12" fill="currentColor" text-anchor="middle">Best Sustained</text>
<text x="205" y="200" font-size="12" fill="currentColor">Sustained (Ps = 0)</text>
<text x="474" y="276" font-size="12" fill="currentColor" text-anchor="middle">Vmax (1 G)</text>
</svg>

*Schema, nicht maßstäblich. Gestrichelt = Instant-Grenze, durchgezogen = Sustained, gepunktet = Linien gleichen Radius.*

| Element | Bedeutung und Folge |
|---|---|
| **Lift-Limit** (gestrichelt, steigend) | Unter Corner Speed begrenzt der Flügel. Die T-15 liegt hier bei jeder Speed vorn. Im Flug erreichst du nur ~85–92 % davon (*gemessen*); laut Spieldaten liegt die Linie 13–24 % über dem größten Auftrieb ohne Override ([Voller Zug](#voller-zug-was-ohne-override-wirklich-geht)). |
| **Corner-Punkt** (Info-Karte: MAX) | Niedrigste Speed mit 9 G: höchste Instant Rate, kleinster Radius, hoher Energieverlust. Für Schuss und Break, nicht zum Kreisen. |
| **9G-Limit** (gestrichelt, fallend) | Für alle drei Jets dieselbe Linie: Über ~435 KIAS haben alle die gleiche Instant Rate. |
| **Sustained** (durchgezogen, Ps = 0) | Drehrate ohne Energieverlust. Alles darüber kostet Speed oder Höhe. |
| **Best Sustained** (Gipfel, Info-Karte: SUS) | Speed der besten Dauer-Rate, in VFM ~450–500 KIAS, deutlich über Corner Speed. Das Plateau ist flach: Im Kampf lohnt laut Simulation etwas darunter (~400–440 KIAS), fast gleiche Rate bei kleinerem Radius. |
| **Ende der Sustained-Linie** | Top-Speed im Horizontalflug. 10.000 ft, 50 %: T-18 ~720, T-16 ~835, T-15 über dem Rand (bei ~885 KIAS noch 7 °/s). 0 ft: ~737 / ~858 / ~1.000 KIAS. |

**Radius ablesen:** r = V/ω, Linien gleichen Radius sind Strahlen aus dem Ursprung. **Höher und weiter links = enger.** Nur „weiter links“ reicht nicht: Ein Punkt weiter links, aber deutlich tiefer, kann einen größeren Radius haben. Abgeleitet (TAS ≈ KIAS × 1,115): Im **dauerhaften** Kreis bei Best Sustained fliegt die T-16 den engsten Kreis (~2.800 ft gegen ~3.150 ft bei T-15 und T-18), den kleinsten **Momentan**-Radius hat die T-15.

## Wer ist wo am besten? Speedbänder

Die wichtigste Tabelle der Diagramme (10.000 ft). Sie sagt, wer in welchem Band **dauerhaft schneller dreht**, nicht wer den Kampf gewinnt.

| Speedband | Instant Rate / Radius | Sustained Rate | Wer dreht dort dauerhaft besser? |
|---|---|---|---|
| **unter ~350–380 KIAS** | T-15 > T-18 > T-16 | T-15 ≈ T-18 > T-16 (0 ft, 250–350 KIAS: T-18 knapp vorn) | **T-15 und T-18**; die T-15 zieht bei gleicher Speed mehr G (gemessen). T-16 am schwächsten |
| **~400–500 KIAS** | über ~435 KIAS alle gleich, darunter T-15 > T-18 > T-16 | **T-16** +1–2 °/s (gemessen bei 450 KIAS: 17,6 vs 15,4 / 15,6 °/s). T-15 ≈ T-18 | **T-16**, vor allem tief. T-15 gegen T-18: Gleichstand |
| **über ~520 KIAS** | alle gleich | **T-15** vorn, hält bis ~800 KIAS fast 9 G dauerhaft. T-18 bricht ab ~510 KIAS ein (≈ Mach 0,9) | **T-15** |

Tief liegen die Jets enger beisammen: Auf Meereshöhe halten T-16 (~450–650 KIAS) und T-15 (~480–880 KIAS) dauerhaft 9 G und drehen dort gleich schnell.

**Was heißen 1–2 °/s?** Ein Vollkreis dauert bei ~18–22 °/s etwa 16–20 s. 1,5–2 °/s Vorsprung bringen ~30–40° pro Kreis, 1 °/s (10.000 ft, voller Tank) etwa 20°. Bis zum Schuss vergehen mehrere Kreise.

### Diagramm und Simulation

Aus den Bändern allein folgte bisher: Die T-16 zwingt den Kampf in 420–500 KIAS, die T-18 macht ihn langsam, die T-15 weicht in ein Band aus, in dem der Gegner schwach ist (schnell über 500 oder langsamer One-Circle). **Die Simulation deckt das nur für die T-16.** Über ganze Runden gewinnt für alle drei Jets dieselbe Familie:

- **Two-Circle bei ~440 KIAS** (bestes Raster im Turnier; feiner gerechnet: Ziel T-15 ~380–420, T-16 ~400–420). **Nose-low oder flach, leicht hoch geht auch – nur nicht steil hoch.** Am Pass zum Gegner hin drehen schlägt Wegdrehen (One-Circle); durchfliegen und mit ~440 KIAS wieder einsteigen ist in Ordnung, ein Extend mit Speedverlust nicht.
- **Langsam (~280 KIAS) und schnell (~520) verlieren**, 360 ist gut, aber schwächer als 440. Hoher α kostet im Originalmodell sehr viel Energie ([Voller Zug](#voller-zug-was-ohne-override-wirklich-geht)). Wer langsam kämpft, kommt aus dem Loch nicht mehr heraus. Wer schnell bleibt, fliegt große Kreise und hat am 9G-Limit keinen Rate-Vorteil.
- **Die T-15 gewinnt den Two-Circle gegen die T-16 trotz 1–2 °/s weniger Sustained Rate.** Bei gleicher Speed zieht sie mehr G, fliegt den kleineren Radius und holt verlorene Energie mit mehr Schub schneller zurück.

Daraus folgt die Grundlogik aller Matchups:

- **T-15:** Two-Circle bei ~380–420 KIAS, nose-low oder flach. Gewinnt mit G und Schub, nicht mit Ausweichen in andere Bänder.
- **T-16:** Two-Circle bei ~400–420 KIAS, nie steil hoch, nie langsam. Gegen die T-15 unterlegen, gegen die T-18 praktisch ausgeglichen (+0,03), klar vorn nur, wenn die Jets langsamer rollen als vorgegeben.
- **T-18:** Durchfliegen und nose-low abtauchen oder Two-Circle bei ~440 KIAS, α ~26° zum Kurven. Ihre Nase (35°) ist gegen die T-15 ~0,2 Spielwert wert, gegen die T-16 ~0,08.

**Die Rollrate ist der größte offene Punkt.** Gerechnet wird mit den Vorgaben aus den Spieldaten (T-15 325, T-16 und T-18 420 °/s, über die Fahrt gedämpft). Je schneller die Jets wirklich rollen, desto besser für die T-18: Mit drei Vierteln der Rollrate liegt die T-16 gegen sie +0,36 vorn statt +0,03. Die T-15 bleibt in jeder Variante vorn. Gemessen ist die Rollrate nicht ([Messflug M6](/grundlagen/uebungen#b2-eigenen-jet-vermessen)).

Einschränkung: Bots zielen perfekt, sehen alles und planen nicht voraus. Die Simulation zeigt, was die Physik begünstigt, nicht was gegen Menschen mit Fehlern funktioniert ([Simulation und Praxis](/flugzeuge/simulation#simulation-und-praxis)).

**Und der erste Turn?** Ranked startet auf 10.000 ft mit Mach 0,75 (im HUD **~427 KIAS**), Head-on, **13.100 ft** Abstand, Merge nach **~8 s** (*Replays*). Alle drei liegen also über Corner Speed, die Diagramm-Instant-Rate zählt kaum. Aus 450 KIAS gewinnt die T-15 den ersten Turn gemessen nur ~5° gegen die T-16 und geschätzt ~8° gegen eine sauber geflogene T-18. Details: [Der erste Turn](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen), Flow-Wahl: [One-Circle & Two-Circle](/grundlagen/neutral/one-two-circle).

## Höhe

- **Alle drei drehen tief am besten.** Die Corner Speed in KIAS steigt mit der Höhe (T-15, 50 %: 337 → 360 → 380 KIAS).
- **T-16:** Sustained-Vorsprung auf 0 ft am größten (22 vs 20 °/s), auf 20.190 ft nur 0–1 °/s.
- **T-15:** Hält auf 20.190 ft das flachste Plateau (~12–13 °/s von 350 bis ~600 KIAS). Die T-16 fällt dort ab ~470 KIAS unter sie (500 KIAS: 12,3 vs 11,3 °/s).
- **T-18:** Einbruch in jeder Höhe bei ≈ Mach 0,9: ~600 KIAS auf 0 ft, ~510 auf 10.000 ft, ~450 auf 20.190 ft.

Faustregel: **T-16 und T-18 wollen tief kämpfen, die T-15 kann den Kampf nach oben ziehen.** In der Simulation verliert „steil hoch“ trotzdem für jeden Jet, leicht hoch geht gerade noch: Höhe ist ein Ausweg, kein Plan.

## Treibstoff

| 10.000 ft | T-15 | T-16 | T-18 |
|---|---|---|---|
| Treibstoff voll | 9.091 lbs | 4.741 lbs | 9.259 lbs |
| Instant 100 → 50 → 0 % | 23 → 24 → 26 °/s | 20 → 21 → 22 °/s | 21 → 22 → 24 °/s |
| Sustained 100 → 50 → 0 % | 15 → 17 → 19 °/s | 16 → 18 → 20 °/s | 15 → 16 → 19 °/s |
| Corner Speed 100 → 50 → 0 % | 385 → 360 → 336 | 421 → 409 → 385 | 409 → 385 → 360 |

- Voll → leer: T-15 und T-18 ~22 % leichter (+3 °/s Instant, +4 °/s Sustained), T-16 ~18 %.
- Die Corner Speed wächst mit √Gewicht: voller Tank ~25 KIAS höher, fast leer ~25 KIAS tiefer als bei 50 %. Plane deine Merge-Speed danach.
- **Die Rangfolge bleibt.** Voll ist der T-16-Vorsprung kleiner (16 vs 15 °/s), leer holen T-15 und T-18 auf (20 vs 19 °/s).
- **Ranked startet mit vollem Tank** (Spieldaten; die Lobby hat keine Fuel-Option).

## Patch-Historie

| Patch | Änderung (Patchnotes) | Was die Analyse im Okt 2026 zeigt |
|---|---|---|
| v1.1 | T-15: −3 % Lift, +7 % Schub | Werte identisch mit Dez 2025 (schon enthalten oder nicht abgebildet) |
| v1.1 | T-18: mehr Treibstoff-, weniger Leergewicht | Enthalten (leer 31.967, voll 41.226 lbs) |
| v1.4.1 | T-15: Top-Speed reduziert | Nicht sichtbar (Linie reicht über den Rand) |
| v1.4.1 | T-16: Treibstoffgewicht −20 % | 5.926 → 4.741 lbs. 0 ft, 50 %: Instant 25 → 26 °/s, Corner 392 → 378 KIAS, Radius 1.524 → 1.428 ft. 10.000 ft, 100 %: Corner 434 → 421 KIAS, Radius 2.387 → 2.275 ft. Sustained gleich. |
| v1.4.1 | T-18: Top-Speed erhöht | Nicht sichtbar (weiter ~720 KIAS) |

## Beschleunigung (gemessen)

Vollgas mit Nachbrenner im Geradeausflug, je zwei Läufe.

| 10.000 ft, voller Tank | T-15 Excalibur | T-16 Falchion | T-18 Cutlass |
|---|---|---|---|
| 300 → 500 KIAS (Lauf 1 / 2) | **~8,4 s** (8,5 / 8,3) | ~11,5 s (11,6 / 11,4) | ~12,3 s (12,4 / 12,2) |
| Zuwachs im Mittel | **~24 kt/s** | ~17 kt/s | ~16 kt/s |
| Schubüberschuss (T − D) / W bei 1 G | **~1,4** | ~1,0 | ~0,95 |
| nahe Mach 0,95 (~540 KIAS) | **~1,4** | ~0,8 | ~0,7 |

- **Die T-15 beschleunigt ~40 % schneller** und kann fast immer weg und mit Speed zurückkommen.
- **T-16 und T-18 sind gleichauf** (unter ~370 KIAS die T-18 minimal besser, darüber die T-16). Ab Mach 0,9 bricht die T-18 stärker ein.
- **Vertikal** (gerechnet, bei konstant ~450 KIAS): ~1.200 / ~900 / ~770 ft/s Steigrate. Die T-15 steigt senkrecht und wird dabei noch schneller.
- **Bis zum Merge mit Nachbrenner** kommt man aus dem Ranked-Start mit ~605 (T-15), ~550 (T-16) bzw. ~535 KIAS (T-18) an (*Modell*). In der Simulation bringt das keinen klaren Vorteil.

::: details Kontrolle: Sustained-Kurven bei ~450 KIAS nachgeflogen
| | T-15 | T-16 | T-18 |
|---|---|---|---|
| geflogen (HUD) | 7,0 G, 15,4 °/s | 7,9 G, 17,6 °/s | 7,0 G, 15,6 °/s |
| aus den Diagrammen | 7,0 G | 7,8 G | 6,9 G |

Die Diagramme stimmen im Flug auf ±2–3 %.
:::

### Schub und Widerstand getrennt

Ausrollen im Leerlauf ohne Speedbrake von ~550 auf ~350 KIAS. Der Speedverlust zeigt den Widerstand, mit der Beschleunigung ergibt sich der Schub. Annahme beim Messen: Leerlaufschub ≈ 0. Laut Spieldaten sind es ~5 %; die gemessenen Widerstandswerte sind damit eher etwas zu niedrig, an der Rangfolge ändert das nichts.

| 10.000 ft, voller Tank, 1 G | T-15 | T-16 | T-18 |
|---|---|---|---|
| Speedverlust im Leerlauf bei ~450 KIAS | ~5 kt/s | ~5 kt/s | **~9 kt/s** |
| Widerstand / Gewicht (350–550 KIAS) | 0,18–0,35 | 0,18–0,35 | **0,33–0,60** |
| Schub / Gewicht mit Nachbrenner (gemessen) | **~1,65** | ~1,26 | ~1,35 |
| Schub / Gewicht mit Nachbrenner (*Spieldaten*, ~Mach 0,75) | **1,64** | 1,29 | 1,37 |

**Die T-18 hat mehr Schub als die T-16, aber fast doppelt so viel Widerstand.** Deshalb beschleunigen beide gleich, und deshalb bricht die T-18 bei hoher Speed ein. Gas raus macht sie fast doppelt so schnell langsam: gut als Bremse, eine Falle, wenn du Energie halten willst.

Was die Spieldaten dazu erklären:

- **Schub über Mach:** Die T-16 hat ihr Schubmaximum bei ~Mach 0,8 und verliert darüber, die T-15 bei ~Mach 1,0, die T-18 erst bei ~Mach 1,2. Dass die T-18 trotzdem bei ≈ Mach 0,9 einbricht, liegt an ihrem Grundwiderstand, dem höchsten der drei. Auf 10.000 ft liegt Mach 0,8 bei ~455 KIAS: Darüber fällt der Schub der T-16 schon, ein Grund, warum die T-15 sie über ~520 KIAS überholt.
- **Wellenwiderstand:** bei allen drei ~+20 % um Mach 1.
- **T-18 über ~22° α:** Sie verliert dort etwas Schub. Ein weiterer Grund, nicht dauerhaft auf 35° zu ziehen.

### Voller Zug: was ohne Override wirklich geht

Bei ~450 KIAS Knüppel voll ziehen und halten.

| 10.000 ft, voller Tank | T-15 | T-16 | T-18 |
|---|---|---|---|
| Zeit bis zur Höchst-G | ~2 s | ~3 s | ~3 s |
| Höchst-G (bei KIAS) | **9,1 G** (419) | 8,4 G (428) | 8,7 G (427) |
| α am Anschlag | ~24–25° | ~23° | **bis 35°** (meiste G bei ~26°) |
| G unterhalb der Höchst-G, in % des Diagramm-Lift-Limits | ~90 % | ~92 % | ~85 % (überzogen) |
| Energieverlust im Zug | ~2,3-mal T-16 | **am geringsten** | **extrem** (überzogen) |

- **Die Diagramm-Instant-Werte erreichst du ohne Override nicht ganz.** Und nur die T-15 kam auf 9 G: Bis die G anliegen, vergehen 2–3 s mit Speedverlust. **Für 9 G musst du deutlich über Corner Speed anfangen.**
- **Bei gleicher Speed zieht die T-15 die meisten G** (~355 KIAS: 6,8 / 5,8 / 5,7 G; ~285 KIAS: T-15 4,8, T-18 3,6 G) und fliegt damit den engsten Kreis.
- **T-18: Nasenautorität statt Kurvenrate.** Über ~26° α zieht sie weniger G und verliert enorm Energie (gerechnet ~40 kt/s bei gehaltener Höhe), ihre Nase zeigt dafür ~10° weiter in die Kurve. Dass sie „enger“ wirkt, liegt an dieser Nase und daran, dass sie schnell langsam wird. Zum Kurven ~26°, 35° für den Snapshot.
- **Die T-16 verliert am wenigsten Energie:** weniger G, dafür bleibt sie schneller.

Was die Spieldaten dazu erklären:

- **Auftriebsmaximum bei HUD-α ~27°, bei allen drei Jets** (der Flügel sieht ~2° weniger). Darüber fällt der Auftrieb. Das erklärt die gemessene T-18-Regel „meiste G bei ~26°“: Ihre 35° liegen jenseits des Maximums. T-15 und T-16 stoppt der Limiter knapp darunter, für sie ist Knüppel voll die beste Kurve.
- **Widerstand über α steigt steil:** Bei α 15° hat der Flügel ~4–12-mal, bei α 25° ~12–34-mal so viel Widerstand wie bei α 0. Am stärksten bei der T-15, am schwächsten bei der T-18 (die dafür den höchsten Grundwiderstand hat). Deshalb kostet voller Zug so viel Energie, deshalb lohnt „unter dem Anschlag fliegen“, und deshalb verliert der langsame Kreis in der Simulation.
- **Lift-Limit der Diagramme:** Es liegt 13–24 % über dem größten Auftrieb, den der Jet im Flug ohne Override erreicht. Die gemessenen 85–92 % passen dazu.

## Info-Karten: Balken und Widersprüche

Die Info-Karten der Einzeljets zeigen MAX (Corner Speed), SUS (Best Sustained Speed) und vier grobe Balken.

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| MAX / SUS | 385 / 500 KIAS | 431 / 466 KIAS | 408 / 466 KIAS |
| Sustained Turn | ~75 % | **voll** | ~60 % |
| Turn Radius | ~90 % | ~70 % | **voll** |
| Max Speed | **voll** | ~70 % | ~90 % |
| Thrust to Weight | **voll** | ~75 % | ~95 % |

![Info-Karte T-15 Excalibur](/images/img1.jpg)

![Info-Karte T-16 Falchion](/images/img2.jpg)

![Info-Karte T-18 Cutlass](/images/img3.jpg)

::: warning WIDERSPRÜCHE
- **Turn Radius:** Der Balken zeigt die T-18 vorn, die Tabelle in allen neun Bedingungen die T-15 (10.000 ft: 1.644 vs 1.899 ft). Es gilt die Tabelle. Vermutung: Der Balken bewertet hohes α oder Override; die T-18 hat in den Spieldaten die mit Abstand höchsten α-Grenzen (*Hypothese*).
- **Max Speed:** Laut Balken ist die T-18 schneller als die T-16, im Diagramm ist es umgekehrt (~835 vs ~720 KIAS). Es gilt das Diagramm. Vermutung: Der Balken bewertet nur den Schub bei hoher Mach (T-18 Schubmaximum ~Mach 1,2, T-16 ~Mach 0,8), nicht den Widerstand (*Hypothese*).
- **Thrust to Weight:** Stimmt für den Schub (gemessen ~1,65 / ~1,26 / ~1,35, Spieldaten 1,64 / 1,29 / 1,37), nicht für die Beschleunigung, siehe [Schub und Widerstand getrennt](#schub-und-widerstand-getrennt).
:::

## Nicht in den Daten / offen

- **Langsamflug:** Die Diagramme beginnen bei ~170–200 KIAS, die Messflüge reichen bis ~280 KIAS. Stall und Steuerbarkeit bei hohem α sind offen.
- **AoA-Override:** Wie weit er α freigibt und was er an Energie kostet. Die Spieldaten nennen je Jet zwei α-Grenzen; der zweite Wert könnte das Override-Limit sein (*Hypothese*).
- **Rollrate:** Die Spieldaten nennen die Fly-by-Wire-Vorgabe: bis **325 °/s (T-15), 420 °/s (T-16, T-18)**, Pitch-Rate 40 / 70 / 80 °/s. Die T-15 rollt also am langsamsten. Ob die Werte im Flug erreicht werden, ist nicht gemessen. Die Simulation rechnet mit ihnen; wie schnell die Jets wirklich rollen, entscheidet dort vor allem T-16 gegen T-18 ([Diagramm und Simulation](#diagramm-und-simulation)).
- **Kanone:** bekannt aus Spieldaten und Replays: 1.030 m/s (~3.380 ft/s) Mündungsgeschwindigkeit, 6.000 Schuss/min, 26 Schaden je Treffer, bis 3.000 ft ~0,75 s Flugzeit. Offen sind Streuung und effektive Reichweite.
- **Leerlaufschub:** laut Spieldaten ~5 % (bisher ≈ 0 angenommen).
- **Außerdem offen:** Speedbrake-Wirkung, Greyout-Modell, wie das Spiel bei Zeitablauf den Verfolger bestimmt. Der Ranked-Start ist aus den Replays bekannt (siehe [Spielmodi](/einstieg/spielmodi#ranked)).

::: info IM SPIEL PRÜFEN
- **Rollrate:** 10.000 ft, ~430 KIAS, 1 G, Stick voll zur Seite, Zeit für 360° stoppen. Kommen die Jets an 325 / 420 °/s heran? Die wichtigste offene Messung: Sie entscheidet, ob die T-16 die T-18 klar schlägt.
- **T-18 mit α ~26° aus 450 KIAS:** Der erste Turn ist bisher nur geschätzt (≥ ~138° nach 8 s).
- **Unter ~280 KIAS und mit Override:** Test im [T-18-Profil](/flugzeuge/t18#hypothese-testen).
- **Nach Balance-Patches** die Analyse in denselben neun Bedingungen neu ablesen.
:::

::: tip MERKE
- **Diagramm:** Wer in welchem Band dauerhaft schneller dreht: langsam T-15/T-18, 400–500 KIAS T-16, über ~520 KIAS T-15. Bei ~450 KIAS drehen T-15 und T-18 gleich.
- **Simulation:** Wer den Kampf gewinnt: Two-Circle bei ~440 KIAS (Ziel T-15 ~380–420, T-16 ~400–420), nose-low oder flach, für alle drei Jets. Nicht langsam, nicht schnell, nicht steil hoch. T-15 vorn, T-16 gegen T-18 fast ausgeglichen: Je schneller die Jets rollen, desto besser für die T-18.
- **Corner Speed** (Instant, kleinster Radius) ist nicht **Best Sustained Speed** (~450–500 KIAS); gekämpft wird knapp darunter.
- Die T-15 beschleunigt ~40 % schneller und zieht bei gleicher Speed die meisten G, bezahlt Vollzüge aber teuer: Widerstand steigt mit α steil.
- Auftrieb ist bei HUD-α ~27° am größten. Die T-18 kurvt mit ~26°, 35° nur für den Snapshot.
- Tief dreht jeder besser, weniger Fuel macht jeden besser, die Rangfolge bleibt.
:::

Weiter: [T-15 Excalibur](/flugzeuge/t15) · [T-16 Falchion](/flugzeuge/t16) · [T-18 Cutlass](/flugzeuge/t18) · [Simulation](/flugzeuge/simulation)
