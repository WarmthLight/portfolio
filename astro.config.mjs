import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import rehypeRaw from 'rehype-raw';

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    rehypePlugins: [rehypeRaw],
  },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
  },
});
