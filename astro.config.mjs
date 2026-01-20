// @ts-check
import { defineConfig } from 'astro/config';

import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import remarkHeadingId from 'remark-heading-id';

// https://astro.build/config
export default defineConfig({
  site: 'https://docdriven.dev',
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: false, // /fr/page devient /page
    },
  },
  integrations: [mdx(), react()],
  build: {
    format: 'directory', // URLs propres sans .html
  },
  markdown: {
    remarkPlugins: [remarkHeadingId],
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
});