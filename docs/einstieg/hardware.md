# Hardware & Plattformen

> Was du brauchst, um VFM zu fliegen, und wie du dein Setup so einstellst, dass du den Gegner früher siehst.

VFM ist ein VR-Spiel von Boundless Dynamics (dem Studio hinter VTOL VR). Release war am 19.12.2025, aktuell ist Version v1.4.2. Diese Seite trennt klar zwischen **gesicherten Fakten** (Steam-Store, Patchnotes) und **Tipps** aus der Praxis.

## Plattformen

| Plattform | Status |
|---|---|
| **PCVR** (Steam, OpenXR/SteamVR) | Ja |
| **Meta Quest 2 / 3 / 3S / Pro** | Ja, nativ (standalone, ohne PC) |
| **Crossplay** PC ↔ Quest | Ja |
| **Cross-Buy** | **Nein** – Steam- und Quest-Version musst du getrennt kaufen |
| **Flatscreen** (ohne Headset) | Laut einem Steam-Community-Guide möglich, nachdem das Spiel einmal in VR eingerichtet wurde |

::: warning FLATSCREEN IST KEIN OFFIZIELLER MODUS
Die Menüs werden mit den VR-Controllern bedient. Ohne Headset kommst du also zumindest für die Ersteinrichtung nicht aus. Der Flatscreen-Weg stammt aus einem Community-Guide, nicht aus dem Store-Text.
:::

## PCVR: Mindestanforderungen (Steam)

| Komponente | Minimum |
|---|---|
| Betriebssystem | Windows 10, 64-bit |
| Prozessor | Intel i5-3570 |
| Arbeitsspeicher | 16 GB RAM |
| Grafikkarte | NVIDIA GTX 970 |
| DirectX | Version 11 |
| Speicherplatz | 500 MB |

Der Store nennt **keine empfohlenen Specs**. Alles darüber hinaus ist Erfahrungswert: Mehr GPU-Leistung bringt dir vor allem eine höhere Renderauflösung – und die ist für das Spotten entscheidend (siehe unten).

## Quest standalone oder PCVR?

Beide Versionen spielen gegeneinander (Crossplay). Wie stark sich Grafik, Sichtweite und Darstellung kleiner Ziele unterscheiden, ist nicht offiziell dokumentiert.

::: info IM SPIEL PRÜFEN
- Unterscheidet sich die Sichtweite bzw. Darstellung weit entfernter Jets zwischen Quest und PCVR?
- Ist das Flugmodell auf beiden Plattformen identisch? (Naheliegend wegen Crossplay, aber nicht offiziell bestätigt.)
- Welche Bildrate/Renderauflösung läuft auf Quest nativ, und lässt sie sich einstellen?
:::

**Faustregel für die Wahl (Tipp):** Hast du einen brauchbaren Gaming-PC, lohnt sich ein Test per Link-Kabel oder Air Link mit erhöhter Renderauflösung. Ohne PC ist die native Quest-Version die unkomplizierte Lösung – du spielst im selben Spielerpool.

## Eingabegeräte

VFM unterstützt nativ:

- **VR-Controller** mit virtuellem Stick und Schubhebel im Cockpit (Standard)
- **HOTAS** (Stick + Schubhebel)
- **Pedale**
- **Gamepad**

Hardware-Eingabegeräte musst du in den Einstellungen mit **"enable hardware controllers"** aktivieren. Die Menüs bedienst du trotzdem weiter mit den VR-Controllern. Details zur Belegung: [Steuerung & Einstellungen](/einstieg/cockpit).

## Praxis-Tipps für dein VR-Setup

Diese Punkte sind **Tipps**, keine Spielfakten. Sie helfen dir, länger konzentriert zu fliegen und den Gegner früher zu sehen.

### Sitzend fliegen

- Spiel im Sitzen. Ein fester Stuhl ohne Rollen gibt dir eine stabile Referenz, ein Drehstuhl erleichtert den Blick nach hinten (Kabel beachten).
- Kalibriere die Sitzposition so, dass du dich im Cockpit **vorbeugen und den Oberkörper drehen** kannst. Den Gegner hinter dir siehst du nur mit Kopf **und** Schulter.
- Lege dir **View Recenter** auf eine Taste, die du blind findest.

### Komfort

- Neu in VR-Flug? Kurze Sessions, Pause bei den ersten Anzeichen von Übelkeit – nicht "durchziehen".
- Ein Ventilator, der dir ins Gesicht bläst, hilft vielen Spielern gegen Übelkeit und Hitze.
- Greyout und Blackout sind im Spiel simuliert. Das ist gewollt und kein Grafikfehler.

### Schärfe = früherer Tally

**Tally** heißt: Du hast den Gegner in Sicht (siehe [Begriffe](/grundlagen/begriffe)). Im Nahkampf gewinnt oft, wer den anderen zuerst sieht und nicht mehr verliert.

- **Linsen sauber, IPD richtig, Headset richtig sitzend.** Der scharfe Bereich ist bei vielen Headsets klein – die Augen gehören in die Mitte der Linsen.
- **Renderauflösung so hoch wie möglich bei stabiler Bildrate.** Ein entfernter Jet ist nur wenige Pixel groß; bei niedriger Auflösung flimmert oder verschwindet er.
- **Stabile Bildrate vor Schönheit.** Ruckler in schnellen Kopfbewegungen kosten dich den Gegner. Schatten und Effekte zuerst reduzieren.
- **Bei Quest per Link/Air Link:** Bitrate und Netzwerk sind dann Teil deiner Sicht. Bei Air Link ein Router in Raumnähe, PC per Kabel am Router.

### Verbindung

Zur Netzwerkarchitektur (Server, Hit-Registrierung) gibt es keine offiziellen Angaben. Praktisch gilt wie bei jedem Online-Spiel: PC per LAN-Kabel, Quest mit gutem WLAN nahe am Router.

::: tip MERKE
- PCVR (OpenXR/SteamVR) und Quest 2/3/3S/Pro nativ, Crossplay ja, Cross-Buy nein.
- Offiziell gibt es nur Mindestanforderungen (GTX 970, 16 GB RAM) – keine empfohlenen Specs.
- HOTAS, Pedale und Gamepad gehen nativ, aber erst nach "enable hardware controllers".
- Sitzend fliegen, Platz zum Umdrehen lassen, Recenter auf eine Taste.
- Schärfe und stabile Bildrate sind kein Luxus: Sie entscheiden, wer zuerst Tally hat.
:::

Weiter: [Steuerung & Einstellungen](/einstieg/cockpit)
