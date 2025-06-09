import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
  },
});
// This Vite configuration file sets up a React project with the necessary plugins and build settings.
// It uses the '@vitejs/plugin-react' plugin for React support and specifies the output directory for the build as 'dist'.