# Scissors

> Zwei Jets weben langsam umeinander, und wer weniger vorwärts kommt, landet hinten. Erkenne Scissors früh und entscheide bewusst, ob dein Jet sie gewinnt.

**Scissors** (Schere) sind eine **neutrale** Situation: Beide Jets sind nah beieinander, keiner hat eine Schusslösung, und beide versuchen, hinter den anderen zu kommen. Sie entstehen typischerweise, wenn

- ein Angreifer mit zu viel Closure oder zu hohem Aspect Angle **überschießt** ([Overshoot](/grundlagen/offensiv/overshoot)) und der Verteidiger sofort umkehrt,
- ein [One-Circle](/grundlagen/neutral/one-two-circle) immer langsamer wird und keiner den Radius-Kampf klar gewinnt.

Das Grundprinzip beider Formen: Ihr fliegt grob in dieselbe Richtung. Wer seine **Vorwärtsbewegung** schneller abbaut, fällt hinter den anderen. Dann ist der andere vorn, also das Ziel.

## Flat Scissors

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Draufsicht Flat Scissors: Zwei Jets weben gegenläufig hin und her, kreuzen sich immer wieder und kehren dabei jeweils um. Gesamtrichtung nach oben.">
<path d="M 260 290 C 340 270, 340 230, 260 210 C 180 190, 180 150, 260 130 C 340 110, 340 70, 260 50" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<path d="M 260 290 C 180 270, 180 230, 260 210 C 340 190, 340 150, 260 130 C 180 110, 180 70, 260 50" fill="none" stroke="var(--vp-c-danger-1)" stroke-width="2.5"/>
<polygon points="320,242 315,252 325,252" fill="var(--vp-c-brand-1)"/>
<polygon points="200,162 195,172 205,172" fill="var(--vp-c-brand-1)"/>
<polygon points="320,82 315,92 325,92" fill="var(--vp-c-brand-1)"/>
<polygon points="200,242 195,252 205,252" fill="var(--vp-c-danger-1)"/>
<polygon points="320,162 315,172 325,172" fill="var(--vp-c-danger-1)"/>
<polygon points="200,82 195,92 205,92" fill="var(--vp-c-danger-1)"/>
<line x1="410" y1="270" x2="410" y2="60" stroke="var(--vp-c-text-2)" stroke-width="1.5" stroke-dasharray="4 4"/>
<polygon points="410,52 405,62 415,62" fill="var(--vp-c-text-2)"/>
<text x="420" y="170" font-size="12" fill="currentColor">gemeinsame</text>
<text x="420" y="186" font-size="12" fill="currentColor">Richtung</text>
<text x="336" y="280" font-size="12" fill="currentColor">Du</text>
<text x="146" y="280" font-size="12" fill="currentColor">Bandit</text>
<text x="20" y="206" font-size="12" fill="currentColor">Kreuzen und</text>
<text x="20" y="222" font-size="12" fill="currentColor">Umkehr zueinander</text>
<line x1="130" y1="214" x2="250" y2="210" stroke="var(--vp-c-text-2)" stroke-width="1"/>
</svg>

### So erkennst du sie

- Ihr seid nah beieinander, fast nebeneinander oder knapp versetzt, mit hohem Aspect Angle und kaum Closure.
- Ihr kreuzt **immer wieder** die Flugbahn des anderen. Nach jedem Kreuzen kehrt jeder um und dreht wieder zum anderen hin.
- Die Nasen bleiben ungefähr am Horizont, und beide werden **langsamer**.

### Wer gewinnt

1. **Wer schneller verlangsamt**: Gas auf Idle, hoher AoA. Jeder Knoten weniger heißt weniger Vorwärtsbewegung.
2. **Wer dabei Kontrolle und Rollrate behält**: Wer zu langsam wird, kann nicht mehr schnell genug umkehren und bekommt die Nase nicht für den Schuss herum.
3. **Wer die Umkehr richtig timet**: Kehr um, wenn er dich gerade kreuzt. Kehrst du zu früh um, schiebst du dich vor ihn. Zu spät, und er gewinnt Winkel.

### Ausführung

- Bei jedem Kreuzen: rollen, bis dein **Lift Vector** auf ihn zeigt, und ziehen.
- Gas zurück, AoA hoch, aber nur so weit, dass dein Jet noch rollt und reagiert.
- Behalte ihn im Blick (Tally). Wer in der Schere den Gegner verliert, verliert die Schere.
- Sobald er vor dir ist: Nase auf ihn, Guns. Bleibt er in einer Linie, ist das ein [Tracking Shot](/grundlagen/offensiv/schussloesung). Kreuzt er, ist es ein Snapshot.

::: warning AoA-Override
Mit dem AoA-Override („Cobra-Button“) bekommst du die Nase über das AoA-Limit hinaus sofort herum. Das kostet extrem viel Energie. In einer Flat Scissors kann ein Override dir den entscheidenden Schuss geben oder dich so langsam machen, dass du danach wehrlos bist. Setz ihn nur ein, wenn der Schuss danach sicher ist.
:::

## Rolling Scissors

Bei der **Rolling Scissors** bewegen sich beide Jets wie in Fassrollen umeinander. Ist einer oben, ist der andere unten. Ihr kreuzt euch oben und unten, und jeder nutzt die Vertikale, um Vorwärtsbewegung in Höhe umzusetzen.

