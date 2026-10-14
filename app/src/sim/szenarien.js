// Lern-Szenarien für den 3D-Simulator. Jedes Szenario: beide Jets mit Strategie, Startgeometrie, Lektion.
// Optional ein Haltepunkt am Merge mit Frage; die Antworten sind Strategien für Blau (richtig = Lösung).
// Jedes Szenario ist als Schar nachgerechnet (9 Varianten der Startlage, Versatz 200–600 m bzw. Abstand
// 2.400–3.600 ft): Die Lektion muss die Mehrheit tragen, die gezeigte Startlage zeigt sie.
// Werte zu Spielwerten und Strategien stammen aus dem Turnier in tools/kampfsim (~405.000 Kämpfe, Ranked-Start,
// Originalkurven des Spiels). Ohne geo.versatz_m gilt der echte Ranked-Start (physik.js RANKED).

const S = (wende, ebene, v_ziel, lag = 0, extra = {}) => ({ wende, ebene, v_ziel, lag, alpha_kampf: 26, merge_ab: 0, override: 0, ...extra })

export const KATEGORIEN = ['Grundlagen', 'Merge & Neutral', 'Offensiv & Defensiv', 'T-15', 'T-18']

export const SZENARIEN = [
  {
    id: 'erster-turn', kategorie: 'Merge & Neutral',
    titel: 'Erster Turn aus dem Ranked-Start',
    a: 'T-16', sa: S(1, 0, 440, 1, { merge_ab: 1 }),
    b: 'T-15', sb: S(1, 25, 440, 1, { merge_ab: 1 }),
    geo: {},
    text: 'Ranked-Start wie im Spiel: 10.000 ft, Mach 0,75 (~430 KIAS), 13.100 ft Abstand, ~1.300 ft seitlicher Versatz, Merge nach ~8 s. Die T-16 trifft auf die stärkere T-15. Am Merge hält die Szene an und du entscheidest, wie die T-16 den ersten Turn fliegt.',
    halt: {
      frage: 'Erster Turn?',
      antworten: [
        { text: 'Voll ziehen', s: S(1, 0, 280, 1, { merge_ab: 1 }), fb: 'Nach 8 s gut 10° mehr Winkel, aber ~80 KIAS weniger, und du bist unter deinem Band. In 7 von 9 Varianten verlierst du. Der helle Geist zeigt die Lösung.' },
        { text: 'Sustained ~440', s: S(1, 0, 440, 1, { merge_ab: 1 }), fb: 'Richtig: fast derselbe Winkel, und du bleibst in deinem Band. Gegen die T-15 bleibt der Kampf so meist offen (5 von 9 Varianten), statt verloren.', richtig: true },
        { text: 'Nose-high', s: S(1, 60, 440, 1, { merge_ab: 1 }), fb: 'Schwächste Wahl für die T-16: oben wirst du langsam und verlierst in allen 9 Varianten. Der helle Geist zeigt die Lösung.' },
      ],
    },
    wiki: '/grundlagen/neutral/der-merge#der-erste-turn-aus-450-kias-gemessen',
  },
  {
    id: 't16-two-circle', kategorie: 'Merge & Neutral',
    titel: 'T-16 gegen T-18: Two-Circle bei ~440 KIAS',
    a: 'T-16', sa: S(1, 25, 440, 1),
    b: 'T-18', sb: S(1, 0, 440, 0),
    geo: { versatz_m: 500 },
    text: 'Beide im Two-Circle bei ~440 KIAS. Die T-16 dreht dauerhaft schneller, die T-18 hat die Nase für den Snapshot. Das ist knapp: In 5 von 9 Varianten gewinnt die T-16, in 3 die T-18. Wie knapp, hängt an der Rollrate, die im Spiel noch nicht gemessen ist; rollen die Jets langsamer als die Spieldaten vorgeben, liegt die T-16 klar vorn.',
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
    geo: { versatz_m: 450 },
    text: 'Gleicher Jet, gleiche Speed. Blau dreht nose-low, Orange nose-high. Nose-low wirken Auftrieb und Schwerkraft zusammen, die Speed bleibt. In 5 von 9 Varianten gewinnt Blau, nie Orange. Der Vorteil ist kleiner als gedacht: Mit den Rollraten aus den Spieldaten liegen tief, flach und leicht hoch nah beieinander, klar verliert nur steil hoch.',
    wiki: '/grundlagen/neutral/der-merge#der-erste-zug-nach-dem-pass',
  },
  {
    id: 'extend-merge', kategorie: 'Grundlagen',
    titel: 'Extend gegen einen Gegner, der sofort dreht',
    a: 'T-16', sa: S(0, 0, 440),
    b: 'T-16', sb: S(1, -30, 440),
    geo: {},
    vergleich: [{ sa: S(1, -30, 440) }],
    text: 'Blau fliegt am Merge 6 s geradeaus durch, Orange dreht sofort nose-low. Der Gegner bekommt die Winkel, der Abstand reicht nicht: In 6 von 9 Varianten verliert Blau. Der helle Geist dreht stattdessen sofort und bleibt im Spiel. Über alle Gegner gerechnet ist Durchfliegen mit ~440 KIAS kein Nachteil – teuer wird es, wenn der Gegner sofort dreht und du Speed verlierst.',
    wiki: '/grundlagen/neutral/der-merge#blow-through-und-extension',
  },
  {
    id: 'perch', kategorie: 'Offensiv & Defensiv',
    titel: 'Offensiver Perch: hinten bleiben',
    a: 'T-16', sa: S(1, 0, 400, 1),
    b: 'T-16', sb: S(1, -30, 440),
    geo: { lage: 'perch', abstand_ft: 2700 },
    text: 'Du startest ~2.700 ft hinter ihm, er bricht sofort ein. Lag halten, nicht überschießen, im Speedband bleiben, dann Nase in den Vorhalt. Sicher ist das nicht: In 5 von 9 Varianten gewinnt der Angreifer, in 2 dreht der Verteidiger den Kampf.',
    wiki: '/grundlagen/offensiv-manoever',
  },
  {
    id: 'defensiv', kategorie: 'Offensiv & Defensiv',
    titel: 'Defensiv: Bandit an deiner Six',
    a: 'T-16', sa: S(1, 0, 440),
    b: 'T-16', sb: S(1, 0, 440, 1),
    geo: { lage: 'defensiv', abstand_ft: 2700 },
    vergleich: [{ sa: S(1, -30, 360) }],
    text: 'Er sitzt ~2.700 ft hinter dir. Break Turn: Lift Vector auf ihn, volle G, und zurück ins eigene Band (~440 KIAS). So verweigerst du den Schuss (in 7 von 9 Varianten bleibt es offen), umdrehen gelingt aus dieser Lage aber kaum, und bei Zeitablauf gewinnt der Verfolger. Der helle Geist bleibt langsam und nose-low und wird öfter getroffen.',
    wiki: '/grundlagen/defensiv-manoever',
  },
  {
    id: 't15-hochziehen', kategorie: 'T-15',
    titel: 'Fehler: T-15 zieht gegen die T-16 steil hoch',
    a: 'T-15', sa: S(1, 60, 440),
    b: 'T-16', sb: S(1, -30, 420, 0, { merge_ab: 1 }),
    geo: {},
    vergleich: [{ sa: S(1, -30, 440, 1) }],
    text: 'Die T-15 zieht steil hoch, die T-16 bleibt nose-low und hält ihre Speed. Oben wird die T-15 langsam, und ihr Vorteil ist weg: In 7 von 9 Varianten bleibt der Kampf offen. Der helle Geist fliegt dieselbe T-15 nose-low im Two-Circle und gewinnt in 6 von 9.',
    wiki: '/flugzeuge/matchups/t15-vs-t16',
  },
  {
    id: 't15-one-circle', kategorie: 'T-15',
    titel: 'T-15 gegen T-18: sofort nose-low herum',
    a: 'T-15', sa: S(1, -30, 440, 1),
    b: 'T-18', sb: S(0, -30, 440, 1, { alpha_kampf: 35, merge_ab: 1 }),
    geo: {},
    vergleich: [{ sa: S(-1, -30, 280) }],
    text: 'Die T-18 fliegt am Merge durch und taucht ab, ihre stärkste Wahl gegen ein breites Feld. Die T-15 dreht sofort zu ihr hin, nose-low bei ~440 KIAS: In 8 von 9 Varianten gewinnt sie. Der helle Geist fliegt den langsamen One-Circle (280 KIAS) und gewinnt nur in 4 von 9: Langsam ist für die T-15 nicht die beste Wahl.',
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
    geo: { versatz_m: 450 },
    vergleich: [{ sa: S(-1, -30, 360, 0, { merge_ab: 1 }) }],
    text: 'Mit Override reißt die T-18 die Nase weit hoch (Cobra), die Speed bricht ein. Sitzt der Snapshot nicht, ist sie danach langsam und die T-15 nicht: In 7 von 9 Varianten verliert sie. Der helle Geist fliegt dieselbe T-18 ohne Override und gewinnt in 5 von 9. Override ist ein Werkzeug für den einen Schuss, keine Gewohnheit. Das maximale α im Override ist nicht gemessen.',
    wiki: '/flugzeuge/simulation#aoa-override-annahme',
  },
]

export const OPTIONEN = {
  wende: [[1, 'hin (Two-Circle)'], [-1, 'weg (One-Circle)'], [0, 'durch (Extend)']],
  ebene: [[60, 'steil hoch'], [25, 'hoch'], [0, 'flach'], [-30, 'tief (nose-low)']],
  lag: [[0, 'Pure'], [1, 'Lag']],
}
