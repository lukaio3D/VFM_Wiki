// 1v1-Kampfsimulation der VFM-Jets im Browser.
// Portierung von tools/kampfsim/sim.py (ein Kampf, zwei Jets, gleiche Physik und Bot-Logik).
// Modell und Annahmen kommen aus docs/public/sim/modell.json (tools/kampfsim/export_web.py).
//
// Zusatz gegenüber sim.py: AoA-Override für Snapshots (Strategie-Feld `override`). Nicht gemessen,
// Werte und Verhalten jenseits von 35° sind Annahmen (siehe OVERRIDE).

export const g = 9.80665, KT = 0.514444, LB = 4.44822, FT = 0.3048, RHO0 = 1.225

// AoA-Override: maximales α und Abfall des Auftriebs danach. Annahme nach Spielerberichten, nicht gemessen.
export const OVERRIDE = {
  'T-15': { alpha: 50 },
  'T-16': { alpha: 32 },
  'T-18': { alpha: 80 },
  pitchRate: 40,          // °/s Nase hoch mit Override (Annahme)
}

// --------------------------------------------------------------- Vektoren
const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
const mul = (a, s) => [a[0] * s, a[1] * s, a[2] * s]
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
const norm = (a) => Math.sqrt(dot(a, a))
const einheit = (a, ersatz) => {
  const n = norm(a)
  if (ersatz && n < 1e-6) return ersatz
  return mul(a, 1 / Math.max(n, 1e-9))
}
const senkrecht = (v, zu) => sub(v, mul(zu, dot(v, zu)))
const winkel = (a, b) => Math.acos(Math.min(1, Math.max(-1, dot(a, b)))) * 180 / Math.PI
const clip = (x, a, b) => Math.min(b, Math.max(a, x))
const rad = (d) => d * Math.PI / 180
const UP = [0, 0, 1]
export const vek = { add, sub, mul, dot, cross, norm, einheit, senkrecht, winkel }

// --------------------------------------------------------------- Atmosphäre
export class Atmo {
  constructor(m) { Object.assign(this, m.atm) }
  rho(h) { return RHO0 * Math.exp(-h / this.H) }
  _b(hf) {
    const { hs, b } = this
    if (hf <= hs[0]) return b[0]
    if (hf >= hs[2]) return b[2]
    const i = hf < hs[1] ? 0 : 1
    return b[i] + (b[i + 1] - b[i]) * (hf - hs[i]) / (hs[i + 1] - hs[i])
  }
  _a(hf) { const [c2, c1, c0] = this.la; return Math.exp((c2 * hf + c1) * hf + c0) }
  r(h, kias) { const hf = h / FT; return this._a(hf) + this._b(hf) * (kias - 400) }
  kias(h, V) {
    const hf = h / FT, a = this._a(hf), b = this._b(hf), B = a - 400 * b, c = V / KT
    return 2 * c / (B + Math.sqrt(Math.max(B * B + 4 * b * c, 1e-9)))
  }
  tas(h, kias) { return kias * KT * this.r(h, kias) }
  static schall(h) { return Math.sqrt(1.4 * 287.05 * Math.max(288.15 - 0.0065 * h, 216.65)) }
}

