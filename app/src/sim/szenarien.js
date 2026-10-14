// Lern-Szenarien für den 3D-Simulator. Jedes Szenario: beide Jets mit Strategie, Startgeometrie, Lektion.
// Optional ein Haltepunkt am Merge mit Frage; die Antworten sind Strategien für Blau (richtig = Lösung).
// Jedes Szenario ist nachgerechnet, damit der Kampf seine Lektion zeigt.
// Werte zu Spielwerten und Strategien stammen aus dem Turnier in tools/kampfsim (~405.000 Kämpfe, Ranked-Start,
// Originalkurven des Spiels). Ohne geo.versatz_m gilt der echte Ranked-Start (physik.js RANKED).

const S = (wende, ebene, v_ziel, lag = 0, extra = {}) => ({ wende, ebene, v_ziel, lag, alpha_kampf: 26, merge_ab: 0, override: 0, ...extra })

export const KATEGORIEN = ['Grundlagen', 'Merge & Neutral', 'Offensiv & Defensiv', 'T-15', 'T-18']

export const SZENARIEN = [
  {
    id: 'erster-turn', kategorie: 'Merge & Neutral',
    titel: 'Erster Turn aus dem Ranked-Start',
    a: 'T-16', sa: S(1, 0, 440, 1, { merge_ab: 1 }),
    b: 'T-18', sb: S(1, 0, 440, 0),
    geo: {},
    text: 'Ranked-Start wie im Spiel: 10.000 ft, Mach 0,75 (~430 KIAS), 13.100 ft Abstand, ~1.300 ft seitlicher Versatz, Merge nach ~8 s. Am Merge hält die Szene an und du entscheidest, wie die T-16 den ersten Turn fliegt.',
    halt: {
      frage: 'Erster Turn?',
      antworten: [
        { text: 'Voll ziehen', s: S(1, 0, 280, 1, { merge_ab: 1 }), fb: 'Nach 8 s gut 10° mehr Winkel, aber ~80 KIAS weniger, und du bist unter deinem Band. Der helle Geist zeigt die Lösung.' },
        { text: 'Sustained ~440', s: S(1, 0, 440, 1, { merge_ab: 1 }), fb: 'Richtig: fast derselbe Winkel, und du bleibst in deinem Band.', richtig: true },
        { text: 'Nose-high', s: S(1, 60, 440, 1, { merge_ab: 1 }), fb: 'Schwächste Wahl für die T-16: oben wirst du langsam. Der helle Geist zeigt die Lösung.' },
      ],
    },
    wiki: '/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen',
  },
  {
    id: 't16-two-circle', kategorie: 'Merge & Neutral',
    titel: 'T-16 gegen T-18: Two-Circle bei ~440 KIAS',
    a: 'T-16', sa: S(1, 0, 440, 1, { merge_ab: 1 }),
    b: 'T-18', sb: S(1, 0, 440, 0),
    geo: {},
    text: 'Die beste T-16-Strategie gegen die T-18: am Pass zu ihr hin (Two-Circle), flach oder nose-low, ~440 KIAS. Die T-16 dreht dauerhaft mit ~7,4 G, die T-18 mit ~6,3 G; Kreis für Kreis holt die T-16 Winkel heraus.',
    wiki: '/flugzeuge/matchups/t16-vs-t18',
  },
  {
    id: 't16-bubble', kategorie: 'Merge & Neutral',
    titel: 'T-16 gegen T-18 im One-Circle: in der Bubble bleiben',
    a: 'T-16', sa: S(1, 0, 440, 0, { merge_ab: 1 }),
    b: 'T-18', sb: S(-1, -30, 360, 0, { merge_ab: 1 }),
    geo: {},
    text: 'Die T-18 dreht am Pass weg und taucht nose-low ab, um den Kampf langsam zu machen. Die T-16 folgt nicht in den engen Kreis, sondern bleibt bei ~440 KIAS außerhalb (grün: Bubble) und nutzt ihre Rate.',
    wiki: '/grundlagen/begriffe#bubble',
  },
  {
    id: 'nose-low', kategorie: 'Grundlagen',
    titel: 'Nose-low gegen nose-high',
    a: 'T-16', sa: S(1, -30, 440),
    b: 'T-16', sb: S(1, 25, 440),
    geo: {},
    text: 'Gleicher Jet, gleiche Speed. Blau dreht nose-low, Orange nose-high. Nose-low wirken Auftrieb und Schwerkraft zusammen, die Speed bleibt. In allen Paarungen gilt: tief schlägt flach schlägt hoch.',
    wiki: '/grundlagen/neutral/der-merge#der-erste-zug-nach-dem-pass',
  },
  {
    id: 'extend-merge', kategorie: 'Grundlagen',
    titel: 'Extend direkt am Merge kostet',
    a: 'T-16', sa: S(0, 0, 440),
    b: 'T-16', sb: S(1, -30, 440),
    geo: {},
    vergleich: [{ sa: S(1, -30, 440) }],
    text: 'Blau fliegt am Merge 6 s geradeaus durch, Orange dreht sofort nose-low. Der Gegner bekommt die Winkel, der Abstand reicht nicht. Der helle Geist dreht stattdessen sofort.',
    wiki: '/grundlagen/neutral/der-merge#blow-through-und-extension',
  },
  {
    id: 'perch', kategorie: 'Offensiv & Defensiv',
    titel: 'Offensiver Perch: hinten bleiben',
    a: 'T-16', sa: S(1, 0, 400, 1),
    b: 'T-16', sb: S(1, -30, 440),
    geo: { lage: 'perch' },
    text: 'Du startest 3.000 ft hinter ihm, er bricht sofort ein. Lag halten, nicht überschießen, im Speedband bleiben, dann Nase in den Vorhalt.',
    wiki: '/grundlagen/offensiv-manoever',
  },
  {
    id: 'defensiv', kategorie: 'Offensiv & Defensiv',
    titel: 'Defensiv: Bandit an deiner Six',
    a: 'T-16', sa: S(1, 0, 440),
    b: 'T-16', sb: S(1, 0, 440, 1),
    geo: { lage: 'defensiv' },
    vergleich: [{ sa: S(1, -30, 360) }],
    text: 'Er sitzt 3.000 ft hinter dir. Break Turn: Lift Vector auf ihn, volle G, und zurück ins eigene Band (~440 KIAS). So verweigerst du den Schuss über die ganze Runde, umdrehen gelingt aus dieser Lage aber nicht, und bei Zeitablauf gewinnt der Verfolger. Der helle Geist bleibt langsam und nose-low und wird nach knapp 3 Minuten getroffen.',
    wiki: '/grundlagen/defensiv-manoever',
  },
  {
    id: 't15-hochziehen', kategorie: 'T-15',
    titel: 'Fehler: T-15 zieht gegen die T-16 hoch',
    a: 'T-15', sa: S(1, 25, 360),
    b: 'T-16', sb: S(1, -30, 420, 0, { merge_ab: 1 }),
    geo: { versatz_m: 600 },
    vergleich: [{ sa: S(1, -30, 360) }],
    text: 'Die T-15 dreht nose-high, die T-16 nose-low und hält ihre Speed. Oben wird die T-15 langsam, die T-16 bekommt nach einem Kreis die Nase herum. Der helle Geist fliegt dieselbe T-15 nose-low und überlebt.',
    wiki: '/flugzeuge/matchups/t15-vs-t16',
  },
  {
    id: 't15-one-circle', kategorie: 'T-15',
    titel: 'T-15 gegen T-18: sofort nose-low herum',
    a: 'T-15', sa: S(1, -30, 440, 1),
    b: 'T-18', sb: S(0, -30, 360, 0, { alpha_kampf: 35 }),
    geo: {},
    vergleich: [{ sa: S(-1, -30, 280) }],
    text: 'Die T-18 fliegt am Merge durch und taucht ab, ihre stärkste Wahl gegen ein breites Feld. Die T-15 dreht sofort zu ihr hin, nose-low bei ~440 KIAS, und hat nach einem halben Kreis die Nase vorn. Der helle Geist fliegt den langsamen One-Circle (280 KIAS) und verliert: Im neuen Modell ist langsam für die T-15 nicht mehr die beste Wahl.',
    wiki: '/flugzeuge/matchups/t15-vs-t18',
  },
  {
    id: 't15-mirror', kategorie: 'T-15',
    titel: 'T-15 gegen T-15: im Band und nose-low',
    a: 'T-15', sa: S(1, -30, 440, 1),
    b: 'T-15', sb: S(1, 25, 520),
    geo: {},
    text: 'Blau kämpft nose-low bei ~440 KIAS, Orange will schnell bleiben (520 KIAS). „Schnell bleiben“ ist in jeder Paarung die schlechteste Wahl: Wer dafür entlastet, macht keine Winkel.',
    wiki: '/flugzeuge/t15',
  },
  {
    id: 't18-override', kategorie: 'T-18',
    titel: 'T-18: Snapshot mit AoA-Override (Annahme)',
    a: 'T-18', sa: S(-1, -30, 360, 0, { merge_ab: 1, override: 1 }),
    b: 'T-15', sb: S(1, 0, 440, 0, { merge_ab: 1 }),
    geo: { versatz_m: 150 },
    vergleich: [{ sa: S(-1, -30, 360, 0, { merge_ab: 1 }) }],
    text: 'Mit Override reißt die T-18 die Nase weit hoch (Cobra), die Speed bricht ein, aber hier sitzt der Snapshot. Der helle Geist fliegt ohne Override und braucht Minuten bis zum Abschuss. Über viele Kämpfe kostet Override als Gewohnheit trotzdem mehr, als er bringt. Das maximale α im Override ist nicht gemessen.',
    wiki: '/flugzeuge/simulation#aoa-override-annahme',
  },
]

export const OPTIONEN = {
  wende: [[1, 'hin (Two-Circle)'], [-1, 'weg (One-Circle)'], [0, 'durch (Extend)']],
  ebene: [[60, 'steil hoch'], [25, 'hoch'], [0, 'flach'], [-30, 'tief (nose-low)']],
  lag: [[0, 'Pure'], [1, 'Lag']],
}
