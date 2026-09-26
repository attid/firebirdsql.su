kimi version 2.0.2
• The user wants a reference page written. Just write it directly in the response. Facts: available in DSQL only (per facts — "Доступно в DSQL" only). Syntax ANY_VALUE(<expression>). Description 100-200 words, mention Firebird 6.0 at end.

• # ANY VALUE

  ## Доступно в

  DSQL

  ## Формат

  ```
  ANY_VALUE(<expression>)
  ```

  Параметр `expr` — выражение. Может содержать столбец таблицы, литерал, переменную, выражение, неагрегатную функцию или UDF.

  Тип возвращаемого результата — тот же, что и у аргумента функции `<expression>`.

  ## Описание

  Агрегатная функция `ANY_VALUE` возвращает некоторое значение `<expression>` для группы строк. Функция является недетерминированной: она не гарантирует, какое именно значение из группы будет возвращено. Значения `NULL` игнорируются; `NULL` возвращается только в случае отсутствия записей, значение выражения которых отличается от `NULL`.

  Типичное применение `ANY_VALUE` — упрощение запросов с `GROUP BY`, когда в список выборки нужно включить столбцы, значения которых одинаковы внутри группы (например, зависящие от столбца группировки, являющегося первичным ключом). Стандарт SQL требует, чтобы все неагрегатные выражения из списка `SELECT` присутствовали в `GROUP BY`, но оборачивание такого выражения в `ANY_VALUE` позволяет избежать группировки по дополнительным столбцам.

  Раньше в тех же целях применялись функции `MIN` или `MAX`, однако вычисление `ANY_VALUE` дешевле: `MIN`/`MAX` требуют сравнения значений, тогда как `ANY_VALUE` просто возвращает первое попавшееся значение в группе.

  Функция появилась в Firebird 6.0, который на момент написания находится в разработке и доступен в виде снапшот-сборок.

  ## Пример

  Использование `ANY_VALUE`, чтобы не добавлять `FIRST_NAME` и `LAST_NAME` в `GROUP BY` (поле `EMP_NO` — первичный ключ и уже обеспечивает уникальность сотрудника):

  ```sql
  SELECT
    EMPLOYEE.EMP_NO,
    ANY_VALUE(EMPLOYEE.FIRST_NAME) AS FIRST_NAME,
    ANY_VALUE(EMPLOYEE.LAST_NAME) AS LAST_NAME,
    SUM(SALES.TOTAL_VALUE) AS TOTAL_SUM,
    COUNT(*) AS CNT
  FROM
    SALES
    JOIN EMPLOYEE ON EMPLOYEE.EMP_NO = SALES.SALES_REP
  GROUP BY 1;
  ```

  Эквивалентный запрос без `ANY_VALUE` требует группировки по всем неагрегатным столбцам и обходится дороже:

  ```sql
  SELECT
    EMPLOYEE.EMP_NO,
    EMPLOYEE.FIRST_NAME AS FIRST_NAME,
    EMPLOYEE.LAST_NAME AS LAST_NAME,
    SUM(SALES.TOTAL_VALUE) AS TOTAL_SUM,
    COUNT(*) AS CNT
  FROM
    SALES
    JOIN EMPLOYEE ON EMPLOYEE.EMP_NO = SALES.SALES_REP
  GROUP BY 1, 2, 3;
  ```

  ---

  Примечания по странице:
  - В разделе «Доступно в» указан только DSQL — в присланных фактах перечислен лишь он (PSQL/ESQL/ISQL в источнике не заявлены, добавлять их от себя не стал).
  - Описание уложено в ~190 слов, упоминание о Firebird 6.0 — последним предложением раздела, как требовалось.

To resume this session: kimi -r session_186a083a-1909-433f-89bc-27e876363d97
