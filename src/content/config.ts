import { defineCollection, z } from 'astro:content';

const docsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    sidebar_position: z.number().optional(),
    lang: z.enum(['fr', 'en']),
  }),
});

export const collections = {
  'docs': docsCollection,
};
