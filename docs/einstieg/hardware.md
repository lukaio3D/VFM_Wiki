# Hardware & Systemanforderungen

> Technische Voraussetzungen für Virtual Fighter Maneuvers.

VFM ist für VR-Plattformen entwickelt und unterstützt sowohl PCVR als auch Meta Quest Standalone. Hier findest du die Systemanforderungen für beide Plattformen.

---

## PCVR (Steam)

VFM nutzt die Unity-Engine mit physikalisch korrekter Aerodynamik-Simulation. Die GPU-Last ist moderat, aber die CPU muss die Physikberechnungen in Echtzeit durchführen.

### Minimum

| Komponente | Anforderung |
|------------|-------------|
| **Betriebssystem** | Windows 10 (64-bit) |
| **Prozessor** | Intel i5-3570 oder vergleichbar |
| **Arbeitsspeicher** | 16 GB RAM |
| **Grafikkarte** | NVIDIA GTX 970 oder vergleichbar |
| **Speicherplatz** | 500 MB |
| **VR-Headset** | SteamVR / OpenXR kompatibel |

### Empfohlen

| Komponente | Anforderung |
|------------|-------------|
| **Betriebssystem** | Windows 10/11 |
| **Prozessor** | Intel Core i7-9700K / AMD Ryzen 7 3700X |
| **Arbeitsspeicher** | 32 GB RAM |
| **Grafikkarte** | NVIDIA RTX 3070 / AMD RX 6800 XT |
| **Speicherplatz** | 1 GB SSD |
| **VR-Headset** | Valve Index, Meta Quest 3 (Link), HP Reverb G2 |

::: tip PERFORMANCE
Für flüssige 90 Hz in intensiven Multiplayer-Kämpfen wird die empfohlene Konfiguration angeraten.
:::

---

## Meta Quest Standalone

VFM läuft nativ auf Meta Quest 2 und Quest 3 ohne PC-Verbindung.

| Gerät | Unterstützung |
|-------|---------------|
| **Meta Quest 2** | Vollständig unterstützt |
| **Meta Quest 3** | Vollständig unterstützt |
| **Meta Quest Pro** | Vollständig unterstützt |

### Grafik-Optimierungen

Die Standalone-Version ist für die mobile Hardware optimiert:

- Reduzierte Schattenqualität
- Vereinfachte Partikeleffekte (Rauch, Explosionen)
- Optimierte Texturauflösungen
- Stabile 72/90 Hz für Motion-Sickness-Prävention

::: warning HINWEIS
Die Physik-Simulation ist identisch zur PC-Version. Nur die Grafik wurde optimiert.
:::

---

## Cross-Play

VFM unterstützt plattformübergreifendes Spielen zwischen PCVR und Quest.

- **Netcode:** Server-autoritative Architektur für faire Matches
- **Physik:** Deterministische Berechnung für identisches Verhalten
- **Matchmaking:** Gemeinsamer Spielerpool für alle Plattformen

::: info LATENZ
Für kompetitives Spielen wird eine stabile Internetverbindung mit weniger als 50 ms Ping empfohlen.
:::
