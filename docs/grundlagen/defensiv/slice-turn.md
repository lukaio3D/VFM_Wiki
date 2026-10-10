# Slice Turn

> Die harte Kurve mit Nase unter dem Horizont: überbankt, nahe max G, die Schwerkraft dreht mit und hält deine Speed.

Beim Slice (Nose-low Turn) legst du den Lift Vector unter den Horizont und tauschst Höhe gegen Turn Rate und Speed. Er ist eine **harte** Kurve, kein gemütlicher Sinkflug mit wenig G. Und er bringt keine Energie: Die Gesamtenergie sinkt, du verlierst nur Höhe statt Speed.

## Das Prinzip

In einer Horizontalkurve muss ein Teil des Auftriebs das Gewicht tragen, nur der Rest dreht dich. Liegt der Lift Vector **unter** dem Horizont, zieht die Schwerkraft in dieselbe Richtung und hilft beim Drehen.

<svg viewBox="0 0 520 220" width="100%" style="max-width:520px" role="img" aria-label="Blick von hinten auf zwei Flugzeuge. Links Horizontalkurve mit etwa 75 Grad Querlage, Lift Vector knapp über dem Horizont. Rechts Slice mit etwa 120 Grad Querlage, Lift Vector unter dem Horizont, gleiche Richtung wie ein Teil der Schwerkraft.">
<defs>
<marker id="slA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--vp-c-brand-1)"/></marker>
<marker id="slG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker>
</defs>
<text x="130" y="22" font-size="12" fill="currentColor" text-anchor="middle">Horizontalkurve (~75° Querlage)</text>
<text x="390" y="22" font-size="12" fill="currentColor" text-anchor="middle">Slice (~120° Querlage, überbankt)</text>
<line x1="30" y1="110" x2="230" y2="110" stroke="currentColor" stroke-dasharray="4 4" opacity="0.6"/>
<line x1="290" y1="110" x2="490" y2="110" stroke="currentColor" stroke-dasharray="4 4" opacity="0.6"/>
<text x="30" y="104" font-size="12" fill="currentColor">Horizont</text>
<text x="290" y="104" font-size="12" fill="currentColor">Horizont</text>
<line x1="118" y1="67" x2="142" y2="153" stroke="currentColor" stroke-width="3"/>
<circle cx="130" cy="110" r="5" fill="currentColor"/>
<line x1="130" y1="110" x2="196" y2="92" style="stroke:var(--vp-c-brand-1)" stroke-width="2" marker-end="url(#slA)"/>
<text x="168" y="80" font-size="12" fill="currentColor">Lift Vector</text>
<line x1="60" y1="125" x2="60" y2="168" stroke="currentColor" stroke-width="1.5" marker-end="url(#slG)"/>
<text x="66" y="160" font-size="12" fill="currentColor">g</text>
<line x1="413" y1="71" x2="367" y2="149" stroke="currentColor" stroke-width="3"/>
<circle cx="390" cy="110" r="5" fill="currentColor"/>
<line x1="390" y1="110" x2="449" y2="144" style="stroke:var(--vp-c-brand-1)" stroke-width="2" marker-end="url(#slA)"/>
<text x="430" y="168" font-size="12" fill="currentColor">Lift Vector</text>
<line x1="320" y1="125" x2="320" y2="168" stroke="currentColor" stroke-width="1.5" marker-end="url(#slG)"/>
<text x="326" y="160" font-size="12" fill="currentColor">g</text>
<text x="130" y="200" font-size="12" fill="currentColor" text-anchor="middle">Auftrieb trägt Gewicht und dreht</text>
<text x="390" y="200" font-size="12" fill="currentColor" text-anchor="middle">Schwerkraft dreht mit, Nase fällt</text>
</svg>

*Blick von hinten. Der dicke Strich sind die Tragflächen, der Pfeil zeigt aus dem Kabinendach (Lift Vector). Rechts liegt der Lift Vector unter dem Horizont.*

**Rate:** Mit dem Lift Vector um δ unter dem Horizont wächst die Querbeschleunigung von g·√(n²−1) auf g·√(n² + 2n·sin δ + 1). Bei δ = 30° bringt das bei 9 G ~7 % mehr, bei 5 G ~14 %. Ein Teil davon lässt nur die Nase sinken – kein Wundermittel, aber spürbar, und umso mehr, je weniger G du ziehen kannst.

