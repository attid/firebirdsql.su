kimi version 2.0.2
• Write an article in Russian, 400-600 words, Markdown, table of keys, code verbatim from facts. Deliver as markdown file? User says "напиши статью" for a directory site. Probably output the article text; maybe save to file. I'll write it to /tmp/gstat-firebird.md and also present content. Actually simplest: write the file and show it. Let me just write the article.518 /tmp/gstat-firebird.md
518 words (wc counts code too, but roughly in range). Deliver article in final message.

• Готово — статья сохранена в `/tmp/gstat-firebird.md` (≈500 слов, таблица ключей на месте). Вот текст:

  # gstat: статистика базы данных Firebird

  База «попухла», запросы вдруг пошли по плохим планам, бэкап растёт быстрее данных? Прежде чем гадать, загляните внутрь — штатная утилита **gstat** показывает статистику базы на уровне страниц: версии записей, состояние индексов, занятое и свободное место. Это диагност, а не лекарство: gstat отвечает на вопрос «что происходит», но ничего не чинит.

  ## Где лежит и как запускается

  gstat входит в поставку Firebird: `bin/gstat` в каталоге установки (обычно `/opt/firebird/bin/gstat` на Linux). Запуск требует имени базы и прав администратора, сервер при этом может работать — останавливать ничего не нужно. На локальной машине:

  ```
  gstat -u SYSDBA -p пароль -h /data/bases/mydb.fdb
  ```

  ## Ключи

  | Ключ | Что показывает |
  |------|----------------|
  | `gstat -a база` | всё (all): заголовок, данные, индексы |
  | `gstat -d база` | страницы данных: версии записей, цепочки версий |
  | `gstat -i база` | индексы: глубина, дубликаты, заполненность страниц |
  | `gstat -t TABLE1 TABLE2 база` | только указанные таблицы (имя таблицы, регистр важен) |
  | `gstat -h база` | заголовок базы: ODS, page size, счётчики sweep, лимиты |

  ## Как читать вывод

  **Заголовок (`-h`)** — первым делом смотрите сюда:

  ```
  Attributes                force write
  ODS version               13.1
  Page size                 16384
  Sweep interval            20000
  Oldest transaction        104512
  Oldest active             340987
  Next transaction          341002
  ```

  Если между *Oldest transaction* и *Next transaction* пропасть в сотни тысяч — в базе застряла долгая транзакция, и мусор не собирается. Это главный источник раздувания.

  **Данные (`-d`)** — секция по каждой таблице:

  ```
  ORDERS (142)
      Primary pointer page: 305, Index root page: 306
      Average record length: 118.40, total records: 1520340
      Average version length: 96.12, total versions: 845120
  ```

  Обращайте внимание на *Average record length*, *Average version length* и число *versions*. Много версий записей — значит, накопился недособранный мусор: кто-то держит длинную транзакцию, и старые версии строк не удаляются. Отсюда рост файла и тормоза при чтении.

  **Индексы (`-i`)**:

  ```
  Index IX_ORDERS_DATE (3)
      Depth: 3, leaf buckets: 4210, nodes: 1520340
      Average data length: 4.20, total dup: 12
      Fill distribution:
           80 - 99% = 3901
  ```

  Смотрите *depth*: глубина 1–3 — нормально, 4 и больше — повод перестроить индекс. *Average data length* и *Fill distribution* показывают, насколько плотно заполнены страницы: пустые наполовину страницы — лишние чтения с диска.

  ## Грабли

  - **gstat — диагностика, а не уборка.** Он не покажет «что удалить». Мусор убирается sweep-ом (`gfix -sweep`) или просто итерациями транзакций, если застрявших долгожителей нет.
  - **`-a` на большой базе тормозит сервер** — утилита читает всё. Берите `-t` по конкретным подозрительным таблицам.
  - **ODS базы должен совпадать с версией gstat**: gstat от Firebird 2.5 не откроет базу 5.0. Пользуйтесь утилитой из той же поставки, что и сервер.
  - После чистки мусора проверьте результат тем же gstat — цифры *versions* и разрыв транзакций в заголовке должны уменьшиться.

  Если хочется GUI и графиков вместо консоли, посмотрите **IBAnalyst** или мониторинг в **HQbird** — они строят отчёты по тем же данным.

  ## Что почитать дальше

  - **gfix -sweep** — принудительная уборка мусора и сброс OIT;
  - **gbak** — резервная копия (заодно чистит мусор при backup/restore);
  - **nbackup** — инкрементные копии больших баз;
  - **таблицы мониторинга** (`MON$TRANSACTIONS`, `MON$TABLE_STATS`) — кто именно держит долгую транзакцию прямо сейчас.

  Статья заточена под запрос «gstat firebird»: заголовок-H1 с ключом, боли админа (раздувание, плохие планы) в первом абзаце, дальше быстрый ответ «как запустить и что смотреть». Если нужны мета-теги (title/description) для посадочной — скажите, добавлю.

To resume this session: kimi -r session_39aad485-44a9-4ea9-bc43-b5e135a8b7c1
