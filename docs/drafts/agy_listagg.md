# LISTAGG

## Доступно в
DSQL

## Формат
```sql
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
Агрегатная функция `LISTAGG` выполняет конкатенацию непустых (`NOT NULL`) значений аргумента в пределах группы через запятую или указанный пользователем разделитель. Если группа пуста или содержит только `NULL`, возвращается `NULL`. Результатом выполнения является текстовый `BLOB` (за исключением случаев, когда аргумент имеет другой подтип BLOB).

Устаревший синтаксис `LIST` сохранён для обратной совместимости и является полным синонимом `LISTAGG`. В новом коде рекомендуется использовать `LISTAGG` для соответствия стандарту SQL.

Аргументы `<expr>` и `separator` поддерживают строковые типы и `BLOB` произвольного размера; числовые типы и даты/время неявно приводятся к строке. Опция `DISTINCT` исключает дубликаты (не поддерживается для BLOB).

Порядок конкатенации задаётся предложением `WITHIN GROUP (ORDER BY ...)`; без него порядок значений не определён. Стандартная секция обработки переполнения `<listagg overflow clause>` не реализована и молча игнорируется сервером, поскольку результат всегда формируется в виде BLOB.

Функция является новой и доступна начиная с версии Firebird 6.0 (текущая версия в разработке).

## Пример
```sql
-- Конкатенация значений с разделителем и сортировкой по алфавиту
SELECT LISTAGG(display_name, '; ') WITHIN GROUP (ORDER BY display_name)
FROM GR_WORK;

-- Группировка с сортировкой в обратном порядке
SELECT
  work_type,
  LISTAGG(display_name, '; ') WITHIN GROUP (ORDER BY display_name DESC) AS works
FROM GR_WORK
GROUP BY work_type;
```
