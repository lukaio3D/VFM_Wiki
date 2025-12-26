# T-16 vs T-15 Excalibur

> Rate vs Energy - Den Energiekämpfer aushungern

## Gegner-Profil

| Eigenschaft | T-15 Excalibur |
|-------------|----------------|
| **Typ** | Energy Fighter |
| **Stärke** | Beste Beschleunigung, vertikale Dominanz |
| **Schwäche** | Größerer Turn Radius, schwach unter 300 kts |
| **Corner Speed** | 400-450 kts |
| **Gefährlichkeit** | Extrem hoch in der Vertikalen! |

::: warning ACHTUNG
Die T-15 hat **zwei Triebwerke**. Sie kann dich in der Vertikalen immer überholen!
:::

---

## Die Strategie

### Das Kern-Prinzip

> **Horizontal bleiben. Rate ausspielen. Niemals vertikal folgen!**

```mermaid
flowchart TD
    FIGHT[T-15 Begegnung] --> NEVER[NIEMALS vertikal folgen!]
    NEVER --> DO[Stattdessen:]

    DO --> HORIZ[Horizontal bleiben]
    DO --> RATE[Deine Rate ausspielen]
    DO --> PATIENT[Geduldig sein]

    HORIZ --> WIN[Sie muss zu dir kommen]
    RATE --> OUTRATE[Du drehst schneller]
    PATIENT --> DRAIN[Sie verliert Energie]
```

---

## Phase 1: Der Merge

### Was die T-15 will

- Vertikalen Kampf erzwingen
- Energie aufbauen durch Steigen
- Boom & Zoom Angriffe
- Dich langsam machen

### Deine Antwort

```mermaid
flowchart TD
    MERGE[Am Merge] --> CHOICE{T-15 geht...}

    CHOICE -->|Vertikal| DONT[NICHT FOLGEN!]
    CHOICE -->|Horizontal| GOOD[Perfekt! Rate-Fight!]

    DONT --> STAY[Horizontal bleiben]
    STAY --> WAIT[Warten bis sie zurückkommt]
    WAIT --> READY[Bereit für Re-Engagement]

    GOOD --> RATE[Deine Rate dominiert]
    RATE --> WIN[Du gewinnst Winkel]
```

**Am Merge:**
1. Erkenne früh ob die T-15 steigt
2. **Nicht folgen** wenn sie hochzieht
3. Bleibe horizontal, halte deine Energie
4. Warte auf ihre Rückkehr

---

## Phase 2: Der Horizontale Kampf

### Warum Horizontal funktioniert

Die Mathematik:

| Parameter | T-16 (bei 400 kts) | T-15 (bei 400 kts) |
|-----------|-------------------|-------------------|
| Sustained Turn Rate | **Höher!** | Niedriger |
| Energieverlust pro Turn | Gering | Höher |
| Nach 3 Turns | Immer noch 380 kts | Unter 350 kts |

Du hast die **bessere Sustained Turn Rate**. In einem horizontalen Kurvenkampf gewinnst du langsam aber sicher Winkel.

### Die Ausführung

```mermaid
flowchart TD
    START[Horizontaler Kampf] --> SPEED{Speed Check}

    SPEED -->|"> 380 kts"| GOOD[Perfekt! Sustained Turn]
    SPEED -->|"350-380 kts"| OK[Gut, weiter drehen]
    SPEED -->|"< 350 kts"| WARN[Kurz unloaden]

    GOOD --> TURN[Konstanter Turn]
    OK --> TURN
    WARN --> BUILD[Speed aufbauen, dann weiter]

    TURN --> GAIN[Du gewinnst Winkel pro Umlauf]
    GAIN --> SHOT[Schusslösung nach 3-4 Turns]
```

---

## Phase 3: Wenn die T-15 steigt

### Die Falle

Die T-15 wird versuchen, dich in die Vertikale zu locken:

::: danger TODESFALLE
Wenn du der T-15 in den Steigflug folgst:
- Sie hat mehr Schub → steigt schneller
- Du verlierst Energie → wirst langsam
- Sie kommt von oben → Boom & Zoom
- **Du stirbst!**
:::

### Die richtige Antwort

```mermaid
flowchart TD
    T15CLIMBS[T-15 steigt] --> REACTION{Deine Reaktion}

    REACTION -->|Folgen| DEAD[TOD! Sie hat dich oben]
    REACTION -->|Horizontal bleiben| SMART[Richtig!]

    SMART --> ENERGY[Halte deine Energie]
    ENERGY --> WAIT[Sie MUSS zurückkommen]
    WAIT --> READY[Du bist bereit]
    READY --> ADVANTAGE[Bessere Position beim Re-Merge]
```

**Wenn die T-15 steigt:**
1. **Nicht folgen!**
2. Horizontal weiterdrehen oder geradeaus
3. Speed bei 400+ kts halten
4. Beobachte wo sie hingeht
5. Bereite dich auf ihren Angriff vor

---

## Phase 4: Der Defensive Turn

Wenn die T-15 von oben angreift (Boom & Zoom):

### Das Timing

```mermaid
flowchart LR
    ATTACK[T-15 stürzt herab] --> WAIT[Warten...]
    WAIT --> TIMING[Kurz vor Schussreichweite]
    TIMING --> BREAK[HARTES BREAK!]
    BREAK --> MISS[Sie schießt vorbei]
    MISS --> RESET[Zurück zum Rate-Fight]
```

**Schritt für Schritt:**
1. Beobachte die angreifende T-15
2. Warte bis sie committed ist (nicht zu früh breaken!)
3. **Hartes Break** in ihre Richtung
4. Sie kann nicht folgen (zu schnell)
5. Sie muss wieder steigen → Du hast Zeit

---

## Speed-Management

### Die Speed-Zonen für T-16

| Speed | Status | Aktion |
|-------|--------|--------|
| 400+ kts | Optimal | Sustained Turn dominieren |
| 350-400 kts | Gut | Weiter kämpfen |
| 300-350 kts | Warnung | Kurz unloaden |
| < 300 kts | Gefahr | Separation aufbauen |

### Die goldene Regel

> **Die T-15 will vertikal. Du willst horizontal. Spiele DEIN Spiel!**

---

## Zusammenfassung

### DO's (Machen!)

- Horizontal bleiben
- Sustained Turn Rate ausspielen
- Geduldig sein (3-4 Turns zum Sieg)
- Speed über 350 kts halten

### DON'TS (Vermeiden!)

- Der T-15 vertikal folgen
- Slow-Speed-Kämpfe (unter 300 kts)
- Ungeduldig werden
- In ihre Stärke spielen

```mermaid
flowchart TD
    VS15[vs T-15] --> RULE1[Horizontal bleiben!]
    RULE1 --> RULE2[Rate ausspielen!]
    RULE2 --> RULE3[Nicht vertikal folgen!]
    RULE3 --> RULE4[Geduldig bleiben!]
    RULE4 --> WIN[Sieg!]
```

::: info MERKE
Die T-15 ist ein Energie-Monster, aber sie kann dich horizontal nicht schlagen. Verweigere ihr die Vertikale!
:::
