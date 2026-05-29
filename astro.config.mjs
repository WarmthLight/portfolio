import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  base: '/portfolio/',
  vite: {
    plugins: [tailwindcss()],
  },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
  },
});
