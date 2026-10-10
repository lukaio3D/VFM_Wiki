# Slice Turn

> Die harte Kurve mit Nase unter dem Horizont: überbankt, nahe max G, die Schwerkraft dreht mit und hält deine Speed.

Der Slice (Nose-low Turn) ist eine **harte** Kurve, bei der du den Lift Vector unter den Horizont legst. Du tauschst Höhe gegen Turn Rate und Speed. Er ist kein gemütlicher Messerflug mit wenig G, und er bringt dir auch keine Energie: Deine Gesamtenergie sinkt, du wandelst nur Höhe in Speed um, statt die Speed in der Kurve zu verlieren.

## Das Prinzip

In einer Horizontalkurve muss ein Teil deines Auftriebs das Gewicht tragen. Nur der Rest dreht dich. Legst du den Lift Vector **unter** den Horizont, zieht die Schwerkraft in dieselbe Richtung wie dein Auftrieb: Sie hilft beim Drehen, statt dagegen zu arbeiten.

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

### Wie viel bringt das?

**Turn Rate:** Die Turn Rate ist die Beschleunigung quer zur Flugbahn geteilt durch V. In der Horizontalkurve ist diese Beschleunigung bei gleicher Last n genau g·√(n²−1). Im Slice, mit dem Lift Vector um den Winkel δ unter dem Horizont und zunächst waagerechter Flugbahn, addieren sich n·g entlang des Lift Vectors und 1 g Schwerkraft nach unten zu g·√(n² + 2n·sin δ + 1). Beispiel mit δ = 30°:

| Last | Horizontalkurve | Slice (δ = 30°) | Gewinn |
|---|---|---|---|
| 9 G | √80 ≈ 8,9 g | √91 ≈ 9,5 g | ~7 % |
| 5 G | √24 ≈ 4,9 g | √31 ≈ 5,6 g | ~14 % |

Ein Teil dieser Drehung lässt die Nase sinken, statt nur die Richtung zu ändern. Kein Wundermittel, aber ein spürbarer Vorteil, und er wächst, je weniger G du ziehen kannst.

**Speed:** Höhe wird zu Speed. Rechnung ohne Schub und Widerstand, mit wahrer Fluggeschwindigkeit: 400 kt ≈ 675 ft/s. 3.000 ft Höhenverlust bringen 2·g·h = 2 · 32,2 · 3.000 ≈ 193.200 ft²/s². V² = 455.800 + 193.200 = 649.000, also V ≈ 806 ft/s ≈ 477 kt. **3.000 ft Höhe ergeben aus der Schwerkraft allein nur rund +77 kt.** Mit Schub ist es mehr, mit hoher G-Last (Widerstand) weniger. Höhe ist also ein begrenzter Vorrat, kein Tresor ohne Boden.

## Wann

- Du musst **hart drehen** (Break, Defensivkurve), willst dabei aber **nicht unter Corner Speed fallen** und hast **Höhe** unter dir.
- Der Angreifer ist **höher** als du: Mit dem Slice nutzt du die Schwerkraft für Rate, während er von oben nachkommen muss.
- Du willst nach einem Break **Speed zurückholen**, ohne die Kurve aufzugeben.
- Offensiv: Als nose-low Umkehr, wenn du schnell die Richtung wechseln und dabei Speed halten willst (verwandt mit dem [Low Yo-Yo](/grundlagen/offensiv/yo-yos)).

## Wann nicht

- **Wenig Höhe.** Unter dem Trainings-Hard-Deck (Empfehlung: 2.000 ft über Grund, siehe [Energie-Management](/grundlagen/energie-management)) ist kein Platz.
- **Der Gegner ist tief unter dir und schneller.** Dann fliegst du ihm in die Arme.
- **Du bist schon deutlich über Corner Speed.** Dann bist du G-limitiert, und mehr Speed macht deinen Radius größer (r wächst mit V²). Ein Slice, der dich noch schneller macht, verschlechtert die Kurve. Hier eher Lift Vector auf oder über den Horizont.

