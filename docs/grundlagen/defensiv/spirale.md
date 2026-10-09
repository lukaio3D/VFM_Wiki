# Defensive Spirale

> Last-Ditch: Nase fast senkrecht nach unten, geladen, langsam. Entweder er überschießt, oder er muss zuerst abfangen.

Die defensive Spirale ist das Manöver für den Moment, in dem fast nichts mehr geht: Du bist **langsam**, der Angreifer **klebt hinter dir**, ein Break bringt nichts mehr, weil du nicht mehr genug Speed für Rate hast. Aber du hast **viel Höhe**. Die Spirale nutzt diese Höhe, um den Kampf in eine Richtung zu verlagern, in der seine höhere Speed sein Problem wird statt deins.

Sie ist kein sanfter Sinkflug mit 3–4 G und 45° Querlage, in dem man "Zeit gewinnt". So eine Kurve ist für einen Angreifer ein bequemer Tracking-Schuss.

## Das Prinzip

- Du rollst so, dass dein Lift Vector weit unter dem Horizont liegt, und ziehst die Nase **steil nach unten, nahezu senkrecht**. Dann spiralst du unter Last um eine fast senkrechte Achse nach unten.
- Du hältst dich **so langsam wie möglich**: Gas auf Idle, Speedbrake falls vorhanden. Langsam heißt kleiner Radius (r wächst mit V², siehe [Kurvenphysik](/grundlagen/kurvenphysik)).
- Der Angreifer kommt mit mehr Speed. Im steilen Sturzflug beschleunigen beide. Um in deiner engen Spirale zu bleiben, muss er genauso langsam werden wie du. Schafft er das nicht, wird sein Radius größer als deiner: Er **überschießt** (zuerst über deine Flugbahn, siehe [Overshoot](/grundlagen/offensiv/overshoot)).
- Bleibt er trotzdem dran, wird es ein Abfangduell: Wer schneller ist, braucht mehr Höhe, um aus dem Sturz abzufangen. **Er muss zuerst abfangen** oder riskiert den Boden.

### Wie viel Höhe kostet das Abfangen?

Grobe Abschätzung für das Abfangen aus dem senkrechten Sturz in den Horizontalflug: Der Höhenverlust ist etwa der Radius r ≈ V²/(g·(n−1)). Mit 9 G:

| Speed im Sturz | V | r ≈ V²/(32,2 · 8) |
|---|---|---|
| 300 kt | ~506 ft/s | ~1.000 ft |
| 400 kt | ~675 ft/s | ~1.770 ft |

Grobe Rechnung: Ohne Speedzunahme beim Abfangen und ohne Reaktionszeit. In echt brauchst du mehr. Aber das Verhältnis zeigt den Kern: **Wer 100 kt schneller ist, braucht deutlich mehr Höhe.** Dazu kommt: Der Angreifer sitzt hinter dir und muss dich gleichzeitig beobachten.

## Wann

- Du bist **langsam** und hast keine Speed mehr für einen wirksamen Break.
- Der Angreifer ist **nah hinter dir**, mit mehr Speed als du.
- Du hast **viel Höhe**. Mehrere tausend Fuß über dem Hard Deck sind das Minimum, und die Abfanghöhe von oben musst du einplanen.
- Alternativen ([Break](/grundlagen/defensiv/break-turn), [Slice](/grundlagen/defensiv/slice-turn), [Guns Defense](/grundlagen/defensiv/guns-defense)) helfen nicht mehr.

## Wann nicht

