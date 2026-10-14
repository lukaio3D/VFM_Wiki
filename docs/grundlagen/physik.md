# Das VFM-Flugmodell

> Was VFM simuliert, was du davon im Cockpit merkst – und was noch niemand genau weiß.

VFM ist kein Arcade-Flieger: Speed, Höhe, Gewicht und Anstellwinkel verändern spürbar, wie dein Jet fliegt. Diese Seite sammelt die VFM-spezifische Physik. Allgemeine Physik: [Kurvenphysik](/grundlagen/kurvenphysik), [Energie-Management](/grundlagen/energie-management). Daten: [Flugzeugvergleich](/flugzeuge/vergleich).

## Was VFM simuliert

| Effekt | Was du merkst |
|---|---|
| Höhe | Weniger Rate, größere Radien, transsonischer Bereich schon bei niedriger KIAS |
| Anstellwinkel | Mehr α gibt mehr Auftrieb bis ~27° (HUD), aber steil mehr Widerstand. AoA-Limiter mit Override („Cobra-Button“) |
| Schub über Mach und Höhe | Jeder Jet hat sein Schubmaximum bei einer anderen Mach-Zahl |
| Transsonischer Widerstand | Sustained Rate bricht bei hoher Speed ein, Beschleunigung wird zäh |
| Treibstoff- und Munitionsgewicht | Leichter dreht besser |
| Fly-by-Wire | Höchstwerte für Pitch- und Rollrate je Jet |
| Buffeting | Rütteln bei hoher Last bzw. hohem α |
| G-Limit 9 G, Greyout / Blackout | Mehr als 9 G geht nicht; das Bild wird grau bzw. schwarz |

Es gibt **keinen Strukturschaden** durch G. Die Gipfelhöhe liegt bei 40.000 ft, optional startest du auf 25.000 ft.

## Woher die Zahlen kommen

Die Seite trennt fünf Quellen: *Diagramm* (Ingame-„Aircraft Performance Analysis“), *gemessen* (Messflug, HUD-Video), *Spieldaten* (aus den Dateien der VFM-Installation gelesen), *Simulation* ([Bot-Turnier](/flugzeuge/simulation) mit dem Originalmodell) und *Hypothese*.

Die Spieldaten zeigen ein Flugmodell wie in VTOL VR (gleicher Entwickler): Jeder Jet besteht aus Flächen mit Profilkurven über den Anstellwinkel, der Schub hängt von Mach-Zahl und Luftdichte ab. Das Wiki nennt daraus nur einzelne Kennzahlen. Messwerte bleiben stehen, auch wo das Modell leicht anders rechnet.

