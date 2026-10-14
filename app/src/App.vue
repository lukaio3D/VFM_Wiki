<script setup>
// BFM-Simulator (Konzept v2): 3D-Szene im Zentrum, Inhalt links (einklappbar), Flugdaten und die drei Probleme rechts,
// Zeitleiste mit Energiehöhe unten. Cockpit-Ansicht mit HUD statt Außenkamera. Eigenes Szenario mit Suche nach den besten Strategien.
import { ref, reactive, computed, shallowRef, onMounted, onBeforeUnmount, nextTick } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { simuliere, FT, OVERRIDE } from './sim/physik.js'
import { SZENARIEN, KATEGORIEN, OPTIONEN } from './sim/szenarien.js'
import { jetModell, silhouettePfad } from './sim/modelle.js'
import { dreiProbleme, kurvenkreis, ps, modusText, schubText, zahl } from './sim/lage.js'
import { zeichneHud } from './sim/hud.js'
import { VORLAGEN, neueLage, lageZuGeo, besteStrategien } from './sim/editor.js'

// Das Wiki liegt neben der App auf derselben Seite (GitHub Pages bzw. lokal über den Wiki-Server)
const WIKI = '/VFM_Wiki'
const DATEN = import.meta.env.BASE_URL + 'data/'
const JETS = ['T-15', 'T-16', 'T-18']
const FARBE = [0x4c9aff, 0xff8a3d]
const GEIST_FARBE = [0xa9d0ff, 0xffc8a0]
const SKALA = 100
const STD = { wende: 1, ebene: 0, v_ziel: 440, lag: 0, alpha_kampf: 26, merge_ab: 0, override: 0 }
const KAMERA_AUSSEN = [['aussen', 'Außen'], ['hinter', 'Hinter mir'], ['oben', 'Draufsicht'], ['seite', 'Seite']]
const KAMERA_COCKPIT = [['cockpit', 'Cockpit Du'], ['cockpit-b', 'Cockpit Bandit']]
const EBENEN = [['lift', 'Lift Vector', '#7CF5A8'], ['bubble', 'Bubble', '#7CF5A8'], ['kreise', 'Kurvenkreise', '#C9D5E1'], ['geist', 'Geist', '#A9D0FF']]
const SEITEN = [['sa', 'Du', 'a'], ['sb', 'Bandit', 'b']]

const modell = shallowRef(null)
const fehler = ref('')
const szenarioId = ref('erster-turn')
const eigen = ref(false)
const szenario = computed(() => eigen.value ? null : SZENARIEN.find(s => s.id === szenarioId.value))
const cfg = reactive({ a: 'T-16', b: 'T-18', sa: { ...STD }, sb: { ...STD }, geo: {}, vergleich: [] })
const lage = reactive(neueLage('ranked'))
const ergebnis = shallowRef(null)
const geister = shallowRef([])
const t = ref(0)
const laeuft = ref(false)
const richtung = ref(1)
const tempo = ref(0.5)
const kamera = ref('aussen')
const eb = reactive({ lift: true, bubble: true, kreise: true, geist: true })
const navOffen = ref(false)
const panel = ref('daten')
const lektionOffen = ref(true)
const gross = ref(true)
const halt = reactive({ zeit: null, offen: false, beantwortet: false, fb: '' })
const suche = reactive({ laeuft: false, fortschritt: 0, ergebnis: null })

const buehne = ref(null)
const hudCanvas = ref(null)
const diagramm = ref(null)

const eigeneSeite = computed(() => kamera.value === 'cockpit-b' ? 1 : 0)
const cockpit = computed(() => kamera.value.startsWith('cockpit'))
const tEnde = computed(() => ergebnis.value ? ergebnis.value.frames[ergebnis.value.frames.length - 1].t : 0)

// ------------------------------------------------------------------ Zustand zur Zeit t (zwischen Frames interpoliert)
const lerpV = (a, b, f) => [a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f, a[2] + (b[2] - a[2]) * f]
const einh = v => { const n = Math.hypot(v[0], v[1], v[2]) || 1; return [v[0] / n, v[1] / n, v[2] / n] }
function zustand(r, tt) {
  const fr = r.frames, dtf = fr[1] ? fr[1].t - fr[0].t : 0.08
  const x = Math.min(fr.length - 1, Math.max(0, tt / dtf)), k = Math.floor(x), f = x - k
  const a = fr[k], b = fr[Math.min(k + 1, fr.length - 1)]
  return {
    t: tt, k, j: [0, 1].map(i => {
      const p = a.j[i], q = b.j[i]
      return { ...p, P: lerpV(p.P, q.P, f), vh: einh(lerpV(p.vh, q.vh, f)), l: einh(lerpV(p.l, q.l, f)), alpha: p.alpha + (q.alpha - p.alpha) * f,
        n: p.n + (q.n - p.n) * f, kias: p.kias + (q.kias - p.kias) * f, h: p.h + (q.h - p.h) * f, E: p.E + (q.E - p.E) * f, aq: lerpV(p.aq, q.aq, f) }
    }),
  }
}
const jetzt = computed(() => ergebnis.value ? zustand(ergebnis.value, t.value) : null)
const probleme = computed(() => jetzt.value ? dreiProbleme(jetzt.value, eigeneSeite.value) : [])

// ------------------------------------------------------------------ Laden und Rechnen
function haltZuruecksetzen() { Object.assign(halt, { zeit: null, offen: false, beantwortet: false, fb: '' }) }

function szenarioLaden(id) {
  const s = SZENARIEN.find(x => x.id === id)
  if (!s) return
  szenarioId.value = id; eigen.value = false; panel.value = 'daten'
  cfg.a = s.a; cfg.b = s.b; cfg.sa = { ...STD, ...s.sa }; cfg.sb = { ...STD, ...s.sb }
  cfg.geo = s.geo.lage ? lageZuGeo({ ...neueLage(s.geo.lage), ...s.geo, a: s.a, b: s.b }) : { ...s.geo }
  cfg.vergleich = (s.vergleich || []).map(v => ({ sa: { ...STD, ...v.sa }, sb: { ...STD, ...(v.sb || s.sb) } }))
  haltZuruecksetzen()
  kameraReset = true
  rechne(true)
  if (s.halt) {
    const f = ergebnis.value.frames.find(fr => fr.j[0].phase >= 1)
    halt.zeit = f ? f.t : null
    zeichneDiagramm()
  }
  if (typeof history !== 'undefined') history.replaceState(null, '', `?szenario=${id}`)
}

function rechne(vonVorn = false) {
  if (!modell.value) return
  ergebnis.value = simuliere(modell.value, cfg.a, cfg.b, cfg.sa, cfg.sb, cfg.geo)
  geister.value = cfg.vergleich.slice(0, 2).map(v => simuliere(modell.value, cfg.a, cfg.b, v.sa, v.sb, cfg.geo))
  if (vonVorn) { t.value = 0; laeuft.value = true; richtung.value = 1 }
  t.value = Math.min(t.value, tEnde.value)
  setzeModelle()
  baueSpuren()
  zeichneDiagramm()
}

