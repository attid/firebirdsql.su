# Подключение к Firebird из PHP

Для работы с СУБД Firebird в современном PHP используется расширение `pdo_firebird`. Однако при попытке развернуть проект в контейнере разработчики сразу сталкиваются с сюрпризом: в официальном Docker-образе PHP этого модуля **нет**. Причина проста — дистрибутив не содержит клиентских библиотек Firebird из коробки, поэтому расширение исключено из базовой поставки и требует сборки из исходников.

В этой статье разберём, как быстро собрать контейнер на базе PHP 8.4 CLI, настроить подключение через PDO и избежать типичных подводных камней. Решение проверено в связке с Firebird 5.0.4.

---

### Dockerfile с рецептом сборки

Для сборки расширения понадобятся компилятор, сборочные утилиты и заголовочные файлы клиента Firebird. Ключевой пакет здесь — `firebird-dev` (он содержит заголовки C-API и подтягивает клиентскую библиотеку `libfbclient2` зависимостью).

Готовый `Dockerfile` для `php:8.4-cli`:

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

Команда `docker-php-ext-install pdo_firebird` компилирует модуль непосредственно под установленную версию PHP.

---

### Подключение и выполнение запроса

После сборки модуля работа с базой идёт через стандартный интерфейс PDO:

```php
$dsn = "firebird:dbname=firebird:/var/lib/firebird/data/employee.fdb;charset=UTF8";
$pdo = new PDO($dsn, "SYSDBA", "masterkey", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);
$stmt = $pdo->query(
    "SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5"
);
foreach ($stmt as $row) {
    printf("  %s %s — %.2f\n", $row["FIRST_NAME"], $row["LAST_NAME"], $row["SALARY"]);
}
```

---

### Формат DSN

Строка DSN для Firebird имеет свою специфику:

```text
firebird:dbname=host:path;charset=UTF8
```

- **`host`** — адрес сервера. В Docker Compose в качестве хоста указывается имя сервиса (например, `firebird`).
- **`path`** — полный путь к файлу `.fdb` внутри контейнера или сервера Firebird (например, `/var/lib/firebird/data/employee.fdb`).
- **`charset=UTF8`** — параметр кодировки соединения. Для корректной работы с кириллицей задавать `charset=UTF8` обязательно всегда, иначе при выборке и вставке текста неизбежны кракозябры или ошибки трансляции символов.

---

### Параметризованные запросы

Конкатенация строк в SQL-запросах опасна и ломает кеширование планов выполнения. Используйте подготовленные выражения с позиционными плейсхолдерами:

```php
$stmt = $pdo->prepare("... WHERE DEPT_NO = ?");
$stmt->execute([$dept]);
```

Драйвер `pdo_firebird` корректно биндит параметры, экранирует спецсимволы и предотвращает SQL-инъекции.

---

### Частые грабли

1. **Отсутствие модуля по умолчанию.** Команда `php -m` в чистом образе не покажет `pdo_firebird`. Пакетного `apt-get install php-pdo-firebird` в официальном образе тоже нет — только компиляция через `docker-php-ext-install`.
2. **Забытый `firebird-dev`.** Установка только `libfbclient2` без `-dev` пакета приведёт к ошибке на этапе сборки расширения: компилятор не найдёт заголовочный файл `ibase.h`.
3. **Разделитель хоста и пути.** Не путайте синтаксис: после имени хоста ставится двоеточие (`host:/path/to/db.fdb`), а не слэш или порт, если используется стандартный порт `3050`.

---

### Что почитать дальше

- Управление транзакциями в Firebird: уровни изоляции (`READ COMMITTED`, `SNAPSHOT`) и особенности автокоммита в PDO.
- Диалекты Firebird (Dialect 3 vs Dialect 1) и их влияние на типы данных `BIGINT` и кавычки идентификаторов.
- Ограничение выборки: синтаксис `ROWS n` / `OFFSET m` против стандарта `LIMIT / OFFSET`.
- Тонкая настройка пула соединений и работа с хранимыми процедурами через `EXECUTE PROCEDURE`.
