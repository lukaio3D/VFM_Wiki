# Vertikal-Kampf

> Die dritte Dimension: wie Schwerkraft deine Kurven verändert, wann sich Steigen lohnt und welcher VFM-Jet in die Vertikale gehört.

Wer nur links und rechts denkt, verschenkt die Hälfte seiner Möglichkeiten. In der Vertikalen arbeitet die Schwerkraft mal für und mal gegen dich, und Höhe wird zum Energiespeicher. Steigen vernichtet keine Energie, es wandelt Speed in Höhe um. Verloren geht Energie nur durch Widerstand. Hintergrund: [Energie-Management](/grundlagen/energie-management), Begriffe im [Glossar](/grundlagen/begriffe).

## The Egg: Kurven in der Vertikalen

Fliegst du einen Looping oder eine schräge Kurve, ist deine Bahn kein Kreis, sondern ein **Ei**: oben eng, unten weit.

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Seitenansicht eines Loopings: Die Bahn ist eiförmig, oben eng mit kleinem Radius und hoher Rate, unten weit mit großem Radius.">
<path d="M 260 270 C 380 270, 320 40, 260 40 C 200 40, 140 270, 260 270" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<polygon points="268,270 258,265 258,275" fill="var(--vp-c-brand-1)"/>
<polygon points="252,40 262,35 262,45" fill="var(--vp-c-brand-1)"/>
<line x1="460" y1="120" x2="460" y2="180" stroke="var(--vp-c-text-2)" stroke-width="1.5"/>
<polygon points="460,188 455,178 465,178" fill="var(--vp-c-text-2)"/>
<text x="470" y="156" font-size="12" fill="currentColor">g</text>
<text x="290" y="28" font-size="12" fill="currentColor">oben: langsam, Schwerkraft zieht mit</text>
<text x="290" y="44" font-size="12" fill="currentColor">→ kleiner Radius, hohe Rate</text>
<text x="330" y="246" font-size="12" fill="currentColor">unten: schnell,</text>
<text x="330" y="262" font-size="12" fill="currentColor">Schwerkraft gegen dich</text>
<text x="330" y="278" font-size="12" fill="currentColor">→ großer Radius, niedrige Rate</text>
<text x="20" y="160" font-size="12" fill="currentColor">Seitenansicht</text>
</svg>

Warum? Zwei Effekte addieren sich:

1. **Schwerkraft**: Oben zeigen dein Lift Vector und die Schwerkraft beide zum Kreismittelpunkt. Du drehst mit (n + 1) g. Unten wirken sie gegeneinander, und es bleibt nur (n − 1) g.
2. **Speed**: Oben bist du langsam, unten schnell. Der Radius wächst mit V², die Rate sinkt mit V.

::: details Rechenbeispiel (keine VFM-Messwerte)
Turn Rate ω = a / V, Radius r = V² / a, a = Beschleunigung zum Kreismittelpunkt.

- **Unten**: 450 kt wahre Speed ≈ 760 ft/s, 7 G → a = 6 g ≈ 193 ft/s² → ω ≈ 0,25 rad/s ≈ **15°/s**, r ≈ **3.000 ft**
- **Oben**: 250 kt ≈ 422 ft/s, 4 G → a = 5 g ≈ 161 ft/s² → ω ≈ 0,38 rad/s ≈ **22°/s**, r ≈ **1.100 ft**

Oben drehst du also mit weniger G deutlich schneller. Ob dein Jet bei 250 kt noch 4 G ziehen kann, hängt vom Jet ab und lässt sich im Spiel testen.
:::

**Taktisch heißt das**: Oben über den Scheitel zu ziehen ist billig und schnell. Unten herum ist teuer und weit. Wer oben am Ei ist, wenn der Gegner unten ist, gewinnt Winkel.

## Schräge Kurven (Oblique Turns)

Zwischen der flachen Kurve und dem Looping liegt die **schräge Kurve**. Dein Lift Vector zeigt dabei schräg über oder schräg unter den Horizont. Das ist dein wichtigstes Werkzeug, um die Speed zu regeln:

