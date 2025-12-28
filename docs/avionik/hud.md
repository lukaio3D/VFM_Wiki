# Head-Up Display (HUD)

> Alle wichtigen Flugdaten direkt im Sichtfeld.

Das HUD projiziert kritische Informationen auf die Frontscheibe, sodass du nicht nach unten schauen musst. Im Luftkampf ist jede Sekunde entscheidend.

---

## Übersicht

```
┌─────────────────────────────────────────────────┐
│                    ← 172 →                      │  Heading
│                                                 │
│  483          ╭───────────────╮         9999    │
│  M 0.85       │               │         ┃┃     │
│  G 1.1        │    ──◎──      │         ┃┃     │
│               │       ↖       │                 │
│  GUN 500      │     ╱   ╲     │                 │
│  LOCK         │    ╱ [■] ╲    │                 │
│               ╰───────────────╯                 │
└─────────────────────────────────────────────────┘
     ↑                  ↑              ↑
   Links             Mitte          Rechts
```

---

## Linke Seite: Geschwindigkeit & Status

| Anzeige | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Geschwindigkeit** | Indicated Airspeed (KIAS) | 483 |
| **M (Mach)** | Geschwindigkeit relativ zur Schallmauer | M 0.85 |
| **G** | Aktuelle G-Kraft auf den Piloten | G 1.1 |
| **Waffe** | Ausgewählte Waffe + Munition/Anzahl | GUN 500 |
| **LOCK** | Radar hat Ziel aufgeschaltet | LOCK |

### Wichtige Werte

| Anzeige | Kritischer Bereich | Bedeutung |
|---------|-------------------|-----------|
| **G > 9** | Gefahr | Blackout droht, Struktur am Limit |
| **M < 0.3** | Warnung | Sehr langsam, Stall-Gefahr |
| **M > 1.0** | Info | Überschall |

::: tip G-KRAFT
Beobachte die G-Anzeige! Bei 7-9G wird das Sichtfeld dunkel (Greyout/Blackout).
:::

---

## Rechte Seite: Höhe

| Anzeige | Bedeutung |
|---------|-----------|
| **Höhe (ft)** | Flughöhe in Fuß (z.B. 9999 = ~10.000 ft) |
| **Variometer** | Vertikale Leiter zeigt Steigen/Sinken |

### Variometer lesen

| Position | Bedeutung |
|----------|-----------|
| **Über Mitte** | Steigflug |
| **Mitte** | Horizontalflug |
| **Unter Mitte** | Sinkflug |

---

## Mitte: Flugpfad & Ziel

### Heading (Kompass)

Das Band oben zeigt deinen aktuellen Kurs:

```
        ← 160  170  172  180  190 →
                    ↑
              Aktueller Kurs
```

---

### Velocity Vector (Flight Path Marker)

```
        ──◎──
```

Das wichtigste Symbol im HUD! Es zeigt, **wohin dein Flugzeug tatsächlich fliegt** - nicht wohin die Nase zeigt.

| Position | Bedeutung |
|----------|-----------|
| **Auf Horizontlinie** | Horizontalflug |
| **Über Horizontlinie** | Steigflug |
| **Unter Horizontlinie** | Sinkflug |
| **Links/Rechts der Mitte** | Seitliche Drift |

::: warning WICHTIG
Im Kurvenflug zeigt die Nase woanders hin als du tatsächlich fliegst. Der Velocity Vector zeigt die Wahrheit!
:::

---

### Ziel-Quadrat (Locked Target)

```
        [■]
```

Wenn du ein Ziel mit dem Radar aufgeschaltet hast, erscheint ein **Quadrat** um das Ziel. Das zeigt dir:

- Wo der Gegner ist
- Dass dein Radar ihn verfolgt
- Dass Waffen auf ihn gerichtet werden können

---

### Gun Funnel (Vorhaltelinien)

```
         ╱   ╲
        ╱     ╲
       ╱  [■]  ╲
      ╱         ╲
```

Wenn die **Bordkanone (GUN)** ausgewählt ist, erscheinen geschwungene Linien - der "Trichter".

**So benutzt du ihn:**

1. Verfolge das Ziel
2. Bringe die **Flügelspitzen des Gegners** in den Trichter
3. Je näher das Ziel, desto enger der Trichter
4. Wenn Flügelspitzen den Trichter "berühren" → Feuer!

::: tip VORHALTEN
Der Funnel berechnet das Vorhalten für dich. Du musst nicht "vor" das Ziel zielen - halte es einfach im Trichter!
:::

---

## Waffen-Anzeigen

| Anzeige | Bedeutung |
|---------|-----------|
| **GUN 500** | Bordkanone, 500 Schuss übrig |
| **AIM9 ×4** | 4 Sidewinder-Raketen verfügbar |
| **LOCK** | Ziel aufgeschaltet |

### Raketen-Ton (Growl)

Bei ausgewählter Rakete hörst du den Suchkopf-Ton:

| Ton | Bedeutung | Aktion |
|-----|-----------|--------|
| **Leise** | Keine Erfassung | Weiter manövrieren |
| **Laut** | Ziel erfasst | Schussbereit |

---

## Zusammenfassung: Was du ständig checken solltest

| Element | Warum wichtig |
|---------|---------------|
| **Geschwindigkeit** | Energie-Status, Corner Speed |
| **G-Kraft** | Blackout vermeiden |
| **Velocity Vector** | Wohin fliegst du wirklich? |
| **LOCK** | Hast du das Ziel? |
| **Munition** | Wie viel noch übrig? |

::: tip SCAN-PATTERN
Erfahrene Piloten scannen das HUD in einem Muster: Speed → G → Vector → Target → Speed...
:::
