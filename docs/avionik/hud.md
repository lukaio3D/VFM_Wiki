# Head-Up Display (HUD)

> Die HUD-Elemente, die dir im Dogfight wirklich helfen: Gun-Funnel, Boresight-Kreuz, AoA-Zahl und Beschleunigungs-Indikator.

Das HUD ist in allen drei Jets identisch. Diese Seite trennt **gesicherte Elemente** (aus den Patchnotes) von solchen, die bisher nur beobachtet oder vermutet wurden.

## Gesichert (Patchnotes)

| Element | Seit | Wofür |
|---|---|---|
| **Gun-Funnel** (EEGS-artig) | Release | Zielhilfe für die Kanone mit Vorhalt |
| **Funnel ohne Lock: Durchschnitts-Spannweite** | v1.2.8 | Funnel funktioniert auch ohne Radar-Lock |
| **Gun-Boresight-Kreuz** | v1.3.1 | Zeigt, wohin die Kanone ohne Vorhalt zeigt |
| **AoA-Zahl** | v1.2.0 | Aktueller Anstellwinkel als Zahl |
| **Beschleunigungs-Indikator (Kreis)** | v1.2.7 | Zeigt, ob du gerade Speed gewinnst oder verlierst |

## Gun-Funnel

Der Funnel (Trichter) ist eine Vorhaltehilfe nach dem Prinzip des **EEGS** (Enhanced Envelope Gun Sight): Zwei Linien zeigen, wo deine Geschosse in den nächsten Momenten fliegen werden, wenn du deine aktuelle Kurve beibehältst. Der Abstand zwischen den Linien entspricht an jeder Stelle der **Spannweite eines Ziels** in der dazugehörigen Entfernung.

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

So benutzt du ihn:

1. **Ebene zuerst.** Roll deinen Lift Vector in seine Bewegungsebene. Dann läuft der Funnel entlang seiner Flugbahn und er bleibt länger darin.
2. **Ziel in den Funnel bringen**, dort, wo seine Flügelspitzen beide Linien berühren.
3. **Feuern, solange das passt.** Bei einem **Tracking Shot** hältst du ihn im Funnel; bei einem **Snapshot** läuft er durch den Funnel und du feuerst kurz vorher, sodass die Geschosse ihn kreuzen.

**Ohne Lock** rechnet der Funnel mit einer **durchschnittlichen Spannweite** (v1.2.8). Er stimmt dann nur ungefähr. **Mit Radar-Lock** kennt das System die echte Entfernung und liefert eine bessere Lösung (siehe [Radar](/avionik/radar)).

Ausführlich zu Schusstypen und Waffenreichweite: [Schusslösung](/grundlagen/offensiv/schussloesung).

::: info IM SPIEL PRÜFEN
- Haben die drei Jets unterschiedliche Spannweiten? Falls ja, passt der Funnel ohne Lock bei manchen Gegnern systematisch zu weit oder zu eng.
- Wie sieht die Lock-Anzeige im HUD aus (Zielmarkierung, Entfernung)?
:::

## Gun-Boresight-Kreuz

Das Boresight-Kreuz (seit v1.3.1) zeigt die Richtung, in die die Kanone **ohne Vorhalt** zeigt – also die Waffenachse. Nützlich:

- **Head-on-Schuss** (falls in der Lobby erlaubt): Bei hoher Closure und kleinem Winkel ist der Vorhalt klein; das Kreuz zeigt dir, wo die Geschosse hingehen.
- **Referenz für die Nase:** Wo zeigt deine Nase gerade, relativ zum Gegner? Hilfreich, um Lead, Pure und Lag zu erkennen (siehe [Verfolgungskurven](/grundlagen/verfolgungskurven)).

## AoA-Zahl

Die AoA-Zahl (seit v1.2.0) zeigt deinen aktuellen Anstellwinkel. Damit erkennst du:

- **Wann der AoA-Limiter greift.** Merke dir, bei welchem Wert dein Jet normalerweise begrenzt. Alles darüber geht nur mit dem Override ("Cobra-Button").
- **Wie hart du gerade ziehst**, wenn du langsam bist und die G-Anzeige wenig aussagt.

::: info IM SPIEL PRÜFEN
- Bei welchem AoA greift der Limiter in jedem Jet?
- Welche AoA-Werte erreichst du mit Override, und ab wann wird der Jet unkontrollierbar?
:::

