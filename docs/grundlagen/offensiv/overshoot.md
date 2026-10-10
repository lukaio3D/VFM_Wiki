# Overshoot

> Der Moment, in dem der Angreifer seinen Vorteil verliert: was ihn auslöst, wie du ihn als Angreifer vermeidest, wie du ihn als Verteidiger erzwingst.

Ein Overshoot heißt: Der Angreifer kann die Kurve des Gegners nicht mehr mitgehen und fliegt über dessen Flugbahn oder sogar an ihm vorbei. Es gibt zwei Arten, und der Unterschied ist entscheidend.

## Die zwei Arten

### Flight-Path-Overshoot

Du kreuzt **seine Flugbahn hinter ihm**. Du verlierst Winkelvorteil und stehst danach auf der Außenseite seiner Kurve, bist aber **noch hinter seiner 3/9-Linie**. Unangenehm, aber du bist noch offensiv, wenn du richtig reagierst.

### 3/9-Line-Overshoot

Du schießt **über seine 3/9-Linie hinaus** und bist **vor ihm**. Ab jetzt kann er dich angreifen. Das ist der Rollentausch, den jeder Verteidiger will.

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Draufsicht: Gegner fliegt nach oben. Bahn 1 kreuzt seine Flugbahn hinter ihm und bleibt hinter seiner 3/9-Linie (Flight-Path-Overshoot). Bahn 2 kreuzt seine Flugbahn und überquert danach die 3/9-Linie, endet vor ihm (3/9-Line-Overshoot).">
<defs>
<marker id="osA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--vp-c-brand-1)"/></marker>
<marker id="osD" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--vp-c-danger-1)"/></marker>
<marker id="osG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker>
</defs>
<line x1="30" y1="150" x2="490" y2="150" stroke="currentColor" stroke-dasharray="6 4" opacity="0.6"/>
<text x="490" y="142" font-size="12" fill="currentColor" text-anchor="end">seine 3/9-Linie</text>
<text x="34" y="140" font-size="12" fill="currentColor">vor ihm</text>
<text x="34" y="168" font-size="12" fill="currentColor">hinter ihm</text>
<line x1="260" y1="158" x2="260" y2="290" stroke="currentColor" stroke-dasharray="2 4" opacity="0.6"/>
<text x="266" y="288" font-size="12" fill="currentColor">seine Flugbahn</text>
<polygon points="260,138 252,158 268,158" fill="currentColor"/>
<line x1="260" y1="136" x2="260" y2="100" stroke="currentColor" stroke-width="2" marker-end="url(#osG)"/>
<text x="250" y="122" font-size="12" fill="currentColor" text-anchor="end">Gegner</text>
<path d="M90,285 C170,250 240,232 350,215" fill="none" style="stroke:var(--vp-c-brand-1)" stroke-width="2" marker-end="url(#osA)"/>
<text x="356" y="236" font-size="12" fill="currentColor">1 Flight-Path-Overshoot</text>
<path d="M60,240 C250,225 330,200 340,80" fill="none" style="stroke:var(--vp-c-danger-1)" stroke-width="2" marker-end="url(#osD)"/>
<text x="348" y="86" font-size="12" fill="currentColor">2 3/9-Line-Overshoot</text>
</svg>

*Bahn 1 kreuzt seine Flugbahn, bleibt aber hinter seiner 3/9-Linie. Bahn 2 läuft über die 3/9-Linie hinaus nach vorn: Rollentausch.*

::: info BEGRIFF
"Lateral Overshoot" ist kein Standardbegriff. Gemeint ist meist einer der beiden oben. Wir verwenden nur Flight-Path- und 3/9-Line-Overshoot.
:::

## Warum es passiert

Ein Overshoot ist immer das Ergebnis von **zu viel Closure bei zu großem Winkel**. Konkret:

