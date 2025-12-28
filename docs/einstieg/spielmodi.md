# Spielmodi

> Singleplayer, Multiplayer und Ranglisten in Virtual Fighter Maneuvers.

VFM bietet verschiedene Spielmodi für Training und Wettkampf. Der Kern des Spiels ist der kompetitive Luftkampf.

---

## Singleplayer

Der Einzelspieler-Modus dient primär dem Training gegen KI-Gegner.

### KI-Verhalten

Die KI-Bots ("Challenging AI") nutzen Verhaltensbäume, die die Stärken ihrer Flugzeuge ausspielen:

| KI-Flugzeug | Taktisches Verhalten |
|-------------|---------------------|
| **T-15 (KI)** | Bevorzugt vertikale Manöver, Boom & Zoom |
| **T-16 (KI)** | Erzwingt Ratenkämpfe, bleibt horizontal |
| **T-18 (KI)** | Zieht in langsame Kurvenkämpfe, nutzt Radius |

::: tip TRAINING
Die KI spielt die typischen Stärken jedes Flugzeugs. Nutze sie, um Matchups zu üben, bevor du gegen Menschen fliegst.
:::

### Schwierigkeitsgrade

| Stufe | Beschreibung |
|-------|--------------|
| **Leicht** | KI macht Fehler, verzögerte Reaktionen |
| **Mittel** | Solide Grundmanöver, moderate Aggression |
| **Schwer** | Optimale Entscheidungen, nutzt alle Systeme |

---

## Multiplayer

Der Kern von VFM: PvP-Luftkämpfe gegen echte Piloten.

### Matchmaking

VFM nutzt ein ELO-basiertes Rankingsystem:

- Siege gegen höherrangige Spieler bringen mehr Punkte
- Niederlagen gegen niedrigere Ränge kosten mehr Punkte
- Das System strebt faire Matches basierend auf Skill an

### Spieltypen

| Modus | Beschreibung |
|-------|--------------|
| **1v1 Duel** | Klassischer Dogfight, einer gegen einen |
| **2v2 Team** | Koordination mit einem Wingman |
| **Free-For-All** | Jeder gegen jeden |
| **Ranked** | Wertungskämpfe für die Rangliste |

::: warning RANKED
Ranked-Matches zählen für deine Platzierung. Übe zuerst in unranked Lobbies oder gegen KI.
:::

---

## Ranglisten

Kompetitive Spieler können die Rangliste erklimmen.

### ELO-System

Das Matchmaking-Rating (MMR) basiert auf dem ELO-System:

```
Neues Rating = Altes Rating + K × (Ergebnis - Erwartung)
```

| Faktor | Einfluss |
|--------|----------|
| **K-Faktor** | Volatilität (höher bei neuen Accounts) |
| **Ergebnis** | 1.0 (Sieg), 0.5 (Unentschieden), 0.0 (Niederlage) |
| **Erwartung** | Basierend auf Rating-Differenz |

### Ränge

| Rang | Rating-Bereich |
|------|----------------|
| Bronze | 0 - 1199 |
| Silber | 1200 - 1399 |
| Gold | 1400 - 1599 |
| Platin | 1600 - 1799 |
| Diamant | 1800 - 1999 |
| Elite | 2000+ |

---

## Cross-Play

VFM unterstützt plattformübergreifendes Spielen.

### Gemeinsamer Spielerpool

- PCVR-Spieler (Steam) und Quest-Spieler im selben Pool
- Keine getrennten Ranglisten
- Faire Matches durch identische Physik

### Technische Umsetzung

| Aspekt | Lösung |
|--------|--------|
| **Netcode** | Client-Side Prediction mit Server-Autorität |
| **Physik** | Deterministische Berechnung |
| **Hitboxen** | Identisch auf allen Plattformen |

::: info LATENZ
Die Server-Infrastruktur minimiert Latenzen. Bei Guns-Treffern entscheidet der Server basierend auf Positionen zum Schusszeitpunkt.
:::
