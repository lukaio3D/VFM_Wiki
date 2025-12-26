# Defensive Manöver

Defensive Manöver nutzt du, wenn der Gegner hinter dir ist. Ziel: Überleben und die Situation umkehren.

## Grundprinzip: Overshoot erzwingen

Dein Hauptziel in der Defensive ist es, den Gegner zum **Overshoot** zu zwingen. Dann wechseln die Rollen.

```mermaid
flowchart LR
    DEF[Du: Defensiv] --> FORCE[Overshoot erzwingen]
    FORCE --> SWITCH[Rollentausch!]
    SWITCH --> OFF[Du: Offensiv]
```

---

## Break Turn

Der härteste Turn, den du fliegen kannst. Nutze ihn als erste Reaktion auf einen Angriff.

### Ausführung

1. **Max G** - Ziehe so hart du kannst
2. **In Richtung Bedrohung** - Drehe ZUM Gegner
3. **Leichtes Sinken** - Hilft den Turn zu verschärfen
4. **Afterburner** - Halte Speed so gut es geht

::: warning ENERGIE-KOSTEN
Break Turns kosten enorm viel Energie. Nutze sie nur wenn nötig!
:::

### Wann Break Turn?

```mermaid
flowchart TD
    THREAT[Bedrohung erkannt] --> Q{Gegner Position?}

    Q -->|Direkt hinter dir| BREAK[Break Turn JETZT!]
    Q -->|Seitlich| ASSESS[Situation bewerten]
    Q -->|Weit weg| PREP[Vorbereiten]

    BREAK --> SURVIVE[Überleben]
    ASSESS --> |"Nähert sich"| BREAK
    PREP --> ENERGY[Energie aufbauen]
```

---

## Scissors (Scherenmanöver)

Scissors treten auf, wenn ein Overshoot passiert und der Verteidiger versucht, den Angreifer durch Bremsen und Kurvenwechsel vor sich zu zwingen.

### Flat Scissors (Horizontale Schere)

**Beschreibung:** Zwei Flugzeuge weben horizontal hin und her, wie Scherenblätter. Wer langsamer fliegen kann, gewinnt.

**Ausführung:**
1. Schub reduzieren (Idle)
2. Speedbrakes ausfahren
3. Schnelle Roll-Reversals
4. Versuche, hinter den Gegner zu kommen

::: warning WARNUNG
Flat Scissors sind ein **Slow-Speed Fight**. Flugzeuge mit guter Low-Speed Manövrierbarkeit (Angles Fighter) haben hier Vorteile. Flugzeuge, die auf Energie angewiesen sind, sollten Flat Scissors vermeiden.
:::

### Rolling Scissors (Vertikale Schere)

**Beschreibung:** Beide Flugzeuge fliegen korkenzieherartig umeinander, wobei sie fortlaufend Höhe und Geschwindigkeit tauschen. Es ist eine Serie von "Fassrollen" umeinander.

**Ausführung:**
1. Wenn du am Gegner vorbeischießt, ziehe sofort **hoch in die Vertikale** (ca. 60-70°)
2. Nutze den Schub, um höher zu steigen als der Gegner
3. Rolle über dem Gegner zurück und ziehe die Nase nach unten

**Warum es funktioniert:**
- Die Vertikale bremst beide Flugzeuge natürlich ab
- Wer mehr Schub hat, kann höher steigen
- Von oben hast du Positions- und Energievorteil

::: tip TIPP
Rolling Scissors integrieren eine **vertikale Komponente**. Flugzeuge mit gutem Schub-Gewichts-Verhältnis können hier ihre Stärken ausspielen.
:::

### Zusammenfassung Scissors

| Scissors-Typ | Entscheidend | Bevorzugt für |
|--------------|--------------|---------------|
| **Flat Scissors** | Low-Speed Handling | Angles Fighter |
| **Rolling Scissors** | Thrust-to-Weight | Energy Fighter |

---

## Slice Turn

Ein niedriger Turn mit Sinken, um Speed und Distanz zu gewinnen.

### Wann nutzen?

- Gegner ist höher
- Du brauchst Speed
- Gegner committed zu hartem Turn

