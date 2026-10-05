kimi version 2.0.2
• Write the article in Markdown, Russian, 350-500 words. Just output it in the final message? The user asked to write an article — I should deliver it. Probably write to a file too? The user didn't specify a file. Working directory /tmp. I'll just output the article as the reply. Actually writing a file could be useful, but instructions say don't create unsolicited files. Just respond with the article text.

• # Подключение к Firebird из Python

  Если вам нужно быстро и без нативных зависимостей подключиться к Firebird из Python-скрипта — самый простой путь это драйвер **firebirdsql**. Он написан на чистом Python, не требует ни `fbclient`, ни каких-либо системных библиотек, и поэтому идеально ставится в контейнеры и виртуальные окружения.

  ## Установка

  ```bash
  pip install firebirdsql==1.4.7
  ```

  ## Подключение и выполнение запроса

  ```python
  import firebirdsql

  con = firebirdsql.connect(
      dsn="firebird:/var/lib/firebird/data/employee.fdb",
      user="SYSDBA",
      password="masterkey",
      charset="utf-8",
  )
  cur = con.cursor()
  cur.execute("SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5")
  for first, last, salary in cur.fetchall():
      print(f"  {first} {last} — {salary:.2f}")
  con.close()
  ```

  DSN имеет формат `host:path` — имя или адрес сервера, двоеточие и путь к файлу базы на сервере. Параметр `charset="utf-8"` указывайте всегда, если в базе есть кириллица — иначе получите кракозябры или ошибки кодирования.

  ## Важно: не указывайте порт явно

  > **Проверено на практике с Firebird 5 и firebirdsql 1.4.7.** Документация драйвера допускает DSN вида `host:port:path`, но при явном указании порта — например `firebird/3050:/var/lib/firebird/data/employee.fdb` — подключение падает с ошибкой **«unavailable database»**.
  >
  > Решение простое: порт опускается. Пишите `firebird:/path/to/base.fdb` — будет использован порт 3050 по умолчанию, и всё подключится.

  ## Параметризованные запросы

  Никогда не подставляйте значения в SQL конкатенацией строк. Драйвер поддерживает параметры через `?`:

  ```python
  cur.execute("SELECT * FROM EMPLOYEE WHERE DEPT_NO = ?", (dept,))
  ```

  Вторым аргументом передаётся кортеж значений — по одному на каждый плейсхолдер `?`. Так безопаснее (защита от SQL-инъекций) и часто быстрее, потому что сервер может переиспользовать подготовленный запрос.

  ## Альтернативные драйверы

  Если firebirdsql чем-то не подошёл, есть варианты:

  - **firebird-driver** — официальный драйвер от команды Firebird. Активно развивается, но требует установленной клиентской библиотеки `fbclient`.
  - **fdb** — предшественник firebird-driver, тоже требует `fbclient`. Проект фактически легаси, для новых разработок брать не стоит.

  Оба варианта тянут за собой нативную библиотеку, что усложняет сборку контейнеров и установку в чистый venv. Именно поэтому для простых синхронных скриптов firebirdsql — самый беспроблемный выбор: `pip install`, и работает.

  ## Что почитать дальше

  - **Асинхронная работа с Firebird через SQLAlchemy** — отдельная статья, если ваш проект на asyncio и нужен ORM/пул соединений.
  - **Транзакции в Firebird**: уровни изоляции и зачем нужен `con.commit()` после изменений.
  - **Миграция данных между базами Firebird** скриптами на Python.

  ---

  Статья готова: ~400 слов, Markdown, все факты из ТЗ включены — код дословно, нюанс с портом отдельным врезом, charset, параметризация через `?`, список альтернатив и блок «что почитать дальше» с отсылкой к асинхронной статье.

To resume this session: kimi -r session_1b9f939c-36c7-4aed-a16e-cd8f4382f05a
