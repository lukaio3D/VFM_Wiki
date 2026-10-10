# Kurvenphysik

> Wie ein Jet kurvt: Lastvielfaches, Lift Vector, Turn Rate und Radius – und warum die Corner Speed so wichtig ist.

Jedes Manöver in BFM ist im Kern dasselbe: **Lift Vector dorthin rollen, wo du hinwillst, dann ziehen.** Diese Seite erklärt die allgemeine Physik dahinter. Was VFM konkret simuliert: [Das VFM-Flugmodell](/grundlagen/physik). Begriffe: [Glossar](/grundlagen/begriffe).

## Lastvielfaches n („G“)

Das **Lastvielfache** ist Auftrieb geteilt durch Gewicht: n = L / W.

- **1 G:** Horizontalflug, der Auftrieb trägt genau dein Gewicht.
- **9 G:** neunfaches Gewicht an Auftrieb – in VFM die Grenze.
- **0 G:** kein Auftrieb, die Flugbahn ist ballistisch.

Mehr G heißt engere, schnellere Kurve, aber auch mehr induzierter Widerstand und damit Energieverlust ([Energie-Management](/grundlagen/energie-management)).

## Der Lift Vector: das zentrale Konzept

Der **Lift Vector** zeigt senkrecht aus den Flügeln Richtung Kabinendach. **Wohin er zeigt, dorthin kurvst du, wenn du ziehst.** Ziehen kannst du nur „nach oben“ relativ zum Cockpit. Jede Richtungsänderung hat deshalb zwei Schritte:

1. **Rollen:** Lift Vector auf das Ziel legen (auf den Gegner, vor ihn, über ihn, unter ihn).
2. **Ziehen:** so viel G, wie die Situation verlangt.

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

Willst du in der Horizontalkurve die Höhe halten, muss der senkrechte Anteil des Lifts genau 1 g sein: cos(Querlage) = 1 / n.

| Querlage | G für Höhe halten | „Dreh“-Anteil √(n²−1) |
|---|---|---|
| 60° | 2 G | 1,7 g |
| 75,5° | 4 G | 3,9 g |
| 83,6° | 9 G | 8,9 g |

Bei 9 G liegt der Lift Vector also fast waagrecht. Zeigt er höher, steigst du; zeigt er unter den Horizont, sinkst du, und die Schwerkraft hilft beim Drehen.

::: tip SPRICH IN LIFT VECTORS
Statt „Nase runter“ denk: „Lift Vector unter den Horizont rollen und ziehen.“ Statt „hochziehen“: „Lift Vector über den Gegner rollen und ziehen.“ So lassen sich alle Manöver beschreiben, vom [Yo-Yo](/grundlagen/offensiv/yo-yos) bis zum [Break Turn](/grundlagen/defensiv/break-turn).
:::

## Turn Rate und Radius

Für die Horizontalkurve gilt (V = wahre Geschwindigkeit, g = 9,81 m/s²):

```
Turn Rate     ω = g · √(n² − 1) / V
Turn Radius   r = V² / (g · √(n² − 1))
```

- **Bei gleicher G sinkt die Rate mit der Speed** (ω ~ 1/V): doppelt so schnell = halbe Rate.
- **Bei gleicher G wächst der Radius mit dem Quadrat der Speed** (r ~ V²): doppelt so schnell = vierfacher Radius.
- **Mehr G** verbessert beides, aber nur bis 9 G.

### Rechenbeispiel mit VFM-Zahlen

Auf Meereshöhe sind KIAS und wahre Speed praktisch gleich (1 kt = 0,514 m/s).

| Fall | Turn Rate | Radius |
|---|---|---|
| 9 G bei 337 KIAS | 29,0 °/s | ~1.120 ft |
| 9 G bei 360 KIAS | 27,1 °/s | ~1.280 ft |
| 9 G bei 500 KIAS | 19,5 °/s | ~2.470 ft |
| 5 G bei 360 KIAS | 14,9 °/s | ~2.340 ft |

Rechnung für 9 G bei 360 KIAS: V = 185 m/s, √80 = 8,94. Rate = 9,81 · 8,94 / 185 = 0,474 rad/s = **27,1 °/s**. Radius = 185² / (9,81 · 8,94) = 391 m = **1.280 ft**.

Das Spiel rechnet genauso: Die T-15 hat laut Ingame-Diagramm auf Meereshöhe (50 % Fuel) ihre Max Instant Rate von **29 °/s bei 337 KIAS** und einen Mindestradius von **1.138 ft** – genau 9 G bei Corner Speed. Das gilt für alle Jets und Bedingungen.

Was die Tabelle zeigt:

- **500 statt 360 KIAS** bei 9 G: ein Viertel weniger Rate, fast doppelter Radius.
- **5 statt 9 G** bei 360 KIAS: halbe Rate. Wer am Merge nicht zieht, verschenkt Winkel.

### KIAS vs. wahre Speed in der Höhe

