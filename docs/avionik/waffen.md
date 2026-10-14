# Waffen

> Kanone und IR-Rakete: was du hast, was die Lobby ändert und wann du welche Waffe nutzt.

Alle drei Jets haben dieselbe Bewaffnung. **Radar-Raketen gibt es nicht.**

| Waffe | Beschreibung |
|---|---|
| **Bordkanone** („Guns“) | Zielhilfe über den Gun-Funnel im [HUD](/avionik/hud) |
| **IR-Rakete** („Heater“, Funkruf **Fox 2**) | Wärmesuchend, ein einziger Typ |

## Match-Einstellungen

Was du dabeihast, legt die Lobby fest (siehe [Spielmodi](/einstieg/spielmodi)): Raketen an/aus und Anzahl, Infinite Ammo, Head-on Guns erlaubt oder verboten. **Ranked 1v1 ist Guns-only:** In 71 eigenen 1v1-Replays fielen 63 Abschüsse mit der Kanone, der Rest waren Abstürze, keine einzige Rakete (*Replays*). Vor dem ersten Pass fällt kein Schuss (Merge Safety).

Munition und Treibstoff haben **Gewicht**. Ein leichterer Jet dreht besser (10 % leichter ≈ 10 % mehr dauerhafte G). Voll → leer getankt sind die Jets ~18–22 % leichter (T-15 19,15 → 15,0 t, T-16 12,14 → 10,0 t, T-18 18,70 → 14,5 t, *Spieldaten*); wie viel Munition und Raketen ausmachen, ist nicht dokumentiert (siehe [Das VFM-Flugmodell](/grundlagen/physik#treibstoff-und-munition)).

## Leere Stores: Selbstzerstörung

Ohne Munition und Raketen startet ein **Selbstzerstörungs-Countdown**. Nachladen gibt es nicht. Lange Salven ohne echte Lösung kosten dich im Zweifel die Runde: Schieß, wenn der Funnel passt.

## Bordkanone

Gegen die Kanone helfen keine Flares, nur Manövrieren (siehe [Guns Defense](/grundlagen/defensiv/guns-defense)).

| Kennzahl | Wert | Quelle |
|---|---|---|
| **Mündungsgeschwindigkeit** | 1.030 m/s (~3.380 ft/s), zusätzlich zur eigenen Speed | *Spieldaten*, in *Replays* bestätigt |
| **Kadenz** | 6.000 Schuss/min = 100 pro Sekunde | *Spieldaten* |
| **Schaden** | 26 je Treffer | *Spieldaten* |
| **Flugzeit bis 3.000 ft (~900 m)** | ~0,75 s | *Spieldaten*, *Replays* |
| **Geschosse fliegen** | ~6 s und ~4,5 km weit, am Ende noch ~600 m/s | *Replays* |

Was daraus folgt:

- **Vorhalt ist echt.** Auf 3.000 ft ist das Geschoss eine Dreiviertelsekunde unterwegs; ein Gegner mit 400 KIAS auf 10.000 ft fliegt in der Zeit ~600 ft weiter. Deshalb führt der Funnel vor, und deshalb trifft ein Schuss auf seine heutige Position nicht.
- **Nah ist besser.** Die Geschosse fliegen zwar kilometerweit, aber je weiter, desto länger die Flugzeit und desto mehr muss der Vorhalt stimmen. Wie weit die Kanone effektiv trifft und wie stark sie streut, ist nicht gemessen.
- **Ein Burst sind viele Treffer.** 100 Schuss pro Sekunde: Schon eine Zehntelsekunde im Ziel sind ~10 Geschosse. Wie viele Treffer ein Jet aushält, ist nicht bekannt.

So schießt du:

- **Zielen:** mit dem Funnel, mit Radar-Lock genauer.
- **Schusstypen:** **Tracking Shot** in seiner Ebene, Funnel bleibt auf ihm. **Snapshot** bei großem Winkel, er läuft durch den Funnel.
- **Kurze Bursts,** solange die Lösung passt. Hört die Lösung auf, hörst du auf.
- **Auf der Nase:** Nach dem ersten Pass sind Frontalschüsse möglich; 14 % aller Schüsse in den Replays fallen bei fast frontalem Aspect (160–180°).

## IR-Rakete (Heater / Fox 2)

Die Rakete sucht die Wärme des Gegners und braucht **kein Radar**. Schießt du ohne Radar, sieht er nichts auf dem RWR; nur sein MWS warnt ihn (siehe [RWR & MWS](/avionik/rwr)).

- **Suchkopf-Ton:** Ein Ton zeigt, dass der Suchkopf ein Ziel hat. Lern ihn in Free Flight oder gegen Bots kennen.
- **Aspect:** Laut Community trifft sie auch frontal (All-Aspect), offiziell bestätigt ist das nicht.
- **Abwehr:** Flares und Manöver (siehe [Gegenmaßnahmen](/avionik/gegenmassnahmen)).

Ihre **WEZ** (Weapons Engagement Zone, siehe [Begriffe](/grundlagen/begriffe)) hängt ab von Mindest- und Maximalreichweite, Off-Boresight (wie weit neben der Nase), Aspect (von hinten leichter) sowie Energie und Manöver des Ziels. Für VFM sind diese Grenzen nicht veröffentlicht: Merk dir Bilder („so groß sah er aus, als die Rakete getroffen hat“).

## Kanone oder Rakete?

- **Fox 2 erzwingt Reaktion.** Auch eine Rakete, die vorbeigeht, zwingt ihn meist zu Flares und einem harten Break. Das kostet ihn Energie, danach kommst du leichter zur Kanonenlösung.
- **Dicht hinter ihm in seiner Ebene:** Guns.
- **Enger One-Circle:** Du unterläufst leicht die Mindestreichweite der Rakete, dann bleibt die Kanone.

Ausführlich mit Entscheidungsbaum: [Schusslösung](/grundlagen/offensiv/schussloesung).

::: info IM SPIEL PRÜFEN
- Wie viele Schuss hat die Kanone (bei 100 Schuss/s: Sekunden Dauerfeuer), und wie lang ist der Selbstzerstörungs-Countdown?
- Effektive Reichweite und Streuung der Kanone, Treffer bis zum Abschuss (in einer Infinite-Ammo-Lobby mit einem Freund testen). Mündungsgeschwindigkeit, Kadenz und Schaden sind aus den Spieldaten bekannt.
- IR-Rakete: Mindest- und Maximalreichweite, Off-Boresight, trifft sie zuverlässig frontal?
:::

::: tip MERKE
- Zwei Waffen: Kanone (Funnel) und eine IR-Rakete (Fox 2). Keine Radar-Raketen.
- Die Lobby legt Raketen, Anzahl, Infinite Ammo und Head-on Guns fest; Ranked 1v1 ist Guns-only (Replays).
- Kanone: 1.030 m/s, 100 Schuss/s; auf 3.000 ft ~0,75 s Flugzeit, also Vorhalt über den Funnel.
- Leere Stores = Selbstzerstörung. Nur mit Lösung schießen.
- Die IR-Rakete braucht kein Radar: Der Gegner bekommt nur eine MWS-Warnung.
- Fox 2 zwingt ihn in die Defensive, die Kanone holt den Abschuss.
:::

Weiter: [Gegenmaßnahmen](/avionik/gegenmassnahmen)
