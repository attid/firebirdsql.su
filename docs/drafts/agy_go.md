# Подключение к Firebird из Go

### Драйвер и преимущества чистого Go

Для работы с СУБД Firebird в экосистеме Go де-факто стандартом является драйвер `github.com/nakagami/firebirdsql`. Это полноценная реализация стандартного интерфейса `database/sql`, написанная на чистом Go (pure Go).

Отсутствие cgo дает критически важные преимущества:
* **Никаких внешних зависимостей:** отпадает необходимость компилировать или устанавливать клиентскую библиотеку `fbclient` (`.so` или `.dll`).
* **Простая сборка и деплой:** проект компилируется в единый статический бинарник без танцев с C-компилятором, что идеально для минималистичных Docker-контейнеров (например, Alpine или Scratch).
* **Сетевой обмен:** драйвер взаимодействует с сервером напрямую по проводу (wire protocol), используя сетевую схему `firebirdsql://`.

### Установка

Для подключения драйвера зафиксируйте проверенную версию `v0.9.21`:

```bash
go get github.com/nakagami/firebirdsql@v0.9.21
```

### Подключение и пример кода

Драйвер регистрируется через стандартный пустой импорт `_ "github.com/nakagami/firebirdsql"`, а само соединение создается привычным вызовом `sql.Open`:

```go
package main

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

    rows, err := db.Query("SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5")
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    for rows.Next() {
        var firstName, lastName string
        var salary float64
        if err := rows.Scan(&firstName, &lastName, &salary); err != nil {
            log.Fatal(err)
        }
        fmt.Printf("%s %s: %.2f\n", firstName, lastName, salary)
    }
}
```

Этот пример полностью совместим и стабильно работает с Firebird 5.0.4, а также с более ранними версиями, начиная с 2.5+. В связке с `docker-compose` имя хоста `firebird` совпадает с именем сервиса контейнера базы данных. Если приложение запускается напрямую с хостовой машины или внешней среды, просто укажите `localhost` или фактический IP-адрес сервера. Так как драйвер работает по сети, устанавливать `fbclient` на клиенте не требуется.

Встроенный в `database/sql` пул соединений работает сразу из коробки — вы можете привычно управлять пулом методами `SetMaxOpenConns`, `SetMaxIdleConns` и `SetConnMaxLifetime`.

### Параметры DSN

Формат строки подключения выглядит следующим образом:

`user:password@host:port/path?charset=UTF8`

| Параметр | Назначение | Пример |
| :--- | :--- | :--- |
| `user` | Имя пользователя базы данных | `SYSDBA` |
| `password` | Пароль пользователя | `masterkey` |
| `host` | Имя контейнера в Docker, хостнейм или IP | `firebird`, `localhost`, `10.0.0.5` |
| `port` | Порт сервиса Firebird (по умолчанию `3050`) | `3050` |
| `path` | Абсолютный путь к файлу БД на стороне сервера | `/var/lib/firebird/data/employee.fdb` |
| `charset=UTF8` | Кодировка сессии; параметр критичен для корректной передачи кириллицы | `charset=UTF8` |

### Параметризованные запросы

Никогда не склеивайте строки вручную. Драйвер поддерживает стандартные позиционные плейсхолдеры `?`:

```go
dept := "600"
rows, err := db.Query("SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEE WHERE DEPT = ?", dept)
```

С параметрами также безопасно работают вызовы `db.Exec()` и подготовленные выражения `db.Prepare()`.

### Что почитать дальше

* **Транзакции и уровни изоляции:** специфика транзакционной модели Firebird (`Read Committed`, `Concurrency`, `Consistency`) при вызове `db.BeginTx`.
* **Маппинг типов данных:** обработка `BLOB`, `TIMESTAMP WITH TIME ZONE` и нюансы `NUMERIC`/`DECIMAL`.
* **Контексты и таймауты:** отмена зависших сетевых запросов через `db.QueryContext` и `context.WithTimeout`.