Die Formeln brauchen die **wahre** Speed (TAS). In der Höhe ist die Luft dünner, die wahre Speed liegt über der angezeigten (in VFM ~12 % auf 10.000 ft, ~28 % auf 20.190 ft). Bei gleicher KIAS und 9 G drehst du in der Höhe also langsamer und weiter. Zusätzlich steigt die Corner Speed in KIAS mit der Höhe. Beides zusammen kostet alle Jets Rate: Die T-15 (50 % Fuel) kommt auf Meereshöhe auf 29 °/s, auf 20.190 ft nur noch auf 20 °/s. Details: [Die Atmosphäre in VFM](/grundlagen/physik#die-atmosphare-in-vfm).

## Corner Speed

Zwei Grenzen bestimmen, wie viel G du ziehen kannst:

1. **Lift-Limit:** Langsam erzeugt der Flügel nicht genug Auftrieb für 9 G. Die mögliche G steigt etwa mit dem Quadrat der Speed, die Rate also mit der Speed.
2. **G-Limit:** Ab einer bestimmten Speed hast du 9 G, mehr gibt es nicht. Ab hier sinkt die Rate mit 1/V.

Die **Corner Speed** ist der Schnittpunkt: die niedrigste Speed mit 9 G. Dort hast du die **höchste Instant Turn Rate und den kleinsten Radius**.

| Jet | Corner Speed (Diagramm, 10.000 ft, 50 % Fuel) |
|---|---|
| T-15 Excalibur | ~360 KIAS (24 °/s) |
| T-16 Falchion | ~409 KIAS (21 °/s) |
| T-18 Cutlass | ~385 KIAS (22 °/s) |

Mit mehr Höhe und mehr Fuel steigt die Corner Speed, mit leerem Tank liegt sie ~25 KIAS tiefer. Alle Bedingungen: [Flugzeugvergleich](/flugzeuge/vergleich).

**Warum sie wichtig ist:** Am Merge und im Break Turn willst du in kurzer Zeit maximal Winkel gewinnen – das geht nahe Corner Speed am besten. Darunter fehlen dir G, darüber wird der Radius groß. **Aber:** Bei Corner Speed und 9 G verlierst du sehr schnell Energie und kannst dort nicht bleiben. Die Speed für die Dauerkurve ist die höhere **Best Sustained Speed** – [Corner Speed vs. Best Sustained Speed](/grundlagen/energie-management#corner-speed-vs-best-sustained-speed).

## Schwerkraft in schrägen und vertikalen Kurven

In der Horizontalkurve muss ein Teil des Lifts die Schwerkraft aufheben. Schräg oder vertikal ändert sich das:

- **Lift Vector unter dem Horizont (nose-low):** Die Schwerkraft zieht mit. Du drehst **schneller** und hältst Speed (Höhe wird zu Speed).
- **Lift Vector über dem Horizont (nose-high):** Die Schwerkraft zieht dagegen. Du drehst **langsamer** und verlierst Speed (Speed wird zu Höhe).

Im Looping wirkt Richtung Kurvenmitte:

| Position | Wirkung | bei 9 G | bei 3 G |
|---|---|---|---|
| Oben (Lift Vector nach unten) | (n + 1) g | 10 g | 4 g |
| Horizontalkurve | √(n² − 1) g | 8,9 g | 2,8 g |
| Unten (Lift Vector nach oben) | (n − 1) g | 8 g | 2 g |

Bei 9 G macht die Schwerkraft rund ±10 % aus, bei 3 G – typisch, wenn du oben langsam bist – über 40 %. **Je langsamer und je weniger G, desto stärker hilft oder bremst die Schwerkraft.** Zusammen mit der Speed (oben langsam = enger) ergibt das die typische Form einer vertikalen Kurve, **„The Egg“**: oben eng, unten weit. Anwendung: [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf), [Slice Turn](/grundlagen/defensiv/slice-turn).

## Out-of-Plane-Manövrieren

Jeder Jet kurvt in seiner **Bewegungsebene** aus Flugrichtung und Lift Vector. Rollst du deinen Lift Vector **aus der Ebene des Gegners heraus** (über oder unter ihn), gewinnst du drei Werkzeuge:

- **Schwerkraft:** nose-low für Rate, nose-high, um Speed in Höhe zu parken.
- **Closure-Kontrolle:** Über ihn hinaus kurven baut Closure ab, ohne Energie zu verschenken – die Idee des [High Yo-Yo](/grundlagen/offensiv/yo-yos).
- **Schwer zu treffen:** Um dir zu folgen, muss er erst rollen, dann ziehen – die Basis von [Guns Defense](/grundlagen/defensiv/guns-defense).

Mehr zur Bewegungsebene: [Relative Geometrie](/grundlagen/geometrie#bewegungsebene-plane-of-motion).

::: info IM SPIEL PRÜFEN
- Rollrate der drei Jets – sie bestimmt, wie schnell du den Lift Vector umlegst.
:::

::: tip MERKE
- **Lift Vector platzieren, dann ziehen** – jedes Manöver ist das.
- **Rate ~ 1/V, Radius ~ V²** bei gleicher G. Zu schnell heißt: großer Kreis, langsame Nase.
- **Corner Speed** = niedrigste Speed mit 9 G = beste Instant Rate, aber hoher Energiepreis.
- **Nose-low dreht schneller, nose-high langsamer** – je langsamer du bist, desto stärker.
- **Raus aus der Ebene** gibt dir Schwerkraft, Closure-Kontrolle und macht dich schwerer zu treffen.
:::

Weiter: [Energie-Management](/grundlagen/energie-management)
