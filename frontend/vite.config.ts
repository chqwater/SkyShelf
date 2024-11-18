import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import terminal from 'vite-plugin-terminal'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    terminal({
      // console: 'terminal',
      output: ['terminal', 'console']
    })
  ]
})
