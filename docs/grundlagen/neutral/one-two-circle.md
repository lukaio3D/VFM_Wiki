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

**Two-Circle:** Den ersten halben Kreis gewinnt die bessere Instant Rate, aber nur, wenn beide nahe Corner Speed ankommen. Aus dem Ranked-Start (~427 KIAS) bringt der erste Turn nur wenige Grad und kostet viel Speed, siehe [Der erste Turn](/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen). Danach holt Grad für Grad auf, wer die höhere Sustained Rate hat, und wer bei gleicher Speed mehr G zieht und den kleineren Kreis fliegt.

**One-Circle:** Der Radius wächst mit dem Quadrat der Speed, also werden beide immer langsamer. Der Kampf wird eng, oft enger als die Mindestreichweite einer IR-Rakete. Wie gut ein Jet dort ist, hängt auch davon ab, wie viel Energie ihn der hohe α kostet. In VFM ist das sehr viel (siehe unten).

## Wer wählt den Flow?

Den Flow bestimmt ihr **beide**, keiner kann ihn allein erzwingen. Drehst du zu ihm hin, um einen Two-Circle zu bekommen, kann er weg drehen, und es wird One-Circle. Wer **früher** dreht (Lead Turn), gewinnt Winkel, legt sich aber fest. Wer **später** dreht, sieht die Entscheidung des anderen. Bei jedem Pass wird neu entschieden.

## Den bevorzugten Flow des Gegners verweigern

