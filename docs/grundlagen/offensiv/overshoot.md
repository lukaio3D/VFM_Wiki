# Overshoot

> Der Moment, in dem der Angreifer seinen Vorteil verliert: was ihn auslöst, wie du ihn als Angreifer vermeidest und als Verteidiger erzwingst.

Ein Overshoot heißt: Der Angreifer kann die Kurve des Gegners nicht mehr mitgehen und fliegt über dessen Flugbahn oder an ihm vorbei. Es gibt zwei Arten, und der Unterschied ist entscheidend.

## Die zwei Arten

- **Flight-Path-Overshoot:** Du kreuzt **seine Flugbahn hinter ihm**. Du verlierst Winkel und stehst außen, bist aber **noch hinter seiner 3/9-Linie** und damit offensiv, wenn du richtig reagierst.
- **3/9-Line-Overshoot:** Du schießt **über seine 3/9-Linie hinaus** und bist **vor ihm**. Rollentausch – genau das will jeder Verteidiger.

„Lateral Overshoot“ ist kein Standardbegriff; gemeint ist meist einer der beiden.

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

## Warum es passiert

Ein Overshoot ist immer **zu viel Closure bei zu großem Winkel**:

- **Zu schnell im Vergleich zu ihm.** Bei gleicher Last wächst der Radius mit V² ([Kurvenphysik](/grundlagen/kurvenphysik)): 20 % mehr Speed heißt rund 44 % mehr Radius.
- **Zu früh in Lead am Eintritt** statt in Lag.
- **Schuss-Fixierung:** zu lange tracken, Lead ziehen, immer näher kommen.
- **Er bricht im richtigen Moment ein** oder **wird langsamer**, während du schnell bleibst.

**Warnzeichen:** Er wird schnell größer, die Sichtlinienrate steigt, du bist am G- oder AoA-Limit und er läuft trotzdem nach vorn aus, er wandert Richtung Flächenspitze.

## Als Angreifer: Overshoot vermeiden

Je früher, desto billiger:

1. **Closure früh steuern:** Gas zurück, lieber in Lag ankommen.
2. **Lag statt Lead**, bis du in seinem Kreis bist ([Verfolgungskurven](/grundlagen/verfolgungskurven)).
3. **[Quarter Plane oder High Yo-Yo](/grundlagen/offensiv/yo-yos)**, wenn die Closure zu hoch wird.
4. **[Lag Roll](/grundlagen/offensiv/lag-roll)**, wenn die Nase tief in Lead steht und es knapp wird; **[Barrel Roll Attack](/grundlagen/offensiv/lag-roll)** bei hoher AA am Eintritt.
5. **Schuss aufgeben**, wenn du nur noch schießen kannst, indem du überschießt.

::: warning WENN ES NICHT MEHR ZU VERHINDERN IST
Dann **über seine Flugbahn und nach oben aus seiner Ebene**, nicht in seiner Ebene neben ihm. Ein Flight-Path-Overshoot mit Höhe ist reparierbar, ein 3/9-Line-Overshoot auf gleicher Höhe meist nicht.
:::

## Als Verteidiger: Overshoot erzwingen

Nimm ihm den Winkel, den er zum Mitdrehen bräuchte:

- **[Break Turn](/grundlagen/defensiv/break-turn) im richtigen Moment:** wenn er sich auf Lead festgelegt hat und schnell ist. Zu früh, und er geht einfach in Lag.
- **Eintritt in deinen Kreis verweigern:** mit harter Kurve seine AA hoch halten.
- **Ebene wechseln, wenn er schießen will:** [Guns Defense](/grundlagen/defensiv/guns-defense).
- **Last-Ditch:** [Defensive Spirale](/grundlagen/defensiv/spirale), wenn du langsam bist und er mit Überschuss hinter dir hängt.

::: danger NICHT VERLANGSAMEN, WÄHREND ER TRACKT
Gas raus, um ihn vorbeizulassen, funktioniert nur, wenn er **nicht** in Tracking-Lösung hinter dir sitzt. Sonst machst du dich zum leichteren Ziel. Erst Ebene wechseln, dann über Speed nachdenken.
:::

## Nach dem Overshoot

**Als Angreifer:**
- **Flight-Path-Overshoot:** Mit dem Speed-Überschuss nach oben (Lift Vector über ihn), Sicht halten, von oben wieder hinter ihn. Nicht flach weiterziehen.
- **3/9-Line-Overshoot:** Du bist vor ihm, aber meist schneller. Nutze das: [vertikal](/grundlagen/neutral/vertikal-kampf) aus seiner Reichweite oder [separieren](/grundlagen/defensiv/separation) und neu ansetzen. Keine flache [Schere](/grundlagen/neutral/scissors) gegen einen langsameren Gegner, der langsam besser dreht.

**Als Verteidiger:**
- **Reversal:** Sobald er über deine Flugbahn schießt, Lift Vector auf ihn und in seine Richtung drehen.
- Zieht er nach oben, parkt er Speed in Höhe. Folge nicht blind, wenn du deutlich langsamer bist.

## VFM-Hinweise

- **AoA-Override („Cobra-Button“):** Bringt die Nase schlagartig herum und kann einen Overshoot erzwingen oder einen Snapshot ermöglichen. Er kostet aber extrem Energie; gegen einen zweiten Gegner oder einen Angreifer, der nach oben ausweicht, bist du danach Beute. Siehe [Physik](/grundlagen/physik#anstellwinkel-aoa-limiter-und-override).
- **[T-15](/flugzeuge/t15):** Kleinster Radius und meiste G bei gleicher Speed – als Verteidiger bringt sie einen schnelleren Angreifer leicht zum Overshoot.
- **[T-16](/flugzeuge/t16):** Größter Radius; als Angreifer muss sie besonders früh Closure abbauen.
- **[T-18](/flugzeuge/t18):** Wird durch ihren hohen Widerstand schnell langsam und damit schnell eng. Das hilft als Verteidiger, ist als Angreifer aber eine Falle, wenn du Energie halten willst.

::: info IM SPIEL PRÜFEN
- Wie viel Speed ein kurzer Override-Einsatz kostet (Specific-Energy-Graph im Replay).
- Wie stark die Speedbrake bremst.
:::

::: tip MERKE
- Flight-Path-Overshoot: Du kreuzt seine Bahn, bist noch hinter ihm. 3/9-Line-Overshoot: Du bist vor ihm, Rollentausch.
- Ursache ist immer zu viel Closure bei zu großem Winkel. Früh mit Gas, Lag und Yo-Yo gegensteuern.
- Wenn schon überschießen, dann über seine Flugbahn und nach oben.
- Als Verteidiger: Overshoot mit Break und Ebenenwechsel erzwingen, nicht durch Bremsen in seine Tracking-Lösung hinein.
:::

Weiter: [Schusslösung](/grundlagen/offensiv/schussloesung)
