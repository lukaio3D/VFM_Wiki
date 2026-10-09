# Relative Geometrie

> Wo stehst du relativ zum Gegner, wohin zeigst du, und wie verändert sich das? Die Sprache, in der jede BFM-Lage beschrieben wird.

Im Dogfight zählt nicht, wo du über der Karte bist, sondern wo du **relativ zum Gegner** bist. Mit einer Handvoll Begriffen lässt sich jede Lage beschreiben: offensiv, neutral oder defensiv – und was als Nächstes passiert. Alle Begriffe auch im [Glossar](/grundlagen/begriffe).

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

### Aspect Angle (AA)

Gemessen **am Gegner**: der Winkel zwischen seinem Heck (seiner Six) und der Sichtlinie zu dir. AA sagt, **wo du relativ zu ihm stehst**.

- **0°:** Du bist genau hinter ihm.
- **90°:** Du bist auf seiner 3/9-Linie, seitlich neben ihm.
- **180°:** Du bist genau vor ihm.

Unter 90° bist du hinter seiner 3/9-Linie, über 90° davor.

### Antenna Train Angle (ATA)

Gemessen **an dir**: der Winkel zwischen deiner Nase und der Sichtlinie zum Gegner. ATA sagt, **wohin du zeigst** – wie weit er von deiner Nase weg ist.

- **0°:** Er ist genau vor deiner Nase (im HUD).
- **90°:** Er ist seitlich neben dir (Blick zur Seite).
- **180°:** Er ist genau hinter dir.

### Heading Crossing Angle (HCA)

