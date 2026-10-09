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

Wo liegt Mach 1 in KIAS? Die angezeigte Speed bei Mach 1 sinkt mit der Höhe (Standardatmosphäre, gerechnet):

| Höhe | Mach 0,9 | Mach 1,0 |
|---|---|---|
| Meereshöhe | ~595 KIAS | ~661 KIAS |
| 10.000 ft | ~507 KIAS | ~566 KIAS |
| ~21.500 ft | ~412 KIAS | ~462 KIAS |
| 25.000 ft | ~384 KIAS | ~432 KIAS |

Das passt zu den Ingame-Daten: Auf ~21.500 ft liegt die Best Sustained Speed aller drei Jets bei 405 KIAS (≈ Mach 0,89), und auf 10.000 ft bricht die Sustained Rate der T-18 ab ~480 KIAS (≈ Mach 0,85) ein. Dass genau der transsonische Widerstand die Ursache ist, ist eine plausible Deutung, keine Herstellerangabe.

Was das für dich heißt:

- **BFM findet nicht im Überschall statt.** Die sinnvollen Kampf-Speeds liegen bei ~350–500 KIAS. Am Merge mit Mach 0,9+ anzukommen, bringt dir einen riesigen Radius und keinen Vorteil.
- **In großer Höhe** erreichst du den transsonischen Bereich schon bei viel niedrigerer KIAS. Dort ist der Spielraum zwischen "zu langsam für 9 G" und "Widerstandswand" klein.
- **T-18:** Hohe Speed ist ihr schlechtester Bereich. **T-15:** hält dort am besten durch.

## Höhe

Mit der Höhe sinkt die Luftdichte. Bei gleicher KIAS bist du in der Höhe wahr schneller – dadurch werden Rate kleiner und Radius größer (siehe [Kurvenphysik](/grundlagen/kurvenphysik#kias-vs-wahre-speed-in-der-hohe)). Dazu kommt der transsonische Widerstand bei niedrigerer KIAS.

Ingame-Daten, 50 % Fuel (Stand Dez 2025):

| Höhe | | T-15 | T-16 | T-18 |
|---|---|---|---|---|
| Meereshöhe | Instant | 29 °/s @ 337 | 25 °/s @ 392 | 27 °/s @ 365 |
| | Sustained | 20 °/s @ 475 | 22 °/s @ 447 | 20 °/s @ 447 |
| | Min Radius | 1.138 ft | 1.524 ft | 1.313 ft |
| 10.000 ft | Instant | 24 °/s @ 360 | 21 °/s @ 409 | 22 °/s @ 385 |
| | Sustained | 17 °/s @ 495 | 18 °/s @ 470 | 16 °/s @ 470 |
| | Min Radius | 1.644 ft | 2.102 ft | 1.899 ft |
| ~21.500 ft | Instant | 19 °/s @ 383 | 17 °/s @ 436 | 17 °/s @ 426 |
| | Sustained | 13 °/s @ 405 | 13 °/s @ 405 | 12 °/s @ 405 |
| | Min Radius | 2.578 ft | 3.287 ft | 3.086 ft |

Was du daraus mitnimmst:

- **Alle Jets verlieren mit der Höhe**, und zwar deutlich: Von Meereshöhe auf ~21.500 ft fallen Instant und Sustained um rund ein Drittel bis 40 %, der Radius wächst auf mehr als das Doppelte.
- **Der Sustained-Vorsprung der T-16 ist auf Meereshöhe am größten** (22 vs. 20 °/s) und auf ~21.500 ft weg.
- **Die T-15 profitiert relativ von Höhe:** Sie behält auf ~21.500 ft zwischen ~400 und 600 KIAS ein flaches Sustained-Plateau um 12 °/s, die anderen fallen ab.

## Treibstoff und Munition

VFM simuliert Treibstoff- und Munitionsgewicht. Die Ingame-Daten (10.000 ft) zeigen den Effekt des Treibstoffs:

| | T-15 | T-16 | T-18 |
|---|---|---|---|
| Gewicht 100 % Fuel | 42.160 lbs | 27.972 lbs | 41.226 lbs |
| Gewicht 50 % Fuel | 37.615 lbs | 25.009 lbs | 36.597 lbs |
| Instant 100 % → 50 % | 23 → 24 °/s | 20 → 21 °/s | 21 → 22 °/s |
| Sustained 100 % → 50 % | 15 → 17 °/s | 16 → 18 °/s | 15 → 16 °/s |

- Von 100 auf 50 % Fuel sinkt das Gewicht um **~11 %**. Das bringt **~+1 °/s Instant** und **+1–2 °/s Sustained**.
- **Die Reihenfolge der Jets ändert sich nicht.** Bei vollem Tank ist der Sustained-Vorsprung der T-16 nur kleiner (16 vs. 15 °/s).
- **Munition:** Ihr Gewicht wird simuliert, wie groß der Effekt ist, ist nicht bekannt. Sind alle Waffen leer, startet ein Selbstzerstörungs-Countdown – Nachladen gibt es nicht. Siehe [Waffen](/avionik/waffen).

## Patch-Stand der Daten

Alle Zahlen auf dieser Seite stammen aus der Ingame-Analyse **vor Patch v1.1** (Stand Dez 2025). Seitdem wurde nachjustiert:

- **v1.1:** T-15 −3 % Lift, +7 % Schub. T-18 mehr Treibstoffgewicht, weniger Leergewicht.
- **v1.4.1:** T-15 Top-Speed reduziert. T-16 Treibstoffgewicht −20 %. T-18 Top-Speed erhöht.

Die Grundaussagen (wer wo stark ist) sind dadurch nicht umgedreht, aber die genauen Zahlen können abweichen. Aktuelle Übersicht: [Flugzeugvergleich](/flugzeuge/vergleich).

## Was wir nicht wissen

::: info IM SPIEL PRÜFEN
- **Unter ~170 KIAS:** Die Diagramme beginnen erst bei ~170–200 KIAS. Steuerbarkeit, Rollrate und Stall-Verhalten darunter sind unbekannt.
- **Post-Stall mit AoA-Override:** Wie viel Nase bekommst du, wie viel Speed kostet es, wie fängst du ab?
- **Rollrate** der drei Jets.
- **Steigleistung und Beschleunigung:** Nicht in den Daten. Die T/W-Balken der Info-Karten deuten T-15 > T-18 > T-16 an – grob und nicht exakt.
- **Speedbrake:** Gibt es eine, und wie stark bremst sie?
- **Greyout-Modell:** G-Schwelle, Zeitverhalten, Erholung.
- **Aktuelle Zahlen nach v1.1 und v1.4.1:** Die Ingame-Analyse im aktuellen Spiel aufrufen und mit den Tabellen hier vergleichen.
:::

::: tip MERKE
- VFM simuliert **Höhe, transsonischen Widerstand, AoA, Gewicht**, dazu Buffeting und Greyout. 9 G sind die Grenze, Strukturschaden gibt es nicht.
- **Override** = Nase sofort, Energie weg. Nur für einen Schuss oder als letztes Mittel.
- **Transsonischer Widerstand:** Der Beiwert hat sein Maximum um Mach 1, die Kraft steigt weiter. Kämpf bei ~350–500 KIAS, nicht im Überschall.
- **Tief ist schneller und enger** – für alle Jets, besonders für T-16 und T-18.
- **Halber Tank** bringt ~1–2 °/s, ändert aber die Reihenfolge der Jets nicht.
:::

Weiter: [Relative Geometrie](/grundlagen/geometrie)
