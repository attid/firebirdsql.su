kimi version 2.0.2
• The user wants a reference page in Russian for RECREATE TABLE in Firebird. Format strictly. Facts provided. Note: RECREATE TABLE appeared in Firebird 3.0 (user said). "Доступно в" — from facts: DSQL. Also SQL SECURITY appeared in Firebird 3.0. Keep description 150-250 words. Write it directly as text output — user asked to "напиши справочную страницу" — probably output as text, or write a file? No file path given; just output text.

• # RECREATE TABLE

  ## Доступно в

  DSQL. Оператор появился в Firebird 3.0.

  ## Формат

  ```sql
  RECREATE [GLOBAL TEMPORARY] TABLE tablename
    [EXTERNAL [FILE] 'filespec']
    (<col_def> [, <col_def> | <tconstraint> ...])
    [ON COMMIT {DELETE | PRESERVE} ROWS]
    [SQL SECURITY {DEFINER | INVOKER}]
  ```

  Полное описание определений столбцов и ограничений таблицы смотрите в разделе CREATE TABLE.

  ## Описание

  Оператор `RECREATE TABLE` создаёт новую таблицу или пересоздаёт существующую. Если таблица с таким именем уже существует, оператор попытается удалить её и создать новую. Фактически `RECREATE TABLE` — это последовательность `DROP TABLE` + `CREATE TABLE`, выполняемая одним оператором: вместо двух команд вы пишете одну, и вам не нужно заранее проверять, существует ли таблица. Это удобно в установочных и обновляющих скриптах, когда структуру объекта нужно гарантированно привести к эталонному виду.

  Оператор `RECREATE TABLE` не выполнится, если существующая таблица имеет зависимости (на неё ссылаются ограничения, представления, триггеры, PSQL-модули и т. п.). В этом случае удаление старой таблицы будет отвергнуто, и новая таблица создана не будет.

  В отличие от `ALTER TABLE`, который изменяет структуру существующей таблицы по частям (добавляет, изменяет или удаляет столбцы и ограничения), `RECREATE TABLE` пересоздаёт таблицу целиком, с полным определением, заданным в операторе. При этом все данные существующей таблицы безвозвратно уничтожаются вместе с ней. Поэтому для таблиц, содержащих данные, которые нужно сохранить, следует использовать `ALTER TABLE`.

  По синтаксису `RECREATE TABLE` повторяет `CREATE TABLE`, включая определения столбцов и табличных ограничений, внешние таблицы (`EXTERNAL FILE`), глобальные временные таблицы (`GLOBAL TEMPORARY`) и указание контекста безопасности (`SQL SECURITY`).

  ## Пример

  Пересоздание таблицы `EMPLOYEES` с новой структурой:

  ```sql
  RECREATE TABLE EMPLOYEES
  (
    ID          INTEGER NOT NULL,
    LAST_NAME   VARCHAR(50) NOT NULL,
    FIRST_NAME  VARCHAR(50) NOT NULL,
    HIRED       DATE DEFAULT CURRENT_DATE,
    CONSTRAINT PK_EMPLOYEES PRIMARY KEY (ID)
  );
  ```

  Если таблица `EMPLOYEES` уже существует, она будет удалена и создана заново с указанной структурой; все данные, хранившиеся в ней ранее, будут потеряны. Если на старую таблицу существуют зависимости, оператор завершится с ошибкой, и таблица пересоздана не будет.

To resume this session: kimi -r session_7274cb8f-2d07-4665-baa1-1647cccb1e9b
