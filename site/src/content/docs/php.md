---
title: "Подключение к Firebird из PHP"
old_id: php
section: groups
type: article
date: "2026-10-05"
firebird:
  since: 
  until: 
  deprecated: false
---

# Подключение к Firebird из PHP

Расширение **pdo_firebird** позволяет работать с Firebird через штатный PDO. Подвох один, но важный: **в официальном php-образе этого расширения нет** — его нужно собрать из исходников PHP. Ниже — проверенный рецепт.

## Сборка образа с pdo_firebird

```dockerfile
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
```

Ключевой пакет — **firebird-dev**: клиентская библиотека плюс заголовки, без которых сборка расширения не пойдёт (`libfbclient2` подтягивается зависимостью). `re2c`, `autoconf`, `gcc`, `make` — стандартный набор для сборки PHP-расширений из исходников.

## Подключение и запрос

```php
<?php
$dsn = "firebird:dbname=firebird:/var/lib/firebird/data/employee.fdb;charset=UTF8";

$pdo = new PDO($dsn, "SYSDBA", "masterkey", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);

$stmt = $pdo->query(
    "SELECT FIRST_NAME, LAST_NAME, SALARY "
    . "FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5"
);

foreach ($stmt as $row) {
    printf("  %s %s — %.2f\n", $row["FIRST_NAME"], $row["LAST_NAME"], $row["SALARY"]);
}
```

## Формат DSN

```
firebird:dbname=host:path;charset=UTF8
```

- **charset=UTF8** — для кириллицы всегда.
- `ERRMODE_EXCEPTION` — чтобы ошибки PDO не терялись молча.

## Параметризованные запросы

```php
$stmt = $pdo->prepare(
    "SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEE WHERE DEPT_NO = ?"
);
$stmt->execute([$dept]);
```

## Типичные грабли

| Симптом | Причина | Что делать |
|---|---|---|
| `could not find driver` | pdo_firebird не установлен | Собрать по рецепту выше |
| Сборка падает на configure | Нет firebird-dev (заголовков) | Установить firebird-dev, не только libfbclient2 |
| Кириллица знаками вопроса | Нет charset в DSN | Добавить `charset=UTF8` |

## Пример целиком

Рабочий пример с этим кодом — в [репозитории сайта](https://github.com/attid/firebirdsql.su/tree/main/examples/php): Dockerfile с рецептом сборки + docker compose с Firebird 5.0.4 и демо-базой employee, прогоняется одной командой.

## Что почитать дальше

- [Порты Firebird](/port_3050/) — что открывать в firewall
- [Глоссарий](/glossarij/) — сам язык SQL с примерами
- [Коды ошибок](/gdscodes/) — расшифровка ошибок Firebird
