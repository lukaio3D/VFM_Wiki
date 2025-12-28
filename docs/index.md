# VFM Flight Academy

> Taktische Doktrin für Virtual Fighter Maneuvers

Willkommen in der **Flight Academy**. Dieses Wiki dient als umfassendes Handbuch für Luftkampf-Taktiken in **Virtual Fighter Maneuvers** (VFM).

Es ist in drei Hauptbereiche unterteilt:
1. **Grundlagen**: Universelle Konzepte und Theorie für jeden Piloten.
2. **Flugzeug-Daten**: Leistungsdaten und Charakteristiken der drei Muster.
3. **Taktiken**: Spezifische Kampfanleitungen für jedes Flugzeug gegen jeden Gegner.

::: info KONTEXT
VFM von Boundless Dynamics simuliert komplexe Aerodynamik: Transsonischer Widerstand, Anstellwinkel (AoA) und spezifische Energiezustände sind modelliert. Wir wenden hier echte BFM-Prinzipien (Basic Fighter Maneuvers) an.
:::

## Schnellstart

Für neue Piloten ist dies der empfohlene Pfad:

1. **Grundlagen**: Lerne die [Golden Rules](/grundlagen/golden-rules) – die 10 universellen Gebote des Luftkampfs.
2. **Theorie**: Verstehe die [Kampf-Geometrie](/grundlagen/geometrie) (One-Circle vs. Two-Circle).
3. **Dein Flugzeug**: Wähle dein Muster und studiere die Leistungsdaten.
4. **Taktiken**: Lerne die spezifischen Taktiken gegen jeden Gegnertyp.

---

## Die Flugzeug-Typen (Archetypen)

Im Luftkampf gibt es drei fundamentale Design-Philosophien. Jedes Flugzeug in VFM verkörpert eines dieser Extreme.

| Archetyp | VFM Muster | Stärke | Schwäche |
|---|---|---|---|
| **Energy Fighter** | **[T-15 Excalibur](/flugzeuge/t15/daten)** | Schub, Vertikale, Speed | Wenderadius |
| **Rate Fighter** | **[T-16 Falchion](/flugzeuge/t16/daten)** | Beste Wenderate (Sustained) | Vertikale Ausdauer |
| **Angles Fighter** | **[T-18 Cutlass](/flugzeuge/t18/daten)** | Bester Radius (Instantaneous) | Energie-Erhalt |

```mermaid
flowchart TD
    subgraph "Schere-Stein-Papier des Luftkampfs"
        T15["Energy Fighter<br/>T-15"] --> |"Dominiert vertikal"| T16["Rate Fighter<br/>T-16"]
        T16 --> |"Dominiert horizontal (Rate)"| T18["Angles Fighter<br/>T-18"]
        T18 --> |"Dominiert im Slow-Fight (Radius)"| T15
    end
```

---

## Modul-Übersicht

### Grundlagen (Theorie)
Die theoretische Basis für alle Piloten - flugzeugneutral.

- **[Golden Rules](/grundlagen/golden-rules)**: Die 10 Gebote des Luftkampfs
- **[Kampf-Geometrie](/grundlagen/geometrie)**: One-Circle vs Two-Circle
- **[Energie-Management](/grundlagen/energie-management)**: Corner Speed & Unloading
- **[Verfolgungskurven](/grundlagen/verfolgungskurven)**: Lead, Lag und Pure Pursuit
- **[Offensiv-Manöver](/grundlagen/offensiv-manoever)**: High/Low Yo-Yo, Barrel Roll Attack
- **[Defensiv-Manöver](/grundlagen/defensiv-manoever)**: Scissors, Break Turn, Overshoot
- **[Vertikal-Manöver](/grundlagen/vertikal-manoever)**: Taktische Spirale

### Flugzeug-Daten
Leistungsdaten, Stärken und Schwächen - ohne Taktiken.

- **[T-15 Excalibur](/flugzeuge/t15/daten)**: Energy Fighter
- **[T-16 Falchion](/flugzeuge/t16/daten)**: Rate Fighter
- **[T-18 Cutlass](/flugzeuge/t18/daten)**: Angles Fighter

### Taktiken

#### T-15 Excalibur Pilot
- **[vs T-16 Falchion](/flugzeuge/t15/matchups#vs-t-16-falchion-rate-fighter)**: Energy vs Rate
- **[vs T-18 Cutlass](/flugzeuge/t15/matchups#vs-t-18-cutlass-angles-fighter)**: Energy vs Radius
- **[vs T-15 (Spiegel)](/flugzeuge/t15/matchups#vs-t-15-excalibur-mirror-match)**: Energy vs Energy

#### T-16 Falchion Pilot
- **[vs T-15 Excalibur](/flugzeuge/t16/matchups#vs-t-15-excalibur-energy-fighter)**: Rate vs Energy
- **[vs T-18 Cutlass](/flugzeuge/t16/matchups#vs-t-18-cutlass-angles-fighter)**: Rate vs Radius
- **[vs T-16 (Spiegel)](/flugzeuge/t16/matchups#vs-t-16-falchion-mirror-match)**: Rate vs Rate

#### T-18 Cutlass Pilot
- **[vs T-15 Excalibur](/flugzeuge/t18/matchups#vs-t-15-excalibur-energy-fighter)**: Radius vs Energy
- **[vs T-16 Falchion](/flugzeuge/t18/matchups#vs-t-16-falchion-rate-fighter)**: Radius vs Rate
- **[vs T-18 (Spiegel)](/flugzeuge/t18/matchups#vs-t-18-cutlass-mirror-match)**: Radius vs Radius

---

## Philosophie

Der Schlüssel zum Sieg liegt nicht im engeren Ziehen, sondern im **Verständnis der Physik**. Ein guter Pilot kennt nicht nur sein eigenes Flugzeug, sondern auch das seines Gegners genau. Er zwingt dem Gegner den Kampf auf, den dieser nicht gewinnen kann.

**[Starte mit den Golden Rules](/grundlagen/golden-rules)**