// --------------------------------------------------------------- Jet
export class Jet {
  constructor(m, typ) {
    Object.assign(this, m.jets[typ])
    this.typ = typ
    this.MK = m.MK; this.cb = m.cb; this.a_stall = m.a_stall; this.sig10 = m.sig10
  }
  _interp(tab, M) {
    const MK = this.MK
    const i = clip(Math.floor((M - MK[0]) / 0.1), 0, MK.length - 2)
    const f = clip((M - MK[i]) / 0.1, 0, 1)
    return tab[i] * (1 - f) + tab[i + 1] * f
  }
  sclm(M) { const d = M - 0.5; return this.scl[0] + this.scl[1] * d + this.scl[2] * d * d }
  schub(rho, M) { return 1e5 * Math.exp(this._interp(this.lnT, M)) * Math.pow(rho / RHO0 / this.sig10, this.x) }
  polare(M) {
    return [Math.exp(this._interp(this.lnD, M)), Math.exp(this.a0) * Math.max(1 + this.a1 * (M - 0.5) ** 2, 0.2), this.sclm(M)]
  }
  // Grenze, ab der Strömungsabriss gilt: T-18 26°, sonst α-Limiter
  aStall() { return this.stall ? this.a_stall : this.alpha_lim }
  widerstand(q, scd0, ks, sclm, L, alpha) {
    const c = L / (q * sclm)
    let D = q * scd0 + ks * L * L / q + this.kx * q * sclm * Math.max(c - this.cb, 0) ** 2
    const ueber = alpha - this.aStall()
    if (ueber > 0) {
      // gemessen (T-18 bis 35°): linear; Override darüber: Flachplatte 2 sin²α bezogen auf S ≈ SCLm / 1,6 (Annahme)
      const kst = this.stall ? this.kst : KST_ANDERE
      D += kst * q * sclm * Math.min(ueber, 9) / 9
      if (ueber > 9) D += q * (sclm / 1.6) * 2 * (Math.sin(rad(alpha)) ** 2 - Math.sin(rad(this.aStall() + 9)) ** 2)
    }
    return D
  }
  cVonAlpha(alpha) {
    const s = this.aStall()
    if (alpha <= s) {
      return this.c_lim * (alpha - this.alpha0) / (this.alpha_lim - this.alpha0)
    }
    const c35 = this.stall ? this.c35 : 0.93 * this.c_lim
    if (alpha <= s + 9) return this.c_lim + (c35 - this.c_lim) * (alpha - s) / 9
    // Override jenseits: Auftrieb wie Flachplatte, fällt bis 90° auf 0 (Annahme)
    return c35 * Math.sin(rad(2 * alpha)) / Math.sin(rad(2 * (s + 9)))
  }
  alphaVonC(c) { return this.alpha0 + (this.alpha_lim - this.alpha0) * c / this.c_lim }
  LfuerD(q, scd0, ks, sclm, D) {
    const rest = Math.max(D - q * scd0, 0)
    const L1 = Math.sqrt(rest * q / ks)
    if (L1 <= this.cb * q * sclm) return L1
    const A = ks * q * sclm ** 2 + this.kx * q * sclm
    const B = -2 * this.kx * q * sclm * this.cb
    const C = this.kx * q * sclm * this.cb ** 2 - rest
    return (-B + Math.sqrt(Math.max(B * B - 4 * A * C, 0))) / (2 * A) * q * sclm
  }
}
const KST_ANDERE = 0.27   // Strömungsabriss-Widerstand wie T-18 (Annahme für T-15/T-16 im Override)

function mitSchwerkraft(lDir, n, gS) {
  const lg = dot(lDir, gS)
  const a = lg + Math.sqrt(Math.max(lg * lg - dot(gS, gS) + (n * g) ** 2, 0))
  return einheit(sub(mul(lDir, a), gS), lDir)
}

// --------------------------------------------------------------- Strategien
export const STRATEGIE_STANDARD = { wende: 1, ebene: 0, v_ziel: 440, lag: 0, alpha_kampf: 26, merge_ab: 0, override: 0 }

export function strategieName(s, jet) {
  const w = { 1: 'hin', '-1': 'weg', 0: 'durch' }[s.wende]
  const e = { 60: 'steil hoch', 25: 'hoch', 0: 'flach', '-30': 'tief' }[s.ebene] ?? `${s.ebene}°`
  return `${w}/${e}/${s.v_ziel} KIAS/${s.lag > 0 ? 'Lag' : 'Pure'}` +
    (jet === 'T-18' ? `, α ${s.alpha_kampf}°` : '') + (s.merge_ab ? ', Merge mit AB' : '') + (s.override ? ', Override' : '')
}

