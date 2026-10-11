// Low-Poly-Modelle der drei Jets, im gleichen Maßstab (Meter). Lokale Achsen: Nase +X, oben +Y, rechts +Z.
// Grundriss nach den Silhouetten im Konzept (Einheit dort 0,1 m); Maße nach den Vorbildern angenommen.
import * as THREE from 'three'

// Halbe Grundriss-Kontur (rechte Seite), [seitlich, Abstand von der Nase] in 0,1 m; wird gespiegelt.
export const GRUNDRISS = {
  'T-15': [[0, 0], [3, 12], [6, 30], [8, 58], [16, 62], [16, 80], [65, 128], [65, 140], [62, 142], [18, 138], [18, 150], [44, 170], [44, 180], [16, 178], [12, 194]],
  'T-16': [[0, 0], [3, 16], [5, 32], [6, 46], [10, 62], [12, 70], [13, 78], [50, 112], [50, 120], [12, 122], [11, 128], [32, 142], [32, 148], [9, 148], [6, 150]],
  'T-18': [[0, 0], [3, 16], [5, 30], [6, 42], [12, 60], [17, 74], [20, 86], [62, 104], [62, 114], [20, 118], [18, 130], [44, 146], [44, 154], [14, 154], [10, 170]],
}
// Rumpfradius [m] über die Länge (Anteil 0 = Nase … 1 = Heck)
const RUMPF = {
  'T-15': [[0, 0], [0.05, 0.5], [0.15, 0.9], [0.3, 1.3], [0.7, 1.35], [0.92, 1.1], [1, 0.9]],
  'T-16': [[0, 0], [0.05, 0.35], [0.15, 0.65], [0.3, 0.85], [0.7, 0.85], [0.92, 0.7], [1, 0.55]],
  'T-18': [[0, 0], [0.05, 0.45], [0.15, 0.8], [0.3, 1.1], [0.7, 1.15], [0.92, 0.95], [1, 0.8]],
}
// Seitenleitwerke: Abstand von der Nase (Wurzel vorn, hinten) [m], Höhe, Spitzensehne, seitlicher Abstand, Neigung nach außen [°]
const LEITWERK = {
  'T-15': { vorn: 14.2, hinten: 18.6, hoehe: 3.3, spitze: 1.8, seite: [-1.3, 1.3], neigung: 0 },
  'T-16': { vorn: 10.8, hinten: 15.0, hoehe: 3.6, spitze: 1.4, seite: [0], neigung: 0 },
  'T-18': { vorn: 10.2, hinten: 13.6, hoehe: 3.0, spitze: 1.4, seite: [-1.0, 1.0], neigung: 20 },
}
const DUESEN = { 'T-15': [-0.75, 0.75], 'T-16': [0], 'T-18': [-0.6, 0.6] }
export const LAENGE = { 'T-15': 19.4, 'T-16': 15.0, 'T-18': 17.0 }

export function jetModell(typ, farbe, { transparent = false } = {}) {
  const L = LAENGE[typ]
  const mat = new THREE.MeshStandardMaterial({ color: farbe, metalness: 0.15, roughness: 0.65, side: THREE.DoubleSide, transparent, opacity: transparent ? 0.3 : 1, depthWrite: !transparent })
  const dunkel = new THREE.MeshStandardMaterial({ color: 0x1b2633, metalness: 0.3, roughness: 0.5, transparent, opacity: transparent ? 0.3 : 1, depthWrite: !transparent })
  const g = new THREE.Group()

  // Flügel, Stabilisatoren: Grundriss als flache Platte
  const halb = GRUNDRISS[typ].map(([s, a]) => [s / 10, a / 10])
  const voll = [...halb, ...halb.slice().reverse().map(([s, a]) => [-s, a])]
  const form = new THREE.Shape(voll.map(([s, a]) => new THREE.Vector2(L / 2 - a, -s)))
  const platte = new THREE.ExtrudeGeometry(form, { depth: 0.25, bevelEnabled: false })
  platte.rotateX(-Math.PI / 2)
  platte.translate(0, -0.1, 0)
  g.add(new THREE.Mesh(platte, mat))

  // Rumpf
  const pts = RUMPF[typ].map(([f, r]) => new THREE.Vector2(r, L / 2 - f * L))
  const rumpf = new THREE.LatheGeometry(pts, 14)
  rumpf.rotateZ(-Math.PI / 2)
  const rm = new THREE.Mesh(rumpf, mat); rm.scale.set(1, 0.8, 1); g.add(rm)

  // Haube
  const haube = new THREE.Mesh(new THREE.SphereGeometry(1, 12, 8), dunkel)
  haube.scale.set(1.6, 0.55, 0.5)
  haube.position.set(L / 2 - L * 0.2, RUMPF[typ][3][1] * 0.75, 0)
  g.add(haube)

  // Seitenleitwerke
  const lw = LEITWERK[typ]
  const lf = new THREE.Shape([
    new THREE.Vector2(L / 2 - lw.vorn, 0), new THREE.Vector2(L / 2 - lw.hinten, 0),
    new THREE.Vector2(L / 2 - lw.hinten, lw.hoehe), new THREE.Vector2(L / 2 - lw.hinten + lw.spitze, lw.hoehe),
  ])
  for (const z of lw.seite) {
    const geo = new THREE.ExtrudeGeometry(lf, { depth: 0.12, bevelEnabled: false })
    const m = new THREE.Mesh(geo, mat)
    m.position.set(0, RUMPF[typ][4][1] * 0.5, z)
    m.rotation.x = z === 0 ? 0 : Math.sign(z) * lw.neigung * Math.PI / 180
    g.add(m)
  }
  // Düsen
  for (const z of DUESEN[typ]) {
    const d = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.45, 1.0, 10, 1, true), dunkel)
    d.rotation.z = Math.PI / 2
    d.position.set(-L / 2 - 0.2, 0, z)
    g.add(d)
  }
  return g
}

// SVG-Pfad der Draufsicht (Einheit 0,1 m, Nase oben bei y = 0) für Icons im Panel
export function silhouettePfad(typ) {
  const halb = GRUNDRISS[typ]
  const voll = [...halb, ...halb.slice().reverse().map(([s, a]) => [-s, a])]
  return 'M' + voll.map(([s, a]) => `${s} ${a}`).join(' L') + ' Z'
}
