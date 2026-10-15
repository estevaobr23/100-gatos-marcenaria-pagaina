import { defineConfig } from 'vite';

export default defineConfig({
  server: { port: 5180, host: true, strictPort: true, watch: { usePolling: true, interval: 200 } },
  build: { outDir: 'dist', assetsInlineLimit: 0 }
});