Der Winkel **zwischen euren Flugrichtungen**, unabhängig davon, wo ihr steht. 0° = parallel in dieselbe Richtung, 90° = ihr kreuzt euch rechtwinklig, 180° = ihr fliegt gegeneinander. Hohe HCA in Schussnähe bedeutet: nur ein [Snapshot](/grundlagen/begriffe#snapshot) ist möglich, kein Tracking Shot.

### AA und ATA zusammen

| Lage | AA | ATA | HCA | Bewertung |
|---|---|---|---|---|
| Du an seiner Six, Nase auf ihm | 0° | 0° | 0° | Offensiv – Schussposition |
| Frontal aufeinander zu | 180° | 0° | 180° | Neutral – Merge |
| Nebeneinander, gleiche Richtung | 90° | 90° | 0° | Neutral |
| Er an deiner Six | 180° | 180° | 0° | Defensiv |

Faustregel: **Kleine AA und kleine ATA = offensiv. Große AA und große ATA = defensiv.** Alles dazwischen ist neutral oder im Wandel.

## Range

Range ist die Entfernung zum Gegner. Sie entscheidet, welche Waffe passt und wie viel Zeit du hast.

- **Mit Radar-Lock** liefert das Radar eine Feuerleitlösung für den Gun-Funnel. Siehe [Radar](/avionik/radar).
- **Ohne Lock** rechnet der Gun-Funnel mit einer durchschnittlichen Spannweite (seit v1.2.8). Füllen die Flügel des Gegners den Funnel aus, passt die Entfernung ungefähr. Siehe [HUD](/avionik/hud).
- **Visuell:** Wie groß ist er, wie schnell wird er größer?

::: info IM SPIEL PRÜFEN
- Zeigt das HUD bei Lock die Range und die Closure als Zahl? In welcher Einheit?
:::

## Die 3/9-Linie

Die gedachte Linie durch die Flügel des Gegners, von seiner 3-Uhr- zu seiner 9-Uhr-Position. Sie teilt den Raum in **vor ihm** und **hinter ihm**.

- **Hinter seiner 3/9:** Du bist im Vorteil. Er muss den Kopf drehen, um dich zu sehen, und seine Nase hat einen weiten Weg zu dir.
- **Vor seiner 3/9:** Er kann dich mit der Nase erreichen. Wer als Angreifer vor die 3/9-Linie rutscht, hat einen [3/9-Line-Overshoot](/grundlagen/offensiv/overshoot) – Rollentausch.

## Closure

**Closure** (Vc) ist die Geschwindigkeit, mit der die Range kleiner wird. Positive Closure: ihr kommt euch näher. Negative: ihr entfernt euch.

- **Zu viel Closure** nahe am Gegner führt zum [Overshoot](/grundlagen/offensiv/overshoot).
- **Zu wenig Closure** heißt: Er zieht davon oder dreht dir aus der Reichweite.
- Closure steuerst du über die [Verfolgungskurve](/grundlagen/verfolgungskurven) (Lead erhöht, Lag senkt), über Out-of-Plane-Manöver wie den [High Yo-Yo](/grundlagen/offensiv/yo-yos) und über den Schub.

## LOS-Rate (Sichtlinienrate)

Die **Line of Sight (LOS)** ist die Sichtlinie von dir zum Gegner. Die **LOS-Rate** ist, wie schnell sich diese Linie dreht – also wie schnell der Gegner über dein Kabinendach "wandert".

- **Gegner wandert Richtung deiner Nase:** Du gewinnst Winkel.
- **Gegner wandert nach hinten über dein Kabinendach:** Du verlierst Winkel – er dreht schneller oder sitzt besser.
- **Gegner steht still auf dem Kabinendach:** Die Geometrie ändert sich gerade nicht (im Anflug: Kollisionskurs).

Vor dem Merge ist die LOS-Rate dein Signal für den **Lead Turn**: Solange der Gegner kaum wandert, bist du weit weg. Steigt die LOS-Rate deutlich – grob, wenn sein seitlicher Versatz etwa einem eigenen Wenderadius entspricht – ist der Moment für den Turn. Details: [Der Merge](/grundlagen/neutral/der-merge).

## Bewegungsebene (Plane of Motion)

Jeder Jet kurvt in einer Ebene: aufgespannt von seiner Flugrichtung und seinem Lift Vector. Das ist seine **Bewegungsebene** (Plane of Motion, POM).

- **In seiner Ebene** kann er dich mit Ziehen erreichen.
- **Außerhalb seiner Ebene** muss er erst rollen, dann ziehen. Das kostet ihm Zeit.

Deshalb verlassen gute Angreifer die Ebene des Gegners, um Closure und Winkel zu steuern ([Yo-Yos](/grundlagen/offensiv/yo-yos), [Lag Roll](/grundlagen/offensiv/lag-roll)), und gute Verteidiger, um aus der Lösung des Angreifers zu kommen ([Guns Defense](/grundlagen/defensiv/guns-defense)). Die Physik dazu: [Kurvenphysik](/grundlagen/kurvenphysik#out-of-plane-manovrieren).

## Kurvenkreise und Turning Room

Jeder Jet beschreibt beim Kurven einen **Kurvenkreis** (Turn Circle). Seine Größe hängt von Speed und G ab (r ~ V²).

- **Bist du in seinem Kreis**, kannst du deine Nase auf ihn bringen und hinter ihm bleiben – er kann dich nicht einfach "wegdrehen".
- **Bist du außerhalb seines Kreises**, kann er dir durch Weiterdrehen die Nase verweigern. Du musst erst in seinen Kreis hinein – über [Lag Pursuit](/grundlagen/verfolgungskurven#turn-circle-entry).

**Turning Room** ist der Platz (seitlich oder vertikal), den du brauchst, um deine Nase auf den Gegner zu drehen. Am Merge bedeutet seitlicher Versatz Turning Room für beide.

- **Gib ihm keinen:** Zeig mit der Nase auf ihn und nimm den seitlichen Versatz weg, bevor ihr euch passiert.
- **Hol dir welchen:** Der [Lead Turn](/grundlagen/neutral/der-merge) nutzt seinen Versatz, um schon vor dem Merge Winkel zu gewinnen. Zu früh angesetzt, verschenkst du den eigenen Turning Room oder kreuzt seine Bahn (Flight-Path-Overshoot).

Was nach dem Merge passiert – ob ihr in einem gemeinsamen Kreis (One-Circle) oder in zwei Kreisen (Two-Circle) landet und wer welchen Flow will – steht auf der Seite [One-Circle vs. Two-Circle](/grundlagen/neutral/one-two-circle).

## Control Zone

Die **Control Zone** ist eine geometrische Position hinter dem Gegner, aus der du trotz seiner Manöver hinter ihm bleiben kannst: Egal ob er bricht, umkehrt oder ausweicht – du hast genug Abstand und Winkel, um zu reagieren, ohne vor seine 3/9-Linie zu geraten.

- **Richtwert:** etwa **30–60° AA** und **einige tausend Fuß** Range, abhängig von Jets und Speed. Im Spiel testen.
- **Zu nah** oder zu viel Closure: Er bricht, du schießt vorbei.
- **Zu weit:** Er kann drehen und neutralisieren, bevor du nachkommst.

Die Control Zone ist **keine Waffenreichweite**. Sie ist der Ort, von dem aus du in Ruhe eine Schussgelegenheit aufbaust.

## WEZ: Gun vs. Fox 2

Die **WEZ** (Weapons Engagement Zone) ist der Raum, in dem eine Waffe treffen kann. Sie wird begrenzt durch **Mindest- und Maximalreichweite**, **Off-Boresight** (wie weit der Gegner von deiner Nase weg sein darf) und **Aspect** (aus welchem Winkel zu ihm).

| | Bordkanone | IR-Rakete (Fox 2) |
|---|---|---|
| Reichweite | Kurz | Deutlich größer als die Gun, mit Mindestreichweite |
| Nase | Muss vor ihn zeigen (Lead) | Suchkopf muss ihn sehen, etwas Off-Boresight möglich |
| Aspect | Jeder Winkel, Tracking am einfachsten bei kleiner AA | Von hinten am zuverlässigsten; Community berichtet Treffer auch frontal |
| Gegenmittel | Jinken, aus der Ebene | Flares, Break, Idle |

Die Logik im Kampf: **Die Fox 2 zwingt ihn zu Flares und Defensive – damit gibt er Energie oder Position ab, und dann kommt die Gun.** Ein One-Circle-Kampf kann so eng werden, dass du unter der Mindestreichweite der Rakete bist; im Two-Circle bekommt der schneller drehende Jet den ersten Fox-2-Schuss. Details: [Schusslösung](/grundlagen/offensiv/schussloesung) und [Waffen](/avionik/waffen).

::: info IM SPIEL PRÜFEN
- Gun-Reichweite, in der der Funnel sinnvoll Treffer bringt.
- Mindest- und Maximalreichweite der IR-Rakete, maximaler Off-Boresight-Winkel, Frontal-Treffer (All-Aspect).
- In vielen Lobbys und im Ranked 1v1 sind Raketen aus (Guns-only) – dann ist die Gun-WEZ alles.
:::

::: tip MERKE
- **AA** = wo du relativ zu ihm stehst. **ATA** = wohin du zeigst. **HCA** = Winkel zwischen euren Flugrichtungen.
- **Hinter seiner 3/9-Linie** bleiben. Wer davor rutscht, tauscht die Rollen.
- **LOS-Rate** lesen: Wandert er Richtung Nase, gewinnst du.
- **In seinen Kreis** kommst du über Lag, aus seiner Ebene raus über Rollen.
- **Control Zone** ist Position, **WEZ** ist Waffe – erst das eine, dann das andere.
:::

Weiter: [Verfolgungskurven](/grundlagen/verfolgungskurven)
