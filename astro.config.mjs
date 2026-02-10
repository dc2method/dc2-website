// @ts-check
import { defineConfig } from 'astro/config';

import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import remarkHeadingId from 'remark-heading-id';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize, { defaultSchema } from 'rehype-sanitize';

import sitemap from '@astrojs/sitemap';

// Schéma étendu pour préserver l'attribut data-language sur les <pre>
// généré par Shiki, nécessaire pour que MermaidInit.astro détecte les blocs Mermaid.
const sanitizeSchema = {
  ...defaultSchema,
  attributes: {
    ...defaultSchema.attributes,
    pre: [...(defaultSchema.attributes?.pre ?? []), 'dataLanguage'],
  },
};

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
    rehypePlugins: [rehypeRaw, [rehypeSanitize, sanitizeSchema]],
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
});