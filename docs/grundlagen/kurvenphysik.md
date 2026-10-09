# Kurvenphysik

> Wie ein Jet kurvt: Lastvielfaches, Lift Vector, Turn Rate und Radius – und warum die Corner Speed so wichtig ist.

Jedes Manöver in BFM ist im Kern dasselbe: **Lift Vector dorthin rollen, wo du hinwillst, dann ziehen.** Diese Seite erklärt, was dabei physikalisch passiert und welche Zahlen in VFM dahinterstecken. Begriffe: [Glossar](/grundlagen/begriffe).

## Lastvielfaches n ("G")

Das **Lastvielfache n** (Load Factor) ist der Auftrieb geteilt durch das Gewicht: n = L / W. Im Alltag sagen wir einfach "G".

- **1 G:** Geradeaus- und Horizontalflug, der Auftrieb trägt genau dein Gewicht.
- **9 G:** Der Flügel erzeugt das Neunfache deines Gewichts an Auftrieb. In VFM ist **9 G die Grenze** – in den Leistungsdiagrammen als "9G LIMIT"-Linie eingezeichnet.
- **0 G:** Kein Auftrieb, die Flugbahn ist ballistisch (sie krümmt sich nur durch die Schwerkraft nach unten).

Mehr G heißt engere, schnellere Kurve – aber auch mehr induzierter Widerstand und damit Energieverlust (siehe [Energie-Management](/grundlagen/energie-management)).

## Der Lift Vector: das zentrale Konzept

Der **Lift Vector** (Auftriebsvektor) zeigt senkrecht aus den Flügeln heraus, Richtung Kabinendach. **Wohin der Lift Vector zeigt, dorthin kurvst du, wenn du ziehst.** Ziehen kannst du nur "nach oben" relativ zum Cockpit. Deshalb ist jede Richtungsänderung zweistufig:

1. **Rollen:** Lift Vector auf das Ziel legen (auf den Gegner, vor ihn, über ihn, unter ihn).
2. **Ziehen:** So viel G, wie die Situation verlangt.

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Jet von hinten in 60 Grad Querlage. Der Lift Vector zeigt schräg nach oben links, die Schwerkraft nach unten. Die senkrechte Komponente des Lifts hebt die Schwerkraft auf, die waagrechte Komponente zieht den Jet in die Kurve.">
<defs><marker id="kp-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker><marker id="kp-ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--vp-c-brand-1)"/></marker><marker id="kp-ahd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--vp-c-danger-1)"/></marker></defs>
<text x="260" y="24" font-size="12" fill="currentColor" text-anchor="middle">Blick von hinten: 60° Querlage links, Höhe wird gehalten (n = 2)</text>
<line x1="20" y1="170" x2="500" y2="170" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="2 4"/>
<text x="500" y="162" font-size="12" fill="var(--vp-c-text-2)" text-anchor="end">Horizont</text>
<line x1="225" y1="230.6" x2="295" y2="109.4" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
<circle cx="260" cy="170" r="9" fill="currentColor"/>
<line x1="260" y1="170" x2="156" y2="110" stroke="var(--vp-c-brand-1)" stroke-width="3" marker-end="url(#kp-ahb)"/>
<text x="150" y="100" font-size="12" fill="var(--vp-c-brand-1)" text-anchor="end">Lift Vector (2 g)</text>
<line x1="156" y1="110" x2="156" y2="170" stroke="var(--vp-c-text-2)" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="150" y="145" font-size="12" fill="var(--vp-c-text-2)" text-anchor="end">trägt dich: 1 g</text>
<line x1="250" y1="178" x2="160" y2="178" stroke="currentColor" stroke-width="2" marker-end="url(#kp-ah)"/>
<text x="135" y="198" font-size="12" fill="currentColor" text-anchor="middle">dreht dich: √(n²−1) g ≈ 1,7 g</text>
<text x="30" y="160" font-size="12" fill="currentColor">← Kurvenmitte</text>
<line x1="268" y1="172" x2="268" y2="240" stroke="var(--vp-c-danger-1)" stroke-width="3" marker-end="url(#kp-ahd)"/>
<text x="276" y="236" font-size="12" fill="var(--vp-c-danger-1)">Schwerkraft 1 g</text>
<text x="300" y="104" font-size="12" fill="currentColor">rechte Fläche</text>
<text x="260" y="285" font-size="12" fill="var(--vp-c-text-2)" text-anchor="middle">Nur der waagrechte Anteil des Lifts dreht dich. Der senkrechte hebt die Schwerkraft auf.</text>
</svg>

### Querlage und G im Horizontalflug

Willst du in einer Horizontalkurve die Höhe halten, muss der senkrechte Anteil des Lifts genau 1 g sein. Daraus folgt: cos(Querlage) = 1 / n.

| Querlage | Nötige G für Höhe halten | "Dreh"-Anteil √(n²−1) |
|---|---|---|
| 60° | 2 G | 1,7 g |
| 70,5° | 3 G | 2,8 g |
| 75,5° | 4 G | 3,9 g |
| 80,4° | 6 G | 5,9 g |
| 83,6° | 9 G | 8,9 g |

