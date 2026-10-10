# Relative Geometrie

> Wo stehst du relativ zum Gegner, wohin zeigst du, und wie verändert sich das? Die Sprache, in der jede BFM-Lage beschrieben wird.

Im Dogfight zählt nicht, wo du über der Karte bist, sondern wo du **relativ zum Gegner** bist. Mit wenigen Begriffen beschreibst du jede Lage als offensiv, neutral oder defensiv. Kurzdefinitionen: [Glossar](/grundlagen/begriffe).

## Die drei Winkel: AA, ATA, HCA

<svg viewBox="0 0 520 340" width="100%" style="max-width:520px" role="img" aria-label="Draufsicht: Der Bandit fliegt nach oben. Du bist hinten links von ihm. Aspect Angle wird an ihm gemessen, zwischen seinem Heck und der Sichtlinie zu dir. Antenna Train Angle wird an dir gemessen, zwischen deiner Nase und der Sichtlinie zu ihm.">
<defs><marker id="geo-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker><marker id="geo-ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--vp-c-brand-1)"/></marker></defs>
<line x1="230" y1="110" x2="440" y2="110" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="6 4"/>
<text x="444" y="114" font-size="12" fill="var(--vp-c-text-2)">3/9-Linie</text>
<line x1="330" y1="122" x2="330" y2="240" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="2 4"/>
<text x="336" y="238" font-size="12" fill="var(--vp-c-text-2)">seine Six (AA 0°)</text>
<polygon points="330,96 322,120 338,120" fill="var(--vp-c-danger-1)"/>
<line x1="330" y1="94" x2="330" y2="50" stroke="var(--vp-c-danger-1)" stroke-width="2" marker-end="url(#geo-ah)"/>
<text x="336" y="56" font-size="12" fill="currentColor">seine Flugrichtung</text>
<text x="344" y="100" font-size="12" fill="var(--vp-c-danger-1)">Bandit</text>
<line x1="214" y1="284" x2="324" y2="119" stroke="currentColor" stroke-width="1.5"/>
<text x="262" y="196" font-size="12" fill="currentColor" text-anchor="end">Sichtlinie / Range</text>
<g transform="translate(210,290) rotate(60)"><polygon points="0,-12 -8,10 8,10" fill="var(--vp-c-brand-1)"/></g>
<line x1="222" y1="283" x2="288" y2="245" stroke="var(--vp-c-brand-1)" stroke-width="2" marker-end="url(#geo-ahb)"/>
<text x="294" y="262" font-size="12" fill="var(--vp-c-brand-1)">deine Nase</text>
<text x="196" y="304" font-size="12" fill="var(--vp-c-brand-1)" text-anchor="end">Du</text>
<path d="M 330 155 A 45 45 0 0 1 305 147.4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="308" y="180" font-size="12" fill="currentColor" text-anchor="middle">AA</text>
<path d="M 244.6 270 A 40 40 0 0 0 232.2 256.7" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="1.5"/>
<text x="258" y="252" font-size="12" fill="var(--vp-c-brand-1)">ATA</text>
<text x="260" y="330" font-size="12" fill="var(--vp-c-text-2)" text-anchor="middle">Beispiel: AA ≈ 34°, ATA ≈ 26°, HCA = 60°</text>
</svg>

| Winkel | Gemessen | Sagt | 0° | 90° | 180° |
|---|---|---|---|---|---|
| **Aspect Angle (AA)** | am Gegner, zwischen seinem Heck und der Sichtlinie zu dir | wo du relativ zu ihm stehst | genau hinter ihm | auf seiner 3/9-Linie | genau vor ihm |
| **Antenna Train Angle (ATA)** | an dir, zwischen deiner Nase und der Sichtlinie zu ihm | wohin du zeigst | er ist vor deiner Nase | er ist neben dir | er ist hinter dir |
| **Heading Crossing Angle (HCA)** | zwischen euren Flugrichtungen | wie ihr euch kreuzt | parallel, gleiche Richtung | rechtwinklig | gegeneinander |

