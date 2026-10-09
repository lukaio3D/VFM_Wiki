# One-Circle vs. Two-Circle

> Nach dem Merge entscheidet die Drehrichtung beider Jets, ob ein Radius- oder ein Rate-Kampf entsteht. Wähl den Flow, den dein Jet gewinnt.

Am [Merge](/grundlagen/neutral/der-merge) dreht ihr beide. Ob ihr in dieselbe oder in entgegengesetzte Richtung dreht, legt die Geometrie des ganzen Kampfes fest, und damit, welche Flugleistung zählt: **Turn Rate** (Grad pro Sekunde) oder **Wenderadius** (wie eng). Die Grundlagen dazu stehen unter [Kurvenphysik](/grundlagen/kurvenphysik), die Begriffe im [Glossar](/grundlagen/begriffe).

## Die Geometrie

Beide Skizzen zeigen die Draufsicht nach einem **Links-an-Links-Pass**: Jeder hat den anderen auf seiner linken Seite passiert.

### One-Circle: entgegengesetzter Drehsinn

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Draufsicht One-Circle: Nach einem Links-an-Links-Pass dreht der eigene Jet links, der Bandit rechts. Beide fliegen auf praktisch demselben Kreis in entgegengesetzter Richtung und treffen sich nach etwa 180 Grad Nase an Nase wieder.">
<circle cx="268" cy="150" r="100" fill="none" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="4 4"/>
<circle cx="252" cy="150" r="100" fill="none" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="4 4"/>
<line x1="368" y1="290" x2="368" y2="150" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<polygon points="368,212 363,222 373,222" fill="var(--vp-c-brand-1)"/>
<path d="M 368 150 A 100 100 0 0 0 174 116" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<polygon points="260,50 269,45 269,55" fill="var(--vp-c-brand-1)"/>
<polygon points="174,116 182,108 173,105" fill="var(--vp-c-brand-1)"/>
<line x1="352" y1="10" x2="352" y2="150" stroke="var(--vp-c-danger-1)" stroke-width="2.5"/>
<polygon points="352,88 347,78 357,78" fill="var(--vp-c-danger-1)"/>
<path d="M 352 150 A 100 100 0 0 1 158 184" fill="none" stroke="var(--vp-c-danger-1)" stroke-width="2.5"/>
<polygon points="244,250 253,245 253,255" fill="var(--vp-c-danger-1)"/>
<polygon points="158,184 166,192 157,195" fill="var(--vp-c-danger-1)"/>
<text x="378" y="285" font-size="12" fill="currentColor">Du</text>
<text x="362" y="22" font-size="12" fill="currentColor">Bandit</text>
<text x="378" y="154" font-size="12" fill="currentColor">Merge (Links an Links)</text>
<text x="110" y="28" font-size="12" fill="currentColor">Du: Linkskurve (zu ihm hin)</text>
<text x="120" y="285" font-size="12" fill="currentColor">Bandit: Rechtskurve (weg)</text>
<text x="14" y="140" font-size="12" fill="currentColor">nach ~180°:</text>
<text x="14" y="156" font-size="12" fill="currentColor">Nase an Nase</text>
<text x="14" y="172" font-size="12" fill="currentColor">(Rechts an Rechts)</text>
</svg>

- Du drehst links (zum Gegner hin), er dreht rechts (von dir weg), oder umgekehrt.
- Ihr fliegt auf **praktisch einem gemeinsamen Kreis** in entgegengesetzter Richtung. Die beiden gestrichelten Kreise liegen nur um den seitlichen Versatz beim Pass auseinander.
- Nach etwa 180° trefft ihr euch **Nase an Nase** wieder, diesmal Rechts an Rechts.
- Wer den **kleineren Radius** hat, kommt dort mit der Nase zuerst auf den anderen. Der Abstand bleibt klein (höchstens etwa ein Kreisdurchmesser).

### Two-Circle: gleicher Drehsinn

