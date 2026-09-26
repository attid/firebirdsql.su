kimi version 2.0.2
• The user wants a reference page. Just write it. The facts cut off at the last example (DISTINCT with grouping). I should include the first 2-3 examples that are complete. Write the page to a file? The user says "Напиши справочную страницу" — probably output it, or write to a file. I'll output in the reply; maybe also save to a file? No filename given. I'll just output the page in the reply. Actually delivering as markdown in reply is fine.

  Note: "Доступно в" facts say only DSQL. So ## Доступно в — DSQL. But the prompt says "перечисление (DSQL, PSQL, ESQL, ISQL) из фактов" — use only what's in facts: DSQL.

  Описание 100-200 words, mention new in Firebird 6.0 at end.

• # LISTAGG

  ## Доступно в

  DSQL

  ## Формат

  ```
  <list_agg_function> ::=
    {LIST | LISTAGG} ([ALL | DISTINCT] <expr> [, separator])
    [ <listagg overflow clause> ] [ <within group specification> ]

  <listagg overflow clause> ::=
    ON OVERFLOW <overflow behavior>

  <overflow behavior> ::=
    ERROR | TRUNCATE [ <listagg truncation filler> ] <listagg count indication>

  <listagg count indication> ::=
    WITH COUNT | WITHOUT COUNT

  <within group specification> ::=
    WITHIN GROUP ( ORDER BY <sort specification list> )
  ```

  ## Описание

  Агрегатная функция `LISTAGG` предназначена для конкатенации значений аргумента. Она возвращает строку, состоящую из значений аргумента, отличных от `NULL` в группе, разделённых запятой или заданным пользователем разделителем. Если значений, отличных от `NULL`, нет (включая случай пустой группы), возвращается `NULL`. Тип возвращаемого результата — `BLOB`.

  Устаревший синтаксис `LIST` сохранён для обратной совместимости и является синонимом `LISTAGG`. В новых проектах рекомендуется использовать `LISTAGG`, поскольку она совместима со стандартом SQL.

  Если перед выражением указано ключевое слово `ALL` (по умолчанию), обрабатываются все значения, отличные от `NULL`. Если указано `DISTINCT`, дубликаты удаляются — кроме случаев, когда выражение является `BLOB`.

  Необязательный аргумент `separator` может быть любым строковым выражением (например, `ascii_char(13)`); по умолчанию разделителем служит запятая. Аргументы поддерживают `BLOB` любого размера и набора символов; значения даты/времени и числа неявно преобразуются к строке. Результат — текстовый `BLOB`, кроме случаев, когда выражение является `BLOB` другого подтипа.

  Порядок значений в списке определяется опцией `WITHIN GROUP (ORDER BY ...)`; без неё порядок конкатенации не определён. При указании `DISTINCT` сортировка в `WITHIN GROUP` игнорируется, за исключением случая, когда агрегированное выражение стоит первым в списке сортировки — тогда направление сортировки учитывается внутри `DISTINCT`.

  Предусмотренное стандартом SQL предложение `ON OVERFLOW` (обработка переполнения результата) не реализовано: поскольку `LISTAGG` всегда возвращает `BLOB`, оно бессмысленно и при указании молча игнорируется.

  Функция `LISTAGG` появилась в Firebird 6.0 (версия находится в разработке, доступны снапшоты).

  ## Пример

  Получение списка в алфавитном порядке с заданным разделителем:

  ```sql
  SELECT LISTAGG (display_name, '; ') WITHIN GROUP (ORDER BY display_name)
  FROM GR_WORK;
  ```

  Группировка с сортировкой в обратном алфавитном порядке:

  ```sql
  SELECT
    work_type,
    LISTAGG (display_name, '; ') WITHIN GROUP (ORDER BY display_name DESC) AS works
  FROM GR_WORK
  GROUP BY work_type;
  ```

  ---

  Примечания по странице:

  - В разделе «Доступно в» указан только DSQL — по присланным фактам другие контексты (PSQL, ESQL, ISQL) в документации не перечислены.
  - Четвёртый пример в ваших фактах обрывается (блок кода с `DISTINCT` не приведён), поэтому в раздел «Пример» я включил только два завершённых варианта. Если пришлёте текст примера с `DISTINCT`, добавлю его.

To resume this session: kimi -r session_61aa3423-9775-41eb-8544-d60cb77c39fd
