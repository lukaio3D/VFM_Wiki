import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Die App liegt neben dem Wiki unter /VFM_Wiki/sim/ (GitHub Pages).
// Lokal leitet der Wiki-Server (Port 5180) /VFM_Wiki/sim/ an diesen Server weiter, siehe docs/.vitepress/config.mts.
export default defineConfig({
  base: '/VFM_Wiki/sim/',
  plugins: [vue()],
  server: { host: '127.0.0.1', port: 5181, strictPort: true },
  build: { outDir: '../docs/.vitepress/dist/sim', emptyOutDir: true, chunkSizeWarningLimit: 900 },
})