## Beschleunigungs-Indikator

Der Kreis (seit v1.2.7) zeigt, ob du **gerade beschleunigst oder verzögerst**. Das ist im Kern das Vorzeichen von **Ps** (spezifische Überschussleistung): Ps > 0 = du gewinnst Energie, Ps < 0 = du verlierst Energie. Mehr dazu: [Energie-Management](/grundlagen/energie-management).

Warum das wertvoll ist: Die Speed-Zahl sagt dir, wo du **bist**. Der Indikator sagt dir, wohin du **gehst** – früher, als du es an der Zahl merkst.

So nutzt du ihn (Tipps):

- **Sustained Turn finden:** Zieh im Turn so, dass der Indikator neutral steht (weder Gewinn noch Verlust). Dann fliegst du auf der Sustained-Linie, Ps = 0. Ziehst du mehr, verlierst du Speed; weniger, und du gewinnst.
- **Unload kontrollieren:** Beim Unload (Lift nahe null, volle Leistung) sollte der Indikator klar Beschleunigung zeigen. Wenn nicht: Du ziehst noch zu viel.
- **Bleed bewusst einsetzen:** Willst du Speed abbauen (z.B. auf Corner Speed), zeigt er dir, wie schnell das geht.
- **Im Kampf ein kurzer Blick:** "Verliere ich gerade Energie, ohne Winkel zu gewinnen?" Wenn ja, ändere etwas.

::: info IM SPIEL PRÜFEN
- Wie genau wird die Beschleunigung dargestellt (Position relativ zu einem anderen Symbol, Größe, Farbe)?
- Wo ist der neutrale Punkt?
:::

## Weitere Elemente (laut Beobachtung, Stand Dez 2025)

Eine frühere Version dieses Wikis beschreibt folgende Elemente. Sie sind plausibel, aber nicht durch Patchnotes bestätigt:

| Element | Laut Beobachtung |
|---|---|
| **Geschwindigkeit** | Links, vermutlich KIAS |
| **Mach** | Links, unter der Geschwindigkeit |
| **G** | Links, aktuelle Lastvielfache |
| **Waffe / Munition** | Links, gewählte Waffe und Anzahl |
| **Höhe** | Rechts, in Fuß |
| **Steig-/Sinkanzeige** | Rechts |
| **Kurs** | Band oben |
| **Velocity Vector** | Zeigt, wohin der Jet tatsächlich fliegt (nicht wohin die Nase zeigt) |
| **Zielmarkierung bei Lock** | Box um den Gegner |

::: info IM SPIEL PRÜFEN
- Gibt es einen Velocity Vector (Flight Path Marker)? Wenn ja: Im Turn liegt er unterhalb der Nase, der Abstand entspricht ungefähr dem AoA.
- Format der Geschwindigkeit: KIAS, TAS oder Mach?
- Wird die Höhe barometrisch (über Meer) oder über Grund angezeigt?
- Gibt es eine Treibstoffanzeige im HUD?
:::

## Greyout und Blackout

Greyout (Sichtfeld wird grau und eng) und Blackout (Sicht weg) sind simuliert. Bei welcher G-Last und nach welcher Dauer sie einsetzen, ist nicht dokumentiert.

**Was das heißt:** Ein zu langer, harter Pull kann dir den Gegner aus dem Blick nehmen – und damit den Kampf. Ziehe so hart, wie es die Situation braucht, nicht reflexhaft immer bis 9 G.

::: info IM SPIEL PRÜFEN
- Ab welcher G-Last und Dauer setzt Greyout ein, wie schnell erholt sich die Sicht?
- Gibt es Redout bei negativer G-Last?
:::

::: tip MERKE
- Funnel: Ebene des Gegners treffen, Flügelspitzen an die Linien, dann feuern.
- Ohne Lock nutzt der Funnel eine Durchschnitts-Spannweite – mit Lock ist er genauer.
- Boresight-Kreuz = Kanonenachse ohne Vorhalt; AoA-Zahl zeigt, wann der Limiter greift.
- Der Beschleunigungs-Indikator zeigt das Vorzeichen von Ps: neutral = Sustained Turn, beim Unload deutlich positiv.
- Greyout/Blackout existieren – unnötig langes Ziehen kostet Sicht und Tally.
:::

Weiter: [RWR & MWS](/avionik/rwr)