| Lift Vector | Wirkung | Benutze sie, wenn … |
|---|---|---|
| **schräg über dem Horizont** (Oblique up, nose-high) | Speed wird zu Höhe, die Kurve wird oben enger | du schneller bist als dein Ziel-Band (z. B. über Corner Speed) und Energie nicht an Widerstand verlieren willst |
| **waagerecht** (Level) | reine Turn Rate in der Ebene | du genau in deinem Band bist |
| **schräg unter dem Horizont** (Oblique down, [Slice](/grundlagen/defensiv/slice-turn)) | Schwerkraft hilft bei Rate und Speed, kostet Höhe | du zu langsam bist oder Speed halten musst |

Faustregel ohne Zahl: **Zu schnell → Lift Vector über den Horizont. Zu langsam → Lift Vector unter den Horizont.** So hältst du dich nahe an Corner- bzw. Best-Sustained-Speed, ohne Energie unnötig an Widerstand zu verlieren. Nebeneffekt: Ein Gegner, der in der Ebene bleibt, muss dich jetzt in 3D verfolgen.

## Pitch-back

Der **Pitch-back** ist der klassische vertikale erste Zug am [Merge](/grundlagen/neutral/der-merge):

1. Nach dem Pass Lift Vector nach oben und ziehen, steil nach oben.
2. Den Gegner über die Schulter im Blick behalten (Tally).
3. Steil oben so rollen, dass dein **Lift Vector auf den Gegner** zeigt, und über den Scheitel auf ihn ziehen.

**Vorteil**: Du drehst oben im engen Teil des Eis um und hast Höhe über dem Gegner, also Energie und Wahlfreiheit.
**Risiko**: Kommst du mit zu wenig Speed rein, hängst du oben langsam vor seiner Nase. Ein Gegner, der in der Ebene schnell herumkommt, kann dann von unten mit Lead auf dich ziehen.

## Zoom Climb

Ein **Zoom** ist ein steiler Steigflug, bei dem du Speed in Höhe umwandelst. Wie hoch du kommst, hängt von deiner **Energie** beim Einstieg und von deiner Überschussleistung **Ps** ab.

::: details Rechnung: Wie viel Höhe steckt in Speed?
Ohne Schub und Widerstand gilt Δh = (V₁² − V₂²) / (2 g).

Von 450 kt wahrer Speed (≈ 760 ft/s) auf 200 kt (≈ 338 ft/s):
Δh = (577.600 − 114.244) / 64,4 ≈ **7.200 ft**

Schub verlängert den Zoom, Widerstand verkürzt ihn. Wer bei gleicher Startspeed mehr Überschussleistung (Ps = V·(T−D)/W) hat, steigt höher oder bleibt oben schneller.
:::

**Wofür**:
- Überschüssige Speed speichern, statt sie in einer flachen Kurve an Widerstand zu verlieren.
- Höhe über einem tieferen, langsameren Gegner gewinnen und von oben angreifen.
- Separation in der Vertikalen, wenn der Gegner dir nicht folgen kann.

**Wann nicht**: Wenn du langsam bist oder der Gegner mehr Energie hat. Dann bist du oben das stehende Ziel. Mit einem Gegner hinter dir in Waffenreichweite ist ein Zoom ein Geschenk an ihn.

## Climbing Spiral (steigende Spirale)

Bei der **Climbing Spiral** steigen beide Jets in einer Spirale umeinander. Das ist ein reiner **Energie-Wettkampf**: Es gewinnt, wer die höhere **Überschussleistung Ps** hat. Er steigt länger und bleibt dabei schneller. Der andere wird zuerst zu langsam, fällt nach unten heraus und bekommt den Gegner von oben.

- Merkst du, dass er über dir bleibt oder dich überholt, steig **früh** aus: Unload (Nase an oder leicht unter den Horizont), Speed aufbauen, Ebene wechseln. Steig nicht erst aus, wenn du oben keine Kontrolle mehr hast.
- Geh nur in eine Spirale, wenn du sicher bist, dass dein Jet mehr Schub hat. In VFM ist das fast immer nur die T-15.