<svg viewBox="0 0 520 300" width="100%" style="max-width:520px" role="img" aria-label="Draufsicht Two-Circle: Nach einem Links-an-Links-Pass drehen beide Jets links, also zueinander hin. Jeder fliegt auf seinem eigenen Kreis, beide im gleichen Drehsinn. Nach 90 Grad zeigen die Hecks zueinander, nach 180 Grad sind beide maximal weit auseinander.">
<circle cx="188" cy="150" r="80" fill="none" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="4 4"/>
<circle cx="332" cy="150" r="80" fill="none" stroke="var(--vp-c-text-2)" stroke-width="1" stroke-dasharray="4 4"/>
<line x1="268" y1="290" x2="268" y2="150" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<polygon points="268,242 263,252 273,252" fill="var(--vp-c-brand-1)"/>
<path d="M 268 150 A 80 80 0 0 0 108 150" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2.5"/>
<polygon points="180,70 189,65 189,75" fill="var(--vp-c-brand-1)"/>
<polygon points="108,158 103,148 113,148" fill="var(--vp-c-brand-1)"/>
<line x1="252" y1="10" x2="252" y2="150" stroke="var(--vp-c-danger-1)" stroke-width="2.5"/>
<polygon points="252,58 247,48 257,48" fill="var(--vp-c-danger-1)"/>
<path d="M 252 150 A 80 80 0 0 0 412 150" fill="none" stroke="var(--vp-c-danger-1)" stroke-width="2.5"/>
<polygon points="340,230 331,225 331,235" fill="var(--vp-c-danger-1)"/>
<polygon points="412,142 407,152 417,152" fill="var(--vp-c-danger-1)"/>
<text x="276" y="285" font-size="12" fill="currentColor">Du</text>
<text x="208" y="22" font-size="12" fill="currentColor">Bandit</text>
<text x="276" y="170" font-size="12" fill="currentColor">Merge</text>
<text x="160" y="154" font-size="12" fill="currentColor">Kreis Du</text>
<text x="300" y="154" font-size="12" fill="currentColor">Kreis Bandit</text>
<text x="40" y="44" font-size="12" fill="currentColor">Du: Linkskurve (zu ihm hin)</text>
<text x="300" y="268" font-size="12" fill="currentColor">Bandit: Linkskurve (zu dir hin)</text>
</svg>

- Ihr dreht beide links, also beide zueinander hin, jeder Richtung Heck des anderen. (Drehen beide **weg** voneinander, ist es ebenfalls Two-Circle, nur mit mehr Abstand.)
- Jeder fliegt auf **seinem eigenen Kreis**, beide im **gleichen Drehsinn** (in der Skizze beide gegen den Uhrzeigersinn).
- Nach 90° zeigen eure Hecks zueinander (**nose-to-tail**). Wer schneller dreht, kommt zuerst herum und zeigt mit der Nase auf das Heck des anderen.
- Der Abstand wird groß: nach 180° etwa zwei Kreisdurchmesser.

### Merkhilfe

| Nach dem Pass | Flow | Entscheidend |
|---|---|---|
| beide drehen zueinander hin | Two-Circle | Turn Rate |
| beide drehen voneinander weg | Two-Circle (weiter) | Turn Rate |
| einer hin, einer weg | One-Circle | Wenderadius |

## Wer gewinnt was

### Two-Circle ist ein Rate-Kampf

- **Die ersten ~180° gewinnt die Instant Rate**: Wer am Merge schneller die Nase herumbekommt (und den besseren [Lead Turn](/grundlagen/neutral/der-merge) geflogen ist), liegt nach dem ersten halben Kreis vorn.
- Danach zählt die **Sustained Rate**: Wer seine Turn Rate halten kann, ohne Speed zu verlieren, holt Grad für Grad auf.
- Der große Abstand gibt dem schneller drehenden Jet den **ersten Fox-2-Schuss** (IR-Rakete), bevor es eng genug für die Kanone wird.
- Rate-Spezialisten wollen Two-Circle.

### One-Circle ist ein Radius-Kampf