function antworte(a) {
  const richtig = szenario.value.halt.antworten.find(x => x.richtig)
  halt.fb = a.fb; halt.beantwortet = true; halt.offen = false
  cfg.sa = { ...STD, ...a.s }
  cfg.vergleich = a.richtig ? [] : [{ sa: { ...STD, ...richtig.s }, sb: { ...cfg.sb } }]
  rechne(false)
  laeuft.value = true; richtung.value = 1
}

function eigenesSzenario() {
  eigen.value = true; panel.value = 'editor'; navOffen.value = false
  lageAnwenden()
}
function lageAnwenden(vonVorn = true) {
  cfg.a = lage.a; cfg.b = lage.b; cfg.geo = lageZuGeo(lage); cfg.vergleich = []
  haltZuruecksetzen()
  kameraReset = true
  rechne(vonVorn)
}
function vorlageWaehlen(id) {
  Object.assign(lage, { ...neueLage(id), a: lage.a, b: lage.b, hoehe_ft: lage.hoehe_ft, fuel: lage.fuel })
  suche.ergebnis = null
  lageAnwenden()
}
async function sucheStarten() {
  if (suche.laeuft) return
  suche.laeuft = true; suche.fortschritt = 0; suche.ergebnis = null
  suche.ergebnis = await besteStrategien(modell.value, { ...lage }, p => { suche.fortschritt = p })
  suche.laeuft = false
}
function ergebnisAbspielen(k) {
  const top = suche.ergebnis.top
  cfg.sa = { ...STD, ...top[k].s }; cfg.sb = { ...STD, ...top[k].antwort }
  cfg.vergleich = top.filter((_, i) => i !== k).map(x => ({ sa: { ...STD, ...x.s }, sb: { ...STD, ...x.antwort } }))
  rechne(true)
}

function strategieName(s, jet, merge = true) {
  const w = merge ? { 1: 'hin', '-1': 'weg', 0: 'durch' }[s.wende] + ' · ' : ''
  const e = { 60: 'steil hoch', 25: 'hoch', 0: 'flach', '-30': 'tief' }[s.ebene] ?? `${s.ebene}°`
  return `${w}${e} · ${s.v_ziel} KIAS · ${s.lag > 0 ? 'Lag' : 'Pure'}` + (jet === 'T-18' && s.alpha_kampf === 35 ? ' · α 35°' : '') + (s.override ? ' · Override' : '')
}

// ------------------------------------------------------------------ Three.js
let renderer, scene, cam, controls, raf, uhr, kameraReset = true
const ziel = new THREE.Vector3()
let jetObj = [null, null], geistObj = [], spuren = [], geistSpuren = [], liftPfeile = [], kreise = [], bubble, gegnerKreis, schussLinie

const v3 = p => new THREE.Vector3(p[0] / SKALA, p[2] / SKALA, -p[1] / SKALA)
const r3 = p => new THREE.Vector3(p[0], p[2], -p[1])

function linie(n, opacity = 1) {
  const geo = new THREE.BufferGeometry()
  geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(n * 3), 3))
  geo.setAttribute('color', new THREE.BufferAttribute(new Float32Array(n * 3), 3))
  const l = new THREE.Line(geo, new THREE.LineBasicMaterial({ vertexColors: true, transparent: opacity < 1, opacity }))
  l.frustumCulled = false
  return l
}
function fuelleSpur(l, frames, i, farbe, nachG) {
  const pos = l.geometry.attributes.position.array, col = l.geometry.attributes.color.array
  const basis = new THREE.Color(farbe), gelb = new THREE.Color(0xffd166), c = new THREE.Color()
  const n = Math.min(frames.length, pos.length / 3)
  for (let k = 0; k < n; k++) {
    const p = v3(frames[k].j[i].P)
    pos[k * 3] = p.x; pos[k * 3 + 1] = p.y; pos[k * 3 + 2] = p.z
    c.copy(basis).lerp(gelb, nachG ? Math.min(1, Math.max(0, (frames[k].j[i].n - 5) / 4)) : 0)
    col[k * 3] = c.r; col[k * 3 + 1] = c.g; col[k * 3 + 2] = c.b
  }
  l.geometry.attributes.position.needsUpdate = true
  l.geometry.attributes.color.needsUpdate = true
}
function kreisLinie(farbe) {
  const pts = []
  for (let k = 0; k <= 64; k++) pts.push(new THREE.Vector3(Math.cos(k / 64 * Math.PI * 2), Math.sin(k / 64 * Math.PI * 2), 0))
  const l = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), new THREE.LineDashedMaterial({ color: farbe, dashSize: 0.06, gapSize: 0.05, transparent: true, opacity: 0.75 }))
  l.computeLineDistances(); l.frustumCulled = false
  return l
}

function baueSzene() {
  renderer = new THREE.WebGLRenderer({ antialias: true })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  buehne.value.prepend(renderer.domElement)
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x0e1621)
  scene.fog = new THREE.Fog(0x0e1621, 250, 900)
  cam = new THREE.PerspectiveCamera(55, 1, 0.005, 3000)
  controls = new OrbitControls(cam, renderer.domElement)
  controls.enableDamping = true
  scene.add(new THREE.HemisphereLight(0xdbeafe, 0x1e293b, 1.3))
  const sonne = new THREE.DirectionalLight(0xffffff, 1.6); sonne.position.set(50, 100, 30); scene.add(sonne)
  scene.add(new THREE.GridHelper(3000, 300, 0x1f2d3a, 0x16212c))
  const deck = new THREE.Mesh(new THREE.PlaneGeometry(3000, 3000), new THREE.MeshBasicMaterial({ color: 0xffd166, transparent: true, opacity: 0.035, side: THREE.DoubleSide, depthWrite: false }))
  deck.rotation.x = -Math.PI / 2; deck.position.y = 3000 * FT / SKALA; scene.add(deck)
  for (const i of [0, 1]) {
    const s = linie(4000); scene.add(s); spuren.push(s)
    const lp = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(), 3, 0x7cf5a8, 0.8, 0.5); scene.add(lp); liftPfeile.push(lp)
    const k = kreisLinie(i ? 0xff8a3d : 0x4c9aff); scene.add(k); kreise.push(k)
  }
  for (let g = 0; g < 4; g++) { const s = linie(4000, 0.4); scene.add(s); geistSpuren.push(s) }
  bubble = new THREE.Mesh(new THREE.CircleGeometry(1, 48, Math.PI, Math.PI), new THREE.MeshBasicMaterial({ color: 0x7cf5a8, transparent: true, opacity: 0.06, side: THREE.DoubleSide, depthWrite: false }))
  gegnerKreis = new THREE.Mesh(new THREE.CircleGeometry(1, 48), new THREE.MeshBasicMaterial({ color: 0xff8a3d, transparent: true, opacity: 0.07, side: THREE.DoubleSide, depthWrite: false }))
  scene.add(bubble); scene.add(gegnerKreis)
  schussLinie = new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(), new THREE.Vector3(1, 0, 0)]), new THREE.LineBasicMaterial({ color: 0xffd166 }))
  schussLinie.frustumCulled = false; scene.add(schussLinie)
  groesse()
  window.addEventListener('resize', groesse)
  uhr = performance.now()
  schleife()
}