::: tip Egg ≠ Spirale
„The Egg“ beschreibt die **Form** einer Kurve in der Vertikalen. Die Climbing Spiral ist ein **Energie-Duell** zweier Jets. Beides wird oft verwechselt.
:::

## Wann vertikal in VFM

| Jet | Vertikal? | Warum |
|---|---|---|
| **T-15 Excalibur** | **Ja, das ist deine Stärke.** Pitch-back, Zoom, Spirale, Angriffe von oben. | Stärkster Schub, höchste Top-Speed (Entwickler). Behält laut Daten auch auf ~21.000 ft ein flaches Sustained-Plateau (~12°/s bei 400–600 KIAS), während die anderen abfallen. Gegen die T-16 ist die Vertikale dein Weg aus ihrem Speedband. |
| **T-16 Falchion** | **Gegen die T-15 vermeiden.** Nur nose-low und kurze schräge Kurven. | Wahrscheinlich schwächster Vertikal-Jet (niedrigster Schub-Balken). Jeder Steigflug kostet dich dein Band von 420–500 KIAS. Dein Vorsprung ist in Bodennähe am größten. |
| **T-18 Cutlass** | **Kurze Zooms**, keine langen Steigflüge oder Spiralen gegen die T-15 | Über ~480 KIAS verliert die T-18 Energie durch Widerstand am stärksten. Ein kurzer Zoom speichert diese Speed als Höhe, statt sie zu verlieren (Folgerung). Oben über den Scheitel ziehen und dann wieder tief und langsam kämpfen. |

Höhe allgemein: T-16 und T-18 kämpfen lieber tief, die T-15 profitiert relativ von Höhe. Im Training gilt ein Hard Deck von **2.000 ft über Grund**. Ein echtes Hard Deck im Spiel ist nicht bekannt, der Boden aber schon.

## Speed oben am Scheitel

Wie langsam du oben werden darfst, ohne die Kontrolle zu verlieren, ist für VFM **nicht dokumentiert**. Die Ingame-Diagramme beginnen erst bei ~170–200 KIAS. Pauschale Werte wie „nie unter 150 kt“ stammen aus anderen Sims und gelten hier nicht automatisch.

::: info IM SPIEL PRÜFEN
Free Flight, gleiche Höhe (z. B. 10.000 ft) und gleicher Treibstoff für alle Jets:
- Ab welcher **Einstiegsspeed** kommst du mit max G noch kontrolliert über den Scheitel eines Loopings? Wie schnell bist du oben?
- Wie verhält sich der Jet oben mit und ohne **AoA-Override**? Bekommst du die Nase herum, und wie viel Speed kostet es?
- Wie hoch kommst du im Zoom von 450 KIAS bis 200 KIAS (60° Steigwinkel)? Vergleiche T-15, T-16 und T-18.
:::

Trag deine Werte hier ein und vergleiche sie:

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| Min. Einstiegsspeed Looping (max G) | ? | ? | ? |
| Speed oben am Scheitel | ? | ? | ? |
| Höhengewinn Zoom 450 → 200 KIAS | ? | ? | ? |

Die Übungen dazu stehen im [Trainingsplan](/grundlagen/uebungen).

::: tip MERKE
- The Egg: Oben ist die Kurve eng und schnell, weil die Schwerkraft mitzieht. Unten ist sie weit und langsam.
- Schräge Kurven regeln die Speed: zu schnell → Lift Vector über den Horizont, zu langsam → darunter.
- Zoom und Climbing Spiral sind Energie-Wettkämpfe. Es gewinnt, wer mehr Ps hat.
- In VFM: T-15 geht in die Vertikale, T-16 bleibt tief und schnell, T-18 zoomt nur kurz.
- Grenzwerte am Scheitel selbst testen, statt fremde Faustzahlen zu glauben.
:::

Weiter: [Trainingsplan](/grundlagen/uebungen)
