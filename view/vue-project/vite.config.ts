import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// proxy https://vertexai-wlfx73ehlq-uc.a.run.app/predict
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
  // ,
  // server: {
  //   proxy: {
  //     '/predict': {
  //       target: 'https://vertexai-wlfx73ehlq-uc.a.run.app',
  //       changeOrigin: true,
  //       rewrite: (path) => path.replace(/^\/predict/, '')
  //     }
  //   }
  // }
})
