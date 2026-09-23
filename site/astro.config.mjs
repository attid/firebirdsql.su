import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

// Схема URL /<old_id>/ (плоская, 1:1 со старой вики, ADR-0004):
// trailingSlash always + directory-формат дают канонический вид со слэшем.
// Двуцветная подсветка кода (Shiki dual themes) переключается CSS-переменными.
export default defineConfig({
  site: "https://firebirdsql.su",
  trailingSlash: "always",
  build: { format: "directory" },
  integrations: [
    sitemap({
      // /en/ — noindex-заглушка, в карту не включаем; 404 туда не попадает
      filter: (page) => !page.endsWith("/en/"),
    }),
  ],
  markdown: {
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark" },
    },
  },
});
