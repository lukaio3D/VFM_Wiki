# Das VFM-Flugmodell

> Was VFM simuliert, was du davon im Cockpit merkst – und was (noch) niemand genau weiß.

VFM ist kein Arcade-Flieger: Speed, Höhe, Gewicht und Anstellwinkel verändern spürbar, wie dein Jet fliegt. Diese Seite trennt sauber zwischen dem, was belegt ist, und dem, was du selbst testen musst. Die allgemeine Physik dahinter: [Kurvenphysik](/grundlagen/kurvenphysik) und [Energie-Management](/grundlagen/energie-management).

## Was VFM simuliert

| Effekt | Quelle | Was du merkst |
|---|---|---|
| Höheneffekte | Steam-Store | Weniger Rate, größere Radien in der Höhe |
| Transsonischer Widerstand | Steam-Store | Sustained Rate bricht bei hoher Speed ein, Beschleunigung wird zäh |
| Anstellwinkel (AoA) | Steam-Store | AoA-Anzeige im HUD, AoA-Limiter |
| Treibstoff- und Munitionsgewicht | Steam-Store | Leichter = besser, sichtbar in den Ingame-Daten |
| Buffeting | Reviews | Rütteln bei hoher Last bzw. hohem AoA |
| Greyout / Blackout | Reviews | Bild wird bei hohen G grau bzw. schwarz |
| AoA-Limiter mit Override ("Cobra-Button") | Spiel | Sofortige Nasen-Autorität über das AoA-Limit hinaus |
| G-Limit 9 G | Ingame-Diagramme ("9G LIMIT") | Mehr als 9 G geht nicht |
| Gipfelhöhe 40.000 ft | Store / Patchnotes | Optionaler High-Altitude-Start auf 25.000 ft (seit v1.2.0) |

Kein Strukturschaden durch G: Du kannst die Flügel nicht abreißen. Die Grenze ist das G-Limit – und dein Bild (Greyout).

## Anstellwinkel, AoA-Limiter und Override

Der **Anstellwinkel (AoA, Angle of Attack)** ist der Winkel zwischen Flügel und anströmender Luft. Mehr AoA heißt mehr Auftrieb – bis zum kritischen Anstellwinkel, danach reißt die Strömung ab (**Stall**), der Auftrieb bricht ein, der Widerstand steigt stark.

- **AoA im HUD:** Seit v1.2.0 zeigt das HUD eine AoA-Zahl. Sie hilft dir, langsam an der Grenze zu fliegen, statt zu raten. Details: [HUD](/avionik/hud).
- **AoA-Limiter:** Begrenzt im normalen Flug den Anstellwinkel. Ziehst du voll, hält er dich am Limit statt darüber.
- **Override ("Cobra-Button"):** Hebt die AoA-Grenze auf und gibt dir sofort Nasen-Autorität darüber hinaus. Das **kostet extrem viel Energie** – danach bist du langsam. Das G-Limit bleibt dabei aktiv.

Wann der Override sinnvoll sein kann:

- Für einen **Schuss**, den du nur so bekommst und der den Kampf beendet.
- Als **letztes Mittel in der Verteidigung**, wenn die Nase sonst nicht rechtzeitig herumkommt.

Wann nicht: Wenn der Gegner Energie hat und nicht getroffen wird. Dann bist du langsam, er nicht – und er kommt zurück.

::: info IM SPIEL PRÜFEN
- Wie hoch ist das AoA-Limit je Jet, und wie weit geht es mit Override?
- Wie viel Speed kostet ein Override-Manöver bei 250, 350 und 450 KIAS?
- Kann der Jet mit Override wegkippen oder trudeln? Wie fängst du ihn ab?
- Ab wann setzt Buffeting ein – nahe AoA-Limit oder bei hoher G?
:::

## G-Limit und Greyout