let modellTypen = [null, null], geistTypen = ''
function setzeModelle() {
  if (!scene) return
  for (const i of [0, 1]) {
    const typ = i ? cfg.b : cfg.a
    if (modellTypen[i] === typ) continue
    if (jetObj[i]) scene.remove(jetObj[i])
    jetObj[i] = jetModell(typ, FARBE[i]); scene.add(jetObj[i]); modellTypen[i] = typ
  }
  const gt = `${cfg.a}|${cfg.b}|${geister.value.length}`
  if (gt !== geistTypen) {
    geistObj.forEach(o => scene.remove(o)); geistObj = []
    geister.value.forEach(() => { for (const i of [0, 1]) { const o = jetModell(i ? cfg.b : cfg.a, GEIST_FARBE[i], { transparent: true }); scene.add(o); geistObj.push(o) } })
    geistTypen = gt
  }
}
function baueSpuren() {
  if (!scene || !ergebnis.value) return
  for (const i of [0, 1]) fuelleSpur(spuren[i], ergebnis.value.frames, i, FARBE[i], true)
  geistSpuren.forEach(s => (s.visible = false))
  geister.value.forEach((r, g) => { for (const i of [0, 1]) fuelleSpur(geistSpuren[g * 2 + i], r.frames, i, GEIST_FARBE[i], false) })
}

function koerper(j) {
  const vh = r3(j.vh), l = r3(j.l), a = j.alpha * Math.PI / 180
  return {
    nase: vh.clone().multiplyScalar(Math.cos(a)).addScaledVector(l, Math.sin(a)).normalize(),
    oben: l.clone().multiplyScalar(Math.cos(a)).addScaledVector(vh, -Math.sin(a)).normalize(),
  }
}
function setzeJet(obj, j, faktor) {
  const { nase, oben } = koerper(j)
  obj.position.copy(v3(j.P))
  obj.quaternion.setFromRotationMatrix(new THREE.Matrix4().makeBasis(nase, oben, new THREE.Vector3().crossVectors(nase, oben)))
  obj.scale.setScalar(faktor / SKALA)
}
function setzeKreis(obj, k, mitte, radius) {
  const e1 = r3(k.e1).normalize(), e2 = r3(k.e2).normalize(), n = new THREE.Vector3().crossVectors(e1, e2)
  obj.position.copy(v3(mitte))
  obj.quaternion.setFromRotationMatrix(new THREE.Matrix4().makeBasis(e1, e2, n))
  obj.scale.setScalar(radius / SKALA)
}

function aktualisiere() {
  const z = jetzt.value
  if (!z || !scene) return
  const eigen0 = eigeneSeite.value, im = cockpit.value
  const abstandM = Math.hypot(z.j[0].P[0] - z.j[1].P[0], z.j[0].P[1] - z.j[1].P[1], z.j[0].P[2] - z.j[1].P[2])
  const faktorAussen = gross.value ? Math.min(40, Math.max(8, abstandM / 110)) * (kamera.value === 'oben' ? 1.3 : 1) : 1
  for (const i of [0, 1]) {
    const j = z.j[i]
    const faktor = im ? (i === eigen0 ? 1 : 3) : (kamera.value === 'hinter' && i === 0 ? 1.5 : faktorAussen)
    setzeJet(jetObj[i], j, faktor)
    jetObj[i].visible = !(im && i === eigen0)
    spuren[i].geometry.setDrawRange(0, z.k + 1)
    liftPfeile[i].visible = eb.lift && !(im && i === eigen0)
    liftPfeile[i].position.copy(v3(j.P))
    liftPfeile[i].setDirection(r3(j.l).normalize())
    const s = Math.max(faktor, 1.5) * 17 / SKALA
    liftPfeile[i].setLength(s * (0.4 + j.n / 9 * 0.8), s * 0.22, s * 0.14)
    const kk = kurvenkreis(j)
    kreise[i].visible = eb.kreise && !!kk
    if (kk) setzeKreis(kreise[i], kk, kk.C, kk.R)
  }
  const sch = z.j[0].schuss ? 0 : z.j[1].schuss ? 1 : -1
  schussLinie.visible = sch >= 0
  if (sch >= 0) schussLinie.geometry.setFromPoints([v3(z.j[sch].P), v3(z.j[1 - sch].P)])

  // Bubble um den Gegner der eigenen Seite: hinter seiner 3/9-Linie; sein Kurvenkreis orange darüber
  const o = z.j[1 - eigen0], ko = kurvenkreis(o)
  const zeigeBubble = eb.bubble && !!ko && o.phase >= 1
  bubble.visible = zeigeBubble; gegnerKreis.visible = zeigeBubble
  if (zeigeBubble) {
    setzeKreis(bubble, ko, o.P, Math.min(3000, Math.max(800, 1.8 * ko.R)))
    setzeKreis(gegnerKreis, ko, ko.C, ko.R)
  }

  geister.value.forEach((r, g) => {
    const zg = zustand(r, Math.min(t.value, r.frames[r.frames.length - 1].t))
    for (const i of [0, 1]) {
      const obj = geistObj[g * 2 + i]
      if (!obj) continue
      obj.visible = eb.geist && !im
      setzeJet(obj, zg.j[i], faktorAussen)
      geistSpuren[g * 2 + i].visible = eb.geist
      geistSpuren[g * 2 + i].geometry.setDrawRange(0, zg.k + 1)
    }
  })

  // Kamera
  const pa = v3(z.j[0].P), pb = v3(z.j[1].P), mitte = pa.clone().add(pb).multiplyScalar(0.5)
  const dist = Math.max(pa.distanceTo(pb), 25)
  controls.enabled = kamera.value === 'aussen'
  cam.fov = im ? 70 : 55
  if (kamera.value === 'aussen') {
    if (kameraReset) { ziel.copy(mitte); cam.position.copy(mitte).add(new THREE.Vector3(dist * 0.6, dist * 0.45, dist * 0.8)); kameraReset = false }
    cam.position.add(mitte.clone().sub(ziel)); ziel.copy(mitte); controls.target.copy(mitte)
    cam.up.set(0, 1, 0)
  } else if (kamera.value === 'hinter') {
    const j = z.j[0], own = v3(j.P), vh = r3(j.vh), up = r3(j.l)
    cam.position.copy(own).addScaledVector(vh, -1.2).addScaledVector(up, 0.35)
    cam.up.copy(up); cam.lookAt(own.clone().addScaledVector(vh, 4))
  } else if (kamera.value === 'oben') {
    cam.position.set(mitte.x, mitte.y + dist * 1.5 + 15, mitte.z + 0.001); cam.up.set(0, 0, -1); cam.lookAt(mitte)
  } else if (kamera.value === 'seite') {
    const los = pb.clone().sub(pa); los.y = 0
    let quer = new THREE.Vector3(-los.z, 0, los.x)
    quer = quer.lengthSq() < 1e-6 ? new THREE.Vector3(1, 0, 0) : quer.normalize()
    cam.position.copy(mitte).addScaledVector(quer, dist * 1.4 + 15); cam.up.set(0, 1, 0); cam.lookAt(mitte)
  } else {
    const j = z.j[eigen0], own = v3(j.P), { nase, oben } = koerper(j)
    cam.position.copy(own).addScaledVector(oben, 0.012)
    cam.up.copy(oben); cam.lookAt(own.clone().addScaledVector(nase, 10))
  }
  cam.updateProjectionMatrix()
}