## Ausführung

1. **Überbanken.** Roll über 90° Querlage hinaus, bis der Lift Vector unter dem Horizont liegt. Wie weit, hängt davon ab, wie viel Höhe du opfern willst: leicht unter dem Horizont für einen flachen Slice, deutlich darunter für mehr Rate und Speed.
2. **Hart ziehen**, nahe max G bzw. nahe am AoA-Limit. Ein Slice mit 2–4 G ist keine Defensivkurve, sondern ein Sinkflug, in dem der Angreifer dich in Ruhe abholt.
3. **Speed beobachten.** Ziel ist, nahe Corner Speed zu bleiben. Wirst du deutlich schneller: Lift Vector höher legen. Wirst du langsamer: tiefer legen.
4. **Sicht auf den Angreifer halten** und reagieren: Kommt er in Lösung, [jinken](/grundlagen/defensiv/guns-defense). Fällt er zurück, Energie halten.
5. **Rechtzeitig beenden**, mit einer klaren Höhenreserve. Danach: Defensivkurve, Reversal oder [Separation](/grundlagen/defensiv/separation).

## Typische Fehler

- **Zu flach und zu sanft.** Messerflug mit wenig G und Nase knapp unter dem Horizont ist keine Defensive. Der Slice ist eine harte Kurve.
- **Glauben, der Slice bringe Energie.** Die Gesamtenergie sinkt immer. Du parkst nur nichts mehr in der Höhe.
- **Zu lange.** Erst ist der Slice dein Freund, dann bist du tief, schnell, G-limitiert und hast keine Höhe mehr für den nächsten Zug.
- **Vorhersehbar bleiben.** Ein langer, gleichmäßiger Slice ist leicht vorauszuberechnen. Ein Angreifer mit Höhe kann ihn abschneiden.
- **Gelände.** Auf Mountains und anderen Maps mit Höhenunterschieden ist "Höhe über Grund" nicht "Höhe über Meer".

## VFM: die Jets im Slice

Daten Stand Okt 2026, siehe [Flugzeugvergleich](/flugzeuge/vergleich):

- **T-16 Falchion:** Höchste Corner Speed (~409–421 KIAS) und stärkste sustained Kurve bei ~420–500 KIAS. Für sie ist der Slice das natürliche Werkzeug, um in diesem Band zu bleiben, statt in der Kurve unter ~400 KIAS zu fallen.
- **T-18 Cutlass:** Ab ~480 KIAS steigt ihr Widerstand stark, die sustained Rate bricht ein. Lange, tiefe Slices, die sie weit über diesen Bereich beschleunigen, verschenken ihren Vorteil.
- **T-15 Excalibur:** Niedrigste Corner Speed (~360–385 KIAS). Sie braucht den Slice weniger, um Speed zu halten, kann aber mit ihrem Schub nach einem Slice Höhe am schnellsten zurückholen.

::: info IM SPIEL PRÜFEN
- Wie die Höhe im HUD angezeigt wird und ob es eine Radarhöhe (Höhe über Grund) gibt. Siehe [HUD](/avionik/hud).
- Fliege im Free Flight denselben 180°-Turn einmal horizontal und einmal als Slice mit gleicher Last. Vergleiche im Replay Zeit, Speed und Höhenverlust.
:::

::: tip MERKE
- Slice = überbankt, Lift Vector unter dem Horizont, nahe max G. Eine harte Kurve, kein sanfter Sinkflug.
- Die Schwerkraft dreht mit und bremst den Speedverlust. Die Gesamtenergie sinkt trotzdem.
- 3.000 ft bringen aus der Schwerkraft allein nur rund +77 kt.
- Ziel ist Speed nahe Corner, nicht maximale Speed. Rechtzeitig mit Höhenreserve beenden.
:::

Weiter: [Defensive Spirale](/grundlagen/defensiv/spirale)
