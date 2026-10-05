---
title: "Подключение к Firebird из Go"
old_id: go
section: groups
type: article
date: "2026-10-05"
firebird:
  since: 
  until: 
  deprecated: false
---

# Подключение к Firebird из Go

Драйвер [nakagami/firebirdsql](https://github.com/nakagami/firebirdsql) — `database/sql`-драйвер на **чистом Go**: ни cgo, ни клиентской библиотеки fbclient ставить не нужно. Работает по сети с Firebird 2.5 и новее (проверено на 5.0).

## Установка

```bash
go get github.com/nakagami/firebirdsql@v0.9.21
```

## Подключение и запрос

```go
import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/nakagami/firebirdsql"
)

func main() {
    dsn := "SYSDBA:masterkey@firebird:3050/var/lib/firebird/data/employee.fdb?charset=UTF8"

    db, err := sql.Open("firebirdsql", dsn)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    rows, err := db.Query(
        "SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE " +
        "ORDER BY SALARY DESC ROWS 5")
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    for rows.Next() {
        var first, last string
        var salary float64
        if err := rows.Scan(&first, &last, &salary); err != nil {
            log.Fatal(err)
        }
        fmt.Printf("  %s %s — %.2f\n", first, last, salary)
    }
}
```

## Формат DSN

```
user:password@host:port/path/to/database?charset=UTF8
```

- **charset=UTF8** — для кириллицы указывайте всегда: без него строки из базы приходят знаками вопроса.
- Хост — это имя контейнера/сервера Firebird; в docker compose — имя сервиса.
- Путь к базе — абсолютный путь на сервере.

## Параметризованные запросы

Как и везде в `database/sql` — плейсхолдером `?`:

```go
rows, err := db.Query(
    "SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEE WHERE DEPT_NO = ?", dept)
```

Пул соединений `database/sql` работает из коробки; настраивается стандартно — `db.SetMaxOpenConns()`, `db.SetMaxIdleConns()`.

## Пример целиком

Рабочий пример с этим кодом — в [репозитории сайта](https://github.com/attid/firebirdsql.su/tree/main/examples/go): Dockerfile + docker compose с Firebird 5.0.4 и демо-базой employee, пример прогоняется одной командой.

## Что почитать дальше

- [Порты Firebird](/port_3050/) — что открывать в firewall для сетевых подключений
- [Оконные функции](/window_functions/) — аналитические запросы на стороне базы
- [Глоссарий](/glossarij/) — сам язык SQL с примерами