- **Wenig Höhe.** Dann bringt die Spirale dich in den Boden, nicht ihn.
- **Er ist weit hinter dir oder hoch über dir.** Dann kann er die Spirale von außen beobachten und dich am Boden erwarten.
- **Gegen eine Rakete.** Die Spirale ist keine Raketenabwehr. Dafür: [Break + Flares + Idle](/grundlagen/defensiv/break-turn#raketenabwehr-kurzfassung).
- **Mehrere Gegner.** Der zweite wartet einfach, bis du unten abfängst.

## Ausführung

1. **Abfanghöhe festlegen, bevor du anfängst.** Unter dieser Höhe fängst du ab, egal was er tut. Trainings-Empfehlung: Hard Deck 2.000 ft über Grund plus Abfangreserve.
2. **Gas auf Idle**, Speedbrake falls vorhanden.
3. **Rollen und ziehen**, bis die Nase steil nach unten zeigt. Die Spirale läuft eng um eine fast senkrechte Achse.
4. **Geladen bleiben.** Last halten, damit der Radius klein bleibt. Kein Rhythmus, der ihm eine ruhige Lösung gibt. Ist er in Kanonenlösung: Ebene wechseln wie bei der [Guns Defense](/grundlagen/defensiv/guns-defense).
5. **Ihn beobachten.**
   - **Er überschießt:** Sofort umkehren, Lift Vector auf ihn, abfangen in seine Richtung. Er ist jetzt schnell, tief und vor dir.
   - **Er fängt ab und geht hoch:** Er parkt Speed in Höhe. Du fängst ebenfalls ab und hast den Kampf neutralisiert, aber mit Energienachteil. Jetzt ist [Separation](/grundlagen/defensiv/separation) oft die richtige Wahl.
   - **Er bleibt drin:** Spätestens an deiner Abfanghöhe abfangen. Er ist schneller und muss früher abfangen als du, sonst geht er in den Boden.

::: danger BODEN
Der Boden schießt nicht vorbei. Abfangen heißt: genug Höhe für den Bogen aus dem Sturz. Auf Mountains und anderen Maps mit Gelände zählt die Höhe über Grund, nicht über Meer.
:::

## Typische Fehler

- **Zu flach.** Eine 45°-Spirale mit 3–4 G ist keine defensive Spirale, sondern eine vorhersehbare Kurve nach unten.
- **Zu schnell.** Mit Leistung oder ohne Last baust du Speed auf, dein Radius wächst, und sein Vorteil verschwindet.
- **Ohne Abfanghöhe.** Wer erst unten überlegt, wann er abfängt, hat schon verloren.
- **Zu früh.** Wer noch Speed für einen Break hat, verschenkt mit der Spirale Höhe ohne Not.
- **Er bleibt oben und du merkst es nicht.** Dann spiralst du allein nach unten, und er wartet. Sicht halten.

## VFM-Hinweise

- **T-18 Cutlass:** Der Entwickler positioniert sie als High-AoA-/Low-Speed-Jet. Wenn sich das im Spiel bestätigt, ist sie in einer langsamen, engen Spirale am stärksten. Unterhalb ~170 KIAS gibt es keine Daten, das ist eine Hypothese.
- **T-16 Falchion:** Unter ~380 KIAS ist sie laut Daten der schwächste Jet. Eine langsame Spirale ist ihr ungünstigstes Terrain. Wenn eine T-16 hier landet, ist meist vorher etwas schiefgelaufen.
- **T-15 Excalibur:** Mit dem kleinsten Radius im Diagrammbereich kann sie eng spiralen, ist aber schwer und beschleunigt im Sturz entsprechend.

::: info IM SPIEL PRÜFEN
- Ob VFM eine Speedbrake hat und wie sie belegt ist. Bisher gibt es keine Quelle dafür.
- Wie langsam du mit Idle in steiler Spirale bleiben kannst, ohne die Nose Authority zu verlieren.
- Wie die Höhe über Grund angezeigt wird (siehe [HUD](/avionik/hud)).
:::

::: tip MERKE
- Last-Ditch: langsam, Angreifer nah, viel Höhe, sonst nichts mehr übrig.
- Steil nose-low, nahezu senkrecht, geladen, Idle, so langsam wie möglich.
- Ziel: Er überschießt oder muss zuerst abfangen. Der Schnellere braucht mehr Höhe.
- Abfanghöhe vorher festlegen. Der Boden gewinnt immer.
:::

Weiter: [Separation](/grundlagen/defensiv/separation)
