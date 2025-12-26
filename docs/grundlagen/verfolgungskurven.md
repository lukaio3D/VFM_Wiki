# Pursuit Curves

Pursuit Curves (Verfolgungskurven) beschreiben, wie du deine Nase relativ zum Gegner ausrichtest. Die richtige Wahl beeinflusst Annäherungsrate, Energie und Schusslösung.

## Die drei Pursuit-Typen

### Lead Pursuit

Du zielst **vor** den Gegner (in seine Flugrichtung).

```
     Gegner →
        ↗
    Deine Nase
```

**Effekt:**
- Schnellste Annäherung
- Höchster Energie-Verlust
- Führt zu Overshoot wenn zu aggressiv

::: tip WANN NUTZEN
- Schusslösung herstellen
- Gegner ist langsam/dreht vorhersehbar
- Du hast Energie-Überschuss
:::

---

### Pure Pursuit

Du zielst **direkt auf** den Gegner.

```
     Gegner →
        ↑
    Deine Nase
```

**Effekt:**
- Mittlere Annäherung
- Mittlerer Energie-Verlust
- Stabile Verfolgung

::: tip WANN NUTZEN
- Standardverfolgung
- Gegner-Verhalten beobachten
- Energie-neutral bleiben
:::

---

### Lag Pursuit

Du zielst **hinter** den Gegner.

```
     Gegner →
        ↖
    Deine Nase
```

**Effekt:**
- Langsamste Annäherung
- Niedrigster Energie-Verlust
- Baut Separation auf

::: tip WANN NUTZEN
- Energie sparen
- Overshoot vermeiden
- Gegner zur Reaktion zwingen
:::

---

## Pursuit-Entscheidung

```mermaid
flowchart TD
    SIT[Situation analysieren] --> Q1{Wie viel Energie?}

    Q1 -->|Viel Energie| LEAD[Lead Pursuit möglich]
    Q1 -->|Wenig Energie| LAG[Lag Pursuit empfohlen]
    Q1 -->|Neutral| PURE[Pure Pursuit]

    LEAD --> Q2{Schusslösung?}
    Q2 -->|Ja| SHOOT[Schießen!]
    Q2 -->|Nein| PURE

    LAG --> Q3{Gegner dreht hart?}
    Q3 -->|Ja| LAGMORE[Lag halten - kein Overshoot]
    Q3 -->|Nein| PURE

    PURE --> TRACK[Stabile Verfolgung]
```

## Das Pursuit-Problem: Overshoot

**Overshoot** = Du fliegst am Gegner vorbei und wirst zum Ziel.

### Warum passiert Overshoot?

1. Zu viel Lead Pursuit
2. Zu hohe Geschwindigkeit
3. Gegner bremst plötzlich (Break Turn)

### Overshoot verhindern

```mermaid
flowchart LR
    APPROACH[Annäherung] --> CHECK{Closure Rate?}

    CHECK -->|Sehr hoch| DANGER[Overshoot-Gefahr!]
    CHECK -->|Moderat| OK[Weiter]
    CHECK -->|Niedrig| GOOD[Sicher]

    DANGER --> FIX[Lag Pursuit!]
    FIX --> GOOD
```

**Lag Pursuit** ist dein Werkzeug gegen Overshoot:
- Ziele hinter den Gegner
- Deine Nase zeigt "behind the 3/9 line"
- Du verlierst Closure Rate
- Gegner kann nicht plötzlich hinter dich kommen

## Pursuit vs Flugzeugtyp

| Gegner | Empfohlene Pursuit | Begründung |
|--------|-------------------|------------|
| T-16 Falchion | Lag/Pure | Er dreht gut - Overshoot-Gefahr |
| T-18 Cutlass | Lag! | Sie bremst extrem - hohes Overshoot-Risiko |
| T-15 Excalibur | Abhängig von Energie | Energie-Management entscheidet |

::: warning T-18 SPEZIAL
Die T-18 Cutlass wird im Turn extrem langsam (250 kts). Wenn du mit 450 kts in Lead Pursuit anfliegst, wirst du **garantiert** overshooten. Nutze **Lag Pursuit** und halte Distanz!
:::

## Zusammenfassung

| Pursuit | Energie | Annäherung | Risiko |
|---------|---------|------------|--------|
| Lead | Hoch verbraucht | Schnell | Overshoot |
| Pure | Neutral | Mittel | Ausgeglichen |
| Lag | Spart Energie | Langsam | Separation |

**Die T-15 Philosophie:** Nutze Lag Pursuit um Energie zu sparen, wechsle zu Lead nur für die Schusslösung.
