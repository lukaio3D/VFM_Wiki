# Performance-Daten & Vergleich

> Alle Leistungsdaten der drei Jets an einem Ort: Diagramme, Messflüge und was sie für deinen Kampf bedeuten.

::: info DATENSTAND
- **Diagramme:** Ingame-Ansicht „Aircraft Performance Analysis“, aufgenommen im Oktober 2026 (v1.4.2) in neun Bedingungen (0 / 10.000 / 20.190 ft × 0 / 50 / 100 % Fuel). T-15 und T-18 zeigen exakt dieselben Werte wie im Dezember 2025, die T-16 ist durch v1.4.1 minimal besser ([Patch-Historie](#patch-historie)).
- **Messflüge:** Oktober 2026, 10.000 ft, voller Tank, nur Guns, Werte aus dem HUD-Video.
- **Info-Karten:** Dezember 2025.

Kennzeichnung im ganzen Wiki: *Diagramm* (Ingame-Analyse), *gemessen* (Messflug), *geschätzt*, *Hypothese*.
:::

## Die drei Jets in einem Satz

Es gibt kein Stein-Schere-Papier. Wer vorn liegt, hängt vom **Speedband** ab.

| Jet | Charakter | Spielplan |
|---|---|---|
| **[T-15 Excalibur](/flugzeuge/t15)** | Stärkster Jet auf dem Papier: meiste G bei gleicher Speed, kleinster Radius, ~40 % mehr Beschleunigung, höchste Top-Speed. Bestraft unnötige Vollzüge. | Das Band wählen, in dem der Gegner schwach ist: schnell (> 500 KIAS) oder langsamer One-Circle |
| **[T-16 Falchion](/flugzeuge/t16)** | Rate-Spezialist: leichtester Jet, beste Sustained Rate bei ~420–500 KIAS, verliert im Zug am wenigsten Energie | Speed halten, Two-Circle, tief, nie langsam werden |
| **[T-18 Cutlass](/flugzeuge/t18)** | Low-Speed-Brawler: Nasenautorität (α bis 35°), hoher Widerstand, über ~510 KIAS schwach | Kampf langsam machen, One-Circle von unten, α ~26° zum Kurven |

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

**Gewichte (0 / 50 / 100 % Fuel):** T-15 33.069 / 37.615 / 42.160 lbs, T-16 22.046 / 24.417 / 26.787 lbs, T-18 31.967 / 36.597 / 41.226 lbs. Auf 20.190 ft stand der Regler bei 49 %.

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
„Min Radius“ ist der Radius am Corner-Punkt (Instant): Alle 27 Werte erfüllen exakt r = V² / (g · √80), also 9 G. Daraus folgt die wahre Fahrt in VFM: auf 10.000 ft ~12 % über KIAS, auf 20.190 ft ~28 % (Standardatmosphäre: 16 % bzw. ~36 %). Details: [Die Atmosphäre in VFM](/grundlagen/physik#die-atmosphare-in-vfm).
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
| **Lift-Limit** (gestrichelt, steigend) | Unter Corner Speed begrenzt der Flügel. Die T-15 liegt hier bei jeder Speed vorn. Im Flug erreichst du nur ~85–92 % davon ([Voller Zug](#voller-zug-was-ohne-override-wirklich-geht)). |
| **Corner-Punkt** (Info-Karte: MAX) | Niedrigste Speed mit 9 G: höchste Instant Rate, kleinster Radius, hoher Energieverlust. Für Schuss und Break, nicht zum Kreisen. |
| **9G-Limit** (gestrichelt, fallend) | Für alle drei Jets dieselbe Linie: Über ~435 KIAS haben alle die gleiche Instant Rate. |
| **Sustained** (durchgezogen, Ps = 0) | Drehrate ohne Energieverlust. Alles darüber kostet Speed oder Höhe. |
| **Best Sustained** (Gipfel, Info-Karte: SUS) | Speed für lange Kreiskämpfe, in VFM ~450–500 KIAS, deutlich über Corner Speed. |
| **Ende der Sustained-Linie** | Top-Speed im Horizontalflug. 10.000 ft, 50 %: T-18 ~720, T-16 ~835, T-15 über dem Rand (bei ~885 KIAS noch 7 °/s). 0 ft: ~737 / ~858 / ~1.000 KIAS. |

**Radius ablesen:** r = V/ω, Linien gleichen Radius sind Strahlen aus dem Ursprung. **Höher und weiter links = enger.** Nur „weiter links“ reicht nicht: Ein Punkt weiter links, aber deutlich tiefer, kann einen größeren Radius haben. Abgeleitet (TAS ≈ KIAS × 1,115): Im **dauerhaften** Kreis bei Best Sustained fliegt die T-16 den engsten Kreis (~2.800 ft gegen ~3.150 ft bei T-15 und T-18), den kleinsten **Momentan**-Radius hat die T-15.

## Wer ist wo am besten? Speedbänder

Die wichtigste Tabelle dieser Seite (10.000 ft).

| Speedband | Instant Rate / Radius | Sustained Rate | Wer gewinnt den Kreiskampf? |
|---|---|---|---|
| **unter ~350–380 KIAS** | T-15 > T-18 > T-16 | T-15 ≈ T-18 > T-16 (0 ft, 250–350 KIAS: T-18 knapp vorn) | **T-15 und T-18**; die T-15 zieht bei gleicher Speed mehr G (gemessen). T-16 am schwächsten |
| **~400–500 KIAS** | über ~435 KIAS alle gleich, darunter T-15 > T-18 > T-16 | **T-16** +1–2 °/s (gemessen bei 450 KIAS: 17,6 vs 15,4 / 15,6 °/s). T-15 ≈ T-18 | **T-16** im Two-Circle, vor allem tief. T-15 gegen T-18: Gleichstand |
| **über ~520 KIAS** | alle gleich | **T-15** vorn, hält bis ~800 KIAS fast 9 G dauerhaft. T-18 bricht ab ~510 KIAS ein (≈ Mach 0,9) | **T-15** |

Tief liegen die Jets enger beisammen: Auf Meereshöhe halten T-16 (~450–650 KIAS) und T-15 (~480–880 KIAS) dauerhaft 9 G und drehen dort gleich schnell.

Daraus folgt die Grundlogik aller Matchups:

- **T-16** zwingt den Kampf ins Band **~420–500 KIAS** und hält ihn dort.
- **T-18** macht den Kampf **langsam**.
- **T-15** sucht das Band, in dem der Gegner schwach ist: gegen die T-16 nicht 400–500 KIAS, gegen die T-18 nicht ~450 KIAS, sondern schnell (> 500) oder langsam.

**Was heißen 1–2 °/s?** Ein Vollkreis dauert bei ~18–22 °/s etwa 16–20 s. 1,5–2 °/s Vorsprung bringen ~30–40° pro Kreis, 1 °/s (10.000 ft, voller Tank) etwa 20°. Bis zum Schuss vergehen mehrere Kreise im richtigen Band.

**Und der erste Turn?** Die Diagramm-Instant-Rate zählt nur, wenn du nahe Corner Speed ankommst. Aus 450 KIAS (Ranked-Start) ist der erste Turn fast ausgeglichen: Die T-15 gewinnt gemessen ~5° gegen die T-16 und geschätzt ~8° gegen eine sauber geflogene T-18. Details: [Der erste Turn aus 450 KIAS](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen), Flow-Wahl: [One-Circle & Two-Circle](/grundlagen/neutral/one-two-circle).

## Höhe

- **Alle drei drehen tief am besten.** Die Corner Speed in KIAS steigt mit der Höhe (T-15, 50 %: 337 → 360 → 380 KIAS).
- **T-16:** Sustained-Vorsprung auf 0 ft am größten (22 vs 20 °/s), auf 20.190 ft nur 0–1 °/s.
- **T-15:** Hält auf 20.190 ft das flachste Plateau (~12–13 °/s von 350 bis ~600 KIAS). Die T-16 fällt dort ab ~470 KIAS unter sie (500 KIAS: 12,3 vs 11,3 °/s).
- **T-18:** Einbruch in jeder Höhe bei ≈ Mach 0,9: ~600 KIAS auf 0 ft, ~510 auf 10.000 ft, ~450 auf 20.190 ft.

Faustregel: **T-16 und T-18 wollen tief kämpfen, die T-15 kann den Kampf nach oben ziehen.**

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

::: details Kontrolle: Sustained-Kurven bei ~450 KIAS nachgeflogen
| | T-15 | T-16 | T-18 |
|---|---|---|---|
| geflogen (HUD) | 7,0 G, 15,4 °/s | 7,9 G, 17,6 °/s | 7,0 G, 15,6 °/s |
| aus den Diagrammen | 7,0 G | 7,8 G | 6,9 G |

Die Diagramme stimmen im Flug auf ±2–3 %.
:::

### Schub und Widerstand getrennt

Ausrollen im Leerlauf ohne Speedbrake von ~550 auf ~350 KIAS. Der Speedverlust zeigt den Widerstand, mit der Beschleunigung ergibt sich der Schub. Annahme: Leerlaufschub ≈ 0 (T-16: Fuel Flow ~600 PPH gegenüber ~59.000 PPH mit Nachbrenner).

| 10.000 ft, voller Tank, 1 G | T-15 | T-16 | T-18 |
|---|---|---|---|
| Speedverlust im Leerlauf bei ~450 KIAS | ~5 kt/s | ~5 kt/s | **~9 kt/s** |
| Widerstand / Gewicht (350–550 KIAS) | 0,18–0,35 | 0,18–0,35 | **0,33–0,60** |
| Schub / Gewicht mit Nachbrenner | **~1,65** | ~1,26 | ~1,35 |

**Die T-18 hat mehr Schub als die T-16, aber fast doppelt so viel Widerstand.** Deshalb beschleunigen beide gleich, und deshalb bricht die T-18 bei hoher Speed ein. Gas raus macht sie fast doppelt so schnell langsam: gut als Bremse, eine Falle, wenn du Energie halten willst.

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
- **Turn Radius:** Der Balken zeigt die T-18 vorn, die Tabelle in allen neun Bedingungen die T-15 (10.000 ft: 1.644 vs 1.899 ft). Es gilt die Tabelle. Vermutung: Der Balken bewertet etwas außerhalb des Diagramms, etwa sehr niedrige Speed oder hohes α.
- **Max Speed:** Laut Balken ist die T-18 schneller als die T-16, im Diagramm ist es umgekehrt (~835 vs ~720 KIAS). Es gilt das Diagramm.
- **Thrust to Weight:** Stimmt für den Schub (~1,65 / ~1,26 / ~1,35), nicht für die Beschleunigung, siehe [Schub und Widerstand getrennt](#schub-und-widerstand-getrennt).
:::

## Nicht in den Daten / offen

- **Langsamflug:** Die Diagramme beginnen bei ~170–200 KIAS, die Messflüge reichen bis ~280 KIAS. Stall und Steuerbarkeit bei hohem α sind offen.
- **AoA-Override:** Wie viel Nose Authority er welchem Jet bringt.
- **Außerdem offen:** Rollrate, Leerlaufschub, Speedbrake-Wirkung, Gun-Reichweite und Streuung, Greyout-Modell, Startgeometrie im Ranked.

::: info IM SPIEL PRÜFEN
- **T-18 mit α ~26° aus 450 KIAS:** Der erste Turn ist bisher nur geschätzt (≥ ~138° nach 8 s).
- **Unter ~280 KIAS und mit Override:** Test im [T-18-Profil](/flugzeuge/t18#hypothese-testen).
- **Nach Balance-Patches** die Analyse in denselben neun Bedingungen neu ablesen.
:::

::: tip MERKE
- Es zählt das **Speedband**: langsam T-15/T-18, 400–500 KIAS T-16, über ~520 KIAS T-15. Bei ~450 KIAS drehen T-15 und T-18 gleich.
- **Corner Speed** (Instant, kleinster Radius) ist nicht **Best Sustained Speed** (~450–500 KIAS).
- Die T-15 beschleunigt ~40 % schneller und zieht bei gleicher Speed die meisten G, bezahlt Vollzüge aber teuer.
- Die T-18 hat viel Widerstand und Nasenautorität: α ~26° zum Kurven, 35° für den Snapshot.
- Tief dreht jeder besser, weniger Fuel macht jeden besser, die Rangfolge bleibt.
:::

Weiter: [T-15 Excalibur](/flugzeuge/t15) · [T-16 Falchion](/flugzeuge/t16) · [T-18 Cutlass](/flugzeuge/t18)