// --------------------------------------------------------------- Simulation
// geo: { versatz_m, kias, hoehe_ft, sek_bis_merge, fuel }  (Ranked-Start, Head-on)
//   oder geo.start = [{ x, y (m), hoehe_ft, kurs (° rechtweisend, 0 = +y), kias, fuel }, {…}], geo.imKampf = true:
//   beide Bots starten direkt im Kampf (kein Merge), z. B. Perch oder Defensive.
// Rückgabe: { ergebnis (+1 A, -1 B, 0 offen), t_ende, frames: [{t, j:[{P, vh, l, alpha, n, kias, h, gas, phase, gun, bedroht, schuss, treffer}]}], ... }
export function simuliere(m, typA, typB, stratA, stratB, geo = {}, opt = {}) {
  const AN = { ...m.annahmen, ...(opt.annahmen || {}) }
  const dt = opt.dt ?? 0.04, tMax = opt.tMax ?? 150, frameAlle = opt.frameAlle ?? 2
  const atm = new Atmo(m)
  const fl = [new Jet(m, typA), new Jet(m, typB)]
  const S = [{ ...STRATEGIE_STANDARD, ...stratA }, { ...STRATEGIE_STANDARD, ...stratB }]
  const kias0 = geo.kias ?? 450, h0 = (geo.hoehe_ft ?? 10000) * FT
  const V0 = atm.tas(h0, kias0), abstand = 2 * V0 * (geo.sek_bis_merge ?? 5)
  let P = [[0, -abstand / 2, h0], [geo.versatz_m ?? 150, abstand / 2, h0 + (geo.hoehe_versatz_m ?? 0)]]
  let V = [[0, V0, 0], [0, -V0, 0]]
  const fuel = geo.fuel ?? AN.fuel_start
  let W = fl.map(f => f.W_leer + (f.W_voll - f.W_leer) * fuel)
  if (geo.start) {
    P = geo.start.map(s => [s.x, s.y, s.hoehe_ft * FT])
    V = geo.start.map((s, i) => {
      const v = atm.tas(P[i][2], s.kias), k = rad(s.kurs)
      return [v * Math.sin(k), v * Math.cos(k), 0]
    })
    W = geo.start.map((s, i) => fl[i].W_leer + (fl[i].W_voll - fl[i].W_leer) * (s.fuel ?? fuel))
  }
  let l = [[0, 0, 1], [0, 0, 1]]
  const p0 = geo.imKampf ? 2 : 0
  let alpha = [2, 2], Aprev = [[0, 0, 0], [0, 0, 0]], phase = [p0, p0], tPhase = [0, 0]
  let Nebene = [[0, 0, 0], [0, 0, 0]], dirPrev = null, dfirePrev = null, tCpaAlt = [0, 0]
  let treffer = [0, 0], nAkt = [1, 1], gas = [1, 1]
  const tTot = [Infinity, Infinity], absturz = [false, false]
  const roll = rad(AN.rollrate_dps) * dt, u = AN.geschoss_mps
  const frames = []
  const schritte = Math.round(tMax / dt)
  let tEnde = tMax

  for (let it = 0; it < schritte; it++) {
    const t = it * dt
    if (isFinite(tTot[0]) || isFinite(tTot[1])) { tEnde = t; break }
    const z = [0, 1].map(i => {
      const h = P[i][2]
      const Vm = Math.max(norm(V[i]), 20)
      const vh = einheit(V[i], [0, 1, 0])
      const rho = atm.rho(h), q = 0.5 * rho * Vm * Vm, M = Vm / Atmo.schall(h)
      const kias = atm.kias(h, Vm)
      const [scd0, ks, sclm] = fl[i].polare(M)
      return { h, Vm, vh, rho, q, M, kias, T: fl[i].schub(rho, M), scd0, ks, sclm, mass: W[i] / g }
    })
    const geo2 = [0, 1].map(i => {
      const o = 1 - i
      const rel = sub(P[o], P[i]), R = norm(rel), los = mul(rel, 1 / R)
      const nose = add(mul(z[i].vh, Math.cos(rad(alpha[i]))), mul(l[i], Math.sin(rad(alpha[i]))))
      const relv = sub(V[o], V[i])
      return {
        rel, R, los, nose, relv, ata: winkel(z[i].vh, los), ataNose: winkel(nose, los), aa: winkel(z[o].vh, los),
        tCpa: -dot(rel, relv) / Math.max(dot(relv, relv), 1e-6),
      }
    })
    // Schusslösung
    const dFire = [], fehler = [], schuss = [false, false]
    for (const i of [0, 1]) {
      const o = 1 - i, G = geo2[i]
      const aRel = add(Aprev[o], [0, 0, g])
      let tf = G.R / u, pt
      for (let k = 0; k < 2; k++) {
        pt = add(add(G.rel, mul(G.relv, tf)), mul(aRel, 0.5 * tf * tf))
        tf = norm(pt) / u
      }
      dFire[i] = einheit(pt)
      fehler[i] = winkel(G.nose, dFire[i])
      const fenster = Math.max(Math.atan(AN.ziel_radius_m / G.R) * 180 / Math.PI, AN.gun_streuung_deg)
      schuss[i] = phase[i] >= 1 && phase[o] >= 1 && G.R > AN.gun_r_min_m && G.R < AN.gun_r_max_m && fehler[i] < fenster
    }
    for (const i of [0, 1]) if (schuss[i]) treffer[i] += dt
    const neuTot = [treffer[1] >= AN.treffer_s_bis_abschuss, treffer[0] >= AN.treffer_s_bis_abschuss]

    // Phasen
    for (const i of [0, 1]) {
      const G = geo2[i]
      const neuerPass = phase[i] === 2 && G.tCpa < 0 && tCpaAlt[i] >= 0 && G.R < 1000 && G.aa > 60 && G.ata > 60
      tCpaAlt[i] = G.tCpa
      if ((phase[i] === 0 && (G.tCpa < 0.3 || G.R < 300)) || neuerPass) {
        let seite = senkrecht(G.rel, z[i].vh); seite = [seite[0], seite[1], 0]
        seite = mul(einheit(seite, [1, 0, 0]), S[i].wende < 0 ? -1 : 1)
        const e = rad(S[i].ebene)
        const l0 = einheit(senkrecht(add(mul(seite, Math.cos(e)), mul(UP, Math.sin(e))), z[i].vh))
        Nebene[i] = cross(z[i].vh, l0)
        phase[i] = 1; tPhase[i] = 0
      }
    }
    const extend = [0, 1].map(i => phase[i] === 1 && S[i].wende === 0)
    for (const i of [0, 1]) {
      tPhase[i] += dt
      if (phase[i] === 1 && ((S[i].wende !== 0 && ((geo2[i].ata < 75 && tPhase[i] > 2) || tPhase[i] > 20)) || (extend[i] && tPhase[i] > 6))) phase[i] = 2
    }

    // Steuerung
    const dir = [], lSoll = [], nSoll = [], gun = [], bedroht = [], aGrenze = [], overrideAktiv = []
    for (const i of [0, 1]) {
      const o = 1 - i, Z = z[i], G = geo2[i], s = S[i], f = fl[i]
      const upS = einheit(senkrecht(UP, Z.vh), l[i])
      const gS = senkrecht([0, 0, -g], Z.vh)
      const sinGam = Z.vh[2]
      const dVdt = clip(0.3 * (s.v_ziel - Z.kias), -40, 40) * KT * atm.r(Z.h, Z.kias)
      const Dreq = Z.T - Z.mass * (dVdt + g * sinGam)
      const nSpeed = clip(f.LfuerD(Z.q, Z.scd0, Z.ks, Z.sclm, Dreq) / W[i], 0.5, 9)

      const lagEff = s.lag * clip((2000 - G.R) / 800, 0, 1)
      const ziel = sub(P[o], mul(V[o], lagEff))
      dir[i] = einheit(sub(ziel, P[i]))
      const dp = dirPrev ? dirPrev[i] : dir[i]
      const Om = mul(cross(dp, dir[i]), 1 / dt)
      const eS = senkrecht(dir[i], Z.vh)
      let th = Math.asin(clip(norm(eS), 0, 1))
      if (dot(dir[i], Z.vh) < 0) th = Math.PI - th
      const eHat = einheit(eS, l[i])
      const aDes = add(cross(Om, V[i]), mul(eHat, 1.5 * th * Z.Vm))
      const bias = rad(s.ebene * 0.5)
      const Lvec = sub(aDes, gS)
      const nPur = norm(Lvec) / g
      const lKampf = einheit(add(einheit(Lvec, l[i]), mul(upS, Math.tan(bias))))
      const nKampf = Math.min(nSpeed, nPur)

      // mit Override versucht der Bot den Snapshot auch bei großem Winkel, sobald der Gegner nah ist
      const gunKegel = s.override && G.R < 1000 ? 70 : 30
      gun[i] = phase[i] >= 1 && G.R < 1500 && G.ataNose < gunKegel && dot(G.los, Z.vh) > 0
      const dfp = dfirePrev ? dfirePrev[i] : dFire[i]
      const OmG = mul(cross(dfp, dFire[i]), 1 / dt)
      const eG = senkrecht(sub(dFire[i], G.nose), Z.vh)
      const aG = add(cross(OmG, V[i]), mul(einheit(eG, l[i]), 2.0 * rad(fehler[i]) * Z.Vm))
      const Lg = sub(aG, gS)
      const lGun = einheit(Lg, l[i]), nGun = norm(Lg) / g

      bedroht[i] = phase[i] >= 1 && G.R < 1500 && geo2[o].ataNose < 30 && G.ata > 90
      const lDef = mitSchwerkraft(einheit(senkrecht(G.los, Z.vh), l[i]), 8.0, gS)
      const lTurn = mitSchwerkraft(einheit(cross(Nebene[i], Z.vh), l[i]), nAkt[i], gS)

      let ls = phase[i] === 0 ? upS : lTurn, ns = phase[i] === 0 ? 1.0 : nSpeed
      if (extend[i]) { ls = upS; ns = clip(-gS[2] / g, 0.5, 1.0) }
      if (phase[i] === 2) { ls = lKampf; ns = nKampf }
      if (bedroht[i]) { ls = lDef; ns = 9.0 }
      if (gun[i]) { ls = lGun; ns = nGun }

      const wB = clip((900 - (Z.h + 4 * V[i][2])) / 600, 0, 1) * (sinGam < 0.1 ? 1 : 0)
      ls = einheit(add(mul(ls, 1 - wB), mul(upS, wB)), l[i]); ns = Math.max(ns, wB * 9)
      const wC = clip((Z.h + 4 * V[i][2] - 6700) / 600, 0, 1) * (sinGam > -0.1 ? 1 : 0)
      ls = einheit(sub(mul(ls, 1 - wC), mul(upS, wC)), l[i]); ns = Math.max(ns, wC * 4)
      lSoll[i] = ls; nSoll[i] = ns

      // AoA-Override für den Snapshot: Gegner nah, Nase muss weiter herum, als der Auftrieb hergibt
      overrideAktiv[i] = !!s.override && gun[i] && G.R < 1000 && fehler[i] > 3 && wB === 0
      const aMax = overrideAktiv[i] ? OVERRIDE[f.typ].alpha : f.alpha_max
      let ag = gun[i] ? aMax : Math.min(s.alpha_kampf ?? 99, f.alpha_max)
      if (!overrideAktiv[i]) ag = Math.min(ag, f.stall ? 35 : f.alpha_lim)
      aGrenze[i] = ag
    }
    dirPrev = dir; dfirePrev = dFire

    for (const i of [0, 1]) {
      const Z = z[i], f = fl[i]
      let aCmd = f.alphaVonC(nSoll[i] * W[i] / (Z.q * Z.sclm))
      const bisLim = Math.min(aGrenze[i], f.alpha_lim)
      if (aCmd > bisLim) aCmd = (nSoll[i] >= 8.99 || gun[i]) ? aGrenze[i] : bisLim
      if (overrideAktiv[i]) aCmd = Math.min(alpha[i] + fehler[i], aGrenze[i])
      aCmd = clip(aCmd, -5, aGrenze[i])
      const rateAuf = overrideAktiv[i] && alpha[i] > f.alpha_lim ? OVERRIDE.pitchRate : f.alpha_rate
      alpha[i] += clip((aCmd - alpha[i]) / AN.alpha_tau_s, -AN.alpha_rate_ab_dps, rateAuf) * dt
    }

    const A = [], Lsave = []
    for (const i of [0, 1]) {
      const Z = z[i], f = fl[i]
      let L = Math.min(f.cVonAlpha(alpha[i]) * Z.q * Z.sclm, 9 * W[i])
      if (L >= 9 * W[i] - 1 && !overrideAktiv[i]) alpha[i] = Math.min(alpha[i], f.alphaVonC(9 * W[i] / (Z.q * Z.sclm)))
      nAkt[i] = L / W[i]; Lsave[i] = L
      // Rollen
      const ls = einheit(senkrecht(lSoll[i], Z.vh), l[i])
      const sinp = dot(cross(l[i], ls), Z.vh), cosp = dot(l[i], ls)
      const phi = clip(Math.atan2(sinp, cosp), -roll, roll)
      l[i] = add(mul(l[i], Math.cos(phi)), mul(cross(Z.vh, l[i]), Math.sin(phi)))
      const D = f.widerstand(Z.q, Z.scd0, Z.ks, Z.sclm, L, alpha[i])
      const Thalten = clip(D + Z.mass * (0.5 * (450 - Z.kias) * KT + g * Z.vh[2]), 0, Z.T)
      gas[i] = phase[i] === 0 ? (S[i].merge_ab > 0 ? 1 : Thalten / Z.T) : ((extend[i] || Z.kias < S[i].v_ziel + 60) ? 1 : 0)
      const T = Z.T * gas[i]
      A[i] = add(add(mul(Z.vh, (T - D) / Z.mass), mul(l[i], L / Z.mass)), [0, 0, -g])
      Lsave[i] = senkrecht(A[i], Z.vh)   // Beschleunigung quer zur Bahn: Kurvenkreis
    }
    if (it % frameAlle === 0) {
      frames.push({
        t, j: [0, 1].map(i => ({
          P: P[i].slice(), vh: z[i].vh, l: l[i].slice(), alpha: alpha[i], n: nAkt[i], kias: z[i].kias, h: z[i].h,
          M: z[i].M, gas: gas[i], phase: phase[i], gun: gun[i], bedroht: bedroht[i], schuss: schuss[i],
          treffer: treffer[i], R: geo2[i].R, ata: geo2[i].ata, aa: geo2[i].aa, override: overrideAktiv[i],
          W: W[i], E: z[i].h + z[i].Vm ** 2 / (2 * g), V: z[i].Vm, aq: Lsave[i], dFire: dFire[i], fehler: fehler[i],
          vc: -dot(geo2[i].rel, geo2[i].relv) / geo2[i].R, ataNose: geo2[i].ataNose, typ: fl[i].typ,
        })),
      })
    }
    for (const i of [0, 1]) {
      V[i] = add(V[i], mul(A[i], dt))
      P[i] = add(P[i], mul(V[i], dt))
      W[i] = Math.max(W[i] - fl[i].burn * gas[i] * dt, fl[i].W_leer)
      l[i] = einheit(senkrecht(l[i], einheit(V[i])), einheit(senkrecht(UP, z[i].vh), l[i]))
      Aprev[i] = A[i]
      if (P[i][2] <= 0) { absturz[i] = true; tTot[i] = Math.min(tTot[i], t + dt) }
      if (neuTot[i] && !isFinite(tTot[i])) tTot[i] = t + dt
    }
  }
  const ergebnis = tTot[1] < tTot[0] ? 1 : tTot[0] < tTot[1] ? -1 : 0
  return { ergebnis, tTot, absturz, treffer, frames, tEnde: isFinite(Math.min(...tTot)) ? Math.min(...tTot) : tEnde }
}