function zeichneHudJetzt() {
  const c = hudCanvas.value
  if (!c) return
  const dpr = window.devicePixelRatio || 1
  const ctx = c.getContext('2d'), w = c.width / dpr, h = c.height / dpr
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  if (!cockpit.value || !jetzt.value) { ctx.clearRect(0, 0, w, h); return }
  const i = eigeneSeite.value, j = jetzt.value.j[i]
  cam.updateMatrixWorld()
  zeichneHud(ctx, w, h, cam, jetzt.value, i, v3, { schub: schubText(j.gas), ps: ps(ergebnis.value.frames, jetzt.value.k, i) })
}

function groesse() {
  if (!renderer) return
  const w = buehne.value.clientWidth, h = buehne.value.clientHeight
  renderer.setSize(w, h)
  cam.aspect = w / h; cam.updateProjectionMatrix()
  const dpr = window.devicePixelRatio || 1
  if (hudCanvas.value) { hudCanvas.value.width = w * dpr; hudCanvas.value.height = h * dpr }
  zeichneDiagramm()
}

function schleife() {
  raf = requestAnimationFrame(schleife)
  const ms = performance.now(), d = Math.min(0.1, (ms - uhr) / 1000); uhr = ms
  if (laeuft.value && ergebnis.value) {
    const vorher = t.value
    let neu = vorher + d * tempo.value * richtung.value
    if (halt.zeit != null && !halt.beantwortet && richtung.value > 0 && vorher < halt.zeit && neu >= halt.zeit) {
      neu = halt.zeit; laeuft.value = false; halt.offen = true
    }
    if (neu >= tEnde.value) { neu = tEnde.value; laeuft.value = false }
    if (neu <= 0) { neu = 0; laeuft.value = false }
    t.value = neu
  }
  aktualisiere()
  if (kamera.value === 'aussen') controls.update()
  renderer.render(scene, cam)
  zeichneHudJetzt()
  zeichneCursor()
}

// ------------------------------------------------------------------ Zeitleiste mit Energiehöhe
let diagrammBild = null
function zeichneDiagramm() {
  const c = diagramm.value, r = ergebnis.value
  if (!c || !r) return
  const w = c.clientWidth, h = c.clientHeight, dpr = window.devicePixelRatio || 1
  if (!w || !h) return
  c.width = w * dpr; c.height = h * dpr
  const x = c.getContext('2d'); x.setTransform(dpr, 0, 0, dpr, 0, 0); x.clearRect(0, 0, w, h)
  const T = Math.max(tEnde.value, 1)
  let lo = Infinity, hi = -Infinity
  for (const res of [r, ...geister.value]) for (const f of res.frames) for (const j of f.j) { lo = Math.min(lo, j.E); hi = Math.max(hi, j.E) }
  const pad = (hi - lo) * 0.1 + 50; lo -= pad; hi += pad
  const yv = e => 16 + (h - 20) * (1 - (e - lo) / (hi - lo))
  x.strokeStyle = 'rgba(147,164,182,0.15)'; x.lineWidth = 1
  for (let k = 1; k < 4; k++) { const yy = 16 + (h - 20) * k / 4; x.beginPath(); x.moveTo(0, yy); x.lineTo(w, yy); x.stroke() }
  const reihen = [[r, 0, '#4C9AFF', 2], [r, 1, '#FF8A3D', 2]]
  geister.value.forEach(g => { reihen.push([g, 0, 'rgba(169,208,255,0.55)', 1.2]); reihen.push([g, 1, 'rgba(255,200,160,0.4)', 1.2]) })
  for (const [res, i, farbe, lw] of reihen) {
    x.strokeStyle = farbe; x.lineWidth = lw; x.beginPath()
    res.frames.forEach((f, k) => { const px = f.t / T * w, py = yv(f.j[i].E); k ? x.lineTo(px, py) : x.moveTo(px, py) })
    x.stroke()
  }
  x.font = '11px "IBM Plex Mono", monospace'
  let vorher = r.frames[0].j[0].phase
  for (const f of r.frames) {
    const p = f.j[0].phase
    if (p === 1 && vorher !== 1) { const px = f.t / T * w; x.fillStyle = 'rgba(147,164,182,0.7)'; x.fillRect(px, 0, 1, h); x.fillText('Pass', px + 3, 10) }
    vorher = p
    for (const i of [0, 1]) if (f.j[i].schuss) { x.fillStyle = i ? '#FF8A3D' : '#4C9AFF'; x.fillRect(f.t / T * w - 1, h - (i ? 5 : 10), 2, 5) }
  }
  if (halt.zeit != null) { x.fillStyle = '#FFD166'; x.fillRect(halt.zeit / T * w - 1, 0, 2, h) }
  if (r.ergebnis !== 0) { x.fillStyle = r.ergebnis > 0 ? '#8CC2FF' : '#FFB27F'; x.textAlign = 'right'; x.fillText('Abschuss', w - 4, 10); x.textAlign = 'left' }
  diagrammBild = x.getImageData(0, 0, c.width, c.height)
}
function zeichneCursor() {
  const c = diagramm.value
  if (!c || !diagrammBild || diagrammBild.width !== c.width) return
  const x = c.getContext('2d')
  x.putImageData(diagrammBild, 0, 0)
  const dpr = window.devicePixelRatio || 1, w = c.width / dpr
  x.setTransform(dpr, 0, 0, dpr, 0, 0)
  x.fillStyle = '#E6EDF3'; x.fillRect(t.value / Math.max(tEnde.value, 1) * w - 0.75, 0, 1.5, c.height / dpr)
}
let ziehen = false
function suchen(e) {
  const rect = diagramm.value.getBoundingClientRect()
  t.value = Math.min(tEnde.value, Math.max(0, (e.clientX - rect.left) / rect.width * tEnde.value))
  laeuft.value = false
}
const zeitDown = e => { ziehen = true; suchen(e) }
const zeitMove = e => { if (ziehen) suchen(e) }
const zeitUp = () => { ziehen = false }

function spiele(r) {
  if (laeuft.value && richtung.value === r) { laeuft.value = false; return }
  richtung.value = r
  if (r > 0 && t.value >= tEnde.value) t.value = 0
  if (r < 0 && t.value <= 0) t.value = tEnde.value
  laeuft.value = true
}
function springe(d) { t.value = Math.min(tEnde.value, Math.max(0, t.value + d)); laeuft.value = false }
function waehleKamera(k) { kamera.value = k; if (k === 'aussen') kameraReset = true }

function tasten(e) {
  if (e.target.closest && e.target.closest('input, select, textarea')) return
  if (e.code === 'Space') { spiele(1); e.preventDefault() }
  if (e.code === 'ArrowRight') springe(1)
  if (e.code === 'ArrowLeft') springe(-1)
}