Praktisch heißt das: Bei 9 G liegt der Lift Vector fast waagrecht. Zeigt er weiter nach oben, steigst du; zeigt er unter den Horizont, sinkst du (und die Schwerkraft hilft dir beim Drehen, siehe unten). Im Luftkampf fliegst du selten eine exakt horizontale Kurve – du legst den Lift Vector dorthin, wo du den Gegner haben willst.

::: tip SPRICH IN LIFT VECTORS
Statt "Nase runterdrücken" denk: "Lift Vector unter den Horizont rollen und ziehen." Statt "hochziehen": "Lift Vector über den Gegner rollen und ziehen." So lassen sich alle Manöver in diesem Wiki beschreiben – vom [Yo-Yo](/grundlagen/offensiv/yo-yos) bis zum [Break Turn](/grundlagen/defensiv/break-turn).
:::

## Turn Rate und Radius

Für eine Kurve in der Horizontalen gilt (V = wahre Geschwindigkeit, g = 9,81 m/s²):

```
Turn Rate     ω = g · √(n² − 1) / V
Turn Radius   r = V² / (g · √(n² − 1))
```

Die wichtigsten Folgen:

- **Bei festem G sinkt die Rate mit der Speed** (ω ~ 1/V) – doppelt so schnell = halbe Rate.
- **Bei festem G wächst der Radius mit dem Quadrat der Speed** (r ~ V²) – doppelt so schnell = vierfacher Radius.
- **Mehr G** verbessert beides, aber nur bis 9 G.

### Rechenbeispiel mit VFM-Zahlen

Auf Meereshöhe sind KIAS (angezeigte Speed) und wahre Speed praktisch gleich. 1 kt = 0,514 m/s.

| Fall | Turn Rate | Radius |
|---|---|---|
| 9 G bei 337 KIAS | 29,0 °/s | ~1.120 ft |
| 9 G bei 360 KIAS | 27,1 °/s | ~1.280 ft |
| 9 G bei 500 KIAS | 19,5 °/s | ~2.470 ft |
| 5 G bei 360 KIAS | 14,9 °/s | ~2.340 ft |

Rechnung für 9 G bei 360 KIAS: V = 360 · 0,514 = 185 m/s, √(81 − 1) = 8,94. Rate = 9,81 · 8,94 / 185 = 0,474 rad/s = **27,1 °/s**. Radius = 185² / (9,81 · 8,94) = 391 m = **1.280 ft**.

Vergleich mit dem Spiel: Die T-15 hat laut Ingame-Analyse auf Meereshöhe (50 % Fuel, Stand Dez 2025) ihre Max Instant Rate von **29 °/s bei 337 KIAS** und einen Mindestradius von **1.138 ft** – genau das, was die Formel bei 9 G ergibt. Gleiches gilt für T-16 (25 °/s @ 392 KIAS) und T-18 (27 °/s @ 365 KIAS). Die Ingame-Werte sind also schlicht "9 G bei Corner Speed".

Was die Tabelle zeigt:

- **500 statt 360 KIAS** bei gleichen 9 G: gut ein Viertel weniger Rate, fast der doppelte Radius.
- **5 statt 9 G** bei 360 KIAS: die Hälfte der Rate. Wer am Merge nicht voll zieht, verschenkt Winkel.

### KIAS vs. wahre Speed in der Höhe

