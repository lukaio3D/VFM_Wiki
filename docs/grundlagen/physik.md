# Das VFM-Flugmodell

> Was VFM simuliert, was du davon im Cockpit merkst – und was noch niemand genau weiß.

VFM ist kein Arcade-Flieger: Speed, Höhe, Gewicht und Anstellwinkel verändern spürbar, wie dein Jet fliegt. Diese Seite sammelt die VFM-spezifische Physik und trennt *Diagramm* (Ingame-Analyse), *gemessen* (Messflug) und *Hypothese*. Allgemeine Physik: [Kurvenphysik](/grundlagen/kurvenphysik), [Energie-Management](/grundlagen/energie-management). Daten: [Flugzeugvergleich](/flugzeuge/vergleich).

## Was VFM simuliert

| Effekt | Was du merkst |
|---|---|
| Höhe | Weniger Rate, größere Radien, transsonischer Bereich schon bei niedriger KIAS |
| Transsonischer Widerstand | Sustained Rate bricht bei hoher Speed ein, Beschleunigung wird zäh |
| Anstellwinkel | α-Anzeige im HUD, AoA-Limiter mit Override („Cobra-Button“) |
| Treibstoff- und Munitionsgewicht | Leichter dreht besser |
| Buffeting | Rütteln bei hoher Last bzw. hohem α |
| G-Limit 9 G, Greyout / Blackout | Mehr als 9 G geht nicht; das Bild wird grau bzw. schwarz |

Es gibt **keinen Strukturschaden** durch G. Die Gipfelhöhe liegt bei 40.000 ft, optional startest du auf 25.000 ft.

## Anstellwinkel, AoA-Limiter und Override

Der **Anstellwinkel** (α, AoA) ist der Winkel zwischen Flügel und anströmender Luft. Mehr α gibt mehr Auftrieb – bis zum Stall, danach bricht der Auftrieb ein und der Widerstand steigt stark. Das HUD zeigt α als Zahl ([HUD](/avionik/hud)).

- **AoA-Limiter:** Ziehst du voll, hält er dich am Limit statt darüber.
- **Override („Cobra-Button“):** hebt die Grenze auf und gibt sofort Nasen-Autorität darüber hinaus. Das **kostet extrem viel Energie**, das G-Limit bleibt aktiv.

**Gemessen: voller Zug ohne Override** (ab ~450 KIAS, 10.000 ft, voller Tank):

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| α am Limiter | ~24–25° | ~23° | bis 35° (meiste G bei ~26°) |
| Höchst-G | 9,1 nach ~2 s | 8,4 nach ~3 s | 8,7 nach ~3 s |
| G bei ≈ 355 KIAS | 6,8 | 5,8 | 5,7 |
| Anteil am Diagramm-Lift-Limit | ~90 % | ~92 % | ~85 % (überzogen) |

Was daraus folgt:

