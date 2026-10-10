# Head-Up Display (HUD)

> Was dir das HUD im Dogfight sagt: Gun-Funnel, Drehrate, Speed, α und ob du gerade Energie gewinnst.

Das HUD ist in allen drei Jets identisch.

## Die Anzeigen im Überblick

| Position | Anzeige |
|---|---|
| **Oben links** | **G** (Lastvielfaches) und **Drehrate** in °/s |
| **Darunter** | **Speed in KIAS**, **Mach** und **α** (Anstellwinkel, seit v1.2.0) |
| **Rechts** | **Höhe** |
| **Unten rechts** | **„BRAKE“**, solange die Speedbrake ausgefahren ist |
| **Mitte** | **Gun-Funnel** (seit Release), **Gun-Boresight-Kreuz** (v1.3.1), **Beschleunigungs-Indikator** (v1.2.7) |

Beobachtet, aber nicht bestätigt: Kursband oben, Steig-/Sinkanzeige rechts, gewählte Waffe und Munition links, Velocity Vector, Box um ein gelocktes Ziel.

## Drehrate und G: dein Messgerät im Turn

Die Drehrate in °/s zeigt dir direkt, was die Leistungsdiagramme versprechen. Zusammen mit dem Beschleunigungs-Indikator findest du so deinen besten Sustained Turn: Indikator neutral, Drehrate ablesen. Bei ~450 KIAS auf 10.000 ft sind das gemessen 15,4 °/s (T-15), 17,6 °/s (T-16) und 15,6 °/s (T-18). Alle Werte: [Flugzeugvergleich](/flugzeuge/vergleich).

Die G-Zahl zeigt, wie nah du am 9-G-Limit bist. Bei niedriger Speed sagt sie wenig über deinen Zug; dann schau auf α.

## Gun-Funnel

Der Funnel (Trichter) ist eine Vorhaltehilfe nach dem Prinzip des **EEGS** (Enhanced Envelope Gun Sight): Zwei Linien zeigen, wo deine Geschosse fliegen, wenn du deine Kurve beibehältst. Ihr Abstand entspricht an jeder Stelle der **Spannweite eines Ziels** in der zugehörigen Entfernung.

<svg viewBox="0 0 320 220" width="100%" style="max-width:520px" role="img" aria-label="Gun-Funnel: zwei Linien, unten weit, oben eng. Ein Ziel, dessen Flügelspitzen beide Linien berühren, ist in der passenden Entfernung.">
<path d="M70 210 Q120 120 145 20" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2"/>
<path d="M250 210 Q200 120 175 20" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2"/>
<line x1="118" y1="100" x2="202" y2="100" stroke="var(--vp-c-danger-1)" stroke-width="3"/>
<line x1="160" y1="92" x2="160" y2="112" stroke="var(--vp-c-danger-1)" stroke-width="3"/>
<text x="210" y="96" font-size="12" fill="currentColor">Ziel: Flügel berühren</text>
<text x="210" y="110" font-size="12" fill="currentColor">beide Linien → feuern</text>
<text x="10" y="200" font-size="12" fill="currentColor">nah</text>
<text x="10" y="30" font-size="12" fill="currentColor">weit</text>
<line x1="35" y1="190" x2="35" y2="40" stroke="var(--vp-c-text-2)" stroke-width="1"/>
</svg>

1. **Ebene zuerst.** Roll deinen Lift Vector in seine Bewegungsebene, dann läuft der Funnel entlang seiner Flugbahn.
2. **Ziel in den Funnel**, dort, wo seine Flügelspitzen beide Linien berühren.
3. **Feuern, solange das passt.** Tracking Shot: Du hältst ihn im Funnel. Snapshot: Er läuft durch, du feuerst kurz vorher.

**Ohne Lock** rechnet der Funnel mit einer **durchschnittlichen Spannweite** (v1.2.8) und stimmt nur ungefähr. **Mit Radar-Lock** kennt er die echte Entfernung (siehe [Radar](/avionik/radar)). Schusstypen und Reichweite: [Schusslösung](/grundlagen/offensiv/schussloesung).

## Gun-Boresight-Kreuz

Das Kreuz zeigt die Kanonenachse **ohne Vorhalt**:

- **Head-on-Schuss** (falls erlaubt): Bei kleinem Winkel ist der Vorhalt klein, das Kreuz zeigt, wohin die Geschosse gehen.
- **Referenz für die Nase:** Wo zeigt sie relativ zum Gegner? So erkennst du Lead, Pure und Lag (siehe [Verfolgungskurven](/grundlagen/verfolgungskurven)).

## α (AoA)

Die α-Zahl zeigt, wie hart du gerade ziehst, gerade wenn du langsam bist und die G wenig aussagen. Voll gezogen stoppt der Limiter gemessen bei ~24–25° (T-15) und ~23° (T-16). Die T-18 geht bis 35°, hat ihre meisten G aber bei ~26°: Halte dort zum Kurven und nimm 35° nur für den Snapshot. Mehr nur mit Override (siehe [Das VFM-Flugmodell](/grundlagen/physik#anstellwinkel-aoa-limiter-und-override)).

## Beschleunigungs-Indikator

Der Kreis zeigt, ob du **gerade beschleunigst oder verzögerst**, also das Vorzeichen von **Ps** (siehe [Energie-Management](/grundlagen/energie-management)). Die Speed-Zahl sagt dir, wo du **bist**; der Indikator sagt dir, wohin du **gehst**.

- **Sustained Turn:** Zieh so, dass er neutral steht. Mehr Zug kostet Speed, weniger bringt Speed.
- **Unload:** Er muss klar Beschleunigung zeigen. Wenn nicht, ziehst du noch.
- **Bleed:** Er zeigt, wie schnell du Speed abbaust, etwa auf Corner Speed.
- **Im Kampf:** „Verliere ich Energie, ohne Winkel zu gewinnen?“ Wenn ja, ändere etwas.

## Greyout und Blackout

Beides ist simuliert. Ein zu langer, harter Zug kann dir den Gegner aus dem Blick nehmen. Zieh so hart, wie die Situation es braucht, nicht reflexhaft bis 9 G (siehe [Golden Rules](/grundlagen/golden-rules#g-awareness-greyout-und-blackout)).

::: info IM SPIEL PRÜFEN
- Wie sieht die Lock-Anzeige aus, und haben die Jets unterschiedliche Spannweiten (dann liegt der Funnel ohne Lock systematisch daneben)?
- Welche α-Werte erreichst du mit Override?
- Ab welcher G-Last und nach welcher Dauer setzt Greyout ein?
:::

::: tip MERKE
- Oben links G und Drehrate, darunter KIAS, Mach und α, rechts die Höhe, unten rechts „BRAKE“.
- Funnel: Ebene des Gegners treffen, Flügelspitzen an die Linien, dann feuern. Mit Lock genauer.
- Indikator neutral + Drehrate ablesen = dein Sustained Turn.
- α zeigt den Zug bei niedriger Speed; die T-18 kurvt bei ~26°, 35° nur für den Snapshot.
- Unnötig langes Ziehen kostet Sicht und Tally.
:::

Weiter: [RWR & MWS](/avionik/rwr)