Die Formeln brauchen die **wahre** Speed (TAS). In der Höhe ist die Luft dünner, die wahre Speed liegt über der angezeigten: auf 10.000 ft etwa 16 % höher, auf ~21.500 ft etwa 40 %. Bei gleicher KIAS und gleichen 9 G drehst du in der Höhe also langsamer und weiter. Das erklärt einen großen Teil, warum alle Jets mit der Höhe Rate verlieren (Beispiel T-15: 29 °/s auf Meereshöhe, 24 °/s auf 10.000 ft, 19 °/s auf ~21.500 ft). Details: [Das VFM-Flugmodell](/grundlagen/physik#hohe).

## Corner Speed

Zwei Grenzen bestimmen, wie viel G du ziehen kannst:

1. **Lift-Limit (aerodynamisch):** Langsam kann der Flügel nicht genug Auftrieb für 9 G erzeugen. Die maximale G steigt etwa mit dem Quadrat der Speed – und damit steigt auch die Turn Rate mit der Speed.
2. **G-Limit:** Ab einer bestimmten Speed erreichst du 9 G, mehr gibt es nicht. Ab hier sinkt die Rate mit 1/V.

Die **Corner Speed** ist der Schnittpunkt: die niedrigste Speed, bei der du 9 G erreichst. Dort hast du die **höchste Instant Turn Rate und den kleinsten Radius bei 9 G**.

| Jet (Stand Dez 2025) | Corner Speed 10.000 ft, 50 % Fuel | Meereshöhe, 50 % | 10.000 ft, 100 % |
|---|---|---|---|
| T-15 Excalibur | ~360 KIAS (24 °/s) | ~337 KIAS (29 °/s) | ~385 KIAS (23 °/s) |
| T-16 Falchion | ~409 KIAS (21 °/s) | ~392 KIAS (25 °/s) | ~434 KIAS (20 °/s) |
| T-18 Cutlass | ~385 KIAS (22 °/s) | ~365 KIAS (27 °/s) | ~409 KIAS (21 °/s) |

### Warum die Corner Speed so wichtig ist

- **Am Merge und im Break Turn** willst du in kurzer Zeit maximal Winkel gewinnen – das gelingt nahe Corner Speed am besten.
- **Darunter** fehlen dir G. **Darüber** ist der Radius groß und die Rate kleiner.
- **Aber:** Bei Corner Speed und 9 G verlierst du sehr schnell Energie. Du kannst dort nicht bleiben. Die Speed, bei der du eine Kurve **dauerhaft** halten kannst, ist die **Best Sustained Speed** – in VFM meist deutlich höher (~450–500 KIAS). Beides nicht verwechseln: [Energie-Management](/grundlagen/energie-management#corner-speed-vs-best-sustained-speed).

## Schwerkraft in schrägen und vertikalen Kurven

In der Horizontalkurve kostet dich die Schwerkraft immer etwas: Ein Teil des Lifts muss sie aufheben. Kurvst du schräg oder vertikal, ändert sich das.

- **Lift Vector unter dem Horizont (nose-low):** Die Schwerkraft zieht in dieselbe Richtung wie dein Lift. Du drehst **schneller**, und die Speed bleibt eher erhalten (Höhe wird in Speed umgewandelt).
- **Lift Vector über dem Horizont (nose-high):** Die Schwerkraft wirkt gegen deinen Lift. Du drehst **langsamer** und verlierst Speed (Speed wird in Höhe umgewandelt).

Extremfall Looping (senkrechte Kurve), die Beschleunigung Richtung Kurvenmitte:

| Position | Wirkung in Richtung Kurvenmitte | bei 9 G | bei 3 G |
|---|---|---|---|
| Oben (Lift Vector zeigt nach unten) | (n + 1) g | 10 g | 4 g |
| Horizontalkurve | √(n² − 1) g | 8,9 g | 2,8 g |
| Unten (Lift Vector zeigt nach oben) | (n − 1) g | 8 g | 2 g |

Bei 9 G macht die Schwerkraft rund ±10 % aus. Bei 3 G – typisch, wenn du oben langsam bist – sind es über 40 %. **Je langsamer und je weniger G, desto stärker hilft (oder bremst) die Schwerkraft.** Genau deshalb drehen Jets oben in der Vertikalen so gut.

Kombiniert mit der Speed (oben langsam = kleinerer Radius, unten schnell = größerer Radius) ergibt sich die typische Form einer vertikalen Kurve: **"The Egg"** – oben eng, unten weit. Wie du das im Kampf nutzt: [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf). Wie du nose-low gezielt Rate holst: [Slice Turn](/grundlagen/defensiv/slice-turn).

## Out-of-Plane-Manövrieren

Jeder Jet kurvt in einer Ebene – der Ebene aus Flugrichtung und Lift Vector, seiner **Bewegungsebene** (Plane of Motion). Wenn du deinen Lift Vector **aus der Ebene des Gegners heraus** rollst (über oder unter ihn), passiert dreierlei:

- **Du nutzt die Schwerkraft:** nose-low für Rate, nose-high, um Speed in Höhe zu parken.
- **Du steuerst Closure:** Über ihn hinaus kurven baut Closure ab, ohne Energie zu verschenken – das ist die Idee des [High Yo-Yo](/grundlagen/offensiv/yo-yos).
- **Du erschwerst ihm das Zielen:** Um dir zu folgen, muss er erst rollen, dann ziehen. Das kostet ihn Zeit – die Basis von [Guns Defense](/grundlagen/defensiv/guns-defense).

Wer nur flach in der Horizontalen kurvt, verschenkt diese Werkzeuge. Mehr zur Bewegungsebene: [Relative Geometrie](/grundlagen/geometrie#bewegungsebene-plane-of-motion).

::: info IM SPIEL PRÜFEN
- Rollrate der drei Jets (nicht in den Daten) – sie bestimmt, wie schnell du den Lift Vector umlegen kannst.
- Verhalten unter ~170 KIAS: Die Ingame-Diagramme beginnen erst bei ~170–200 KIAS.
:::

::: tip MERKE
- **Lift Vector platzieren, dann ziehen** – jedes Manöver ist das.
- **Rate ~ 1/V, Radius ~ V²** bei gleicher G. Zu schnell heißt: großer Kreis, langsame Nase.
- **Corner Speed** = niedrigste Speed mit 9 G = beste Instant Rate. T-15 ~360, T-16 ~409, T-18 ~385 KIAS (10.000 ft, 50 %).
- **Nose-low dreht schneller, nose-high langsamer** – je langsamer du bist, desto stärker.
- **Raus aus der Ebene** gibt dir Schwerkraft, Closure-Kontrolle und macht dich schwerer zu treffen.
:::

Weiter: [Energie-Management](/grundlagen/energie-management)