- **Im Flug gibt es weniger G als im Diagramm**, solange du unterhalb der Höchst-G bist. Rechne langsam mit rund einem Zehntel weniger.
- **Bei gleicher Speed zieht die T-15 die meisten G.**
- **Die T-18** zieht über ~26° weniger G und hat viel mehr Widerstand. Dafür zeigt ihre Nase bei 35° rund 10° weiter in die Kurve – Nasenautorität für einen [Snapshot](/grundlagen/begriffe#snapshot). Zum Kurven α ~26° halten, 35° nur für den Schuss.

Den **Override** nutzt du nur für einen Schuss, der den Kampf beendet, oder als letztes Mittel in der Verteidigung. Trifft er nicht und der Gegner hat Energie, bist du danach langsam, er nicht. Alle Messwerte: [Voller Zug](/flugzeuge/vergleich#voller-zug-was-ohne-override-wirklich-geht).

## G-Limit und Greyout

- **9 G sind die Grenze.** Im Diagramm ist das die „9G LIMIT“-Linie. Max Instant Rate und Min Radius der Ingame-Tabellen sind genau 9 G bei Corner Speed ([Rechenbeispiel](/grundlagen/kurvenphysik#rechenbeispiel-mit-vfm-zahlen)).
- **Greyout / Blackout** sind simuliert. Wird das Bild grau, verlierst du den Gegner – G kontrolliert aufbauen und nachlassen. Siehe [Golden Rules](/grundlagen/golden-rules#g-awareness-greyout-und-blackout).

## Transsonischer Widerstand

Nahe der Schallgeschwindigkeit bilden sich Stoßwellen. Der **Widerstandsbeiwert** C_D steigt ab etwa Mach 0,8–0,9 steil an und hat um **Mach 1** sein Maximum. Die **Widerstandskraft** ist Beiwert × Staudruck, und der Staudruck wächst mit V². Deshalb **steigt die Kraft auch über Mach 1 weiter**.

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
| 10.000 ft | ~510 KIAS | ~565 KIAS | gemessen: Schall ~630 kt wahre Fahrt |
| 20.190 ft | ~435 KIAS | ~480 KIAS | Standardatmosphäre, geschätzt |

Das Diagramm passt dazu: **Die T-18 bricht in jeder Höhe bei etwa Mach 0,9 ein** – auf Meereshöhe ab ~600 KIAS, auf 10.000 ft ab ~510, auf 20.190 ft ab ~450 KIAS. Dass der Einbruch an der Mach-Zahl hängt statt an der KIAS, ist ein starkes Indiz für transsonischen Widerstand. Gemessen bestätigt sich das: Nahe Mach 0,95 sinkt der Schubüberschuss von T-16 und T-18 deutlich, bei der T-15 kaum.

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

VFM rechnet nicht mit der Standardatmosphäre. Das lässt sich aus den Diagrammen ablesen: Auf der 9G-Linie gilt ω = g · √80 / V, aus jeder Rate folgt also die wahre Fahrt, mit der das Spiel rechnet.

| Höhe | Wahre Fahrt / KIAS in VFM | Standardatmosphäre | Luftdichte in VFM |
|---|---|---|---|
| Meereshöhe | 1,00 | 1,00 | 100 % |
| 10.000 ft | **~1,12** | ~1,16 | ~69 % (real 74 %) |
| 20.190 ft | **~1,28** | ~1,36 | ~48 % (real 54 %) |

- **Bei gleicher KIAS bist du in der Höhe langsamer als in der Realität.**
- **Der Flügel trägt in der Höhe weniger, als die KIAS vermuten lassen.** Deshalb steigt die Corner Speed in KIAS mit der Höhe (T-15, 50 %: 337 → 360 → 380 KIAS auf 0 / 10.000 / 20.190 ft).

Beides ist aus den Diagrammen abgeleitet, keine Herstellerangabe.

## Was die Kurven über das Flugmodell verraten

Wertet man alle neun Diagramme und die Messflüge gemeinsam aus, ergibt sich ein klassisches Flugmodell:

- **Corner = genau 9 G.** Alle Min-Radius-Werte passen exakt zu r = V² / (g · √80).
- **Schub hängt nicht vom Gewicht ab, der induzierte Widerstand wächst mit (G × Gewicht)².** Faustregel: **10 % leichter = 10 % mehr dauerhafte G**, solange du nicht am 9-G-Limit hängst.
- **Schub und Widerstand ändern sich frei mit der Mach-Zahl.** Die Sustained-Kurven haben Knicke und Plateaus, eine einfache Formel reicht nicht.
- **Schub und Widerstand getrennt** (gemessen): Schub/Gewicht mit Nachbrenner ~1,65 (T-15), ~1,26 (T-16), ~1,35 (T-18). Die T-18 hat mehr Schub als die T-16, aber fast doppelt so viel Widerstand. → [Schub und Widerstand getrennt](/flugzeuge/vergleich#schub-und-widerstand-getrennt)

Ein daraus kalibriertes Rechenmodell trifft die Sustained-Kurven im Kampfbereich (300–550 KIAS) auf etwa 0,1–0,5 °/s; Kurven im Flug bestätigen es auf ±2–3 %. Daten und Skripte: [tools/flugmodell im Repo](https://github.com/lukaio3D/VFM_Wiki/tree/main/tools/flugmodell).

## Treibstoff und Munition

Von vollem zu leerem Tank werden T-15 und T-18 ~22 % leichter, die T-16 ~18 %. Das bringt bis zu **+3 °/s Instant und +4 °/s Sustained**, ein halber Tank ~1–2 °/s. **Die Reihenfolge der Jets ändert sich dadurch nicht.**

Munitionsgewicht wird simuliert, der Effekt ist nicht bekannt. Sind alle Waffen leer, startet ein Selbstzerstörungs-Countdown. Siehe [Waffen](/avionik/waffen).

## Offene Fragen

::: info IM SPIEL PRÜFEN
- **Override:** Wie weit geht α, wie viel G bringt das, wie viel Speed kostet es, und wie fängst du den Jet ab?
- **Unter ~280 KIAS:** Steuerbarkeit, Rollrate und Stall-Verhalten sind nicht gemessen (die Diagramme beginnen bei ~170–200 KIAS).
- **Greyout-Modell:** G-Schwelle, Zeitverhalten, Erholung.
:::

Ebenfalls unbekannt: die Rollrate allgemein, der Leerlaufschub (bisher ≈ 0 angenommen) und die Wirkung der Speedbrake.

::: tip MERKE
- VFM simuliert **Höhe, transsonischen Widerstand, α und Gewicht**. 9 G sind die Grenze, Strukturschaden gibt es nicht.
- **Im Flug gibt es ~10 % weniger G als im Diagramm**, bis die Höchst-G erreicht ist. Die T-18 kurvt mit α ~26°, 35° nur für den Snapshot.
- **Override** = Nase sofort, Energie weg. Nur für einen Schuss oder als letztes Mittel.
- **Transsonischer Widerstand** setzt bei ~Mach 0,9 ein, auf 10.000 ft ab ~510 KIAS. Kämpf darunter.
- **10 % leichter = 10 % mehr dauerhafte G** – tief und leicht dreht besser.
:::

Weiter: [Relative Geometrie](/grundlagen/geometrie)
