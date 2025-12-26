# T-16 vs T-18 Cutlass

> Rate vs Radius - Den Radius-Kämpfer überholen

## Gegner-Profil

| Eigenschaft | T-18 Cutlass |
|-------------|--------------|
| **Typ** | Angles/Radius Fighter |
| **Stärke** | Kleinster Turn Radius, beste Nose Authority |
| **Schwäche** | Langsam, schlechter Schub, massives Energie-Bleed |
| **Corner Speed** | ~250-275 kts |
| **Gefährlichkeit** | Extrem hoch im One-Circle! |

::: tip GUTE NACHRICHT
Die T-18 ist dein **idealer Gegner** - solange du schnell bleibst!
:::

---

## Die Strategie

### Das Kern-Prinzip

> **Speed halten. Two-Circle erzwingen. Sie aushungern!**

```mermaid
flowchart TD
    FIGHT[T-18 Begegnung] --> NEVER[Niemals langsam werden!]
    NEVER --> DO[Stattdessen:]

    DO --> SPEED[Speed 380-420 kts halten]
    DO --> TWO[Two-Circle erzwingen]
    DO --> PATIENT[Sie langsam werden lassen]

    SPEED --> FAST[Du bleibst schnell]
    TWO --> RATE[Deine Rate > ihr Radius]
    PATIENT --> DRAIN[Sie verliert alle Energie]
```

---

## Phase 1: Der Merge

### Was die T-18 will

- One-Circle-Fight (Nase auf Nase)
- Dich in ihren "Slow Bubble" ziehen (< 300 kts)
- Ihre überlegene Nose Authority nutzen
- Schneller Snapshot

### Deine Antwort

```mermaid
flowchart TD
    MERGE[Am Merge] --> CHOICE{Flow-Entscheidung}

    CHOICE -->|One-Circle| DANGER[GEFÄHRLICH! Ihr Radius gewinnt]
    CHOICE -->|Two-Circle| WIN[Du gewinnst! Deine Rate dominiert]

    DANGER --> EXPLAIN1["Sie dreht enger<br/>Sie bekommt Nase auf dich"]
    WIN --> EXPLAIN2["Du drehst schneller<br/>Du holst sie ein"]
```

**Am Merge:**
1. Erkenne die T-18 früh
2. Halte Speed über 380 kts!
3. Two-Circle initiieren (drehe ZUM Gegner)
4. **Nicht verlangsamen!**

---

## Phase 2: Der Two-Circle-Fight

### Warum Two-Circle funktioniert

Die Mathematik:

| Parameter | T-16 (bei 400 kts) | T-18 (bei 250 kts) |
|-----------|-------------------|-------------------|
| Turn Rate | **Hoch** | Mittel |
| Turn Radius | Mittel | Klein |
| Winkelgeschwindigkeit | **Höher!** | Niedriger |
| Energie nach 2 Turns | ~380 kts | ~200 kts |

Im Two-Circle zählt **Rate**, nicht Radius. Du umkreist sie schneller als sie dich!

### Die Ausführung

```mermaid
flowchart TD
    START[Two-Circle initiiert] --> SPEED{Speed Check}

    SPEED -->|"> 380 kts"| GOOD[Perfekt! Weiter drehen]
    SPEED -->|"350-380 kts"| OK[Gut, Afterburner an]
    SPEED -->|"< 350 kts"| WARN[Achtung! Separation aufbauen]

    GOOD --> TURN[Sustained Turn halten]
    OK --> TURN
    WARN --> EXTEND[Kurz geradeaus, dann re-engage]

    TURN --> GAIN[Du gewinnst Winkel]
    GAIN --> SHOT[Schusslösung in 2-3 Turns]
```

---

## Phase 3: Die T-18 aushungern

### Das Energie-Problem der T-18

Die T-18 verblutet Energie mit jedem Turn:

