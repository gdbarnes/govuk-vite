import { defineConfig } from 'vite';
import { resolve } from 'path';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
    },
    assetsDir: 'assets',
    manifest: true,
  },
  css: {
    preprocessorOptions: {
      scss: {
        quietDeps: true,
      },
    },
  },
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'node_modules/govuk-frontend/dist/govuk/assets/images/*',
          dest: 'assets/images',
        },
        {
          src: 'node_modules/govuk-frontend/dist/govuk/assets/fonts/*',
          dest: 'assets/fonts',
        },
        {
          src: 'node_modules/govuk-frontend/dist/govuk/assets/manifest.json',
          dest: 'assets',
        },
      ],
    }),
  ],
});