- **9 G ist die Grenze.** In den Ingame-Diagrammen ist die gestrichelte Linie oberhalb der Corner Speed die "9G LIMIT"-Linie. Die Ingame-Werte für Max Instant Rate und Min Radius passen genau zu 9 G bei Corner Speed (Rechnung: [Kurvenphysik](/grundlagen/kurvenphysik#rechenbeispiel-mit-vfm-zahlen)).
- **Greyout / Blackout:** Laut Reviews simuliert. Wird das Bild grau, verlierst du den Gegner aus dem Blick – kontrolliert G aufbauen und nachlassen, wenn es grau wird. Siehe [Golden Rules](/grundlagen/golden-rules#g-awareness-greyout-und-blackout).

::: info IM SPIEL PRÜFEN
- Ab welcher G und nach welcher Zeit kommt Greyout? Wie schnell erholt sich das Bild?
:::

## Transsonischer Widerstand

Nahe der Schallgeschwindigkeit bilden sich Stoßwellen am Jet. Der **Widerstandsbeiwert** (C_D – wie "windschlüpfrig" der Jet ist) steigt ab etwa Mach 0,8–0,9 steil an und erreicht um **Mach 1** herum sein Maximum. Danach sinkt der Beiwert wieder etwas.

Wichtig: Die **Widerstandskraft** ist Beiwert × Staudruck, und der Staudruck wächst mit dem Quadrat der Speed. Deshalb **steigt die Widerstandskraft auch über Mach 1 weiter** – sie wird nicht kleiner, nur weil der Beiwert sinkt.

```
Widerstands-BEIWERT C_D            Widerstands-KRAFT D
    │       ╱╲                         │              ╱
    │      ╱  ╲___                     │            ╱
    │     ╱       ────                 │         ╱
    │____╱                             │_____╱
    └─────┬──┬─────── Mach             └─────┬──┬──── Mach
         0,9 1,0                            0,9 1,0
```

Wo liegt Mach 1 in KIAS? Die angezeigte Speed bei Mach 1 sinkt mit der Höhe. Gerechnet mit dem in VFM gemessenen Verhältnis von wahrer Fahrt zu KIAS (siehe [Die Atmosphäre in VFM](#die-atmosphare-in-vfm)) und der Schallgeschwindigkeit der Standardatmosphäre:

| Höhe | Mach 0,9 | Mach 1,0 |
|---|---|---|
| Meereshöhe | ~595 KIAS | ~661 KIAS |
| 10.000 ft | ~516 KIAS | ~573 KIAS |
| 20.190 ft | ~433 KIAS | ~482 KIAS |

Welche Schallgeschwindigkeit VFM verwendet, ist nicht bekannt. Die Tabelle ist deshalb eine gute Näherung, kein exakter Wert.

Das passt zu den Ingame-Daten: **Die T-18 bricht in allen drei Höhen bei etwa Mach 0,9 ein** – auf Meereshöhe ab ~600 KIAS, auf 10.000 ft ab ~510 KIAS, auf 20.190 ft ab ~450 KIAS. Auf 20.190 ft liegt die Best Sustained Speed aller drei Jets bei 412–423 KIAS (≈ Mach 0,86–0,88). Dass der Einbruch so sauber an einer Mach-Zahl hängt statt an einer KIAS-Zahl, ist ein starkes Indiz für transsonischen Widerstand. Eine Herstellerangabe ist es nicht.

Was das für dich heißt:

- **BFM findet nicht im Überschall statt.** Die sinnvollen Kampf-Speeds liegen bei ~350–500 KIAS. Am Merge mit Mach 0,9+ anzukommen, bringt dir einen riesigen Radius und keinen Vorteil.
- **In großer Höhe** erreichst du den transsonischen Bereich schon bei viel niedrigerer KIAS. Dort ist der Spielraum zwischen "zu langsam für 9 G" und "Widerstandswand" klein.
- **T-18:** Hohe Speed ist ihr schlechtester Bereich. **T-15:** hält dort am besten durch.

## Höhe

Mit der Höhe sinkt die Luftdichte. Bei gleicher KIAS bist du in der Höhe wahr schneller – dadurch werden Rate kleiner und Radius größer (siehe [Kurvenphysik](/grundlagen/kurvenphysik#kias-vs-wahre-speed-in-der-hohe)). Dazu kommt der transsonische Widerstand bei niedrigerer KIAS.

Ingame-Daten, 50 % Fuel (auf 20.190 ft 49 %), Stand Okt 2026:

| Höhe | | T-15 | T-16 | T-18 |
|---|---|---|---|---|
| Meereshöhe | Instant | 29 °/s @ 337 | 26 °/s @ 378 | 27 °/s @ 365 |
| | Sustained | 20 °/s @ 475 | 22 °/s @ 447 | 20 °/s @ 447 |
| | Min Radius | 1.138 ft | 1.428 ft | 1.313 ft |
| 10.000 ft | Instant | 24 °/s @ 360 | 21 °/s @ 409 | 22 °/s @ 385 |
| | Sustained | 17 °/s @ 495 | 18 °/s @ 470 | 16 °/s @ 470 |
| | Min Radius | 1.644 ft | 2.099 ft | 1.899 ft |
| 20.190 ft | Instant | 20 °/s @ 380 | 18 °/s @ 434 | 18 °/s @ 412 |
| | Sustained | 13 °/s @ 412 | 14 °/s @ 423 | 13 °/s @ 423 |
| | Min Radius | 2.387 ft | 3.073 ft | 2.816 ft |

Was du daraus mitnimmst:

- **Alle Jets verlieren mit der Höhe**, und zwar deutlich: Von Meereshöhe auf 20.190 ft fallen Instant und Sustained um rund ein Drittel, der Radius wächst auf mehr als das Doppelte.
- **Der Sustained-Vorsprung der T-16 ist auf Meereshöhe am größten** (22 vs. 20 °/s) und schrumpft auf 20.190 ft auf 0–1 °/s.
- **Die T-15 profitiert relativ von Höhe:** Sie hält auf 20.190 ft zwischen ~350 und ~600 KIAS ein flaches Sustained-Plateau um 12–13 °/s. Die T-16 fällt dort ab ~470 KIAS unter sie, die T-18 ab ~450 KIAS deutlich.

## Die Atmosphäre in VFM

VFM rechnet nicht mit der Standardatmosphäre der echten Luftfahrt. Das lässt sich aus den Diagrammen messen: Auf der 9G-Linie gilt ω = g·√80 / V. Aus jeder abgelesenen Rate folgt also die wahre Fahrt V, mit der das Spiel rechnet.

| Höhe | Wahre Fahrt / KIAS in VFM | zum Vergleich: Standardatmosphäre | Luftdichte in VFM (aus dem Lift-Limit) |
|---|---|---|---|
| Meereshöhe | 1,00 | 1,00 | 100 % |
| 10.000 ft | **~1,12** | ~1,16 | ~69 % (real: 74 %) |
| 20.190 ft | **~1,28** | ~1,36 | ~48 % (real: 54 %) |

Was das heißt:

- **Bei gleicher KIAS bist du in der Höhe weniger schnell als in der Realität**, das Mach-Problem kommt also etwas später (siehe Tabelle oben).
- **Der Flügel trägt in der Höhe weniger, als die KIAS vermuten lassen.** Deshalb steigt die Corner Speed in KIAS mit der Höhe, bei allen drei Jets um denselben Faktor: Auf 20.190 ft brauchst du ~13 % mehr KIAS für 9 G als auf Meereshöhe (T-15, 50 %: 337 → 380 KIAS).
- Die Dichte folgt sehr gut einer einfachen Exponentialkurve (halbiert sich etwa alle 5.800 m bzw. ~19.000 ft). Das ist eine Ableitung aus den Diagrammen, keine Herstellerangabe.

## Was die Kurven über das Flugmodell verraten

Wertet man alle neun Diagramme gemeinsam aus, ergibt sich ein klassisches Flugmodell:

- **Corner = genau 9 G.** Alle 27 Min-Radius-Werte passen exakt zu r = V² / (g · √80).
- **Schub hängt nicht vom Gewicht ab, der induzierte Widerstand wächst mit (G × Gewicht)².** Gemessen: Bei gleicher Höhe und KIAS ist „dauerhafte G × Gewicht“ über alle Fuel-Stände auf 1 % konstant. Faustregel: **10 % leichter = 10 % mehr dauerhafte G** (solange du nicht am 9-G-Limit hängst).
- **Schub und Widerstand ändern sich frei mit der Mach-Zahl.** Die Sustained-Kurven haben Knicke und Plateaus, etwa die T-16 auf 10.000 ft bei ~520 KIAS. Eine einfache Formel reicht dafür nicht.

Ein daraus kalibriertes Rechenmodell trifft alle Sustained-Kurven im Kampfbereich (300–550 KIAS) auf etwa 0,1–0,5 °/s. Es ist die Grundlage für eine geplante 3D-Lernsimulation. Daten und Skripte: [tools/flugmodell im Repo](https://github.com/lukaio3D/VFM_Wiki/tree/main/tools/flugmodell).

## Treibstoff und Munition

VFM simuliert Treibstoff- und Munitionsgewicht. Die Ingame-Daten (10.000 ft) zeigen den Effekt des Treibstoffs:

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| Gewicht 100 / 50 / 0 % Fuel | 42.160 / 37.615 / 33.069 lbs | 26.787 / 24.417 / 22.046 lbs | 41.226 / 36.597 / 31.967 lbs |
| Instant 100 → 50 → 0 % | 23 → 24 → 26 °/s | 20 → 21 → 22 °/s | 21 → 22 → 24 °/s |
| Sustained 100 → 50 → 0 % | 15 → 17 → 19 °/s | 16 → 18 → 20 °/s | 15 → 16 → 19 °/s |

- Von 100 auf 50 % Fuel sinkt das Gewicht um **~9–11 %**. Das bringt **~+1 °/s Instant** und **+1–2 °/s Sustained**. Mit leerem Tank sind es bis zu +3 °/s Instant und +4 °/s Sustained.
- **Die Reihenfolge der Jets ändert sich nicht.** Bei vollem Tank ist der Sustained-Vorsprung der T-16 nur kleiner (16 vs. 15 °/s), mit leerem Tank holen T-15 und T-18 auf (20 vs. 19 °/s).
- **Munition:** Ihr Gewicht wird simuliert, wie groß der Effekt ist, ist nicht bekannt. Sind alle Waffen leer, startet ein Selbstzerstörungs-Countdown – Nachladen gibt es nicht. Siehe [Waffen](/avionik/waffen).

## Patch-Stand der Daten

Alle Zahlen auf dieser Seite stammen aus der Ingame-Analyse, **Stand Okt 2026** (neun Bedingungen: 0 / 10.000 / 20.190 ft × 0 / 50 / 100 % Fuel). Gegenüber den Screenshots von Dez 2025 sind T-15 und T-18 unverändert. Die T-16 ist durch −20 % Treibstoffgewicht (v1.4.1) etwas leichter und minimal besser. Übersicht und Patch-Historie: [Flugzeugvergleich](/flugzeuge/vergleich#patch-historie).

## Was wir nicht wissen

::: info IM SPIEL PRÜFEN
- **Unter ~170 KIAS:** Die Diagramme beginnen erst bei ~170–200 KIAS. Steuerbarkeit, Rollrate und Stall-Verhalten darunter sind unbekannt.
- **Post-Stall mit AoA-Override:** Wie viel Nase bekommst du, wie viel Speed kostet es, wie fängst du ab?
- **Rollrate** der drei Jets.
- **Steigleistung:** Nicht direkt gemessen. Die Beschleunigung ist gemessen (siehe [Flugzeugvergleich](/flugzeuge/vergleich#beschleunigung-gemessen)), daraus folgt die Reihenfolge T-15 deutlich vor T-16 ≈ T-18.
- **Speedbrake:** Gibt es eine, und wie stark bremst sie?
- **Greyout-Modell:** G-Schwelle, Zeitverhalten, Erholung.
- **Schallgeschwindigkeit:** Welches Temperaturmodell VFM nutzt und wo Mach 1 damit genau in KIAS liegt.
:::

::: tip MERKE
- VFM simuliert **Höhe, transsonischen Widerstand, AoA, Gewicht**, dazu Buffeting und Greyout. 9 G sind die Grenze, Strukturschaden gibt es nicht.
- **Override** = Nase sofort, Energie weg. Nur für einen Schuss oder als letztes Mittel.
- **Transsonischer Widerstand:** Der Beiwert hat sein Maximum um Mach 1, die Kraft steigt weiter. Kämpf bei ~350–500 KIAS, nicht im Überschall.
- **Tief ist schneller und enger** – für alle Jets, besonders für T-16 und T-18.
- **VFM-Luft ist nicht die echte Luft:** wahre Fahrt nur ~12 % (10.000 ft) bzw. ~28 % (20.190 ft) über KIAS, die Corner Speed in KIAS steigt mit der Höhe.
- **Halber Tank** bringt ~1–2 °/s, leerer Tank bis zu 4 °/s – die Reihenfolge der Jets ändert das nicht.
:::

Weiter: [Relative Geometrie](/grundlagen/geometrie)
