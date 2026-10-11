// HUD für die Cockpit-Ansicht: zeichnet auf ein 2D-Canvas über der 3D-Szene.
// Position von Flugbahn-Marker, Leiter und Bandit kommt aus der Projektion der Three.js-Kamera.
import { FT, KT } from './physik.js'

const GRUEN = '#7CF5A8', ORANGE = '#FFB27F'
const zahl = (v, d = 0) => Number(v).toLocaleString('de-DE', { maximumFractionDigits: d, minimumFractionDigits: d })

// w3: Sim-Vektor [x, y, z] (m) -> Three-Koordinaten in Szenen-Einheiten
export function zeichneHud(ctx, w, h, cam, f, i, w3, info) {
  ctx.clearRect(0, 0, w, h)
  const j = f.j[i], o = f.j[1 - i]
  ctx.save()
  ctx.strokeStyle = GRUEN; ctx.fillStyle = GRUEN; ctx.lineWidth = 2
  ctx.font = '15px "IBM Plex Mono", monospace'
  ctx.shadowColor = 'rgba(0,0,0,0.6)'; ctx.shadowBlur = 3

  const proj = (simPunkt) => {
    const v = w3(simPunkt).project(cam)
    return { x: (v.x + 1) / 2 * w, y: (1 - v.y) / 2 * h, vorn: v.z < 1 && v.z > -1 }
  }
  const weit = (dir, d = 20000) => [j.P[0] + dir[0] * d, j.P[1] + dir[1] * d, j.P[2] + dir[2] * d]

  // Leiter: Linien in je 10° Längsneigung um den Kurs
  const kurs = Math.atan2(j.vh[0], j.vh[1])
  ctx.lineWidth = 1.5
  for (let e = -60; e <= 60; e += 10) {
    const pk = []
    for (const dA of [-0.12, -0.03, 0.03, 0.12]) {
      const el = e * Math.PI / 180, az = kurs + dA
      pk.push(proj(weit([Math.cos(el) * Math.sin(az), Math.cos(el) * Math.cos(az), Math.sin(el)])))
    }
    if (!pk.every(p => p.vorn)) continue
    ctx.setLineDash(e < 0 ? [8, 6] : [])
    ctx.globalAlpha = e === 0 ? 0.9 : 0.6
    ctx.beginPath(); ctx.moveTo(pk[0].x, pk[0].y); ctx.lineTo(pk[1].x, pk[1].y); ctx.moveTo(pk[2].x, pk[2].y); ctx.lineTo(pk[3].x, pk[3].y); ctx.stroke()
    if (e !== 0) { ctx.globalAlpha = 0.7; ctx.font = '11px "IBM Plex Mono", monospace'; ctx.fillText(String(e), pk[3].x + 6, pk[3].y + 4) }
  }
  ctx.setLineDash([]); ctx.globalAlpha = 1; ctx.lineWidth = 2; ctx.font = '15px "IBM Plex Mono", monospace'

  // Nase (Bildmitte) und Flugbahn-Marker
  const cx = w / 2, cy = h / 2
  ctx.beginPath(); ctx.moveTo(cx - 18, cy); ctx.lineTo(cx - 8, cy); ctx.lineTo(cx - 4, cy + 6); ctx.lineTo(cx, cy); ctx.lineTo(cx + 4, cy + 6); ctx.lineTo(cx + 8, cy); ctx.lineTo(cx + 18, cy); ctx.stroke()
  const fpm = proj(weit(j.vh))
  if (fpm.vorn) {
    ctx.beginPath(); ctx.arc(fpm.x, fpm.y, 8, 0, Math.PI * 2); ctx.stroke()
    ctx.beginPath(); ctx.moveTo(fpm.x - 20, fpm.y); ctx.lineTo(fpm.x - 8, fpm.y); ctx.moveTo(fpm.x + 8, fpm.y); ctx.lineTo(fpm.x + 20, fpm.y); ctx.moveTo(fpm.x, fpm.y - 8); ctx.lineTo(fpm.x, fpm.y - 16); ctx.stroke()
    // Lift-Vector-Marke: kleiner Winkel in Richtung des Auftriebs
    const lp = proj(weit([j.vh[0] + j.l[0] * 0.05, j.vh[1] + j.l[1] * 0.05, j.vh[2] + j.l[2] * 0.05]))
    const dx = lp.x - fpm.x, dy = lp.y - fpm.y, n = Math.hypot(dx, dy) || 1
    const ux = dx / n, uy = dy / n, bx = fpm.x + ux * 30, by = fpm.y + uy * 30
    ctx.beginPath(); ctx.moveTo(bx - uy * 8 - ux * 6, by + ux * 8 - uy * 6); ctx.lineTo(bx, by); ctx.lineTo(bx + uy * 8 - ux * 6, by - ux * 8 - uy * 6); ctx.stroke()
  }

  // Bandit: Raute oder Pfeil am Rand, Pipper mit Vorhalt
  const b = proj(o.P)
  ctx.strokeStyle = ORANGE; ctx.fillStyle = ORANGE
  if (b.vorn && b.x > 20 && b.x < w - 20 && b.y > 20 && b.y < h - 20) {
    ctx.beginPath(); ctx.moveTo(b.x, b.y - 14); ctx.lineTo(b.x + 14, b.y); ctx.lineTo(b.x, b.y + 14); ctx.lineTo(b.x - 14, b.y); ctx.closePath(); ctx.stroke()
    ctx.fillText(`${zahl(j.R / FT)} ft`, b.x + 18, b.y - 6)
  } else {
    let dx = b.x - cx, dy = b.y - cy
    if (!b.vorn) { dx = -dx; dy = -dy }
    const n = Math.hypot(dx, dy) || 1, r = Math.min(w, h) * 0.38
    const px = cx + dx / n * r, py = cy + dy / n * r, ux = dx / n, uy = dy / n
    ctx.beginPath(); ctx.moveTo(px + ux * 16, py + uy * 16); ctx.lineTo(px - uy * 9, py + ux * 9); ctx.lineTo(px + uy * 9, py - ux * 9); ctx.closePath(); ctx.fill()
  }
  if (j.gun && j.dFire) {
    const p = proj([j.P[0] + j.dFire[0] * j.R, j.P[1] + j.dFire[1] * j.R, j.P[2] + j.dFire[2] * j.R])
    if (p.vorn) {
      ctx.strokeStyle = GRUEN; ctx.fillStyle = GRUEN
      ctx.beginPath(); ctx.arc(p.x, p.y, 22, 0, Math.PI * 2); ctx.setLineDash([4, 5]); ctx.stroke(); ctx.setLineDash([])
      ctx.beginPath(); ctx.arc(p.x, p.y, 3, 0, Math.PI * 2); ctx.fill()
      if (j.schuss) { ctx.fillText('TREFFER', p.x + 28, p.y + 5) }
    }
  }

  // Bänder links und rechts, Kurs oben, Werte
  ctx.strokeStyle = GRUEN; ctx.fillStyle = GRUEN
  const sx = w * 0.22, ax = w * 0.78
  ctx.strokeRect(sx - 48, cy - 18, 96, 36); ctx.strokeRect(ax - 56, cy - 18, 112, 36)
  ctx.font = '20px "IBM Plex Mono", monospace'
  ctx.textAlign = 'center'
  ctx.fillText(zahl(j.kias), sx, cy + 7); ctx.fillText(zahl(j.h / FT), ax, cy + 7)
  ctx.font = '13px "IBM Plex Mono", monospace'
  ctx.fillText('KIAS', sx, cy - 26); ctx.fillText('ALT', ax, cy - 26)
  const hdg = ((kurs * 180 / Math.PI) + 360) % 360
  ctx.fillText(String(Math.round(hdg)).padStart(3, '0'), cx, 40)
  ctx.beginPath(); ctx.moveTo(cx - 120, 50); ctx.lineTo(cx + 120, 50); ctx.stroke()
  ctx.beginPath(); ctx.moveTo(cx - 6, 58); ctx.lineTo(cx, 52); ctx.lineTo(cx + 6, 58); ctx.stroke()
  ctx.textAlign = 'left'
  ctx.font = '15px "IBM Plex Mono", monospace'
  const zeilen = [`M ${zahl(j.M, 2)}`, `G ${zahl(j.n, 1)}`, `α ${zahl(j.alpha)}°`, info.schub, `E ${zahl(j.E / FT)}`, `Ps ${info.ps >= 0 ? '+' : '−'}${zahl(Math.abs(info.ps))}`]
  zeilen.forEach((z, k) => ctx.fillText(z, sx - 48, cy + 50 + k * 22))
  ctx.fillStyle = ORANGE
  ctx.fillText(`R ${zahl(j.R / FT)}`, ax - 56, cy + 50)
  ctx.fillText(`Vc ${j.vc >= 0 ? '+' : '−'}${zahl(Math.abs(j.vc / KT))}`, ax - 56, cy + 72)
  ctx.fillText(o.typ, ax - 56, cy + 94)
  ctx.restore()
}
