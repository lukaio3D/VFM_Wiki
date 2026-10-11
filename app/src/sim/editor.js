// Szenario-Editor: Ausgangslage aus wenigen Zahlen, Vorlagen, Suche nach den besten Strategien.
import { simuliere, FT } from './physik.js'

export const VORLAGEN = {
  ranked: { name: 'Ranked-Start (450 KIAS, Merge in ~5 s)', merge: true, versatz_ft: 500 },
  pass: { name: 'High-Aspect-Pass, 2.000 ft Versatz', merge: true, versatz_ft: 2000 },
  perch: { name: 'Offensiver Perch: 3.000 ft hinter ihm', merge: false, abstand_ft: 3000, peilung: 0, kurs: 0, dh_ft: 500, kiasA: 420, kiasB: 400 },
  defensiv: { name: 'Defensiv: Bandit 3.000 ft an deiner Six', merge: false, abstand_ft: 3000, peilung: 180, kurs: 0, dh_ft: 500, kiasA: 400, kiasB: 420 },
  butterfly: { name: 'Butterfly: nebeneinander, 6.000 ft', merge: false, abstand_ft: 6000, peilung: 90, kurs: 0, dh_ft: 0, kiasA: 400, kiasB: 400 },
}

export function neueLage(id = 'ranked') {
  const v = VORLAGEN[id]
  return {
    vorlage: id, a: 'T-16', b: 'T-18', hoehe_ft: 10000, fuel: 100,
    kiasA: v.kiasA ?? 450, kiasB: v.kiasB ?? 450, versatz_ft: v.versatz_ft ?? 500,
    abstand_ft: v.abstand_ft ?? 3000, peilung: v.peilung ?? 0, kurs: v.kurs ?? 0, dh_ft: v.dh_ft ?? 0,
  }
}

export function lageZuGeo(l) {
  const v = VORLAGEN[l.vorlage]
  if (v.merge) return { versatz_m: l.versatz_ft * FT, kias: l.kiasA, hoehe_ft: l.hoehe_ft, fuel: l.fuel / 100 }
  const D = l.abstand_ft * FT, p = l.peilung * Math.PI / 180
  return {
    imKampf: true,
    start: [
      { x: 0, y: 0, hoehe_ft: l.hoehe_ft, kurs: 0, kias: l.kiasA, fuel: l.fuel / 100 },
      { x: D * Math.sin(p), y: D * Math.cos(p), hoehe_ft: l.hoehe_ft + l.dh_ft, kurs: l.kurs, kias: l.kiasB, fuel: l.fuel / 100 },
    ],
  }
}

const S = (wende, ebene, v_ziel, lag = 0) => ({ wende, ebene, v_ziel, lag, alpha_kampf: 26, merge_ab: 0, override: 0 })

function kandidaten(merge) {
  const du = [], er = []
  if (merge) {
    for (const w of [1, -1, 0]) for (const e of [25, 0, -30]) for (const v of [280, 360, 440, 520]) du.push(S(w, e, v))
    for (const w of [1, -1]) for (const e of [0, -30]) for (const v of [360, 440]) er.push(S(w, e, v))
  } else {
    for (const e of [60, 25, 0, -30]) for (const v of [280, 360, 440, 520]) for (const lag of [0, 1]) du.push(S(1, e, v, lag))
    for (const e of [25, 0, -30]) for (const v of [360, 440]) er.push(S(1, e, v))
  }
  return { du, er }
}

// Rechnet alle eigenen Kandidaten gegen alle Antworten des Bandits, in Häppchen, damit die Seite flüssig bleibt.
// Bewertung: Mittel der zwei schlechtesten Ergebnisse (robust) plus ein Teil des Gesamtmittels.
export async function besteStrategien(m, lage, fortschritt) {
  const v = VORLAGEN[lage.vorlage], geo = lageZuGeo(lage)
  const { du, er } = kandidaten(v.merge)
  const E = du.map(() => er.map(() => 0)), T = du.map(() => er.map(() => Infinity))
  const gesamt = du.length * er.length
  let n = 0
  for (let a = 0; a < du.length; a++) {
    for (let b = 0; b < er.length; b++) {
      const r = simuliere(m, lage.a, lage.b, du[a], er[b], geo, { frameAlle: 100000 })
      E[a][b] = r.ergebnis
      T[a][b] = Math.min(...r.tTot)
      n++
    }
    fortschritt(n / gesamt)
    await new Promise(res => setTimeout(res, 0))
  }
  const liste = du.map((s, a) => {
    const werte = E[a].map((e, b) => ({ e, b, t: T[a][b] })).sort((x, y) => x.e - y.e || (x.e < 0 ? x.t - y.t : y.t - x.t))
    const schlecht = (werte[0].e + werte[1].e) / 2
    const mittel = E[a].reduce((x, y) => x + y, 0) / er.length
    // Gleichstand: schnellere Abschüsse und spätere Niederlagen zählen etwas mehr
    const tempo = E[a].reduce((x, e, b) => x + (e > 0 ? (150 - T[a][b]) : e < 0 ? -(150 - T[a][b]) : 0), 0) / (150 * er.length)
    return {
      s, score: 0.6 * schlecht + 0.4 * mittel + 0.1 * tempo,
      siege: E[a].filter(e => e > 0).length, niederlagen: E[a].filter(e => e < 0).length, n: er.length,
      antwort: er[werte[0].b], antwortErgebnis: werte[0].e,
    }
  })
  liste.sort((x, y) => y.score - x.score)
  return { top: liste.slice(0, 3), schlechteste: liste[liste.length - 1], kaempfe: gesamt }
}
