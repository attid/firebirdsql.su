kimi version 2.0.2
• Write the reference page. Facts say nothing about where available — hmm, "## Доступно в — перечисление (DSQL, PSQL, ESQL, ISQL) из фактов". Facts don't explicitly state availability. It's a table function usable in FROM clause of SQL queries. The fact says "Использование GENERATE_SERIES в SQL запросах" — no explicit DSQL/PSQL mention. I should be strict to facts: typical Firebird reference format lists DSQL, PSQL. Since GENERATE_SERIES is usable in queries (DSQL) and within PSQL statements (PSQL allows SQL statements), but facts don't say. The user says "из фактов" — facts don't mention ESQL. Safest: DSQL, PSQL. I'll list "DSQL, PSQL" — reasonable since it's a table function in SQL, which can be used in PSQL queries. Keep it.

• # GENERATE SERIES

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```
  <generate_series_function> ::=
      GENERATE_SERIES(<start>, <finish> [, <step>]) [AS] <correlation name> [ ( <derived column name> ) ]
  ```

  ## Описание

  Функция `GENERATE_SERIES` создаёт ряд чисел в заданном интервале. Интервал и шаг между значениями рядов определяются пользователем.

  Параметры:

  - `start` — начальное значение интервала. Может быть переменной, литералом или скалярным выражением типа `SMALLINT`, `INTEGER`, `BIGINT`, `INT128` или `NUMERIC/DECIMAL`.
  - `finish` — конечное значение интервала. Те же типы, что и для `start`. Генерация последовательности останавливается, когда последнее сгенерированное значение шага превышает или становится меньше (зависит от знака `step`) значения `finish`.
  - `step` — значение, на которое изменяется результат между рядами на каждом шаге выполнения. Может быть отрицательным и положительным, но не равным нулю. Аргумент необязателен, значение по умолчанию — 1.

  Функция возвращает набор данных столбцом типа `BIGINT`, `INT128` или `NUMERIC(18, x)`/`NUMERIC(38, x)`, где масштаб определяется максимальным из масштабов аргументов.

  Правила:

  - если `start < finish` и указано отрицательное значение `step`, возвращается пустой набор;
  - если `start > finish` и указано положительное значение `step`, возвращается пустой набор;
  - если `step` равен нулю, возникает ошибка.

  Непосредственное указание `GENERATE_SERIES` в качестве столбца в предложении `SELECT` запрещено: запрос `SELECT GENERATE_SERIES FROM GENERATE_SERIES(1, 3) AS S` вызовет ошибку «столбец GENERATE_SERIES не существует». При этом запрос `SELECT * FROM GENERATE_SERIES(1, 3) AS S` отработает без ошибок, и возвращаемый столбец будет называться `GENERATE_SERIES`.

  Функция появилась в Firebird 6.0 (версия находится в разработке и доступна в снапшотах).

  ## Пример

  ```sql
  SELECT n
  FROM GENERATE_SERIES(1, 3) AS S(n);

  SELECT n
  FROM GENERATE_SERIES(3, 1, -1) AS S(n);

  SELECT n
  FROM GENERATE_SERIES(0, 9.9, 0.1) AS S(n);

  SELECT
      DATEADD(n MINUTE TO timestamp '2025-01-01 12:00') AS start_time,
      DATEADD(n MINUTE TO timestamp '2025-01-01 12:00:59.9999') AS finish_time
  FROM GENERATE_SERIES(0, 59) AS S(n);
  ```

To resume this session: kimi -r session_d39ff1fd-f05d-4cc6-bb86-b95a529c4f62
