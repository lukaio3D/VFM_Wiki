# Radar

> Wozu du das Radar im Nahkampf brauchst, was es dich kostet und wie du es bedienst.

In VFM gibt es **keine Radar-Raketen**. Das Radar hat im Dogfight vor allem zwei Aufgaben: den Gegner finden und per **Lock** eine Feuerleitlösung für die Kanone liefern. Gleichzeitig verrät es dich: Wer sein Radar an hat, erscheint beim Gegner auf dem RWR.

## Was gesichert ist

| Funktion | Stand |
|---|---|
| **An/Aus** | Radar kann ausgeschaltet werden. Radar aus = der gegnerische RWR empfängt nichts von dir. |
| **Vertikaler Scan** | Das Radar sucht auch nach oben und unten, bis **30° unter die Nase** (v1.1 / v1.2.0). |
| **Bodenclutter** | Bodenechos stören die Erfassung tief fliegender Ziele (v1.2.0). |
| **Notching** | Gegen Clutter möglich (v1.2.0): Ein Ziel kann im Bodenclutter verschwinden. |
| **Bedienung** | Über das **linke MFD** (Multifunktionsdisplay) mit Cursor/TDC |
| **Tastenbelegung** | Radarfunktionen sind seit **v1.4.1** auf Tasten belegbar. |
| **Lock** | Liefert die Feuerleitlösung für den Gun-Funnel (siehe [HUD](/avionik/hud)) |

Der **TDC** (Target Designation Controller) ist der Cursor, mit dem du auf dem Radarbild ein Ziel auswählst.

## Modi und Display (laut Beobachtung, Stand Dez 2025)

Eine frühere Version dieses Wikis beschreibt drei Modi, die unten auf dem Radar-Display wählbar sind, und einen Power-Schalter links am Display. Die Namen sind nicht durch Patchnotes bestätigt.

| Modus | Beschreibung (laut Beobachtung) | Typischer Einsatz |
|---|---|---|
| **SCAN** | Suchmodus, breiter Bereich | Vor dem Merge den Gegner finden |
| **BST** (Boresight) | Radar schaut geradeaus, lockt das Ziel vor der Nase | Im Kurvenkampf: Nase auf den Gegner, Lock |
| **VERT** (Vertical) | Sucht einen vertikalen Streifen ab | Gegner über dir im Kurvenkampf (z.B. oberhalb der Nase im Turn) |

Ist das Radar aus, erscheint laut Beobachtung ein rotes "RADAR OFF" auf dem Display.

::: info IM SPIEL PRÜFEN
- Heißen die Modi im aktuellen Patch noch SCAN / BST / VERT? Wie wird gewechselt?
- Lockt BST automatisch, oder brauchst du eine Lock-Taste?
- Wie groß sind Reichweitenmaßstab und Suchbereich (Azimut) in jedem Modus?
- Wo sitzt der Power-Schalter, und wie zeigt das HUD einen Lock an?
- Unterstützt ein Radar-Lock auch die IR-Rakete (z.B. Suchkopf auf das Ziel ausrichten)?
- Löst schon der Suchmodus beim Gegner eine RWR-Anzeige aus, oder erst ein Lock?
:::

## Radar an oder aus? Der Grundkonflikt

| | Radar an | Radar aus |
|---|---|---|
| **Vorteil** | Lock = Feuerleitlösung für die Kanone; Ziele finden, die du nicht siehst | Du bist auf dem gegnerischen RWR unsichtbar |
| **Nachteil** | Der Gegner weiß, dass du da bist und woher du kommst | Gun-Funnel nutzt nur eine durchschnittliche Spannweite; Suche nur mit den Augen |

Daraus ergibt sich eine einfache Logik (Tipps):

- **Anflug, Gegner noch nicht gesehen:** Abwägen. Radar an hilft dir, ihn zu finden, verrät dich aber. Gegen einen Gegner, der selbst kein Radar nutzt, gibst du ihm so die erste Information.
- **Ziel im Visier, Schussgelegenheit naht:** Radar an und locken. Eine echte Entfernung macht den Funnel genauer.
- **Teamkampf, du willst unbemerkt an einen gebundenen Gegner heran:** Radar aus, mit den Augen anfliegen, erst kurz vor dem Schuss locken (oder ganz ohne Lock schießen).

Wie RWR und Warnsystem auf der Gegenseite aussehen: [RWR & MWS](/avionik/rwr).

## Bodenclutter und Notching

**Clutter** sind Radarechos vom Boden. Fliegt ein Ziel tief vor Boden-Hintergrund, kann es im Clutter untergehen. **Notching** heißt: Das Ziel fliegt so, dass es sich relativ zu deinem Radar kaum auf dich zu oder von dir weg bewegt (etwa quer zu dir, 90° Aspect). Dann ist es für ein Doppler-Radar schwer vom Boden zu unterscheiden. In VFM ist das laut Patchnotes gegen Clutter möglich.

Was das praktisch heißt:

- **Du jagst einen tief fliegenden Gegner:** Ein Lock kann abreißen, wenn er quer vor Boden-Hintergrund fliegt. Dann zählt dein Auge, nicht das Radar.
- **Du bist defensiv und tief:** Quer zum Gegner vor Boden-Hintergrund zu fliegen kann seinen Lock brechen – das nimmt ihm die genaue Funnel-Lösung, aber nicht die Kanone selbst und nicht die IR-Rakete.

::: warning NOTCHING SCHÜTZT NICHT VOR DER IR-RAKETE
Notching wirkt nur gegen Radar. Die IR-Rakete braucht kein Radar. Gegen sie helfen nur Manöver und Flares (siehe [Gegenmaßnahmen](/avionik/gegenmassnahmen)).
:::

::: info IM SPIEL PRÜFEN
- Ab welcher Höhe über Grund und welchem Aspect verliert das Radar ein Ziel im Clutter?
- Bricht Notching einen bestehenden Lock oder nur die Suche?
:::

## Radar im WVR-Dogfight

**WVR** (Within Visual Range) heißt: Der Kampf findet in Sichtweite statt – der Normalfall in VFM.

1. **Augen zuerst.** Der Gegner bleibt außerhalb des Cockpits. Ein Blick aufs linke MFD kostet dich Tally, also nur kurz und gezielt.
2. **Lock, wenn ein Schuss naht.** Im Kurvenkampf bringst du die Nase in seine Richtung; das Radar fasst ihn innerhalb seines Suchbereichs auf. Der vertikale Scan reicht bis 30° unter die Nase.
3. **Lock weg? Weiterfliegen.** Ein verlorener Lock ist kein Grund, die Geometrie zu vernachlässigen. Ohne Lock nutzt der Funnel eine durchschnittliche Spannweite – Schießen geht trotzdem.
4. **Belegung nutzen.** Seit v1.4.1 kannst du Radarfunktionen auf Tasten legen. Lock auf eine Taste, die du blind findest (siehe [Steuerung & Einstellungen](/einstieg/cockpit)).

::: tip MERKE
- Keine Radar-Raketen: Das Radar dient zum Finden und als Feuerleitlösung (Lock → genauerer Gun-Funnel).
- Radar an = du bist auf seinem RWR. Radar aus = still, aber Funnel nur mit Durchschnitts-Spannweite.
- Vertikaler Scan bis 30° unter die Nase; tiefe Ziele können im Clutter verschwinden (Notching).
- Bedienung über linkes MFD + TDC, Tasten seit v1.4.1 – Lock blind erreichbar belegen.
- Augen vor Display: Tally ist wichtiger als ein Radarbild.
:::

Weiter: [HUD](/avionik/hud)