// ------------------------------------------------------------------ Anzeigen
const ergebnisText = computed(() => {
  const r = ergebnis.value
  if (!r || t.value < tEnde.value - 0.01 || r.ergebnis === 0) return ''
  return `${r.ergebnis > 0 ? 'Abschuss durch Blau' : 'Abschuss durch Orange'} nach ${zahl(Math.min(...r.tTot), 1)} s`
})
function karte(i) {
  const z = jetzt.value
  if (!z || !modell.value) return null
  const j = z.j[i], typ = i ? cfg.b : cfg.a, fl = modell.value.jets[typ]
  const aMax = typ === 'T-18' ? (cfg[i ? 'sb' : 'sa'].override ? OVERRIDE['T-18'].alpha : 35) : fl.alpha_lim
  return {
    typ, rolle: i === eigeneSeite.value ? 'Du' : 'Bandit', modus: modusText(j),
    kias: zahl(j.kias), alt: zahl(j.h / FT), e: zahl(j.E / FT), ps: ps(ergebnis.value.frames, z.k, i),
    g: j.n, gProz: Math.min(100, Math.max(0, j.n / 9 * 100)), alpha: j.alpha,
    aProz: Math.min(100, Math.max(0, j.alpha / aMax * 100)), aMarke: Math.min(100, fl.alpha_lim / aMax * 100),
    fuel: (j.W - fl.W_leer) / (fl.W_voll - fl.W_leer) * 100, schub: schubText(j.gas),
  }
}
const karten = computed(() => [0, 1].map(karte))
const nachKategorie = computed(() => KATEGORIEN.map(k => ({ name: k, liste: SZENARIEN.filter(s => s.kategorie === k) })))
const wikiLink = computed(() => WIKI + (szenario.value?.wiki || '/flugzeuge/simulation'))

// ------------------------------------------------------------------ Lebenszyklus
onMounted(async () => {
  try {
    modell.value = await fetch(DATEN + 'modell.json').then(r => r.json())
    await nextTick()
    baueSzene()
    const q = new URLSearchParams(location.search).get('szenario')
    szenarioLaden(SZENARIEN.some(s => s.id === q) ? q : 'erster-turn')
    window.addEventListener('keydown', tasten)
    window.addEventListener('pointerup', zeitUp)
  } catch (e) { fehler.value = 'Simulator konnte nicht geladen werden: ' + e.message }
})
onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  window.removeEventListener('resize', groesse); window.removeEventListener('keydown', tasten); window.removeEventListener('pointerup', zeitUp)
  renderer?.dispose()
})
</script>

