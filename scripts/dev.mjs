// Startet Wiki (VitePress, Port 5180) und Simulator-App (Vite, Port 5181) zusammen.
// Der Wiki-Server reicht /VFM_Wiki/sim/ an die App weiter, also läuft alles unter http://127.0.0.1:5180/VFM_Wiki/.
// Sind die Ports belegt (z. B. weil schon ein Server läuft), bricht das Skript mit einer klaren Meldung ab,
// statt auf andere Ports auszuweichen. Ctrl-C beendet beide Server.
import { spawn } from 'node:child_process'
import net from 'node:net'

const PORTS = { 5180: 'Wiki', 5181: 'Simulator-App' }

function belegt(port) {
  return new Promise(res => {
    const s = net.createServer()
    s.once('error', () => res(true))
    s.once('listening', () => s.close(() => res(false)))
    s.listen(port, '127.0.0.1')
  })
}

for (const [port, name] of Object.entries(PORTS)) {
  if (await belegt(Number(port))) {
    console.error(`\nPort ${port} (${name}) ist schon belegt. Läuft der Server schon in einem anderen Terminal?`)
    console.error(`Dann dort weiterarbeiten oder ihn mit Ctrl-C beenden. Prozess finden: lsof -nP -iTCP:${port} -sTCP:LISTEN\n`)
    process.exit(1)
  }
}

const kinder = [
  spawn('npm', ['--prefix', 'app', 'run', 'dev'], { stdio: 'inherit' }),
  spawn('npx', ['vitepress', 'dev', 'docs', '--port', '5180', '--strictPort', '--host', '127.0.0.1'], { stdio: 'inherit' }),
]
let ende = false
function beenden(code = 0) {
  if (ende) return
  ende = true
  for (const k of kinder) k.kill('SIGTERM')
  process.exit(code)
}
for (const k of kinder) k.on('exit', c => beenden(c ?? 0))
process.on('SIGINT', () => beenden(0))
process.on('SIGTERM', () => beenden(0))

setTimeout(() => console.log('\n  Wiki:       http://127.0.0.1:5180/VFM_Wiki/\n  Simulator:  http://127.0.0.1:5180/VFM_Wiki/sim/\n'), 2500)