**Speed:** Rechnung ohne Schub und Widerstand: Aus 400 kt wahrer Fahrt bringen 3.000 ft Höhenverlust nur rund **+77 kt**. Mit Schub ist es mehr, unter hoher G-Last weniger. Höhe ist ein begrenzter Vorrat.

## Wann

- Du musst **hart drehen** (Break, Defensivkurve), willst **nicht unter Corner Speed fallen** und hast **Höhe**.
- Der Angreifer ist **höher**: Du nutzt die Schwerkraft, er muss von oben nachkommen.
- Du willst nach einem Break **Speed zurückholen**, ohne die Kurve aufzugeben.
- Offensiv als nose-low Umkehr (verwandt mit dem [Low Yo-Yo](/grundlagen/offensiv/yo-yos)).

## Wann nicht

- **Wenig Höhe** – am [Hard Deck](/grundlagen/golden-rules#hard-deck-2-000-ft) ist kein Platz.
- **Der Gegner ist tief unter dir und schneller.** Dann fliegst du ihm in die Arme.
- **Du bist deutlich über Corner Speed.** Dann bist du G-limitiert, mehr Speed vergrößert nur den Radius. Lift Vector eher auf oder über den Horizont.

## Ausführung

1. **Überbanken**, bis der Lift Vector unter dem Horizont liegt: leicht darunter für einen flachen Slice, deutlich darunter für mehr Rate und Speed.
2. **Hart ziehen**, nahe max G bzw. AoA-Limit. Ein Slice mit 2–4 G ist ein Sinkflug, in dem er dich in Ruhe abholt.
3. **Speed steuern:** nahe Corner Speed bleiben. Zu schnell: Lift Vector höher. Zu langsam: tiefer.
4. **Sicht halten:** Kommt er in Lösung, [jinken](/grundlagen/defensiv/guns-defense). Fällt er zurück, Energie halten.
5. **Rechtzeitig beenden**, mit Höhenreserve. Danach Defensivkurve, Reversal oder [Separation](/grundlagen/defensiv/separation).

## Typische Fehler

- **Zu flach und zu sanft.** Der Slice ist eine harte Kurve.
- **Glauben, der Slice bringe Energie.** Die Gesamtenergie sinkt immer.
- **Zu lange.** Am Ende bist du tief, schnell, G-limitiert und ohne Höhe für den nächsten Zug.
- **Vorhersehbar.** Einen langen, gleichmäßigen Slice schneidet ein Angreifer mit Höhe ab.
- **Gelände.** Auf Mountains zählt die Höhe über Grund, nicht über Meer.

## Die Jets

- **[T-16](/flugzeuge/t16):** Höchste Corner Speed, stärkste sustained Kurve bei ~420–500 KIAS. Für sie ist der Slice das natürliche Werkzeug, um im Band zu bleiben.
- **[T-18](/flugzeuge/t18):** Bricht ab ~510 KIAS (≈ Mach 0,9) ein. Lange, tiefe Slices, die sie dorthin beschleunigen, verschenken ihren Vorteil.
- **[T-15](/flugzeuge/t15):** Niedrigste Corner Speed, braucht den Slice weniger. Mit ihrem Schubüberschuss holt sie die Höhe danach am schnellsten zurück.

::: info IM SPIEL PRÜFEN
- Denselben 180°-Turn einmal horizontal und einmal als Slice mit gleicher Last fliegen und im Replay Zeit, Speed und Höhenverlust vergleichen.
:::

::: tip MERKE
- Slice = überbankt, Lift Vector unter dem Horizont, nahe max G. Eine harte Kurve, kein sanfter Sinkflug.
- Die Schwerkraft dreht mit und bremst den Speedverlust. Die Gesamtenergie sinkt trotzdem.
- 3.000 ft bringen aus der Schwerkraft allein nur rund +77 kt.
- Ziel ist Speed nahe Corner, nicht maximale Speed. Rechtzeitig mit Höhenreserve beenden.
:::

Weiter: [Defensive Spirale](/grundlagen/defensiv/spirale)
