# В официальном php-образе расширения pdo_firebird нет — собираем из исходников
# PHP против клиентской библиотеки Firebird из пакетов Debian.
FROM php:8.4-cli

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        gcc \
        make \
        pkg-config \
        re2c \
        libfbclient2 \
        firebird-dev \
    && docker-php-ext-install pdo_firebird \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY index.php .
CMD ["php", "index.php"]
