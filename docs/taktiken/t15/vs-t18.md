# T-15 vs T-18 Cutlass

> Anti-Radius-Fight Taktik

## Gegner-Profil

| Eigenschaft | T-18 Cutlass |
|-------------|--------------|
| **Typ** | Angles/Radius Fighter |
| **Stärke** | High-Alpha Fähigkeit, Nose Authority |
| **Schwäche** | Schlechteste Sustained Rate, schlechter Schub |
| **Corner Speed** | ~385 kts |
| **Gefährlichkeit** | Extrem hoch in One-Circle! |

::: tip GUTE NACHRICHT
Die T-18 ist der Gegner, den du am **leichtesten** besiegen kannst - wenn du die Regeln befolgst!
:::

---

## Die Strategie

### Das Kern-Prinzip

> **Two-Circle erzwingen. Speed halten. Niemals "Slow One-Circle"!**

```mermaid
flowchart TD
    FIGHT[T-18 Begegnung] --> NEVER[KEIN Slow One-Circle!]
    NEVER --> DO[Stattdessen:]

    DO --> TWO[Two-Circle erzwingen]
    DO --> SPEED[Speed 400-450 kts halten]
    DO --> SNAP[Snap Turn (Risiko!)]

    TWO --> WIN[Deine Rate > ihr Radius]
    SPEED --> FAST[Du: schnell, Sie: langsam]
    SNAP --> |"Nur 1. Turn!"| KILL[Sofort-Kill oder Flucht]
```

---

## Phase 1: Der Merge

### Was die T-18 will

- **Slow One-Circle** (Nase auf Nase bei < 300 kts)
- Dass du langsam wirst
- In ihren "Angles Bubble" ziehen

### Deine Antwort

```mermaid
flowchart TD
    MERGE[Am Merge] --> CHOICE{Flow-Entscheidung}

    CHOICE -->|One-Circle| RISK[HOCHES RISIKO!]
    CHOICE -->|Two-Circle| WIN[Du gewinnst!]

    RISK --> |"Nur bei >450 kts"| SNAP[24°/s Snap möglich]
    RISK --> |"Wenn langsam"| DEAD[TOD! Sie dreht besser]
    WIN --> EXPLANATION2["Deine Rate bei 450 kts<br/>schlägt ihren Radius bei 250 kts"]
```

**Am Merge:**
1. **Standard:** Drehe **zum Gegner** (Two-Circle). Das ist dein sicherer Sieg.
2. **Risiko:** Ein High-Speed One-Circle Snap ist möglich, aber wenn du ihn verpasst, bist du in ihrer Welt (Radius). **Nicht empfohlen für Anfänger.**

---

## Phase 2: Der Two-Circle-Fight

### Warum Two-Circle funktioniert

Die Mathematik (50% Fuel, 10.000 ft):

| Parameter | T-15 | T-18 |
|-----------|------|------|
| Sustained Turn Rate | 17°/s @ 495 kts | 16°/s @ 470 kts |
| Turn Radius | 1.644 ft | 1.899 ft |
| **Vorteil** | **Bessere Rate UND Radius!** | Nur High-AoA |

Im Two-Circle zählt **Sustained Rate** - und dort bist du überlegen (17°/s vs 16°/s). Zusätzlich hast du den kleineren Radius!

### Die Ausführung

```mermaid
flowchart TD
    START[Two-Circle initiiert] --> SPEED{Speed Check}

    SPEED -->|"> 400 kts"| GOOD[Perfekt! Weiter drehen]
    SPEED -->|"300-400 kts"| WARN[Achtung! Beschleunigen]
    SPEED -->|"< 300 kts"| DANGER[GEFAHR! Abort!]

    GOOD --> TURN[Sustained Turn halten]
    WARN --> UNLOAD[Kurz unloaden, dann weiter]
    DANGER --> VERT[Sofort vertikal!]

    TURN --> RESULT[Du gewinnst Winkel]
    RESULT --> SHOT[Schusslösung in ~2-3 Turns]
```

---

## Phase 3: Schusslösung

### Das Problem: Overshoot

Die T-18 wird im Turn **extrem langsam** (250 kts). Du kommst mit 450 kts an.

::: warning OVERSHOOT-GEFAHR
Wenn du in Lead Pursuit anfliegst, wirst du **garantiert** overshooten!
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
2. Reduziere Closure Rate
3. Wechsle zu **Pure/Lead** nur für den Schuss
4. Sofort zurück zu Lag nach Schuss

---

## Notfall: T-18 hat Nase auf dich

Wenn die T-18 die Nase auf dich bekommt:

::: danger SOFORTMASSNAHMEN
1. **Vollgas (Afterburner)** - SOFORT!
2. **Steigen!** - Sie kann dir nicht nach oben folgen
3. **Rollen** - Schusslinie brechen
4. Separation aufbauen, dann neu engagen
:::

### Warum Steigen funktioniert

```mermaid
flowchart TD
    TROUBLE[T-18 hat Nase auf dich] --> CLIMB[STEIGEN!]

    CLIMB --> PHYSICS[T-18 Probleme:]
    PHYSICS --> P1[Schlechter Schub]
    PHYSICS --> P2[Viel Widerstand = dreckige Flügel]
    PHYSICS --> P3[Kann nicht steigen]

    P1 --> SAFE[Du entkommst!]
    P2 --> SAFE
    P3 --> SAFE
```

---

## Speed-Management

### Die Speed-Zonen

| Speed | Status | Aktion |
|-------|--------|--------|
| 450+ kts | Optimal | Two-Circle dominieren |
| 400-450 kts | Gut | Weiter kämpfen |
| 300-400 kts | Warnung | Unloaden, Speed aufbauen |
| < 300 kts | Gefahr | SOFORT vertikal! |

### Die goldene Regel

> **Die T-18 bei 250 kts ist ein Monster. Bei 450 kts bist DU das Monster.**

---

## Zusammenfassung

### DO's (Machen!)

- Two-Circle erzwingen
- Speed 400-450 kts halten
- Lag Pursuit bei Annäherung
- Vertikal bei Problemen

### DON'TS (Vermeiden!)

- One-Circle (= Tod)
- Langsam werden (< 300 kts)
- Lead Pursuit (= Overshoot)
- Horizontaler Slow-Speed-Fight

```mermaid
flowchart TD
    VS18[vs T-18] --> RULE1[Two-Circle!]
    RULE1 --> RULE2[Speed halten!]
    RULE2 --> RULE3[Lag Pursuit!]
    RULE3 --> RULE4[Bei Problemen: Steigen!]
    RULE4 --> WIN[Sieg!]
```

::: info MERKE
Die T-18 ist ein One-Trick-Pony. Verweigere ihr den One-Circle und sie ist hilflos!
:::
