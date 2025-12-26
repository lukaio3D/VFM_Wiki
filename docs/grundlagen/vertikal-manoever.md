# Vertikale Manöver

Die Vertikale ist ein mächtiges Werkzeug im BFM. Hier lernst du, wann und wie du sie effektiv nutzt.

## Warum Vertikal kämpfen?

Die Vertikale bietet mehrere Vorteile gegenüber dem horizontalen Kampf:

- **Energie-Umwandlung**: Tausche Geschwindigkeit gegen Höhe und umgekehrt
- **Radius-Verkleinerung**: Am Apex (Scheitelpunkt) ist der Radius minimal
- **Schub-Vorteile**: Flugzeuge mit hohem TWR dominieren gegen die Schwerkraft
- **Separation**: Verlasse einen ungünstigen Fight durch Steigen

```mermaid
flowchart TD
    VERT[Vertikaler Kampf] --> ADV1[Energie-Management]
    VERT --> ADV2[Radius-Kontrolle]
    VERT --> ADV3[Schub-Vorteile nutzen]
```

---

## Der kritische Fehler: Pure Vertical

::: danger FEHLER: Stumpfes Hochziehen
Einfach 90° hochziehen ist **gefährlich**!

**Was passiert:**
- Bei 0 Knoten hast du **keine Kontrolle**
- Du bist ein **stationäres Ziel**
- Gegner kann dich leicht abschießen
:::

### Das Problem visualisiert

```mermaid
flowchart TD
    BAD[90° Hochziehen] --> SLOW[Speed fällt]
    SLOW --> ZERO[0 Knoten am Apex]
    ZERO --> SITTING[Sitting Duck!]
    SITTING --> DEAD[Abgeschossen]
```

---

## Die Lösung: Die Taktische Spirale ("The Egg")

Statt gerade hoch zu fliegen, fliege ein "Ei" - eine spiralförmige Steigkurve.

### Das Konzept

```
        ___
       /   \     ← Apex (aber mit Speed!)
      |     |
       \   /     ← Du siehst den Gegner
        | |
        |_|      ← Start
```

### Ausführung

1. **Steigwinkel: 40-60°** - Nicht 90°!
2. **Leichte Querneigung** (Bank) beibehalten
3. **Rollrichtung** - So dass du den Gegner siehst
4. **Speed-Minimum: 150-180 kts** am Apex

```mermaid
flowchart TD
    START[Vertikalen Kampf starten] --> CLIMB[40-60° Steigen]
    CLIMB --> BANK[Leichte Bank halten]
    BANK --> WATCH[Gegner beobachten]
    WATCH --> APEX{Am Apex}

    APEX -->|"Speed > 150 kts"| CONTROL[Noch Kontrolle!]
    APEX -->|"Speed < 150 kts"| DANGER[Zu langsam!]

    CONTROL --> NEXT[Nächste Phase]
    DANGER --> RECOVER[Nase runter, Speed aufbauen]
```

---

## Vorteile der Taktischen Spirale

| Aspekt | Pure Vertical | Taktische Spirale |
|--------|---------------|-------------------|
| Sicht auf Gegner | Verloren | Behalten |
| Speed am Apex | ~0 kts | 150+ kts |
| Kontrolle | Keine | Ja |
| Reaktionsfähigkeit | Null | Gut |

---

## Vertikale Taktiken

### Zoom Climb

Nutze überschüssige Energie für schnellen Höhengewinn.

1. Bei hoher Speed (Corner Speed+) hochziehen
2. Steile Steigung (60-70°)
3. Vor Speed-Verlust abflachen
4. Höhenvorteil gewonnen

::: tip WANN NUTZEN
- Nach High-Speed-Pass
- Gegner ist tiefer und langsamer
- Du willst Separation
:::

### Yo-Yo mit Vertikaler Komponente

Kombiniere High Yo-Yo mit mehr Höhengewinn:

1. Statt 30° hochziehen, gehe auf 50°
2. Rolle über den Gegner
3. Du bist jetzt **über** ihm mit Energie-Vorteil

---

## Vertikale Defensive

Wenn du in der Defensive bist, nutze die Vertikale:

### Das "High-Speed Climb Out"

```mermaid
flowchart TD
    DEF[Gegner hinter dir] --> CHECK{Speed?}

    CHECK -->|"Hoch (Corner Speed+)"| CLIMB[Steil steigen!]
    CHECK -->|"Niedrig"| FIRST[Erst Speed aufbauen]

    CLIMB --> EFFECT[Separation gewinnen]
    EFFECT --> REVERSE[Umdrehen mit Höhenvorteil]
```

**Warum es funktioniert:**
- Flugzeuge mit hohem TWR steigen schneller
- Einmotorige Flugzeuge haben Schwierigkeiten zu folgen
- Du gewinnst Zeit und Position

::: warning VORAUSSETZUNG
Du brauchst **genug Energie** (Speed) um vertikal zu flüchten. Versuche nicht, mit 250 kts zu steigen - du wirst nur langsamer und verletzlicher.
:::

---

## Minimum Speed Regeln

| Situation | Minimum Speed |
|-----------|---------------|
| Apex der Spirale | 150-180 kts |
| Vertikaler Turn | 200 kts |
| Generell im Kampf | Nie unter 150 kts |

::: warning UNTER 150 KNOTEN
Unter 150 kts verlieren die meisten Kampfflugzeuge die Kontrollfähigkeit. Du kannst nicht mehr effektiv manövrieren - du bist ein Ziel!
:::

---

## Zusammenfassung

### DO's (Machen!)

- Taktische Spirale statt stumpf hochziehen
- Speed am Apex behalten (150+ kts)
- Gegner im Auge behalten
- Vertikale nutzen wenn du Schub-Vorteil hast

### DON'Ts (Vermeiden!)

- 90° Pure Vertical
- 0 kts am Apex
- Sicht auf Gegner verlieren
- Panisches Hochziehen ohne Plan

```mermaid
flowchart LR
    GOOD[Taktische Spirale] --> WIN[Kontrolle behalten]
    BAD[Stumpfes Hochziehen] --> LOSE[Kontrolle verlieren]
```

::: info MERKE
Die Vertikale ist dein Freund - aber nur mit der richtigen Technik. **Spirale > Pure Vertical!**
:::