- **Zu schnell im Vergleich zu ihm.** Bei gleichem G wächst der Kurvenradius mit dem Quadrat der Geschwindigkeit (r = V²/(g·√(n²−1)), siehe [Kurvenphysik](/grundlagen/kurvenphysik)). 20 % mehr Speed als er heißt bei gleicher Last rund 44 % mehr Radius. Du kannst seine Kurve schlicht nicht mitfliegen.
- **Zu früh in Lead am Eintritt.** Wer an seinem Kreis vorbei auf seine Nase zieht, statt in Lag einzutreten, schneidet mit hoher AA und hoher Closure hinein.
- **Schuss-Fixierung.** Du willst den Gun-Schuss unbedingt haben, trackst zu lange, ziehst Lead, kommst immer näher und merkst zu spät, dass du nicht mehr hinter ihm bleiben kannst.
- **Er bricht im richtigen Moment ein.** Ein harter Break, wenn du dich auf Lead festgelegt hast, lässt seine AA schlagartig wachsen.
- **Er wird langsamer, während du schnell bleibst.** Gas raus, harte Kurve, im Extremfall Kurve mit AoA-Override: seine Speed fällt, deine Closure steigt.

### Warnzeichen

- Er wird **schnell größer** im Visier.
- Die **Sichtlinienrate steigt**: Du musst immer härter ziehen, um ihn vor der Nase zu halten.
- Du bist **am G-Limit** (9 G) oder am AoA-Limit und er läuft trotzdem nach vorn aus.
- Er kommt Richtung deiner Flächenspitze statt vor deiner Nase zu bleiben.

## Als Angreifer: Overshoot vermeiden

In dieser Reihenfolge, je früher, desto billiger:

1. **Closure früh steuern.** Gas zurück, wenn du schneller wirst als nötig. Lieber in Lag ankommen.
2. **Lag statt Lead**, bis du in seinem Kreis bist. Siehe [Verfolgungskurven](/grundlagen/verfolgungskurven).
3. **Aus der Ebene gehen:** [Quarter Plane oder High Yo-Yo](/grundlagen/offensiv/yo-yos), wenn die Closure zu hoch wird.
4. **[Lag Roll](/grundlagen/offensiv/lag-roll)**, wenn die Nase schon tief in Lead steht und es knapp wird.
5. **[Barrel Roll Attack](/grundlagen/offensiv/lag-roll)**, wenn du mit hoher AA am Eintritt ankommst.
6. **Schuss aufgeben.** Wenn du nur noch schießen kannst, indem du überschießt: nicht schießen, Position halten.

::: warning WENN ES NICHT MEHR ZU VERHINDERN IST
Wenn du überschießen wirst, dann **über seine Flugbahn und aus seiner Ebene nach oben**, nicht neben ihm in seiner Ebene. Ein Flight-Path-Overshoot mit Höhe ist reparierbar. Ein 3/9-Line-Overshoot auf gleicher Höhe direkt neben ihm ist es meist nicht.
:::

## Als Verteidiger: Overshoot erzwingen

Der Overshoot des Angreifers ist dein Weg zurück ins Spiel. Du erzwingst ihn, indem du ihm den Winkel nimmst, den er zum Mitdrehen bräuchte:

- **Break Turn im richtigen Moment:** wenn er sich auf Lead festgelegt hat und schnell ist. Zu früh, und er geht einfach in Lag. Siehe [Break Turn](/grundlagen/defensiv/break-turn).
- **Seinen Eintritt in deinen Kurvenkreis verweigern:** Halte ihn mit harter Kurve bei hoher AA, sodass er nicht in Lag hinter dich kommt.
- **Ebene wechseln, wenn er schießen will:** [Guns Defense](/grundlagen/defensiv/guns-defense).
- **Last-Ditch:** [Defensive Spirale](/grundlagen/defensiv/spirale) in der Vertikalen, wenn du langsam bist und er mit Überschuss hinter dir hängt.