<template>
  <div class="bfm">
    <p v-if="fehler" class="fehler">{{ fehler }}</p>
    <header class="kopf">
      <a class="logo" :href="WIKI + '/'" title="Zum Wiki">VFM FLIGHT ACADEMY · BFM-SIMULATOR</a>
      <span class="titel">{{ eigen ? 'Eigenes Szenario' : szenario?.titel }}</span>
      <a class="knopf" :href="wikiLink" target="_blank" rel="noopener">Im Wiki lesen</a>
      <button class="knopf primaer" @click="eigenesSzenario">Eigenes Szenario</button>
    </header>

    <div class="koerper">
      <nav class="inhalt" :class="{ offen: navOffen }" aria-label="Szenarien">
        <button class="icon" @click="navOffen = !navOffen" :aria-label="navOffen ? 'Inhalt einklappen' : 'Inhalt ausklappen'" :aria-expanded="navOffen">
          <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 4 H16 M2 9 H16 M2 14 H16" stroke="currentColor" stroke-width="1.8" /></svg>
        </button>
        <div v-if="navOffen" class="liste">
          <div v-for="k in nachKategorie" :key="k.name" class="gruppe">
            <div class="gruppe-titel">{{ k.name }}</div>
            <button v-for="s in k.liste" :key="s.id" class="eintrag" :class="{ aktiv: !eigen && s.id === szenarioId }" @click="szenarioLaden(s.id); navOffen = false">{{ s.titel }}</button>
          </div>
          <div class="gruppe">
            <div class="gruppe-titel">Selbst</div>
            <button class="eintrag" :class="{ aktiv: eigen }" @click="eigenesSzenario">Eigenes Szenario</button>
          </div>
        </div>
      </nav>

      <main class="mitte">
        <div ref="buehne" class="buehne">
          <canvas ref="hudCanvas" class="hud" v-show="cockpit"></canvas>
          <div class="chip-paarung">
            <svg width="20" height="26" viewBox="-70 -5 140 205" aria-hidden="true"><path :d="silhouettePfad(cfg.a)" fill="#4C9AFF" /></svg>
            <span>Du</span><span class="gedimmt">gegen</span>
            <svg width="20" height="26" viewBox="-70 -5 140 205" aria-hidden="true"><path :d="silhouettePfad(cfg.b)" fill="#FF8A3D" /></svg>
            <span>Bandit</span>
          </div>
          <div class="kameras">
            <div class="gruppe-knoepfe" role="group" aria-label="Außenkamera">
              <button v-for="[k, n] in KAMERA_AUSSEN" :key="k" :class="{ aktiv: kamera === k }" @click="waehleKamera(k)">{{ n }}</button>
            </div>
            <div class="gruppe-knoepfe" role="group" aria-label="Cockpit">
              <button v-for="[k, n] in KAMERA_COCKPIT" :key="k" :class="{ aktiv: kamera === k }" @click="waehleKamera(k)">{{ n }}</button>
            </div>
          </div>
          <div class="ebenen">
            <button v-for="[k, n, f] in EBENEN" :key="k" :class="{ an: eb[k] }" :aria-pressed="eb[k]" @click="eb[k] = !eb[k]">
              <span class="punkt" :style="{ background: eb[k] ? f : 'transparent', borderColor: f }"></span>{{ n }}
            </button>
            <button :class="{ an: gross }" :aria-pressed="gross" @click="gross = !gross"><span class="punkt" :style="{ background: gross ? '#C9D5E1' : 'transparent', borderColor: '#C9D5E1' }"></span>Jets groß</button>
          </div>
          <div v-if="ergebnisText" class="ergebnis">{{ ergebnisText }}</div>
          <div v-if="halt.offen && szenario?.halt" class="halt">
            <span class="halt-frage">{{ zahl(halt.zeit, 1) }} s · {{ szenario.halt.frage }}</span>
            <button v-for="a in szenario.halt.antworten" :key="a.text" @click="antworte(a)">{{ a.text }}</button>
          </div>
          <div v-else-if="halt.beantwortet" class="halt klein"><span>{{ halt.fb }}</span></div>
        </div>

        <section class="zeitleiste" aria-label="Zeitleiste">
          <div class="steuerung">
            <button class="icon" aria-label="Zum Anfang" @click="t = 0; laeuft = false"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 2 V12 M12 2 L4 7 L12 12 Z" fill="currentColor" stroke="currentColor" stroke-width="1.5" /></svg></button>
            <button class="icon" :class="{ an: laeuft && richtung < 0 }" aria-label="Rückwärts abspielen" @click="spiele(-1)"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M11 1.5 L2 7 L11 12.5 Z" fill="currentColor" /></svg></button>
            <button class="knopf" @click="springe(-1)">−1 s</button>
            <button class="play" :aria-label="laeuft && richtung > 0 ? 'Pause' : 'Abspielen'" @click="spiele(1)">
              <svg v-if="laeuft && richtung > 0" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M3 2 H6 V12 H3 Z M8 2 H11 V12 H8 Z" fill="currentColor" /></svg>
              <svg v-else width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M3 1.5 L12 7 L3 12.5 Z" fill="currentColor" /></svg>
            </button>
            <button class="knopf" @click="springe(1)">+1 s</button>
            <button class="icon" aria-label="Zum Ende" @click="t = tEnde; laeuft = false"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M12 2 V12 M2 2 L10 7 L2 12 Z" fill="currentColor" stroke="currentColor" stroke-width="1.5" /></svg></button>
            <label class="tempo">Tempo
              <select v-model.number="tempo"><option :value="0.25">¼×</option><option :value="0.5">½×</option><option :value="1">1×</option><option :value="2">2×</option><option :value="4">4×</option></select>
            </label>
            <span class="flex"></span>
            <span class="zeit">{{ zahl(t, 1) }} / {{ zahl(tEnde, 1) }} s</span>
          </div>
          <div class="diagramm-kopf"><span>Energiehöhe (Höhe + v²/2g)</span>
            <span v-if="jetzt" class="mono"><span style="color:#8CC2FF">{{ zahl(jetzt.j[0].E / FT) }} ft</span> · <span style="color:#FFB27F">{{ zahl(jetzt.j[1].E / FT) }} ft</span></span>
          </div>
          <canvas ref="diagramm" class="diagramm" @pointerdown="zeitDown" @pointermove="zeitMove"></canvas>
        </section>
      </main>

      <aside class="daten" aria-label="Flugdaten">
        <div class="tabs" role="tablist">
          <button role="tab" :aria-selected="panel === 'daten'" :class="{ aktiv: panel === 'daten' }" @click="panel = 'daten'">Flugdaten</button>
          <button role="tab" :aria-selected="panel === 'editor'" :class="{ aktiv: panel === 'editor' }" @click="eigen ? (panel = 'editor') : eigenesSzenario()">Szenario</button>
        </div>

        <template v-if="panel === 'daten'">
          <template v-for="(k, i) in karten" :key="i">
            <div v-if="k && cockpit && i === eigeneSeite" class="karte" :class="i ? 'orange' : 'blau'">
              <div class="karte-kopf"><span class="name">{{ k.typ }} · {{ k.rolle }}</span><span class="gedimmt">Werte im HUD</span></div>
            </div>
            <div v-else-if="k" class="karte" :class="i ? 'orange' : 'blau'">
              <div class="karte-kopf">
                <span class="name"><svg width="14" height="18" viewBox="-70 -5 140 205" aria-hidden="true"><path :d="silhouettePfad(k.typ)" :fill="i ? '#FF8A3D' : '#4C9AFF'" /></svg>{{ k.typ }} · {{ k.rolle }}</span>
                <span class="gedimmt">{{ k.modus }}</span>
              </div>
              <div class="werte3">
                <div><div class="lbl">KIAS</div><div class="gross">{{ k.kias }}</div></div>
                <div><div class="lbl">HÖHE ft</div><div class="gross">{{ k.alt }}</div></div>
                <div><div class="lbl">ENERGIE ft</div><div class="gross">{{ k.e }}</div></div>
              </div>
              <div class="balken"><span class="lbl">G</span><div class="spur"><div class="fuell" :style="{ width: k.gProz + '%', background: i ? '#FF8A3D' : '#4C9AFF' }"></div></div><span class="mono">{{ zahl(k.g, 1) }}</span></div>
              <div class="balken"><span class="lbl">α</span><div class="spur"><div class="fuell" :style="{ width: k.aProz + '%', background: i ? '#FF8A3D' : '#4C9AFF' }"></div><div class="marke" :style="{ left: k.aMarke + '%' }"></div></div><span class="mono">{{ zahl(k.alpha) }}°</span></div>
              <div class="balken"><span class="lbl">Fuel</span><div class="spur"><div class="fuell" :style="{ width: k.fuel + '%', background: '#5D7186' }"></div></div><span class="mono">{{ zahl(k.fuel) }} %</span></div>
              <div class="zeile-klein"><span>Schub <b>{{ k.schub }}</b></span><span title="Nicht gemessen, im Modell nicht enthalten">Speedbrake <b>–</b></span><span>Ps <b>{{ k.ps >= 0 ? '+' : '−' }}{{ zahl(Math.abs(k.ps)) }}</b> ft/s</span></div>
            </div>
          </template>

          <div class="karte">
            <div class="karte-kopf"><span class="name">Die drei Probleme</span><span class="gedimmt">aus Sicht {{ eigeneSeite ? 'Bandit' : 'Du' }}</span></div>
            <div v-for="p in probleme" :key="p.name" class="problem">
              <div class="problem-kopf">
                <span class="stufe" :class="p.stufe">{{ p.stufe === 'ok' ? '✓' : '!' }}</span>
                <span class="pname">{{ p.name }}</span>
                <span class="mono wert">{{ p.wert }}</span>
              </div>
              <div class="loesung">{{ p.loesung }}</div>
            </div>
          </div>

          <div v-if="szenario" class="karte lektion">
            <button class="karte-kopf knopf-flach" @click="lektionOffen = !lektionOffen" :aria-expanded="lektionOffen">
              <span class="name">Lektion</span><span class="gedimmt">{{ lektionOffen ? 'einklappen' : 'ausklappen' }}</span>
            </button>
            <p v-if="lektionOffen">{{ szenario.text }}</p>
          </div>
        </template>

        <template v-else>
          <div class="karte">
            <label class="feld">Vorlage
              <select :value="lage.vorlage" @change="vorlageWaehlen($event.target.value)">
                <option v-for="(v, k) in VORLAGEN" :key="k" :value="k">{{ v.name }}</option>
              </select>
            </label>
            <div class="zwei">
              <label class="feld">Du <select v-model="lage.a" @change="lageAnwenden()"><option v-for="j in JETS" :key="j">{{ j }}</option></select></label>
              <label class="feld">Bandit <select v-model="lage.b" @change="lageAnwenden()"><option v-for="j in JETS" :key="j">{{ j }}</option></select></label>
            </div>
            <div class="zwei">
              <label class="feld">Speed Du {{ lage.kiasA }} KIAS<input type="range" min="250" max="600" step="10" v-model.number="lage.kiasA" @change="lageAnwenden()" /></label>
              <label class="feld">Speed Bandit {{ VORLAGEN[lage.vorlage].merge ? lage.kiasA : lage.kiasB }} KIAS<input type="range" min="250" max="600" step="10" v-model.number="lage.kiasB" @change="lageAnwenden()" :disabled="VORLAGEN[lage.vorlage].merge" /></label>
            </div>
            <div class="zwei">
              <label class="feld">Höhe {{ zahl(lage.hoehe_ft) }} ft<input type="range" min="5000" max="20000" step="500" v-model.number="lage.hoehe_ft" @change="lageAnwenden()" /></label>
              <label class="feld">Fuel {{ lage.fuel }} %<input type="range" min="10" max="100" step="5" v-model.number="lage.fuel" @change="lageAnwenden()" /></label>
            </div>
            <label v-if="VORLAGEN[lage.vorlage].merge" class="feld">Seitlicher Versatz {{ zahl(lage.versatz_ft) }} ft<input type="range" min="0" max="4000" step="100" v-model.number="lage.versatz_ft" @change="lageAnwenden()" /></label>
            <template v-else>
              <div class="zwei">
                <label class="feld">Abstand {{ zahl(lage.abstand_ft) }} ft<input type="range" min="1000" max="9000" step="250" v-model.number="lage.abstand_ft" @change="lageAnwenden()" /></label>
                <label class="feld">Peilung {{ lage.peilung }}°<input type="range" min="0" max="350" step="10" v-model.number="lage.peilung" @change="lageAnwenden()" /></label>
              </div>
              <div class="zwei">
                <label class="feld">Kurs Bandit {{ lage.kurs }}°<input type="range" min="0" max="350" step="10" v-model.number="lage.kurs" @change="lageAnwenden()" /></label>
                <label class="feld">Höhe Bandit {{ lage.dh_ft >= 0 ? '+' : '' }}{{ zahl(lage.dh_ft) }} ft<input type="range" min="-4000" max="4000" step="250" v-model.number="lage.dh_ft" @change="lageAnwenden()" /></label>
              </div>
            </template>
          </div>

          <div class="karte">
            <button class="knopf primaer breit" :disabled="suche.laeuft" @click="sucheStarten">{{ suche.laeuft ? `Rechne … ${Math.round(suche.fortschritt * 100)} %` : 'Beste Strategien finden' }}</button>
            <p v-if="!suche.ergebnis && !suche.laeuft" class="gedimmt">Rechnet deine Strategien gegen die Antworten des Bandits und zeigt, was gegen seine stärkste Antwort am besten hält.</p>
            <template v-if="suche.ergebnis">
              <div class="gedimmt">{{ suche.ergebnis.kaempfe }} Kämpfe gerechnet</div>
              <div v-for="(e, k) in suche.ergebnis.top" :key="k" class="treffer">
                <div><b>{{ k + 1 }}.</b> {{ strategieName(e.s, lage.a, VORLAGEN[lage.vorlage].merge) }}</div>
                <div class="gedimmt">gewinnt {{ e.siege }} von {{ e.n }}, verliert {{ e.niederlagen }} · gegen seine beste Antwort: {{ e.antwortErgebnis > 0 ? 'Sieg' : e.antwortErgebnis < 0 ? 'Niederlage' : 'offen' }}</div>
                <button class="knopf" @click="ergebnisAbspielen(k)">Abspielen, die anderen als Geist</button>
              </div>
              <div class="gedimmt">Schwächste Wahl: {{ strategieName(suche.ergebnis.schlechteste.s, lage.a, VORLAGEN[lage.vorlage].merge) }}</div>
            </template>
          </div>

          <details class="karte">
            <summary class="name">Strategien selbst festlegen</summary>
            <div v-for="[seite, label, jetKey] in SEITEN" :key="seite" class="strategie">
              <div class="lbl">{{ label }}</div>
              <label class="feld">Am Pass <select v-model.number="cfg[seite].wende" @change="rechne()"><option v-for="[v, n] in OPTIONEN.wende" :key="v" :value="v">{{ n }}</option></select></label>
              <label class="feld">Ebene <select v-model.number="cfg[seite].ebene" @change="rechne()"><option v-for="[v, n] in OPTIONEN.ebene" :key="v" :value="v">{{ n }}</option></select></label>
              <label class="feld">Kampf-Speed {{ cfg[seite].v_ziel }} KIAS<input type="range" min="280" max="520" step="20" v-model.number="cfg[seite].v_ziel" @change="rechne()" /></label>
              <label class="feld">Verfolgung <select v-model.number="cfg[seite].lag" @change="rechne()"><option v-for="[v, n] in OPTIONEN.lag" :key="v" :value="v">{{ n }}</option></select></label>
              <label class="check"><input type="checkbox" :checked="!!cfg[seite].merge_ab" @change="cfg[seite].merge_ab = $event.target.checked ? 1 : 0; rechne()" /> Nachbrenner bis zum Merge</label>
              <label v-if="cfg[jetKey] === 'T-18'" class="feld">α beim Kurven <select v-model.number="cfg[seite].alpha_kampf" @change="rechne()"><option :value="26">26°</option><option :value="35">35°</option></select></label>
              <label class="check"><input type="checkbox" :checked="!!cfg[seite].override" @change="cfg[seite].override = $event.target.checked ? 1 : 0; rechne()" /> AoA-Override für Snapshots (Annahme)</label>
            </div>
          </details>
        </template>
      </aside>
    </div>
  </div>