### Ausführung

1. Rolle auf die Seite (90° Bank)
2. Ziehe mit leichtem Sinken
3. Beschleunige während des Turns
4. Verlasse den Fight mit Speed

::: tip VORTEIL
Nach einem Slice kannst du mit der gewonnenen Energie wieder in den Kampf einsteigen - oder fliehen.
:::

---

## Defensive Spirale

Wenn du Energie verloren hast und der Gegner hartnäckig bleibt.

### Das Konzept

Statt immer härter zu drehen (und mehr Energie zu verlieren), fliege eine kontrollierte absteigende Spirale.

```mermaid
flowchart TD
    STUCK[Gegner bleibt dran] --> SPIRAL[Defensive Spirale]
    SPIRAL --> EFFECT1[Speed halten]
    SPIRAL --> EFFECT2[Höhe verlieren - akzeptabel]
    SPIRAL --> EFFECT3[Zeit gewinnen]

    EFFECT3 --> |"Auf Hilfe warten"| TEAM[Wingman?]
    EFFECT3 --> |"Gegner macht Fehler"| MISTAKE[Chance nutzen!]
```

### Wichtig

- **Nicht stumpf abwärts drehen** - kontrolliert!
- **Speed halten** - Nicht unter Minimum Speed fallen
- **Auf Gegner-Fehler warten**

---

## Overshoot erzwingen (Die "Notbremse")

Wenn ein Gegner an deinem Heck klebt (6 Uhr Position):

### Die Technik

1. **Drosseln**: Schub sofort auf **Leerlauf (Idle)**
2. **Airbrakes**: Ausfahren
3. **Jink**: Unregelmäßige Roll- und Ziehbewegungen um das Zielen zu erschweren, aber **keine konstante Kurve** fliegen
4. **Der Snap**: Sobald du siehst, dass der Gegner näher kommt und droht vorbeizufliegen:
   - Ziehe **hart in die Vertikale** oder
   - Führe eine **High Yo-Yo Defense** aus
5. **Reversal**: Wenn er vorbeigeflogen ist: **Nachbrenner rein**, Nase auf ihn drehen!

```mermaid
flowchart TD
    STUCK[Gegner an deinem Heck] --> BRAKE[Drosseln + Airbrakes]
    BRAKE --> JINK[Jinking - unberechenbar]
    JINK --> WATCH{Gegner kommt näher?}
    WATCH -->|Ja| SNAP[SNAP: Hart hochziehen!]
    WATCH -->|Nein| JINK
    SNAP --> OVERSHOOT[Gegner schießt vorbei]
    OVERSHOOT --> REVERSE[Nachbrenner + Reversal]
    REVERSE --> ATTACK[Du bist jetzt Angreifer!]
```

---

## Notfall: Gegner hat Schusslösung

::: danger SOFORTMASSNAHMEN
Wenn der Gegner gerade schießen will:

1. **Harter Break Turn** - Max G in seine Richtung
2. **Flares/Chaff** - Gegen Missiles
3. **Jink** - Unvorhersehbare Bewegungen
4. **Rollen** - Ändere Flugbahn ständig
:::

### Jinking

Kleine, schnelle Richtungsänderungen um Schusslösung zu stören:

- Links-rechts rollen
- Pitch up/down variieren
- **Nicht vorhersehbar** sein
- **Keine konstante Kurve** - das gibt dem Gegner einen Vorhaltewinkel

---

## Defensive Zusammenfassung

| Manöver | Wann | Ziel |
|---------|------|------|
| Break Turn | Sofort bei Bedrohung | Winkel gewinnen |
| Flat Scissors | Nach Overshoot (langsam) | Position umkehren |
| Rolling Scissors | Nach Overshoot (vertikal) | Höhenvorteil gewinnen |
| Slice Turn | Energie niedrig | Speed + Distanz |
| Defensive Spirale | Auswegslos | Zeit gewinnen |
| Jinking | Gegner schießt | Schuss stören |

::: info PHILOSOPHIE
Die beste Defensive ist, nie in die Defensive zu geraten. Halte Energie, halte Situationsbewusstsein!
:::