- Wer den **kleineren Radius** hat, bekommt beim nächsten Treffen die Nase zuerst auf den Gegner.
- Weil der Radius mit dem Quadrat der Speed wächst (r = V² / (g·√(n²−1))), werden beide **immer langsamer**. One-Circle endet fast immer im Low-Speed-Kampf, oft in [Scissors](/grundlagen/neutral/scissors).
- Der Abstand bleibt klein. Das kann dich **unter die Mindestreichweite** der IR-Rakete bringen, und dann zählt nur noch die Kanone.
- Radius-Spezialisten wollen One-Circle.

::: info IM SPIEL PRÜFEN
- Die Mindestreichweite der IR-Rakete in VFM ist nicht dokumentiert. Teste, ab welchem Abstand die Rakete noch zuverlässig trifft, bevor du einen One-Circle bewusst als „Raketenschutz“ einsetzt.
:::

| | Two-Circle | One-Circle |
|---|---|---|
| Drehsinn | gleich | entgegengesetzt |
| Kreise | zwei | einer (praktisch) |
| Begegnung | nose-to-tail | Nase an Nase nach ~180° |
| Gewinnt | höhere Rate (erst Instant, dann Sustained) | kleinerer Radius |
| Speed | bleibt eher im Band um Best-Sustained | fällt stark |
| Abstand | groß, Raum für Fox 2 | klein, oft nur Guns |

## Wer wählt den Flow?

Den Flow bestimmt ihr **beide**. Keiner kann ihn allein erzwingen:

- Willst du Two-Circle und drehst zu ihm hin, kann er weg drehen und es wird One-Circle. Umgekehrt genauso.
- Wer **später** festlegt, sieht die Entscheidung des anderen und kann darauf reagieren. Wer **früher** dreht (Lead Turn), gewinnt Winkel, legt sich aber fest. Das ist der Grundkonflikt am Merge.
- Bei jedem weiteren Pass wird neu entschieden. Ein One-Circle kann beim nächsten Pass zum Two-Circle werden und umgekehrt.

## Den bevorzugten Flow des Gegners verweigern

1. **Speed kontrollieren**: Ein One-Circle-Jet will dich langsam machen. Folge ihm nicht unter dein Band. Ein Two-Circle-Jet will sein Speedband halten. Mach den Kampf schneller oder langsamer als dieses Band.
2. **Beim nächsten Pass umdrehen**: Wenn er dir den falschen Flow aufgezwungen hat, wähle beim nächsten Pass die Drehrichtung neu.
3. **Ebene wechseln**: Ein Pitch-back oder eine Kurve schräg nach oben oder unten macht aus einem flachen Rate- oder Radius-Duell einen Kampf in der Vertikalen, siehe [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf).
4. **Pass-Geometrie steuern**: Ein Rate-Jet braucht seitlichen Versatz (Turning Room) für den Lead Turn. Ein Radius-Jet will einen engen Pass. Verkleinere oder vergrößere den Versatz vor dem Merge entsprechend.
5. **Nicht mitspielen**: Blow-Through und Extend, dann ein neuer Merge unter deinen Bedingungen ([Separation](/grundlagen/defensiv/separation)).

## Flow-Wahl in VFM: alle 9 Paarungen

Grundlage sind die Ingame-Daten (Stand Dez 2025, vor Patch v1.1) und die Speedbänder aus dem [Flugzeugvergleich](/flugzeuge/vergleich). Kurz:
- Die **T-15** hat die beste Instant Rate, die niedrigste Corner Speed und die beste Sustained Rate über ~500 KIAS.
- Die **T-16** hat die beste Sustained Rate, aber nur bei ~420–500 KIAS, am stärksten in Bodennähe.
- Die **T-18** ist unter ~380 KIAS stark und bricht über ~480 KIAS ein.

Es ist kein Stein-Schere-Papier, sondern eine Frage des **Speedbands**.