1. **Speed kontrollieren:** Ein One-Circle-Jet will dich langsam machen, folge ihm nicht unter dein Band. Einem Two-Circle-Jet nimmst du sein Band, indem du den Kampf schneller oder langsamer machst.
2. **Beim nächsten Pass umdrehen:** die Drehrichtung neu wählen.
3. **Ebene wechseln:** Pitch-back oder schräge Kurve macht aus dem flachen Duell einen [Vertikal-Kampf](/grundlagen/neutral/vertikal-kampf).
4. **Pass-Geometrie steuern:** Ein Rate-Jet braucht Versatz für den Lead Turn, ein Radius-Jet will einen engen Pass.
5. **Nicht mitspielen:** Blow-Through, Extend, neuer Merge unter deinen Bedingungen ([Separation](/grundlagen/defensiv/separation)). Am ersten Merge geht das in VFM, wenn du dabei ~440 KIAS hältst und nose-low wieder einsteigst; mit Speedverlust kostet es ([Blow-Through](/grundlagen/neutral/der-merge#blow-through-und-extension)).

## Flow-Wahl in VFM

Zwei Quellen sagen hier Verschiedenes, und beide stimmen auf ihre Art.

**Die Diagramme** zeigen, wer in welchem Speedband **dauerhaft schneller dreht** (gilt weiter, [Flugzeugvergleich](/flugzeuge/vergleich#wer-ist-wo-am-besten-speedbander)):

| Band (10.000 ft) | Sustained Rate |
|---|---|
| unter ~380 KIAS | T-15 ≈ T-18 > T-16; die T-15 zieht bei gleicher Speed die meisten G |
| ~400–500 KIAS | T-16 +1–2 °/s |
| über ~520 KIAS | T-15; die T-18 bricht über ~480–510 KIAS ein |

Daraus kamen die älteren Spielpläne: T-16 Two-Circle im Band, T-18 „Kampf langsam machen, One-Circle“, T-15 „langsamer One-Circle oder schnell“.

**Die Simulation** (~405.000 Bot-Kämpfe mit dem Originalmodell, echter Ranked-Start, bis 8 Minuten, Rollraten aus den Spieldaten) zeigt, was **im ganzen Kampf** gewinnt: **Two-Circle („hin“) schlägt One-Circle („weg“), und ~440 KIAS ist für alle drei Jets die beste Kampf-Speed.** Durchfliegen und mit ~440 KIAS wieder einsteigen ist ebenfalls in Ordnung. Der langsame One-Circle (280 KIAS) ist in jeder Paarung schwach, zum Beispiel gegen ein breites Feld:

| Paarung | Two-Circle ~440 (beste Ebene) | langsamer One-Circle (280, nose-low) |
|---|---|---|
| T-15 gegen T-16 | **+0,77** | +0,29 |
| T-16 gegen T-15 | **+0,21** | −0,42 |
| T-18 gegen T-16 | **+0,30** | −0,09 |
| T-18 gegen T-15 | **+0,15** | −0,35 |

::: info SIMULATION: Warum der One-Circle in VFM verliert
- **Hoher α kostet im Originalmodell sehr viel Energie.** Laut Spieldaten hat der Flügel bei α 25° ~12–34-mal so viel Widerstand wie bei α 0. Wer den Kampf langsam und eng macht, zieht dauerhaft viel α und kommt aus dem Loch nicht mehr heraus. Bei 280 KIAS verlieren beide Seiten zu viel Energie.
- **Im Two-Circle bei ~400–440 KIAS passen Rate, Radius und Energie zusammen.** Dort gewinnt die T-15 sogar gegen die T-16, obwohl diese 1–2 °/s mehr Sustained Rate hat: Die T-15 zieht bei gleicher Speed mehr G, fliegt den kleineren Kreis und hat mehr Schub.
- **Schnell bleiben (520 KIAS) verliert ebenfalls.** Wer dafür entlastet, macht keine Winkel.
- **Rollrate:** Die Werte gelten für die Rollraten aus den Spieldaten. Rollen die Jets langsamer, liegen T-15 und T-16 gegen die T-18 deutlicher vorn; die Rollrate im Flug ist nicht gemessen ([Pitch- und Rollrate](/grundlagen/physik#pitch-und-rollrate)).
- **Grenzen:** Bots zielen perfekt, sehen alles und planen nicht voraus. Unter ~280 KIAS und mit Override ist nichts gemessen. Die Diagramm-Fakten bleiben richtig, nur die Spielpläne daraus sind durch die Simulation nicht gedeckt.
:::

Für die Flow-Wahl heißt das (*Simulation*; vollständige Matrix: [Merge-Strategien](/grundlagen/neutral/der-merge#merge-strategien-fur-ranked-start-450-kias)):

| Du fliegst | gegen T-15 | gegen T-16 | gegen T-18 |
|---|---|---|---|
| **T-15** | **Two-Circle** nose-low bei ~380–420 KIAS; nicht schnell bleiben | **Two-Circle** bei ~400–440, nose-low, flach oder leicht hoch; taucht sie ab, mitgehen, nicht steil hoch; kein langsamer One-Circle | **Two-Circle** bei ~400–440; taucht sie ab, sofort zu ihr hin |
| **T-16** | **Two-Circle** bei ~440, flach oder nose-low; Speed halten, nie steil in die Vertikale | **Two-Circle** bei ~400–420 | **Two-Circle** bei ~440 (fast ausgeglichen); dreht sie weg, nicht in ihren langsamen Kreis folgen |
| **T-18** | durchfliegen, abtauchen, mit ~440 wieder einsteigen, oder flacher **Two-Circle** bei ~440 | durchfliegen und tief wieder einsteigen oder **Two-Circle** bei ~440; nicht langsam machen | **Two-Circle** bei ~440, α diszipliniert |

::: info IM SPIEL PRÜFEN
- Wie sich die Jets **unter ~280 KIAS** und mit AoA-Override verhalten. Dort soll laut Entwickler die Stärke der T-18 liegen (*Hypothese*). Die Simulation spricht bisher dagegen, kann den Bereich aber nicht prüfen.
- Die Mindestreichweite der IR-Rakete, bevor du einen One-Circle als Raketenschutz einsetzt (nur in Lobbys mit Raketen; Ranked 1v1 ist Guns-only).
:::

::: tip MERKE
- Gleicher Drehsinn = Two-Circle = Rate-Kampf. Entgegengesetzter Drehsinn = One-Circle = Radius-Kampf.
- Two-Circle: erst Instant Rate (nur nahe Corner Speed), dann Sustained Rate, G und Radius.
- One-Circle macht den Kampf langsam und eng, und in VFM teuer.
- Keiner kann den Flow allein erzwingen. Kontrolliere Speed, Pass-Geometrie und Ebene.
- In VFM laut Simulation für jeden Jet: am Pass zu ihm hin, Two-Circle bei ~440 KIAS, nose-low oder flach (nicht steil hoch). Langsamer One-Circle (280) und schnell bleiben (520) verlieren.
:::

Weiter: [Scissors](/grundlagen/neutral/scissors)