| Die Spieldaten bestätigen | Die Spieldaten zeigen neu |
|---|---|
| [Luftdichte](#die-atmosphare-in-vfm) 69 % auf 10.000 ft, 48 % auf 20.190 ft | [Auftrieb](#anstellwinkel-aoa-limiter-und-override) am größten bei HUD-α ~27°, Widerstand steigt mit α steil |
| [Massen](#treibstoff-und-munition) = Diagrammgewichte | [Lift-Limit der Diagramme](#voller-zug-gemessen) im Flug nicht erreichbar |
| Schub/Gewicht mit Nachbrenner 1,64 / 1,29 / 1,37 (gemessen 1,65 / 1,26 / 1,35) | [Schub über Mach](#schub-uber-mach-spieldaten) je Jet verschieden, Wellenwiderstand ~+20 % um Mach 1 |
| G-Limit 9 G für alle Jets | [Pitch- und Rollrate](#pitch-und-rollrate) des Fly-by-Wire |

## Anstellwinkel, AoA-Limiter und Override

Der **Anstellwinkel** (α, AoA) ist der Winkel zwischen Flügel und anströmender Luft. Das HUD zeigt ihn als Zahl ([HUD](/avionik/hud)). Laut Spieldaten zeigt das HUD **~2° mehr, als der Flügel sieht** (HUD-α ≈ Flügel-α + 2°). Alle α-Werte im Wiki sind HUD-Werte.

- **AoA-Limiter:** Ziehst du voll, hält er dich am Limit statt darüber.
- **Override („Cobra-Button“):** hebt die Grenze auf und gibt sofort Nasen-Autorität darüber hinaus. Das **kostet extrem viel Energie**, das G-Limit bleibt aktiv.

### Auftrieb und Widerstand über α (Spieldaten)

- **Auftrieb:** steigt mit α bis **HUD-α ~27°**, bei allen drei Jets. Darüber fällt er wieder. Das erklärt die gemessene T-18-Regel „meiste G bei ~26°“: Ihr Limiter lässt bis 35° zu, also über das Maximum hinaus.
- **Widerstand:** steigt mit α steil. Bei α 15° hat der Flügel ~4–12-mal, bei α 25° ~12–34-mal so viel Widerstand wie bei α 0. Am stärksten steigt er bei der T-15, am wenigsten bei der T-18 – die dafür den höchsten Grundwiderstand hat.
- **T-18:** verliert über ~22° α zusätzlich etwas Schub.

Nahe am Auftriebsmaximum bringen die letzten Grad α wenig Auftrieb, aber viel Widerstand. Deshalb ist voller Zug so teuer und deshalb lohnt es, **knapp unter dem Anschlag** zu fliegen → [Warum voller Zug so teuer ist](/grundlagen/energie-management#warum-voller-zug-so-teuer-ist).

### Voller Zug (gemessen)

Ab ~450 KIAS, 10.000 ft, voller Tank, ohne Override:

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| α am Limiter | ~24–25° | ~23° | bis 35° (meiste G bei ~26°) |
| Höchst-G | 9,1 nach ~2 s | 8,4 nach ~3 s | 8,7 nach ~3 s |
| G bei ≈ 355 KIAS | 6,8 | 5,8 | 5,7 |
| Anteil am Diagramm-Lift-Limit | ~90 % | ~92 % | ~85 % (überzogen) |

Was daraus folgt:

- **Im Flug gibt es weniger G als im Diagramm**, solange du unterhalb der Höchst-G bist. Rechne langsam mit rund einem Zehntel weniger. Die Spieldaten bestätigen das: Das Lift-Limit der Diagramme liegt 13–24 % über dem größten Auftrieb, den der Jet im Flug ohne Override erreicht. **Die Diagramm-Instant-Werte sind im Flug nicht erreichbar.**
- **Bei gleicher Speed zieht die T-15 die meisten G.**
- **Die T-18** zieht über ~26° weniger G und hat viel mehr Widerstand. Dafür zeigt ihre Nase bei 35° rund 10° weiter in die Kurve – Nasenautorität für einen [Snapshot](/grundlagen/begriffe#snapshot). Zum Kurven α ~26° halten, 35° nur für den Schuss.

Alle Messwerte: [Voller Zug](/flugzeuge/vergleich#voller-zug-was-ohne-override-wirklich-geht).

### Override

Den **Override** nutzt du nur für einen Schuss, der den Kampf beendet, oder als letztes Mittel in der Verteidigung. Trifft er nicht und der Gegner hat Energie, bist du danach langsam, er nicht. Die [Simulation](/flugzeuge/simulation#aoa-override-annahme) bestätigt das: Als Gewohnheit schadet Override, gezielt für einen Snapshot kann er entscheiden.

Die Spieldaten nennen je Jet zwei α-Grenzen (Flügel-α): T-15 30° / 63°, T-16 27° / 43°, T-18 40° / 82°. Die erste liegt über dem gemessenen Limiter, die zweite könnte das Override-Limit sein (*Hypothese*).

## G-Limit und Greyout

- **9 G sind die Grenze**, laut Spieldaten bei allen drei Jets. Im Diagramm ist das die „9G LIMIT“-Linie. Max Instant Rate und Min Radius der Ingame-Tabellen sind genau 9 G bei Corner Speed ([Rechenbeispiel](/grundlagen/kurvenphysik#rechenbeispiel-mit-vfm-zahlen)).
- **Greyout / Blackout** sind simuliert. Wird das Bild grau, verlierst du den Gegner – G kontrolliert aufbauen und nachlassen. Siehe [Golden Rules](/grundlagen/golden-rules#g-awareness-greyout-und-blackout).

## Pitch- und Rollrate

Das Fly-by-Wire begrenzt, wie schnell der Jet nickt und rollt (*Spieldaten*):

| Vorgabe | T-15 | T-16 | T-18 |
|---|---|---|---|
| Pitch-Rate max. | 40 °/s | 70 °/s | 80 °/s |
| Rollrate max. | 325 °/s | 420 °/s | 420 °/s |

- **Die T-15 rollt am langsamsten** und hat die kleinste Pitch-Vorgabe.
- Die Pitch-Vorgaben liegen über den Kurvenraten der Diagramme (höchstens ~31 °/s). In normalen Kurven begrenzen also Auftrieb und 9 G, nicht das Fly-by-Wire.
- **Ob die Jets diese Werte im Flug erreichen, ist nicht gemessen.** Die Simulation rechnet mit 180 °/s Rollrate für alle (Annahme). T-15 gegen T-18 hängt stark davon ab: mit 270 °/s ausgeglichen, mit 120 °/s +0,71. Rollen die Jets im Flug wirklich so schnell wie vorgegeben, ist der Vorsprung der T-15 gegen die T-18 eher kleiner (*Hypothese*).

## Transsonischer Widerstand

Nahe der Schallgeschwindigkeit bilden sich Stoßwellen. Der **Widerstandsbeiwert** C_D steigt ab etwa Mach 0,8–0,9 an und hat um **Mach 1** sein Maximum – laut Spieldaten bei allen drei Jets **~+20 %**. Die **Widerstandskraft** ist Beiwert × Staudruck, und der Staudruck wächst mit V². Deshalb **steigt die Kraft auch über Mach 1 weiter**.

```
Widerstands-BEIWERT C_D            Widerstands-KRAFT D
    │       ╱╲                         │              ╱
    │      ╱  ╲___                     │            ╱
    │     ╱       ────                 │         ╱
    │____╱                             │_____╱
    └─────┬──┬─────── Mach             └─────┬──┬──── Mach
         0,9 1,0                            0,9 1,0
```

Wo Mach 1 in KIAS liegt, hängt von der Höhe ab:

| Höhe | Mach 0,9 | Mach 1,0 | Grundlage |
|---|---|---|---|
| Meereshöhe | ~600 KIAS | ~660 KIAS | Standardatmosphäre |
| 10.000 ft | ~510 KIAS | ~565 KIAS | gemessen: Schall ~630 kt wahre Fahrt; Mach 0,75 = ~427 KIAS |
| 20.190 ft | ~435 KIAS | ~480 KIAS | Standardatmosphäre, geschätzt |

### Schub über Mach (Spieldaten)

Der Schub ändert sich mit der Mach-Zahl, je Jet verschieden. Zusammen mit dem Wellenwiderstand erklärt das Diagramme und Messflüge:

- **T-15:** Schubmaximum bei ~Mach 1,0 (10.000 ft: ~565 KIAS). Sie hält bei hoher Speed am besten durch; gemessen sinkt ihr Schubüberschuss nahe Mach 0,95 kaum.
- **T-16:** Schubmaximum bei ~Mach 0,8 (10.000 ft: ~455 KIAS). Darüber verliert sie Schub, während der Widerstand weiter wächst; gemessen sinkt ihr Schubüberschuss nahe Mach 0,95 deutlich.
- **T-18:** Schubmaximum erst bei ~Mach 1,2, aber der höchste Grundwiderstand. Deshalb **bricht sie in jeder Höhe bei etwa Mach 0,9 ein** (*Diagramm*: Meereshöhe ab ~600 KIAS, 10.000 ft ab ~510, 20.190 ft ab ~450).

Für dich heißt das:

- **BFM findet nicht im Überschall statt.** Mit Mach 0,9+ in den Merge bringt nur einen riesigen Radius.
- **In großer Höhe** ist der Spielraum zwischen „zu langsam für 9 G“ und „Widerstandswand“ klein.
- **T-18:** Hohe Speed ist ihr schlechtester Bereich. **T-15:** hält dort am besten durch.

## Höhe

Mit der Höhe sinkt die Luftdichte. Bei gleicher KIAS bist du wahr schneller, die Rate sinkt, der Radius wächst – und der transsonische Bereich beginnt bei niedrigerer KIAS.

- **Alle Jets drehen tief besser.** Von Meereshöhe auf 20.190 ft fallen Instant und Sustained Rate um rund ein Drittel, der Mindestradius wächst auf mehr als das Doppelte.
- **Der Sustained-Vorsprung der T-16 ist tief am größten** (Meereshöhe 22 vs. 20 °/s) und schrumpft auf 20.190 ft auf 0–1 °/s.
- **Die T-15 hält in großer Höhe das flachste Sustained-Plateau.**

Werte aller Höhen: [Flugzeugvergleich](/flugzeuge/vergleich).

## Die Atmosphäre in VFM

VFM rechnet nicht mit der Standardatmosphäre. Das ließ sich zuerst aus den Diagrammen ablesen (auf der 9G-Linie gilt ω = g · √80 / V, aus jeder Rate folgt also die wahre Fahrt, mit der das Spiel rechnet). Die Dichtekurve in den Spieldaten bestätigt es.

| Höhe | Wahre Fahrt / KIAS in VFM | Standardatmosphäre | Luftdichte in VFM |
|---|---|---|---|
| Meereshöhe | 1,00 | 1,00 | 100 % |
| 10.000 ft | **~1,12** | ~1,16 | 69 % (real 74 %) |
| 20.190 ft | **~1,28** | ~1,36 | 48 % (real 54 %) |

- **Bei gleicher KIAS bist du in der Höhe langsamer als in der Realität.**
- **Der Flügel trägt in der Höhe weniger, als die KIAS vermuten lassen.** Deshalb steigt die Corner Speed in KIAS mit der Höhe (T-15, 50 %: 337 → 360 → 380 KIAS auf 0 / 10.000 / 20.190 ft).

## Treibstoff und Munition

| Spieldaten | T-15 | T-16 | T-18 |
|---|---|---|---|
| Masse leer | 15,0 t | 10,0 t | 14,5 t |
| Masse voll | ~19,15 t | ~12,14 t | ~18,70 t |

Das sind die Gewichte der Diagramme (voll 42.160 / 26.787 / 41.226 lbs). Von vollem zu leerem Tank werden T-15 und T-18 ~22 % leichter, die T-16 ~18 %. Das bringt bis zu **+3 °/s Instant und +4 °/s Sustained**, ein halber Tank ~1–2 °/s. **Die Reihenfolge der Jets ändert sich dadurch nicht.**

**Im Ranked startest du mit vollem Tank:** Die Lobby hat keine Fuel-Option, der Tank startet laut Spieldaten voll ([Spielmodi](/einstieg/spielmodi#ranked)).

Munitionsgewicht wird simuliert, der Effekt ist nicht bekannt. Sind alle Waffen leer, startet ein Selbstzerstörungs-Countdown. Siehe [Waffen](/avionik/waffen).

## Was die Kurven über das Flugmodell verraten

Wertet man alle neun Diagramme und die Messflüge gemeinsam aus, ergibt sich ein klassisches Flugmodell:

- **Corner = genau 9 G.** Alle Min-Radius-Werte passen exakt zu r = V² / (g · √80).
- **Schub hängt nicht vom Gewicht ab, der induzierte Widerstand wächst mit (G × Gewicht)².** Faustregel: **10 % leichter = 10 % mehr dauerhafte G**, solange du nicht am 9-G-Limit hängst.
- **Die Sustained-Kurven haben Knicke und Plateaus**, weil Schub und Widerstand sich je Jet anders mit der Mach-Zahl ändern ([Schub über Mach](#schub-uber-mach-spieldaten)).
- **Schub und Widerstand getrennt** (gemessen): Die T-18 hat mehr Schub als die T-16, aber fast doppelt so viel Widerstand. → [Schub und Widerstand getrennt](/flugzeuge/vergleich#schub-und-widerstand-getrennt)
- **Die Diagramme stimmen im Flug auf ±2–3 %** (Sustained-Kurven bei ~450 KIAS nachgeflogen).

### Das Rechenmodell

Für [Simulation](/flugzeuge/simulation) und [3D-Simulator](/VFM_Wiki/sim/){target="_self"} rechnet das Wiki mit dem **Originalmodell des Spiels**: Auftrieb und Widerstand über α aus den Flächen und Profilen, Schub über Mach und Dichte aus den Triebwerksdaten, Dichte und Massen aus den Spieldaten. Offen sind nur einige Umrechnungsfaktoren aus dem Spielcode; sie sind an den Messflügen kalibriert. Ergebnis: **Schub auf 2–4 %** wie in den Spieldaten, **Ingame-Diagramme auf 0,2–1,0 °/s** (300–550 KIAS), **Energieverlust im vollen Zug auf wenige Meter** Energiehöhe. Das frühere, frei angepasste Modell ist damit ersetzt. Daten und Skripte: [tools/flugmodell im Repo](https://github.com/lukaio3D/VFM_Wiki/tree/main/tools/flugmodell).

## Offene Fragen

::: info IM SPIEL PRÜFEN
- **Rollrate im Flug:** Die Spieldaten nennen nur die Vorgabe (325 / 420 / 420 °/s). Erreichen die Jets sie, auch langsam?
- **Override:** Wie weit geht α, wie viel G bringt das, wie viel Speed kostet es, und wie fängst du den Jet ab?
- **Unter ~280 KIAS:** Steuerbarkeit und Stall-Verhalten sind nicht gemessen (die Diagramme beginnen bei ~170–200 KIAS).
- **Greyout-Modell:** G-Schwelle, Zeitverhalten, Erholung.
:::

Ebenfalls offen: die Wirkung der Speedbrake. Der **Leerlaufschub** liegt laut Spieldaten bei ~5 % (bisher ≈ 0 angenommen). Die Widerstandswerte aus dem Ausrollen sind deshalb eher etwas zu niedrig.

::: tip MERKE
- VFM simuliert **Höhe, α, Schub über Mach, transsonischen Widerstand und Gewicht**. 9 G sind die Grenze, Strukturschaden gibt es nicht.
- **Auftrieb ist bei HUD-α ~27° am größten, der Widerstand steigt mit α steil.** Die letzten Grad bis zum Anschlag sind teuer. Die T-18 kurvt mit α ~26°, 35° nur für den Snapshot.
- **Im Flug gibt es ~10 % weniger G als im Diagramm**, bis die Höchst-G erreicht ist. Die Diagramm-Instant-Werte erreichst du nicht.
- **Override** = Nase sofort, Energie weg. Nur für einen Schuss oder als letztes Mittel.
- **Transsonischer Widerstand** setzt bei ~Mach 0,9 ein, auf 10.000 ft ab ~510 KIAS. Kämpf deutlich darunter, laut Simulation bei ~360–440 KIAS.
- **10 % leichter = 10 % mehr dauerhafte G** – tief und leicht dreht besser.
:::

Weiter: [Relative Geometrie](/grundlagen/geometrie)
