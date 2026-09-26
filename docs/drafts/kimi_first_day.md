kimi version 2.0.2
• Write the reference page. Just output markdown. Facts: DSQL, PSQL only (no ESQL/ISQL in facts — format says перечисление из фактов, so DSQL, PSQL). Description 100-200 words in Russian. Examples 1-2 meaningful SQL examples.

• # FIRST_DAY

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```
  FIRST_DAY(OF <period> FROM date_or_timestamp)

  <period> ::= YEAR | QUARTER | MONTH | WEEK
  ```

  **Параметры**

  | Параметр | Описание |
  |---|---|
  | date_or_timestamp | Выражение типа `DATE` или `TIMESTAMP [WITH \| WITHOUT] TIME ZONE` |

  **Тип возвращаемого результата:** `DATE` или `TIMESTAMP [WITH | WITHOUT] TIME ZONE`

  ## Описание

  Функция `FIRST_DAY` возвращает первый день периода — года, квартала, месяца или недели, — которому принадлежит заданная дата или отметка времени. Период задаётся ключевым словом после `OF`: `YEAR`, `QUARTER`, `MONTH` или `WEEK`.

  Тип результата совпадает с типом аргумента: для выражения типа `DATE` возвращается `DATE`, для `TIMESTAMP` — `TIMESTAMP` соответствующей разновидности (с часовым поясом или без). При этом, если аргумент имеет тип `TIMESTAMP`, возвращаемое значение сохраняет временную часть исходного значения — сдвигается только дата.

  При вычислении первого дня недели (`WEEK`) первым днём недели считается воскресенье, в соответствии с тем, что возвращает функция `EXTRACT` с частью `WEEKDAY`. Это важно учитывать в локалях, где неделя традиционно начинается с понедельника: результат может отличаться от ожидаемого.

  Функция удобна для группировки и агрегирования данных по календарным периодам, построения отчётов и вычисления границ интервалов. Обратной операцией является функция `LAST_DAY`, возвращающая последний день периода.

  ## Пример

  ```sql
  -- Первый день текущего месяца
  SELECT FIRST_DAY(OF MONTH FROM current_date) FROM rdb$database;

  -- Первый день недели (воскресенье) для заданной даты
  SELECT FIRST_DAY(OF WEEK FROM date '2017-11-01') FROM rdb$database;
  ```

To resume this session: kimi -r session_c1bb541e-0e2a-4471-b9b0-d6b8e902f51f
