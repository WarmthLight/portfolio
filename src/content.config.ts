import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.object({ zh: z.string(), en: z.string() }),
    description: z.object({ zh: z.string(), en: z.string() }),
    cover: z.string(),
    video: z.string(),
    tags: z.array(z.string()),
    order: z.number().default(0),
  }),
});

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/case-studies' }),
  schema: z.object({
    title: z.object({ zh: z.string(), en: z.string() }),
    subtitle: z.object({ zh: z.string(), en: z.string() }),
    cover: z.string(),
    role: z.object({ zh: z.string(), en: z.string() }),
    timeline: z.string(),
    tags: z.array(z.string()),
    order: z.number().default(0),
    metrics: z.array(z.object({
      label: z.object({ zh: z.string(), en: z.string() }),
      value: z.string(),
    })).optional(),
  }),
});

export const collections = { projects, caseStudies };
