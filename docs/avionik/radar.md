# Radar

> Wozu du das Radar im Nahkampf brauchst, was es dich kostet und wie du es bedienst.

In VFM gibt es **keine Radar-Raketen**. Das Radar hat zwei Aufgaben: den Gegner finden und per **Lock** eine Feuerleitlösung für die Kanone liefern. Gleichzeitig verrät es dich: Wer sein Radar an hat, erscheint beim Gegner auf dem [RWR](/avionik/rwr).

## Was gesichert ist (Patchnotes)

| Funktion | Stand |
|---|---|
| **An/Aus** | Radar aus = der gegnerische RWR empfängt nichts von dir. |
| **Vertikaler Scan** | Sucht auch nach oben und unten, bis **30° unter die Nase** (v1.1 / v1.2.0). |
| **Bodenclutter und Notching** | Bodenechos stören die Erfassung tiefer Ziele; ein Ziel kann im Clutter verschwinden (v1.2.0). |
| **Bedienung** | Linkes MFD mit Cursor/**TDC** (Target Designation Controller, wählt das Ziel auf dem Radarbild) |
| **Tastenbelegung** | Seit **v1.4.1** |
| **Lock** | Liefert die echte Entfernung für den Gun-Funnel (siehe [HUD](/avionik/hud)) |

## Modi (beobachtet)

Beobachtet, nicht durch Patchnotes bestätigt: drei Modi unten am Radar-Display, ein Power-Schalter links, bei ausgeschaltetem Radar ein rotes „RADAR OFF“.

| Modus | Was er tut | Einsatz |
|---|---|---|
| **SCAN** | Sucht einen breiten Bereich ab | Vor dem Merge den Gegner finden |
| **BST** (Boresight) | Schaut geradeaus, lockt das Ziel vor der Nase | Im Kurvenkampf: Nase auf den Gegner, Lock |
| **VERT** (Vertical) | Sucht einen vertikalen Streifen ab | Gegner über deiner Nase im Turn |

## Radar an oder aus?

| | Radar an | Radar aus |
|---|---|---|
| **Vorteil** | Lock = genauerer Funnel; Ziele finden, die du nicht siehst | Du bist auf seinem RWR unsichtbar |
| **Nachteil** | Er weiß, dass du da bist und woher du kommst | Funnel nur mit Durchschnitts-Spannweite; Suche nur mit den Augen |

- **Anflug, Gegner noch nicht gesehen:** abwägen. Radar an hilft dir suchen, gibt ihm aber die erste Information.
- **Schussgelegenheit naht:** Radar an und locken.
- **Teamkampf, Gegner ist gebunden:** Radar aus, mit den Augen anfliegen, erst kurz vor dem Schuss locken oder ohne Lock schießen.

## Bodenclutter und Notching

**Clutter** sind Radarechos vom Boden. **Notching** heißt: Das Ziel fliegt quer zu dir (etwa 90° Aspect), bewegt sich also kaum auf dich zu oder von dir weg. Vor Boden-Hintergrund ist es dann für das Radar kaum vom Boden zu unterscheiden.

- **Du jagst einen tiefen Gegner:** Der Lock kann abreißen. Dann zählt dein Auge.
- **Du bist defensiv und tief:** Quer zu ihm vor Boden-Hintergrund nimmst du ihm den genauen Funnel, aber nicht die Kanone.

::: warning NOTCHING SCHÜTZT NICHT VOR DER IR-RAKETE
Die IR-Rakete braucht kein Radar. Gegen sie helfen nur Manöver und Flares (siehe [Gegenmaßnahmen](/avionik/gegenmassnahmen)).
:::

## Radar im WVR-Dogfight

WVR (Within Visual Range) ist der Normalfall in VFM.

1. **Augen zuerst.** Ein Blick aufs linke MFD kostet Tally, also nur kurz.
2. **Lock, wenn ein Schuss naht.** Nase in seine Richtung, das Radar fasst ihn im Suchbereich auf.
3. **Lock weg? Weiterfliegen.** Ohne Lock schießt du mit Durchschnitts-Spannweite trotzdem.
4. **Lock blind erreichbar belegen** (siehe [Steuerung & Einstellungen](/einstieg/cockpit)).

::: info IM SPIEL PRÜFEN
- Heißen die Modi noch SCAN / BST / VERT, und lockt BST automatisch?
- Löst schon der Suchmodus beim Gegner eine RWR-Anzeige aus oder erst ein Lock?
- Bricht Notching einen bestehenden Lock oder nur die Suche, und ab welcher Höhe über Grund?
:::

::: tip MERKE
- Keine Radar-Raketen: Das Radar dient zum Finden und als Feuerleitlösung (Lock = genauerer Funnel).
- Radar an = du bist auf seinem RWR. Radar aus = still, Funnel nur mit Durchschnitts-Spannweite.
- Vertikaler Scan bis 30° unter die Nase; tiefe Ziele können im Clutter verschwinden.
- Notching wirkt nur gegen Radar, nie gegen die IR-Rakete.
- Augen vor Display: Tally ist wichtiger als ein Radarbild.
:::

Weiter: [HUD](/avionik/hud)