Hohe HCA in Schussnähe heißt: nur ein [Snapshot](/grundlagen/begriffe#snapshot) ist möglich, kein Tracking Shot.

| Lage | AA | ATA | HCA | Bewertung |
|---|---|---|---|---|
| Du an seiner Six, Nase auf ihm | 0° | 0° | 0° | Offensiv – Schussposition |
| Frontal aufeinander zu | 180° | 0° | 180° | Neutral – Merge |
| Nebeneinander, gleiche Richtung | 90° | 90° | 0° | Neutral |
| Er an deiner Six | 180° | 180° | 0° | Defensiv |

Faustregel: **Kleine AA und kleine ATA = offensiv. Große AA und große ATA = defensiv.**

## Range

Range ist die Entfernung zum Gegner. Sie entscheidet, welche Waffe passt und wie viel Zeit du hast. Mit Radar-Lock liefert das Radar die Entfernung für den Gun Funnel ([Radar](/avionik/radar)). Ohne Lock rechnet der Funnel mit einer durchschnittlichen Spannweite: Füllen die Flügel des Gegners den Funnel aus, passt die Entfernung ungefähr ([HUD](/avionik/hud)).

## Die 3/9-Linie

Die gedachte Linie durch die Flügel des Gegners, von seiner 3- zu seiner 9-Uhr-Position. Sie teilt den Raum in **vor ihm** und **hinter ihm**.

- **Hinter seiner 3/9:** Du bist im Vorteil. Er muss den Kopf drehen, um dich zu sehen, und seine Nase hat einen weiten Weg zu dir.
- **Vor seiner 3/9:** Er erreicht dich mit der Nase. Rutschst du als Angreifer davor, ist das ein [3/9-Line-Overshoot](/grundlagen/offensiv/overshoot) – Rollentausch.

## Closure

**Closure** (Vc) ist die Geschwindigkeit, mit der die Range kleiner wird. Zu viel Closure nahe am Gegner führt zum [Overshoot](/grundlagen/offensiv/overshoot), zu wenig lässt ihn davonziehen. Du steuerst sie über die [Verfolgungskurve](/grundlagen/verfolgungskurven) (Lead erhöht, Lag senkt), über Out-of-Plane-Manöver wie den [High Yo-Yo](/grundlagen/offensiv/yo-yos) und über den Schub.

## LOS-Rate (Sichtlinienrate)

Die **LOS-Rate** ist, wie schnell sich die Sichtlinie zum Gegner dreht – wie schnell er über dein Kabinendach „wandert“.

- **Er wandert Richtung deiner Nase:** Du gewinnst Winkel.
- **Er wandert nach hinten:** Du verlierst Winkel.
- **Er steht still:** Die Geometrie ändert sich nicht (im Anflug: Kollisionskurs).

Vor dem Merge ist die LOS-Rate dein Signal für den **Lead Turn**: Steigt sie deutlich – grob, wenn sein seitlicher Versatz etwa einem Wenderadius entspricht –, ist der Moment da. Details: [Der Merge](/grundlagen/neutral/der-merge).

## Bewegungsebene (Plane of Motion)

Jeder Jet kurvt in einer Ebene aus Flugrichtung und Lift Vector, seiner **Bewegungsebene**. **In seiner Ebene** erreicht er dich durch Ziehen. **Außerhalb** muss er erst rollen, dann ziehen – das kostet ihn Zeit.

Deshalb verlassen gute Angreifer die Ebene des Gegners, um Closure und Winkel zu steuern ([Yo-Yos](/grundlagen/offensiv/yo-yos), [Lag Roll](/grundlagen/offensiv/lag-roll)), und gute Verteidiger, um aus der Lösung des Angreifers zu kommen ([Guns Defense](/grundlagen/defensiv/guns-defense)). Physik: [Kurvenphysik](/grundlagen/kurvenphysik#out-of-plane-manovrieren).

## Kurvenkreise und Turning Room

Jeder kurvende Jet beschreibt einen **Kurvenkreis** (r ~ V²).

- **In seinem Kreis** bringst du die Nase auf ihn und bleibst hinter ihm.
- **Außerhalb seines Kreises** kann er dir durch Weiterdrehen die Nase verweigern. Hinein kommst du über [Lag Pursuit](/grundlagen/verfolgungskurven#turn-circle-entry).

**Turning Room** ist der Platz, den du brauchst, um die Nase auf den Gegner zu drehen. Am Merge: **Gib ihm keinen** (Nase auf ihn, seitlichen Versatz wegnehmen) und **nutz seinen** mit dem [Lead Turn](/grundlagen/neutral/der-merge). Ob danach ein gemeinsamer Kreis (One-Circle) oder zwei Kreise (Two-Circle) entstehen: [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle).

## Control Zone

Die **Control Zone** ist eine Position hinter dem Gegner, aus der du trotz seiner Manöver hinter ihm bleibst: Egal ob er bricht oder umkehrt, du hast genug Abstand und Winkel, ohne vor seine 3/9-Linie zu geraten.

- **Richtwert:** etwa 30–60° AA und einige tausend Fuß Range, je nach Jets und Speed.
- **Zu nah** oder zu viel Closure: Er bricht, du schießt vorbei.
- **Zu weit:** Er dreht und neutralisiert, bevor du nachkommst.

Die Control Zone ist **keine Waffenreichweite**, sondern der Ort, von dem aus du in Ruhe einen Schuss aufbaust.

## WEZ: Gun vs. Fox 2

Die **WEZ** (Weapons Engagement Zone) ist der Raum, in dem eine Waffe treffen kann: begrenzt durch Mindest- und Maximalreichweite, Off-Boresight (wie weit er von deiner Nase weg sein darf) und Aspect.

| | Bordkanone | IR-Rakete (Fox 2) |
|---|---|---|
| Reichweite | kurz | deutlich größer, mit Mindestreichweite |
| Nase | muss vor ihn zeigen (Lead) | Suchkopf muss ihn sehen, etwas Off-Boresight möglich |
| Aspect | jeder Winkel, Tracking am einfachsten bei kleiner AA | von hinten am zuverlässigsten; Community berichtet auch frontale Treffer |
| Gegenmittel | Jinken, aus der Ebene | Flares, Break, Idle |

Die Logik: **Die Fox 2 zwingt ihn zu Flares und Defensive – damit gibt er Energie oder Position ab, und dann kommt die Gun.** Im engen One-Circle bist du oft unter der Mindestreichweite der Rakete; im Two-Circle bekommt der schneller drehende Jet den ersten Fox-2-Schuss. Im Ranked 1v1 und in vielen Lobbys sind Raketen aus (Guns-only) – dann ist die Gun-WEZ alles. Details: [Schusslösung](/grundlagen/offensiv/schussloesung), [Waffen](/avionik/waffen).

::: info IM SPIEL PRÜFEN
- Gun-Reichweite und Streuung: Bis zu welcher Entfernung bringt der Funnel sinnvoll Treffer?
- IR-Rakete: Mindest- und Maximalreichweite, maximaler Off-Boresight-Winkel, frontale Treffer.
- Zeigt das HUD bei Lock Range und Closure als Zahl?
:::

::: tip MERKE
- **AA** = wo du relativ zu ihm stehst. **ATA** = wohin du zeigst. **HCA** = Winkel zwischen euren Flugrichtungen.
- **Hinter seiner 3/9-Linie** bleiben. Wer davor rutscht, tauscht die Rollen.
- **LOS-Rate** lesen: Wandert er Richtung Nase, gewinnst du.
- **In seinen Kreis** kommst du über Lag, aus seiner Ebene raus über Rollen.
- **Control Zone** ist Position, **WEZ** ist Waffe – erst das eine, dann das andere.
:::

Weiter: [Verfolgungskurven](/grundlagen/verfolgungskurven)
