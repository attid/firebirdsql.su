import { defineConfig } from "astro/config";

// Схема URL /<old_id>/ (плоская, 1:1 со старой вики, ADR-0004):
// trailingSlash always + directory-формат дают канонический вид со слэшем.
// Двуцветная подсветка кода (Shiki dual themes) переключается CSS-переменными.
export default defineConfig({
  site: "https://firebirdsql.su",
  trailingSlash: "always",
  build: { format: "directory" },
  markdown: {
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark" },
    },
  },
});
