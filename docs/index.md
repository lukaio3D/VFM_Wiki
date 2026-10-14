# VFM Flight Academy

> Echtes Basic Fighter Maneuvering, angewendet auf Virtual Fighter Maneuvers.

Dieses Wiki verbindet die Grundlagen, die echte Kampfpiloten lernen (BFM), mit dem, was wir über die drei Jets in **Virtual Fighter Maneuvers** (VFM) wirklich wissen.

::: info ÜBER DAS SPIEL
VR-Dogfight-Simulator von **Boundless Dynamics** (VTOL VR), erschienen am 19.12.2025 für PCVR und Meta Quest, mit Crossplay. Drei Jets, Kanone, IR-Raketen, Flares, Bots, Lobbys von 1v1 bis 4v4, Ranked mit Elo und Seasons. Stand des Wikis: **v1.4.2**.
:::

## Der Lernpfad

Jede Stufe baut auf der vorherigen auf. Die meisten Fehler im Dogfight sind Fehler aus Stufe 1 und 2.

| Stufe | Thema | Du kannst danach … |
|---|---|---|
| **0** | [Golden Rules](/grundlagen/golden-rules) · [Begriffe](/grundlagen/begriffe) | … die Sprache des Luftkampfs sprechen und überleben. |
| **1** | [Kurvenphysik](/grundlagen/kurvenphysik) · [Energie](/grundlagen/energie-management) · [VFM-Flugmodell](/grundlagen/physik) | … erklären, warum dein Jet bei welcher Speed wie dreht. |
| **2** | [Geometrie](/grundlagen/geometrie) · [Verfolgungskurven](/grundlagen/verfolgungskurven) | … die Lage einschätzen und Lead, Pure und Lag gezielt fliegen. |
| **3** | [Offensiv](/grundlagen/offensiv-manoever) | … hinten bleiben, ohne zu overshooten, und schießen. |
| **4** | [Defensiv](/grundlagen/defensiv-manoever) | … Schüsse schlagen und neutralisieren. |
| **5** | [Neutral & Merge](/grundlagen/neutral/der-merge) | … den Merge gewinnen und den Kampf in dein Band zwingen. |
| **6** | [Trainingsplan](/grundlagen/uebungen) | … gezielt üben und Replays auswerten. |

Danach: [dein Flugzeug](/flugzeuge/vergleich) und die Matchups.

## Die drei Jets in einem Satz

| Jet | Charakter (Diagramme, Messung) | Bester Plan laut Simulation | Verliert |
|---|---|---|---|
| **[T-15 Excalibur](/flugzeuge/t15)** | Höchster Schub, meiste G bei gleicher Speed | Two-Circle bei ~380–420 KIAS, nose-low oder flach; gewinnt so gegen beide, den ersten Turn knapp | Mit unnötigen Vollzügen, schnell (~520 KIAS), langsam (~280) und steil hoch |
| **[T-16 Falchion](/flugzeuge/t16)** | Leichter Rate-Spezialist: dreht bei ~400–500 KIAS dauerhaft 1–2 °/s schneller | Two-Circle bei ~400–420 KIAS, flach oder nose-low; gegen die T-18 praktisch ausgeglichen | Steil hoch und langsam (unter ~380 KIAS); gegen die T-15 unterlegen |
| **[T-18 Cutlass](/flugzeuge/t18)** | Nasenautorität (α bis 35° für den Snapshot), höchster Widerstand, langsam stark im Diagramm | Durchfliegen und nose-low mit ~440 KIAS wieder einsteigen oder Two-Circle bei ~440; Snapshots | Schnell (ab ~480–510 KIAS bricht sie ein) und im langsamen One-Circle; gegen die T-15 laut Simulation unterlegen |

Kein Stein-Schere-Papier. Die Diagramme zeigen, wer in welchem Speedband **dauerhaft schneller dreht**. Die [Simulation](/flugzeuge/simulation) (~405.000 Bot-Kämpfe mit dem Originalmodell, dem echten Ranked-Start und den Rollraten aus den Spieldaten) zeigt, was **im ganzen Kampf** gewinnt: für alle drei Jets der Two-Circle bei ~440 KIAS, nose-low oder flach, nur nicht steil hoch. Dort liegt die T-15 vorn, obwohl die T-16 etwas schneller dreht: Sie zieht mehr G, fliegt den kleineren Kreis und hat mehr Schub. Rangfolge laut Simulation: T-15 vorn, T-16 und T-18 fast gleichauf. **Je schneller die Jets wirklich rollen, desto besser für die T-18; die Rollrate ist nicht gemessen.** Matchups: [T-15 vs. T-16](/flugzeuge/matchups/t15-vs-t16), [T-15 vs. T-18](/flugzeuge/matchups/t15-vs-t18), [T-16 vs. T-18](/flugzeuge/matchups/t16-vs-t18).

**Datenstand:** Die Zahlen stammen aus den Ingame-Diagrammen (Okt 2026), aus Messflügen zu Beschleunigung, Ausrollen und vollem Zug, aus den Dateien der Installation (Massen, Kanone, Auftriebsverlauf), aus 71 eigenen Ranked-Replays (Start, Rundendauer) und aus der Simulation. Details und offene Punkte stehen im [Flugzeugvergleich](/flugzeuge/vergleich).

::: tip MERKE
- Lernpfad ab Stufe 0, nichts überspringen.
- Das Speedband entscheidet: Two-Circle bei ~380–440 KIAS, nicht langsam machen, nicht schnell bleiben.
- Jede Zahl ist gekennzeichnet: *Diagramm*, *gemessen*, *Spieldaten*, *Replays*, *Simulation*, *geschätzt* oder *Hypothese*. Offenes steht unter „Im Spiel prüfen“.
- Üben schlägt Lesen: Der Energie-Graph im Replay ist dein bester Lehrer, `vrb.py` liefert die Zahlen dazu.
:::

Weiter: [Golden Rules](/grundlagen/golden-rules)
