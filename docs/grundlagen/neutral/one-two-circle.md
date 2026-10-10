# One-Circle vs. Two-Circle

> Nach dem Merge entscheidet die Drehrichtung beider Jets, ob ein Radius- oder ein Rate-Kampf entsteht. Wähl den Flow, den dein Jet gewinnt.

Ob ihr nach dem [Merge](/grundlagen/neutral/der-merge) in dieselbe oder in entgegengesetzte Richtung dreht, legt fest, welche Flugleistung zählt: **Turn Rate** (Grad pro Sekunde) oder **Wenderadius** (wie eng). Grundlagen: [Kurvenphysik](/grundlagen/kurvenphysik).

## Die Geometrie

Beide Skizzen zeigen die Draufsicht nach einem **Links-an-Links-Pass**.

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

- Einer dreht zum Gegner hin, der andere von ihm weg. Ihr fliegt auf **praktisch einem Kreis** in entgegengesetzter Richtung.
- Nach etwa 180° trefft ihr euch **Nase an Nase** wieder. Wer den **kleineren Radius** hat, bekommt dort zuerst die Nase auf den anderen.
- Der Abstand bleibt klein, höchstens etwa ein Kreisdurchmesser.

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

- Beide drehen zueinander hin (oder beide voneinander weg, dann mit mehr Abstand). Jeder fliegt **seinen eigenen Kreis**, beide im **gleichen Drehsinn**.
- Nach 90° zeigen die Hecks zueinander (**nose-to-tail**). Wer schneller dreht, kommt zuerst mit der Nase auf das Heck des anderen.
- Der Abstand wird groß: nach 180° etwa zwei Kreisdurchmesser.

## Wer gewinnt was

| | Two-Circle | One-Circle |
|---|---|---|
| Entsteht, wenn | beide zueinander oder beide voneinander weg drehen | einer hin, einer weg dreht |
| Entscheidend | **Turn Rate**: zuerst Instant (nur nahe Corner Speed), dann Sustained | **Wenderadius** |
| Speed | bleibt eher im Band um Best Sustained | fällt stark, endet oft in [Scissors](/grundlagen/neutral/scissors) |
| Abstand | groß, Raum für Fox 2 | klein, oft nur Guns |
| Wer ihn will | Rate-Jets | Radius-Jets |

**Two-Circle:** Den ersten halben Kreis gewinnt die bessere Instant Rate, aber nur, wenn beide nahe Corner Speed ankommen. Aus 450 KIAS (Ranked-Start) ist der erste Turn fast ausgeglichen, siehe [Der erste Turn aus 450 KIAS](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen). Danach holt Grad für Grad auf, wer die höhere Sustained Rate hat.

**One-Circle:** Der Radius wächst mit dem Quadrat der Speed, also werden beide immer langsamer. Der Kampf wird eng, oft enger als die Mindestreichweite einer IR-Rakete.

## Wer wählt den Flow?

Den Flow bestimmt ihr **beide**, keiner kann ihn allein erzwingen. Drehst du zu ihm hin, um einen Two-Circle zu bekommen, kann er weg drehen, und es wird One-Circle. Wer **früher** dreht (Lead Turn), gewinnt Winkel, legt sich aber fest. Wer **später** dreht, sieht die Entscheidung des anderen. Bei jedem Pass wird neu entschieden.

## Den bevorzugten Flow des Gegners verweigern

1. **Speed kontrollieren:** Ein One-Circle-Jet will dich langsam machen, folge ihm nicht unter dein Band. Einem Two-Circle-Jet nimmst du sein Band, indem du den Kampf schneller oder langsamer machst.
2. **Beim nächsten Pass umdrehen:** die Drehrichtung neu wählen.
3. **Ebene wechseln:** Pitch-back oder schräge Kurve macht aus dem flachen Duell einen [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf).
4. **Pass-Geometrie steuern:** Ein Rate-Jet braucht Versatz für den Lead Turn, ein Radius-Jet will einen engen Pass.
5. **Nicht mitspielen:** Blow-Through, Extend, neuer Merge unter deinen Bedingungen ([Separation](/grundlagen/defensiv/separation)).

## Flow-Wahl in VFM

Es ist kein Stein-Schere-Papier, sondern eine Frage des **Speedbands**: Die T-16 dreht dauerhaft am besten bei ~420–500 KIAS, die T-15 über ~520 KIAS und bei gleicher niedriger Speed (meiste G), die T-18 will den Kampf langsam machen und bricht über ~480–510 KIAS ein. Die vollständigen Merge-Strategien je Paarung stehen in der [Merge-Matrix](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias). Für die Flow-Wahl reicht:

| Du fliegst | gegen T-15 | gegen T-16 | gegen T-18 |
|---|---|---|---|
| **T-15** | kein Flow-Vorteil; wer unnötig voll zieht, verliert | **One-Circle langsam** (300–380 KIAS) oder Blow-Through und von oben; kein flacher Kreis bei 400–500 | schnell (> 500 KIAS, vertikal) oder langsam bei mehr G; kein Lag-Kreisen bei ~450 |
| **T-16** | **Two-Circle** bei ~450–470 KIAS, tief; nicht in die Vertikale folgen | **Two-Circle**, nie unter ~420 KIAS | **Two-Circle** bei ~450–470 KIAS; kein One-Circle unter ~380 |
| **T-18** | **One-Circle** sehr langsam, tief; Two-Circle und Vertikale meiden | **One-Circle** unter ~380 KIAS; Two-Circle über ~420 meiden | One-Circle; wer besser langsam fliegt, gewinnt |

::: info IM SPIEL PRÜFEN
- Wie sich die Jets **unter ~280 KIAS** und mit AoA-Override verhalten. Dort soll laut Entwickler die Stärke der T-18 liegen (Hypothese).
- Die Mindestreichweite der IR-Rakete, bevor du einen One-Circle als Raketenschutz einsetzt.
:::

::: tip MERKE
- Gleicher Drehsinn = Two-Circle = Rate-Kampf. Entgegengesetzter Drehsinn = One-Circle = Radius-Kampf.
- Two-Circle: erst Instant Rate (nur nahe Corner Speed), dann Sustained Rate.
- One-Circle macht den Kampf langsam und eng.
- Keiner kann den Flow allein erzwingen. Kontrolliere Speed, Pass-Geometrie und Ebene.
- In VFM entscheidet das Speedband: T-16 im Band um 450, T-18 langsam, T-15 schnell oder langsam, aber nicht im Band der T-16.
:::

Weiter: [Scissors](/grundlagen/neutral/scissors)
