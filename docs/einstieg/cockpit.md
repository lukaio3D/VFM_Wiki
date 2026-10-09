# Steuerung & Einstellungen

> Stick, Schubhebel, die wichtigsten Tastenbelegungen und wie du in VR den Gegner im Blick behältst.

Alle drei Jets haben dasselbe Cockpit mit **Side-Stick** (Steuerknüppel seitlich rechts) und identischer Avionik. Was du hier einmal einrichtest, gilt für T-15, T-16 und T-18. VFM ist bewusst schlank: Es gibt **kein Fahrwerk, keine Landung, keinen Start, keine Klappen- oder Hook-Bedienung**. Du startest in der Luft und kämpfst.

## VR-Controller: virtueller Stick und Schubhebel

Standardmäßig fliegst du mit den VR-Controllern: Die rechte Hand greift den virtuellen Stick, die linke den virtuellen Schubhebel.

In den Einstellungen kannst du anpassen:

- **Position** von Stick und Schubhebel – so, dass deine Hände bequem und entspannt liegen, z.B. auf den Oberschenkeln oder Armlehnen.
- **Modus "translation vs tilt"** – ob der Stick auf das **Verschieben** der Hand oder auf das **Kippen** des Controllers reagiert.

::: info IM SPIEL PRÜFEN
- Wie genau unterscheiden sich "translation" und "tilt" im Flug? Teste beide je 10 Minuten in Free Flight mit derselben Übung (z.B. sauberer 360°-Turn auf konstanter Höhe und Speed).
- Gibt es Einstellungen für Empfindlichkeit, Deadzone oder Kurven des VR-Sticks?
- Gibt der Controller haptisches Feedback (z.B. bei Buffeting oder hohem G)?
:::

**Tipp:** Stütze Unterarm oder Handgelenk ab. Präzises Zielen mit der Kanone geht aus einer abgestützten Hand deutlich besser als aus einem frei schwebenden Arm – egal welcher Modus.

## Hardware: HOTAS, Pedale, Gamepad

VFM unterstützt HOTAS, Pedale und Gamepad nativ. Aktiviere dafür in den Einstellungen **"enable hardware controllers"**. Die Menüs bedienst du weiterhin mit den VR-Controllern – leg sie also griffbereit ab.

Tipps zum HOTAS (Erfahrungswerte, keine Spielvorgabe):

- **Stick rechts seitlich** passt zum Side-Stick im Cockpit und verwirrt das Gehirn weniger als ein Center-Stick.
- **Kleine Deadzone, höchstens leichte Kurve.** Starke Kurven machen das Ziehen bis ans Limit unpräzise – und im Dogfight ziehst du oft bis ans Limit.
- **Schubhebel mit spürbarer Idle-Position.** Du brauchst Idle blind und sofort (Raketenabwehr, Overshoot vermeiden).
- **Pedale** sind optional. Ob und wie stark das Seitenruder im Kampf hilft (z.B. für kleine Korrekturen beim Zielen), testest du am besten selbst.

## Die Belegungen, die du wirklich brauchst

Leg diese Funktionen auf Tasten, die du **ohne Hinschauen und ohne den Stick loszulassen** erreichst. Die genauen Funktionsnamen im Menü und die Standardbelegung sind hier nicht dokumentiert.

| Funktion | Warum wichtig |
|---|---|
| **Kanone feuern** | Schussfenster sind oft unter einer Sekunde lang. |
| **Rakete feuern / Waffe wählen** | Wechsel zwischen Kanone und IR-Rakete ("Heater", Fox 2). |
| **Flares** | Muss blind und sofort gehen, auch mitten im Break Turn. |
| **AoA-Override ("Cobra-Button")** | Hebt den AoA-Limiter auf (siehe unten). Halten, nicht suchen. |
| **Radar an/aus, Lock, Cursor/TDC** | Seit v1.4.1 auf Tasten belegbar. Lock liefert die Feuerleitlösung für den Gun-Funnel. |
| **Push-to-Talk** | Eingebauter Voice-Chat. Im Teamkampf Pflicht. |
| **View Recenter** | Sitzposition nach Verrutschen sofort zurücksetzen. |

