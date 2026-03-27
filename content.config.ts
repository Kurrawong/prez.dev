import { defineContentConfig, defineCollection, z } from "@nuxt/content";

const schema = z.object({
    tags: z.string().array(),
    date: z.date(),
    source: z.string().url(),
    code: z.string().url(),
    editorContent: z.string(),
    icon: z.string(),
});

export default defineContentConfig({
    collections: {
        home: defineCollection({
            type: "page",
            source: "*.md",
            schema,
        }),
        prezui: defineCollection({
            type: "page",
            source: "prezui/**/*.md",
            schema,
        }),
        prez: defineCollection({
            type: "page",
            source: "prezapi/**/*.md",
            schema,
        }),
        prezmanifest: defineCollection({
            type: "page",
            source: "kgmanifest/**/*.md",
            schema,
        }),
    }
});