```mermaid
flowchart TD
    T18TURNS[T-18 dreht hart] --> BLEED[Massives Speed-Bleed]
    BLEED --> SLOW[Sie wird immer langsamer]
    SLOW --> STUCK[Unter 200 kts = hilflos]
    STUCK --> EASY[Leichtes Ziel für dich]
```

### Deine Taktik

1. **Halte den Two-Circle aufrecht**
2. Sie muss drehen um dich zu tracken
3. Jeder Turn kostet sie Speed
4. Nach 2-3 Turns ist sie bei 200 kts
5. Du hast noch 380 kts → **Du dominierst!**

---

## Phase 4: Schusslösung

### Das Problem: Overshoot

Die T-18 ist **extrem langsam** (200-250 kts). Du kommst mit 400 kts.

::: warning OVERSHOOT-GEFAHR
Bei Lead Pursuit fliegst du **garantiert** an ihr vorbei!
:::

### Die Lösung: Lag Pursuit

```mermaid
flowchart LR
    APPROACH[Annäherung] --> LAG[Lag Pursuit!]
    LAG --> BEHIND[Ziele HINTER die T-18]
    BEHIND --> CONTROL[Closure kontrollieren]
    CONTROL --> SHOT[Kontrollierter Schuss]
```

**Schritt für Schritt:**
1. Bleibe in **Lag Pursuit** (hinter sie zielen)
2. Reduziere Closure Rate mit Throttle
3. Wechsle zu **Lead** nur für den Schuss
4. Sofort zurück zu Lag nach Schuss

---

## Notfall: T-18 hat Nase auf dich

Wenn die T-18 die Nase auf dich bekommt:

::: danger SOFORTMASSNAHMEN
1. **Nicht paniken** - du hast Speed!
2. **Weiterfliegen** - nicht verlangsamen
3. **Roll** - Schusslinie brechen
4. **Extend** wenn nötig, dann re-engage
:::

### Warum du überleben kannst

```mermaid
flowchart TD
    TROUBLE[T-18 hat Nase auf dich] --> SPEED{Deine Speed?}

    SPEED -->|"> 350 kts"| SAFE[Du kannst entkommen]
    SPEED -->|"< 300 kts"| DANGER[Gefahr!]

    SAFE --> EXTEND[Geradeaus, Separation]
    EXTEND --> REENGAGE[Neu engagen mit Vorteil]

    DANGER --> ROLL[Rollen, breaken]
    ROLL --> BUILD[Speed aufbauen]
    BUILD --> RETRY[Nochmal versuchen]
```

---

## Speed-Management

### Die Speed-Zonen für T-16

| Speed | Status | Aktion |
|-------|--------|--------|
| 400+ kts | Optimal | Two-Circle dominieren |
| 350-400 kts | Gut | Weiter kämpfen, Afterburner |
| 300-350 kts | Warnung | Separation aufbauen |
| < 300 kts | Gefahr | Du spielst IHR Spiel! |

### Die goldene Regel

> **Sie bei 200 kts ist ein Opfer. Du bei 200 kts bist das Opfer.**

---

## Zusammenfassung

### DO's (Machen!)

- Speed 380-420 kts halten
- Two-Circle erzwingen
- Lag Pursuit bei Annäherung
- Geduldig sein (sie hungert aus)

### DON'TS (Vermeiden!)

- One-Circle (gefährlich!)
- Langsam werden (< 300 kts)
- Lead Pursuit (= Overshoot)
- Ungeduldig in ihre Stärke spielen

```mermaid
flowchart TD
    VS18[vs T-18] --> RULE1[Speed halten!]
    RULE1 --> RULE2[Two-Circle!]
    RULE2 --> RULE3[Lag Pursuit!]
    RULE3 --> RULE4[Geduldig aushungern!]
    RULE4 --> WIN[Sieg!]
```

::: info MERKE
Die T-18 ist ein One-Trick-Pony. Bleib schnell und sie hat keine Chance!
:::
