// @ts-check
import { defineConfig } from 'astro/config';

import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import remarkHeadingId from 'remark-heading-id';
import rehypeSanitize from 'rehype-sanitize';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://dc2method.dev',
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
    routing: {
      prefixDefaultLocale: false, // /en/page devient /page
    },
  },
  integrations: [mdx(), react(), sitemap()],
  build: {
    format: 'directory', // URLs propres sans .html
  },
  markdown: {
    remarkPlugins: [remarkHeadingId],
    rehypePlugins: [rehypeSanitize],
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
});