| Du | Gegner | Dein Flow | Ziel-Speed | Was du verweigerst | Details |
|---|---|---|---|---|---|
| T-15 | T-15 | kein Flow-Vorteil: Energie und Pilot entscheiden. Two-Circle mit vertikaler Komponente, wenn du mehr Energie hast. | ~400–495 KIAS | den Lead Turn | [T-15](/flugzeuge/t15) |
| T-15 | T-16 | **One-Circle langsam** (unter ~380 KIAS) **oder schnell/vertikal** (über ~500 KIAS). Den ersten Turn gewinnst du per Instant Rate. | < 380 oder > 500 | flaches Two-Circle bei 420–500 KIAS in Bodennähe | [T-15 vs T-16](/flugzeuge/matchups/t15-vs-t16) |
| T-15 | T-18 | **Two-Circle schnell und vertikal**, Energie ausspielen | > 450 KIAS | einen langsamen One-Circle unter ~250 KIAS | [T-15 vs T-18](/flugzeuge/matchups/t15-vs-t18) |
| T-16 | T-15 | **Two-Circle tief** im Band 420–500. Den ersten Turn nicht erzwingen (er hat die bessere Instant Rate). Lieber nose-low drehen, Speed halten, dann über Sustained Rate aufholen. | ~420–500 KIAS | Vertikale und langsamen One-Circle | [T-15 vs T-16](/flugzeuge/matchups/t15-vs-t16) |
| T-16 | T-16 | **Two-Circle tief**, beide wollen ihn. Energie und Lift-Vector-Disziplin entscheiden. | ~420–500 KIAS | jeden Speedverlust unter ~420 | [T-16](/flugzeuge/t16) |
| T-16 | T-18 | **Two-Circle tief** | ~420–500 KIAS, ideal um 470 | One-Circle unter ~380 KIAS | [T-16 vs T-18](/flugzeuge/matchups/t16-vs-t18) |
| T-18 | T-15 | **One-Circle langsam und tief**. Laut Daten ist die T-15 auch dort im dargestellten Bereich gut. Dein vermuteter Vorteil liegt noch tiefer (sehr langsam, hoher AoA, Override): Hypothese, testen. | < 350 KIAS | Two-Circle und Vertikale | [T-15 vs T-18](/flugzeuge/matchups/t15-vs-t18) |
| T-18 | T-16 | **One-Circle** | < 380 KIAS | Two-Circle über ~420 KIAS | [T-16 vs T-18](/flugzeuge/matchups/t16-vs-t18) |
| T-18 | T-18 | kein Flow-Vorteil. One-Circle liegt nahe, dann gewinnt, wer besser langsam fliegt und seine Energie einteilt. | < 380 KIAS | Kampf über ~480 KIAS (beide verlieren dort Energie) | [T-18](/flugzeuge/t18) |

::: warning Daten sind kein Ersatz für Testen
Die Werte stammen aus der Zeit vor Patch v1.1. Seitdem hat die T-15 Lift verloren und Schub gewonnen (v1.1). Mit v1.4.1 wurden Top-Speeds und das Treibstoffgewicht der T-16 geändert. Die Reihenfolge der Speedbänder ist plausibel, die exakten Grenzen nicht. Prüfe sie mit den Übungen unter [Trainingsplan](/grundlagen/uebungen).
:::

::: info IM SPIEL PRÜFEN
- Wie sich alle Jets **unter ~170 KIAS** und mit AoA-Override verhalten. Dafür gibt es keine Daten, und genau dort soll laut Entwickler die Stärke der T-18 liegen.
:::

::: tip MERKE
- Gleicher Drehsinn = Two-Circle = Rate-Kampf. Entgegengesetzter Drehsinn = One-Circle = Radius-Kampf.
- Die ersten ~180° eines Two-Circle gewinnt die Instant Rate, danach die Sustained Rate.
- One-Circle macht den Kampf langsam und eng, oft unter der Mindestreichweite der Rakete.
- Keiner kann den Flow allein erzwingen. Kontrolliere Speed, Pass-Geometrie und Ebene.
- In VFM entscheidet das Speedband: T-16 schnell im Band, T-18 langsam, T-15 meidet das Band der T-16 und den Bereich sehr langsamer Speed der T-18.
:::

Weiter: [Scissors](/grundlagen/neutral/scissors)
