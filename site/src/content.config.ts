import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Контентная модель — ADR-0005: поля версий Firebird могут быть пустыми
// (null/пропущены), но удалять их из схемы нельзя: на них рассчитаны
// фильтр версий и будущий RAG (ADR-0007).
// generateId: id = имя файла без расширения БЕЗ слагификации — схема URL
// /<old_id>/ повторяет ID старой вики точь-в-точь (в т.ч. точки в sql0xx).
const docs = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/docs",
    generateId: ({ entry }) => entry.replace(/\.md$/, ""),
  }),
  schema: z.object({
    title: z.string(),
    old_id: z.string(),
    section: z.enum(["glossary", "intro", "install", "errors", "sql", "groups"]),
    type: z.enum(["term", "article", "landing"]),
    firebird: z.object({
      since: z.string().nullish(),
      until: z.string().nullish(),
      deprecated: z.boolean().default(false),
    }),
  }),
});

export const collections = { docs };
