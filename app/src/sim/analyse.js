// Lagebewertung für das Datenpanel: die drei BFM-Probleme (Winkel, Aspect, Abstand/Closure) mit Lösung,
// dazu Kurvenkreis und Ps aus den Simulations-Frames.
import { vek, FT, KT } from './physik.js'

const { norm, mul, add, einheit } = vek

const zahl = (v, d = 0) => Number(v).toLocaleString('de-DE', { maximumFractionDigits: d, minimumFractionDigits: d })

// Bewertung aus Sicht von Jet i. Stufen: 'ok' | 'achtung' | 'problem'
export function dreiProbleme(f, i) {
  const j = f.j[i], o = f.j[1 - i]
  const Rft = j.R / FT, vcKt = j.vc / KT
  const out = []

  let w
  if (o.ataNose < 30 && j.ata > 90 && j.R < 1500) w = ['problem', 'Er hat die Nase auf dir: Break Turn, Lift Vector auf ihn, volle G.']
  else if (j.ataNose < 20) w = ['ok', j.R < 900 ? 'Nase auf ihm: Vorhalt nehmen, schießen.' : 'Nase auf ihm: halten und aufschließen.']
  else if (j.ataNose < 60) w = ['achtung', 'Lift Vector auf ihn, weiter ziehen.']
  else w = ['problem', 'Nase weit weg: Lift Vector auf ihn, nose-low für mehr Rate.']
  out.push({ name: 'Winkel', mass: 'ATA', wert: `${zahl(j.ataNose)}°`, stufe: w[0], loesung: w[1] })

  let a
  if (j.aa < 45) a = ['ok', 'Du bist hinter ihm.']
  else if (j.aa < 90) a = ['achtung', 'Seitlich: in Lag bleiben, außerhalb seines Kreises (Bubble).']
  else if (j.vc > 0 && j.R > 1500) a = ['achtung', 'Head-on: Turning Room im Blick, am Pass entscheiden.']
  else a = ['problem', 'Vor seiner 3/9-Linie: Er kann die Nase auf dich bringen. Nicht in seinen Kreis ziehen.']
  out.push({ name: 'Aspect', mass: 'AA', wert: `${zahl(j.aa)}°`, stufe: a[0], loesung: a[1] })

  let r
  if (j.R < 300 && j.vc > 0 && j.aa < 90) r = ['problem', 'Zu nah, Overshoot droht: High Yo-Yo oder Gas raus.']
  else if (vcKt > 150 && j.R < 1500 && j.aa < 90) r = ['achtung', 'Closure hoch: Lag, High Yo-Yo, Gas raus.']
  else if (j.R > 1500 && j.vc < 0 && j.aa < 90) r = ['achtung', 'Er zieht weg: Low Yo-Yo, Lead, Nachbrenner.']
  else if (j.R <= 900) r = ['ok', 'In Gun-Reichweite.']
  else r = ['ok', 'Abstand passt.']
  out.push({ name: 'Abstand / Closure', mass: 'R · Vc', wert: `${zahl(Rft)} ft · ${vcKt >= 0 ? '+' : '−'}${zahl(Math.abs(vcKt))} kt`, stufe: r[0], loesung: r[1] })
  return out
}

// Kurvenkreis im Bewegungsraum: Mittelpunkt, Radius, Basis (e1 zur Mitte, e2 Flugrichtung). null bei fast geradem Flug.
export function kurvenkreis(j) {
  const a = norm(j.aq)
  if (a < 3) return null
  const R = j.V * j.V / a
  if (R > 6000) return null
  const e1 = mul(j.aq, 1 / a)
  return { R, e1, e2: j.vh, C: add(j.P, mul(e1, R)) }
}

// Spezifische Überschussleistung Ps [ft/s] aus der Energiehöhe benachbarter Frames
export function ps(frames, k, i) {
  const a = frames[Math.max(0, k - 2)], b = frames[Math.min(frames.length - 1, k + 2)]
  if (b.t === a.t) return 0
  return (b.j[i].E - a.j[i].E) / (b.t - a.t) / FT
}

export function modusText(j) {
  if (j.override) return 'AoA-Override'
  if (j.gun) return j.schuss ? 'Gun · Treffer' : 'Gun'
  if (j.bedroht) return 'Break Turn'
  return ['vor dem Merge', 'erster Turn', 'Kampf'][j.phase]
}

export function schubText(gas) {
  if (gas > 0.99) return 'AB'
  if (gas < 0.01) return 'Leerlauf'
  return `${Math.round(gas * 100)} %`
}

export { zahl, einheit }
