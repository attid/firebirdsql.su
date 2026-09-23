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
# 127.0.0.1 явно (не localhost: бывает ::1, а слушаем только IPv4),
# start-period+interval короче минуты — Portainer быстрее показывает healthy
HEALTHCHECK --interval=15s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