</template>

<style scoped>
.bfm { --bg: #0B1016; --panel: #0E151D; --karte: #111922; --linie: #233140; --text: #E6EDF3; --text2: #C9D5E1; --gedimmt: #93A4B6;
  height: 100vh; min-height: 640px; display: flex; flex-direction: column; background: var(--bg); color: var(--text);
  font-family: 'IBM Plex Sans', system-ui, sans-serif; font-size: 14px; }
.bfm button, .bfm select, .bfm input { font: inherit; }
.fehler { color: #ff9f66; padding: 8px 16px; margin: 0; }
.kopf { display: flex; align-items: center; gap: 16px; padding: 6px 16px; border-bottom: 1px solid var(--linie); background: var(--panel); }
.logo { font-weight: 700; letter-spacing: 0.08em; font-size: 13px; color: var(--gedimmt); white-space: nowrap; text-decoration: none; }
.logo:hover { color: var(--text); }
.titel { flex: 1; font-weight: 500; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.knopf { height: 32px; padding: 0 12px; border-radius: 8px; border: 1px solid var(--linie); background: #16212C; color: var(--text); cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; font-size: 13px; }
.knopf:hover { border-color: #3A4D60; color: var(--text); }
.knopf.primaer { background: #4C9AFF; border-color: #4C9AFF; color: #06101C; font-weight: 600; }
.knopf.breit { width: 100%; justify-content: center; height: 40px; }
.knopf:disabled { opacity: 0.75; cursor: progress; }
.icon { width: 36px; height: 36px; border-radius: 8px; border: 1px solid var(--linie); background: #16212C; color: var(--text); cursor: pointer; display: inline-flex; align-items: center; justify-content: center; flex: none; }
.icon.an { border-color: #4C9AFF; color: #8CC2FF; }
.koerper { flex: 1; display: flex; min-height: 0; }
.inhalt { width: 56px; flex: none; border-right: 1px solid var(--linie); background: var(--panel); padding: 10px 8px; box-sizing: border-box; overflow-y: auto; transition: width 0.15s; }
.inhalt.offen { width: 280px; }
.liste { margin-top: 12px; display: flex; flex-direction: column; gap: 14px; }
.gruppe { display: flex; flex-direction: column; gap: 2px; }
.gruppe-titel { font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: var(--gedimmt); padding: 2px 8px; text-transform: uppercase; }
.eintrag { text-align: left; padding: 6px 8px; border-radius: 6px; border: 0; background: transparent; color: var(--text2); cursor: pointer; font-size: 13px; line-height: 1.35; }
.eintrag:hover { background: #16212C; }
.eintrag.aktiv { background: #16304F; color: var(--text); }
.mitte { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.buehne { position: relative; flex: 1; min-height: 300px; overflow: hidden; background: #0E1621; }
.hud { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.chip-paarung { position: absolute; top: 10px; left: 10px; display: inline-flex; align-items: center; gap: 8px; padding: 4px 10px; border-radius: 8px; background: rgba(11,16,22,0.88); border: 1px solid var(--linie); font-size: 13px; }
.gedimmt { color: var(--gedimmt); font-size: 12px; }
.kameras { position: absolute; top: 10px; right: 10px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
.gruppe-knoepfe { display: flex; gap: 2px; padding: 3px; border-radius: 10px; background: rgba(11,16,22,0.88); border: 1px solid var(--linie); }
.gruppe-knoepfe button { height: 30px; padding: 0 10px; border-radius: 7px; border: 0; background: transparent; color: var(--text2); cursor: pointer; font-size: 12px; }
.gruppe-knoepfe button.aktiv { background: #4C9AFF; color: #06101C; font-weight: 600; }
.ebenen { position: absolute; left: 10px; bottom: 10px; display: flex; gap: 6px; flex-wrap: wrap; max-width: 55%; }
.ebenen button { height: 30px; padding: 0 10px; border-radius: 15px; border: 1px solid var(--linie); background: rgba(11,16,22,0.8); color: var(--gedimmt); cursor: pointer; font-size: 12px; display: inline-flex; align-items: center; }
.ebenen button.an { background: #16212C; border-color: #3A4D60; color: var(--text); }
.punkt { width: 8px; height: 8px; border-radius: 50%; border: 1px solid; margin-right: 6px; display: inline-block; }
.ergebnis { position: absolute; top: 52px; left: 50%; transform: translateX(-50%); padding: 6px 14px; border-radius: 8px; background: rgba(11,16,22,0.9); border: 1px solid #7CF5A8; font-weight: 600; }
.halt { position: absolute; right: 10px; bottom: 10px; max-width: 45%; display: flex; flex-wrap: wrap; gap: 6px; align-items: center; padding: 8px 10px; border-radius: 10px; background: rgba(17,25,34,0.95); border: 1px solid #FFD166; }
.halt.klein { border-color: var(--linie); font-size: 13px; color: var(--text2); }
.halt-frage { font-weight: 600; color: #FFD166; margin-right: 4px; }
.halt button { height: 32px; padding: 0 12px; border-radius: 7px; border: 1px solid #2B3B4B; background: #16212C; color: var(--text); cursor: pointer; font-size: 13px; }
.halt button:hover { border-color: #FFD166; }
.zeitleiste { border-top: 1px solid var(--linie); background: var(--panel); padding: 8px 14px 10px; display: flex; flex-direction: column; gap: 4px; }
.steuerung { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.play { width: 42px; height: 42px; border-radius: 50%; border: 0; background: #4C9AFF; color: #06101C; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; }
.tempo { display: inline-flex; align-items: center; gap: 6px; color: var(--gedimmt); font-size: 12px; margin-left: 6px; }
.tempo select, .feld select { height: 32px; border-radius: 7px; border: 1px solid var(--linie); background: #16212C; color: var(--text); padding: 0 6px; }
.flex { flex: 1; }
.zeit, .mono { font-family: 'IBM Plex Mono', ui-monospace, monospace; font-variant-numeric: tabular-nums; }
.diagramm-kopf { display: flex; justify-content: space-between; font-size: 12px; color: var(--gedimmt); }
.diagramm { width: 100%; height: 78px; cursor: ew-resize; touch-action: none; display: block; }
.daten { width: 330px; flex: none; border-left: 1px solid var(--linie); background: var(--panel); padding: 10px; box-sizing: border-box; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; }
.tabs { display: flex; gap: 2px; padding: 3px; border-radius: 10px; background: var(--karte); border: 1px solid var(--linie); }
.tabs button { flex: 1; height: 30px; border-radius: 7px; border: 0; background: transparent; color: var(--text2); cursor: pointer; font-size: 13px; }
.tabs button.aktiv { background: #16304F; color: var(--text); }
.karte { background: var(--karte); border: 1px solid var(--linie); border-radius: 10px; padding: 10px 12px; display: flex; flex-direction: column; gap: 8px; }
.karte.blau { border-top: 3px solid #4C9AFF; }
.karte.orange { border-top: 3px solid #FF8A3D; }
.karte-kopf { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
.knopf-flach { background: transparent; border: 0; padding: 0; color: inherit; cursor: pointer; width: 100%; text-align: left; }
.name { font-weight: 700; font-size: 15px; display: inline-flex; align-items: center; gap: 6px; }
.werte3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; }
.lbl { font-size: 11px; color: var(--gedimmt); }
.gross { font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 18px; font-variant-numeric: tabular-nums; }
.balken { display: grid; grid-template-columns: 40px minmax(0, 1fr) 46px; align-items: center; gap: 8px; font-size: 12px; }
.balken .mono { text-align: right; }
.spur { position: relative; height: 7px; border-radius: 4px; background: var(--linie); }
.fuell { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 4px; }
.marke { position: absolute; top: -3px; bottom: -3px; width: 2px; background: #FFD166; }
.zeile-klein { display: flex; gap: 10px; flex-wrap: wrap; font-size: 12px; color: var(--text2); }
.problem { display: flex; flex-direction: column; gap: 2px; }
.problem-kopf { display: flex; align-items: center; gap: 8px; }
.pname { font-weight: 600; }
.wert { margin-left: auto; color: var(--text2); font-size: 12px; }
.stufe { width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none; }
.stufe.ok { background: #12301F; color: #7CF5A8; }
.stufe.achtung { background: #3A3010; color: #FFD166; }
.stufe.problem { background: #3A1C10; color: #FF9F66; }
.loesung { font-size: 12px; color: var(--gedimmt); padding-left: 28px; line-height: 1.4; }
.lektion p { margin: 0; font-size: 13px; color: var(--text2); line-height: 1.5; }
.feld { display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--gedimmt); }
.feld input[type=range] { width: 100%; }
.zwei { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
.check { display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--text2); }
.treffer { display: flex; flex-direction: column; gap: 4px; padding: 8px 0; border-top: 1px solid var(--linie); font-size: 13px; }
.strategie { display: flex; flex-direction: column; gap: 6px; padding-top: 8px; }
details summary { cursor: pointer; }
@media (max-width: 960px) {
  .bfm { height: auto; }
  .koerper { flex-wrap: wrap; }
  .buehne { min-height: 60vh; }
  .daten { width: 100%; }
}
</style>