### So erkennst du sie

- Typisch nach einem Overshoot mit höherer Speed: Der Verteidiger zieht nach oben aus der Ebene, der Angreifer folgt nach oben.
- Ihr rollt beide um eine gemeinsame, ungefähr vorwärts zeigende Achse.
- Speed und Höhe tauschen sich ständig: oben langsam, unten schnell.

### Wer gewinnt

- **Wer die Nase schneller über oben bzw. durch unten bringt.** Oben hilft die Schwerkraft beim Herumziehen.
- **Energie spielt mit**: Wer mehr Schub hat, kann oben langsamer und höher werden, ohne die Kontrolle zu verlieren, und baut dabei Vorwärtsbewegung ab.
- **Wer oben ist, hat die Wahl**: Von oben kannst du auf ihn herunterziehen. Wer unten mit wenig Energie ist, kann nur reagieren.

### Ausführung

- Geht er hoch, geh mit hoch. Lässt du ihn allein steigen, kommt er von oben.
- Oben: Lift Vector über den Kabinenhimmel auf ihn rollen und die Nase herunterziehen.
- Schub so einsetzen, dass du oben noch Kontrolle hast, aber nicht nach vorn an ihm vorbeischießt.

## Vermeiden und Aussteigen

Aus einer Schere kommst du schwer wieder heraus. Am besten verhinderst du sie:

- **Als Angreifer**: Closure kontrollieren, nicht in einen Overshoot fliegen. Werkzeuge sind [High Yo-Yo](/grundlagen/offensiv/yo-yos), [Lag Roll](/grundlagen/offensiv/lag-roll) und eine Lag-Verfolgungskurve ([Verfolgungskurven](/grundlagen/verfolgungskurven)).
- **Als Verteidiger**: Der Gegner überschießt, und du willst ihn vor dich zwingen? Dann prüf vorher, ob dein Jet die Schere gewinnt. Wenn nicht, nutze den Overshoot lieber, um Abstand und Speed zu gewinnen.

Wenn du schon drin bist und verlierst:

| Ausweg | Wann | Risiko |
|---|---|---|
| **Flat → Rolling** (in die Vertikale wechseln) | Du hast mehr Schub/Energie als er | Bist du oben langsamer als gedacht, hängst du vor seiner Nase |
| **Rolling → Flat** (in der Ebene bleiben, langsam werden) | Du bist der bessere Low-Speed-Jet | Wer zu langsam wird, verliert die Kontrolle |
| **Separation** (unload, beschleunigen, weg) | Nur mit deutlich mehr Speed und wenn seine Nase gerade von dir weg zeigt | Langsam und in Kanonenreichweite wirst du von hinten getroffen, siehe [Separation](/grundlagen/defensiv/separation) |
| **Nose-low beschleunigen** | Genug Höhe über dem [Hard Deck](/grundlagen/begriffe) | Er folgt von oben und bekommt den Schuss |

## Scissors in VFM

| Jet | Flat Scissors | Rolling Scissors |
|---|---|---|
| **T-18 Cutlass** | **wahrscheinlich am besten**. Der Entwickler positioniert sie als High-AoA-/Low-Speed-Jet. *Hypothese, nicht durch Daten belegt.* | mittel (Schub zwischen T-15 und T-16, laut Balken) |
| **T-15 Excalibur** | stark im Datenbereich (beste Instant Rate, kleinster Radius im dargestellten Bereich), darunter unbekannt | **wahrscheinlich am besten** wegen des stärksten Schubs (Folgerung) |
| **T-16 Falchion** | **am schwächsten**: höchste Corner Speed, unter ~380 KIAS der schwächste Jet | **am schwächsten**: niedrigster Schub-Balken (Folgerung) |

Daraus folgt:
- **T-16**: Meide Scheren grundsätzlich. Halte deine Speed, und wenn ein Overshoot droht, nutze ihn für Separation statt für eine Schere.
- **T-18**: Eine Flat Scissors ist vermutlich dein Terrain. Bleib in der Ebene und lass dich nicht in die Vertikale ziehen.
- **T-15**: Gegen die T-18 lieber Rolling als Flat. Gegen die T-16 kannst du beides annehmen.

::: info IM SPIEL PRÜFEN
- Ob die T-18 in einer Flat Scissors unter ~200 KIAS tatsächlich besser ist als die T-15 (mit und ohne AoA-Override). Testaufbau im [Trainingsplan](/grundlagen/uebungen).
- Die Rollrate der Jets bei niedriger Speed (keine Daten).
- Ob VFM eine Speedbrake hat und wie sie bedient wird.
- Wie das Spiel im Ranked bei Zeitablauf den „Verfolger“ bestimmt, wenn ihr gerade in einer Schere seid.
:::

::: tip MERKE
- Scissors sind neutral. Gewinner ist, wer weniger vorwärts kommt und dabei die Kontrolle behält.
- Flat: schneller verlangsamen, Rollrate behalten, Umkehr timen.
- Rolling: Nase schneller über oben bringen. Schub und Energie zählen.
- Vermeiden ist leichter als aussteigen. Als Angreifer Closure kontrollieren.
- VFM: T-18 vermutlich Flat-Spezialist (testen), T-16 meidet Scheren, T-15 nutzt Schub in der Rolling Scissors.
:::

Weiter: [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf)
