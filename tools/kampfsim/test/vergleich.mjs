// Vergleicht die JS-Portierung (docs/.vitepress/components/sim/physik.js) mit sim.py
import fs from 'fs'
import { simuliere } from '../../../app/src/sim/physik.js'
const m = JSON.parse(fs.readFileSync(new URL('../../../app/public/data/modell.json', import.meta.url)))
const faelle = JSON.parse(fs.readFileSync(new URL('./faelle.json', import.meta.url)))
let gleich = 0, zeitGleich = 0, n = 0
const t0 = Date.now()
for (const f of faelle) {
  const r = simuliere(m, f.a, f.b, f.sa, f.sb, { versatz_m: f.versatz }, { frameAlle: 1000 })
  n++
  if (r.ergebnis === f.erg) gleich++
  const tj = isFinite(Math.min(...r.tTot)) ? Math.min(...r.tTot) : null
  if ((tj === null && f.t === null) || (tj !== null && f.t !== null && Math.abs(tj - f.t) < 0.05)) zeitGleich++
}
console.log(`${n} Kämpfe: Ergebnis gleich ${gleich} (${(gleich / n * 100).toFixed(1)} %), Zeitpunkt gleich ${zeitGleich}; ${((Date.now() - t0) / n).toFixed(1)} ms je Kampf`)
