kimi version 2.0.2
• The user wants an article written. Should I write it to a file or output it? They say "Напиши статью ... для русскоязычного справочника firebirdsql.su". I'll write a Markdown file and also show it. Writing to /tmp seems odd; maybe just output the article as the deliverable. I'll create a file and present the content in the final message. Actually the deliverable is the article text itself — I'll output it directly. Maybe also save to file for convenience. I'll just output it in the reply; creating an unrequested file isn't needed. Actually saving a file could help, but instructions say don't create unsolicited files. Output the article in the reply.

  350-500 words. Russian. Structure per spec.

• # Подключение к Firebird из Go

  Firebird и Go сочетаются отлично: для работы с базой не нужно ни cgo, ни установки клиентских библиотек — достаточно одного пакета. Разбираем, как подключиться и выполнить первый запрос.

  ## Драйвер

  Используем [github.com/nakagami/firebirdsql](https://github.com/nakagami/firebirdsql) — драйвер `database/sql`, написанный на чистом Go. Актуальная версия — **v0.9.21**, имя драйвера и протокол — `firebirdsql://`.

  Почему «чистый Go» — это плюс:

  - **Без cgo.** Бинарник собирается статически и кросс-компилируется под любую платформу одной командой — не нужен C-тулчейн на сборочной машине.
  - **Без fbclient.** Драйвер сам реализует сетевой протокол Firebird, поэтому на машине с приложением не нужно ставить клиентскую библиотеку Firebird. Приложение общается с сервером напрямую по TCP.
  - **Стандартный интерфейс.** Работа идёт через привычный `database/sql`: пул соединений, транзакции, подготовленные запросы — всё из коробки.

  ## Установка

  ```bash
  go get github.com/nakagami/firebirdsql@v0.9.21
  ```

  ## Подключение

  Драйвер регистрируется через импорт с пустым идентификатором, дальше — обычный `sql.Open`:

  ```go
  import (
      "database/sql"
      "fmt"
      "log"
      _ "github.com/nakagami/firebirdsql"
  )

  dsn := "SYSDBA:masterkey@firebird:3050/var/lib/firebird/data/employee.fdb?charset=UTF8"
  db, err := sql.Open("firebirdsql", dsn)
  ```

  Выборка данных — стандартными средствами `database/sql`:

  ```go
  rows, err := db.Query("SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5")
  ```

  Пример проверен с Firebird 5.0.4 (подойдёт и 2.5+) в docker-compose: там хост `firebird` — это имя контейнера сервиса базы. Если сервер стоит отдельно, вместо `firebird` указывайте `localhost` или IP сервера. Помните: драйвер работает по сети, так что сервер должен принимать TCP-подключения на порту 3050.

  Обратите внимание: `sql.Open` не устанавливает соединение сразу, а лишь готовит пул. Реальное подключение появится при первом запросе (или после `db.Ping()`). Пул соединений `database/sql` работает без всякой настройки — просто используйте `db` из разных горутин, это безопасно.

  ## Параметры DSN

  Строка подключения имеет вид `user:password@host:port/path?charset=UTF8`:

  - **user:password** — логин и пароль (в примере `SYSDBA:masterkey`);
  - **host:port** — адрес сервера и порт (по умолчанию 3050);
  - **path** — путь к файлу базы **на сервере** или её алиас;
  - **charset=UTF8** — кодировка соединения; для корректной работы с кириллицей указывайте `UTF8` явно.

  ## Параметризованные запросы

  Значения в запросы подставляйте через плейсхолдеры `?`, а не конкатенацией строк — это защищает от SQL-инъекций и упрощает экранирование:

  ```go
  rows, err := db.Query("... WHERE DEPT = ?", dept)
  ```

  ## Что почитать дальше

  Темы для продолжения:

  - транзакции в `database/sql` (`db.Begin`, `tx.Commit`, `tx.Rollback`);
  - подготовленные запросы (`db.Prepare`) для повторяющихся операций;
  - настройка пула: `SetMaxOpenConns`, `SetConnMaxLifetime`;
  - хранимые процедуры Firebird и вызов их из Go;
  - события Firebird (events) и поддержка их в драйвере.

To resume this session: kimi -r session_f6f7d323-21ed-4503-b777-df17ec15182e
