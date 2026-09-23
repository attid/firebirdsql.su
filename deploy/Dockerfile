# Сборка нового сайта firebirdsql.su: два этапа.
# Контекст сборки — корень репозитория:
#   docker build -f deploy/Dockerfile -t firebirdsql-site .

# --- Этап 1: сборка Astro + индекс Pagefind ---
FROM node:24-alpine AS build
WORKDIR /app
COPY site/package.json site/package-lock.json ./
RUN npm ci
COPY site/ ./
RUN npm run build

# --- Этап 2: nginx + статики + карты редиректов ---
FROM nginx:1.29-alpine
COPY deploy/nginx.conf /etc/nginx/nginx.conf
COPY deploy/redirects.map /etc/nginx/redirects.map
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=60s --timeout=3s CMD wget -q -O /dev/null http://localhost/ || exit 1
