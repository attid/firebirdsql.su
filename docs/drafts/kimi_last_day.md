kimi version 2.0.2
• Write the reference page in Russian, strictly per format. Should I write it to a file or just output? The user says "Напиши справочную страницу" — likely output in reply. I'll output the page content directly. Facts: available DSQL, PSQL (not ESQL, ISQL — use facts only). Format code block verbatim. Description 100-200 words. Example: 1-2 meaningful SQL examples.

• # LAST_DAY

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```
  LAST_DAY(OF <period> FROM date_or_timestamp)

  <period> ::=  YEAR | QUARTER | MONTH | WEEK
  ```

  ## Описание

  Функция `LAST_DAY` возвращает последний день указанного периода — года, квартала, месяца или недели — для заданной даты или отметки времени.

  Параметр `date_or_timestamp` — выражение типа `DATE` или `TIMESTAMP [WITH | WITHOUT] TIME ZONE`. Тип возвращаемого результата соответствует типу аргумента: `DATE` или `TIMESTAMP [WITH | WITHOUT] TIME ZONE`. При передаче выражения типа `TIMESTAMP` возвращаемое значение сохраняет временную часть исходной отметки времени.

  Период задаётся ключевым словом после `OF`:

  - `YEAR` — последний день года;
  - `QUARTER` — последний день квартала;
  - `MONTH` — последний день месяца;
  - `WEEK` — последний день недели.

  Обратите внимание: последним днём недели считается суббота — в соответствии с тем, что возвращает функция `EXTRACT` с частью `WEEKDAY`.

  Функция удобна для вычисления границ отчётных периодов, расчёта дат окончания подписок, биллинга и других задач, где требуется дата конца периода, содержащего заданную дату.

  ## Пример

  ```sql
  SELECT LAST_DAY(OF MONTH FROM current_date) FROM rdb$database;
  SELECT LAST_DAY(OF YEAR FROM current_timestamp) FROM rdb$database;
  SELECT LAST_DAY(OF WEEK FROM date '2017-11-01') FROM rdb$database;
  ```

To resume this session: kimi -r session_83f79c88-36ae-46c4-b951-ed76aa944828
