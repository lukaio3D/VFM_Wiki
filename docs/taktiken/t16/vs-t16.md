# T-16 vs T-16 Spiegelkampf

> Gleiche Maschinen - Pilot-Skill entscheidet

## Die Herausforderung

| Parameter | Deine T-16 | Gegner T-16 |
|-----------|-----------|-------------|
| Turn Rate | Identisch | Identisch |
| Schub | Identisch | Identisch |
| Radius | Identisch | Identisch |
| **Unterschied** | **Pilot-Skill** | **Pilot-Skill** |

::: warning HARTER KAMPF
Im Spiegelkampf gibt es keinen technischen Vorteil. Nur **Fehler des Gegners** oder **besseres Flying** entscheiden!
:::

---

## Die Strategie

### Das Kern-Prinzip

> **Keine Fehler machen. Auf Gegner-Fehler warten. Speed-Management perfektionieren!**

```mermaid
flowchart TD
    MIRROR[T-16 Spiegelkampf] --> KEY[Schlüssel zum Sieg:]

    KEY --> NOFAULT[Keine eigenen Fehler]
    KEY --> WATCH[Gegner-Fehler erkennen]
    KEY --> SPEED[Perfektes Speed-Management]

    NOFAULT --> SURVIVE[Du überlebst]
    WATCH --> EXPLOIT[Du nutzt Chancen]
    SPEED --> EDGE[Minimaler Vorteil summiert sich]
```

---

## Entscheidende Faktoren

### 1. Speed-Management

Der Pilot mit der **besseren Corner Speed** gewinnt minimale Vorteile pro Turn:

```mermaid
flowchart TD
    SPEED{Speed Check}

    SPEED -->|"380-420 kts"| OPTIMAL[Optimale Turn Rate]
    SPEED -->|"> 450 kts"| FAST[Zu schnell - größerer Radius]
    SPEED -->|"< 350 kts"| SLOW[Zu langsam - weniger Rate]

    OPTIMAL --> WIN[Du gewinnst Winkel]
    FAST --> LOSE[Du verlierst Winkel]
    SLOW --> LOSE
```

### 2. Energy-State Awareness

Wer hat mehr Energie?

| Situation | Bedeutung | Aktion |
|-----------|-----------|--------|
| Du höher + schneller | Energie-Vorteil | Aggressiv kämpfen |
| Gleiche Energie | Neutral | Auf Fehler warten |
| Er höher + schneller | Nachteil | Defensive, Fehler provozieren |

### 3. Geometrie-Entscheidungen

```mermaid
flowchart TD
    MERGE[Am Merge] --> FLOW{One oder Two Circle?}

    FLOW --> ONE[One-Circle]
    FLOW --> TWO[Two-Circle]

    ONE --> RADIUS[Radius-Fight]
    TWO --> RATE[Rate-Fight]

    RADIUS --> SAME1[Gleiche Fähigkeiten]
    RATE --> SAME2[Gleiche Fähigkeiten]

    SAME1 --> SKILL[Besserer Pilot gewinnt]
    SAME2 --> SKILL
```

---

## Taktiken für den Vorteil

### Lead Turn nutzen

Wenn du den Merge besser timst:

```mermaid
flowchart LR
    EARLY[Früh drehen] --> LEAD[Lead Turn]
    LEAD --> ANGLE[Winkel-Vorteil am Merge]
    ANGLE --> START[Kampf startet mit Vorteil]
```

**Risiko:** Zu früh = du zeigst ihm dein Heck!

### Scissors provozieren

Wenn der Gegner overshoots:

1. **Erkennen:** Er fliegt an dir vorbei
2. **Reversal:** Schnell die Richtung wechseln
3. **Scissors:** Wechselnde Richtungswechsel
4. **Patience:** Wer zuerst überzieht, verliert

### Vertikale Elemente einbauen

Auch im T-16 kannst du vertikal arbeiten:

```mermaid
flowchart TD
    STALL[Kampf wird langsam] --> VERT[Vertikales Element]
    VERT --> OPTIONS{Optionen}

    OPTIONS --> CLIMB[Steigen für Energie]
    OPTIONS --> DIVE[Sturzflug für Speed]
    OPTIONS --> SPIRAL[Taktische Spirale]

    CLIMB --> RESET[Position neu aufbauen]
    DIVE --> ATTACK[Angriff mit Energie]
    SPIRAL --> DRAIN[Gegner aushungern]
```

---

## Häufige Fehler

### Fehler 1: Überzogene Turns

::: danger NICHT ÜBERZIEHEN
Wenn du den Stick zu weit ziehst:
- Speed fällt rapide
- Turn Rate sinkt
- Gegner gewinnt Winkel
:::

**Lösung:** Stick-Druck dosieren. Bleib bei Corner Speed!

### Fehler 2: Ungeduld

::: warning GEDULD IST ALLES
Im Spiegelkampf:
- Keine schnellen Kills
- 5-10 Turns können nötig sein
- Ein Fehler = Niederlage
:::

**Lösung:** Warte auf SEINEN Fehler!

### Fehler 3: Vorhersagbare Manöver

::: tip UNVORHERSEHBAR SEIN
- Variiere deine Turns
- Wechsle zwischen One/Two-Circle
- Nutze vertikale Elemente überraschend
:::

---

## Die Entscheidungsmatrix

### Wann aggressiv sein

| Situation | Aktion |
|-----------|--------|
| Du hast Energie-Vorteil | Pressen! |
| Gegner macht Fehler | Sofort ausnutzen! |
| Du hast Winkel-Vorteil | Lead Pursuit |

### Wann defensiv sein

| Situation | Aktion |
|-----------|--------|
| Du hast Energie-Nachteil | Separation, neu aufbauen |
| Du bist zu langsam | Extend, Speed aufbauen |
| Unklare Situation | Warten, beobachten |

---

## Zusammenfassung

### DO's (Machen!)

- Corner Speed halten (380-420 kts)
- Auf Gegner-Fehler warten
- Eigene Fehler minimieren
- Geduldig bleiben

### DON'TS (Vermeiden!)

- Überziehen (Stick zu weit)
- Ungeduldig werden
- Vorhersagbar sein
- Speed verlieren

```mermaid
flowchart TD
    MIRROR[T-16 Spiegelkampf] --> RULE1[Speed-Management!]
    RULE1 --> RULE2[Keine Fehler!]
    RULE2 --> RULE3[Geduldig warten!]
    RULE3 --> RULE4[Chance nutzen!]
    RULE4 --> WIN[Sieg!]
```

::: info MERKE
Im Spiegelkampf gewinnt nicht das bessere Flugzeug - sondern der bessere Pilot. Sei geduldig, mach keine Fehler, und nutze seine Fehler aus!
:::