::: danger NICHT VERLANGSAMEN, WÄHREND ER TRACKT
Gas raus und Speed abbauen, um ihn vorbeizulassen, funktioniert nur, wenn er **nicht** in einer Tracking-Lösung hinter dir sitzt. Sitzt er in deiner Ebene mit Funnel auf dir, machst du dich durchs Bremsen nur zum leichteren Ziel: Seine AA wird kleiner, er braucht weniger Lead. Erst Ebene wechseln, dann über Speed nachdenken.
:::

## Nach dem Overshoot

### Wenn du der Angreifer warst

- **Flight-Path-Overshoot:** Du bist außen und noch hinter ihm. Geh mit dem Speed-Überschuss nach oben (High Yo-Yo, Lift Vector über ihn), halte die Sicht, komm von oben wieder hinter ihn. Nicht flach weiterziehen.
- **3/9-Line-Overshoot:** Du bist jetzt vor ihm, hast aber meist mehr Speed als er (sonst hättest du nicht überschossen). Nutze genau diesen Vorteil:
  - **Vertikal:** Speed in Höhe tauschen, aus seiner Reichweite nach oben, von dort neu angreifen. Siehe [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf).
  - **Separieren:** Mit Speed-Vorteil aus seiner Waffenreichweite heraus und neu ansetzen. Siehe [Separation](/grundlagen/defensiv/separation).
  - **Nicht** in eine flache Schere gegen einen langsameren Gegner gehen, der langsam besser dreht als du. Siehe [Scissors](/grundlagen/neutral/scissors).

### Wenn du der Verteidiger warst

- **Umkehren (Reversal):** Sobald er über deine Flugbahn schießt, Lift Vector auf ihn rollen und in seine Richtung drehen. Jetzt bist du hinter ihm.
- Achte darauf, wohin er geht: Zieht er nach oben, will er seine Speed in Höhe parken. Folge nicht blind in die Vertikale, wenn du deutlich langsamer bist.
- Läuft es auf eine Schere hinaus: Wer langsamer fliegen und trotzdem die Nase bewegen kann, gewinnt die flache Schere. Siehe [Scissors](/grundlagen/neutral/scissors).

## VFM-Hinweise

- **AoA-Override ("Cobra-Button"):** Der Override gibt dir sofort Nose Authority über das AoA-Limit hinaus und kostet extrem viel Energie. Als Verteidiger kann das einen Overshoot erzwingen oder einen Snapshot ermöglichen, wenn der Angreifer schnell und nah ist. Danach bist du aber sehr langsam. Gegen einen zweiten Gegner oder einen Angreifer, der einfach nach oben ausweicht, ist das ein Kill für ihn.
- **Jet-Unterschiede:** Die T-15 hat laut Daten (Stand Okt 2026) die beste Instant Rate und den kleinsten Radius. Als Verteidiger kann sie einen schnelleren Angreifer besonders leicht zum Overshoot bringen. Die T-16 mit dem größten Radius muss als Angreifer besonders früh Closure abbauen.

::: info IM SPIEL PRÜFEN
- Wie viel Speed ein kurzer AoA-Override-Einsatz in deinem Jet kostet. Teste es im Free Flight und lies den Specific-Energy-Graph im Replay.
- Ob es eine Speedbrake gibt und wie sie belegt ist (bisher keine Quelle).
:::

::: tip MERKE
- Flight-Path-Overshoot: du kreuzt seine Bahn, bist noch hinter ihm. 3/9-Line-Overshoot: du bist vor ihm, Rollentausch.
- Ursache ist immer zu viel Closure bei zu großem Winkel. Früh mit Gas, Lag und Yo-Yo gegensteuern.
- Wenn schon überschießen, dann über seine Flugbahn und nach oben.
- Als Verteidiger: Overshoot mit Break und Ebenenwechsel erzwingen, nicht durch Bremsen in seine Tracking-Lösung hinein.
:::

Weiter: [Schusslösung](/grundlagen/offensiv/schussloesung)