::: info IM SPIEL PRÜFEN
- Standardbelegung aller oben genannten Funktionen auf VR-Controllern, HOTAS und Gamepad.
- Gibt es einen Nachbrenner mit Raste am Schubhebel, und wie wird er angezeigt?
- Gibt es eine Speedbrake (Luftbremse), und ist sie belegbar?
- Welche Radar-Funktionen genau seit v1.4.1 belegbar sind (z.B. Moduswechsel, Lock, TDC-Bewegung).
:::

### AoA-Limiter und Override

Der Jet begrenzt normalerweise den **AoA** (Angle of Attack, Anstellwinkel – siehe [Begriffe](/grundlagen/begriffe)). Mit dem Override-Button ("Cobra-Button") hebst du diese Grenze auf: Du bekommst **sofort Nase**, also Nose Authority über das normale Limit hinaus.

- **Kosten:** extrem viel Energie. Nach einem Override bist du langsam und musst erst wieder Speed aufbauen.
- **G-Limit bleibt aktiv.** Der Override hebt nur das AoA-Limit auf, nicht die 9-G-Grenze.
- **Kein Strukturschaden durch G** – du kannst den Jet nicht zerbrechen.

Einsatz: gezielt für einen Schuss oder als letzte Abwehr, wenn die Nase jetzt sofort herum muss. Nicht als Standard-Turn. Mehr dazu: [Energie-Management](/grundlagen/energie-management).

## Rundumblick und Padlock in VR

VFM hat **kein Helmvisier (HMD)** und keine Padlock-Taste, die deinen Blick automatisch auf den Gegner hält. Dein Kopf ist das Padlock. **Padlocked** heißt im Funk: "Ich kann den Blick nicht vom Gegner nehmen."

Technik (Tipps):

- **Kopf und Oberkörper drehen.** Um nach hinten über die Schulter zu sehen, drehst du den Oberkörper mit und beugst dich leicht zur Seite. Nur den Kopf zu drehen reicht nicht bis zur 6-Uhr-Position.
- **Im Turn durch das Kabinendach schauen.** In einer Kurve liegt der Gegner meist "oben" in deinem Sichtfeld – dort, wohin dein Lift Vector (Auftriebsrichtung, Richtung Kabinendach) zeigt. Kopf in den Nacken, den Gegner durch die Haube verfolgen und den Lift Vector auf ihn rollen.
- **Tally nicht abgeben.** Wenn du nach unten auf ein Display schaust, verlierst du ihn. Blick auf Instrumente nur kurz und nur, wenn der Gegner gerade nicht entscheidend manövriert.
- **Vor dem Merge den Gegner groß ansehen.** Wenn er dich passiert, folgt dein Kopf ihm über die Schulter, nicht die Nase des Jets.
- **Verlierst du ihn:** RWR prüfen (falls er sein Radar an hat), dann in die Richtung schauen, in die er zuletzt gedreht hat. Siehe [RWR & MWS](/avionik/rwr).

::: tip MERKE
- Gleiches Cockpit in allen drei Jets – einmal einrichten, überall nutzen.
- Hardware-Controller erst nach "enable hardware controllers"; Menüs bleiben auf den VR-Controllern.
- Flares, AoA-Override, Waffenwahl, Radar-Lock, Push-to-Talk und Recenter blind erreichbar belegen.
- Override = sofort Nase, kostet extrem Energie; das G-Limit bleibt.
- Dein Kopf ist das Padlock: Oberkörper mitdrehen, durch das Kabinendach schauen, Tally halten.
:::

Weiter: [Spielmodi](/einstieg/spielmodi)
