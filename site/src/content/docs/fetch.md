---
title: "FETCH"
old_id: fetch
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# FETCH

## Версии сервера
Для [DSQL](/raznovidnosti_jazyka_sql/) варианта оператора
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

Для [PSQL](/raznovidnosti_jazyka_sql/) варианта оператора
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
SQL:
```
FETCH cursor
[INTO :hostvar [[INDICATOR] :indvar]
    [, :hostvar [[INDICATOR] :indvar] ...]];
```

DSQL: 
```
FETCH cursor {INTO | USING} SQL DESCRIPTOR xsqlda
```

Для BLOB: FETCH(BLOB)

| Аргумент | Описание |
|---|---|
| cursor | Имя открытого курсора из которого выбираются строки. |
| :hostvar | Переменная базового языка, чтобы сохранить значения возвращенные с помощью FETCH. |
| :invar | Индикаторная переменная, для сообщения, что столбец содержит неизвестное или NULL значение. |
| [INTO  USING] SQL DESCRIPTOR | Определяет, что значения должны быть возвращены в определенном XSQLDA. xsqlda XSQLDA переменная базового языка. |

PSQL:
```
FETCH <cursor_name> INTO <var_name> [, <var_name> ...];
```
| Аргумент | Описание |
|---|---|
| <cursor_name> | Имя открытого курсора, объявленного [DECLARE CURSOR](/declare_cursor/), из которого выбираются строки. |
| <var_name> | Определяет переменные, в которые будет помещен результат очередного FETCH |

## Описание
FETCH возвращает одну строку за один раз в программу из активного набора курсора. Первая операция FETCH возвращает первую строку из активного набора. Последующие инструкции FETCH перемещает курсор по активному набору возвращая по одной строке за один раз, пока не станет невозможным найти строку и SQLCODE не вернет значение 100.

Курсор это односторонний указатель на упорядоченный набор строк возвращаемых выражением [SELECT](/select/) в инструкции [DECLARE CURSOR](/declare_cursor/). Курсор позволяет последовательный доступ к отысканным строкам. Существует четыре связанных инструкции для работы с курсором:

| Стадия | Инструкция | Назначение |
|---|---|---|
| 1 | [DECLARE CURSOR](/declare_cursor/) | Объявляет курсор. Инструкция SELECT определяет строки возвращаемые для курсора. |
| 2 | OPEN | Отыскивает строки определенные, чтобы вернуть, с помощью [DECLARE CURSOR](/declare_cursor/). Результирующие строки становятся текущим набором курсора. |
| 3 | FETCH | Возвращает текущую строку из текущего набора, начиная с первой строки. |
| 4 | CLOSE | Закрывает курсор и освобождает системные ресурсы. |

Количество, размер, тип данных и порядок столбцов в FETCH должно быть таким же, как перечислено в выражении запроса в соответствующей инструкции [DECLARE CURSOR](/declare_cursor/).

Эта инструкция может быть использована в SQL, в DSQL и в PSQL.

⚠️ Для работы с курсорами в PSQL нужно использовать Firebird v2.0 и выше

⚠️ Важные замечания для работы с FETCH, OPEN, CLOSE, [DECLARE CURSOR](/declare_cursor/) в PSQL:
| № | замечание |
|---|---|
| 1 | Объявление курсора как переменной [DECLARE CURSOR](/declare_cursor/) разрешается только в области объявления переменных DECLARE VARIABLE PSQL-блока/хранимой процедуры/триггера. |
| 2 | Cursor names are required to be unique in the given context. They cannot interfere with FOR SELECT cursor (declared via the AS CURSOR clause) names. But a cursor can share its name with any variable in this context, as possible operations are different. |
| 3 | Positioned updates and deletes with cursors using the WHERE CURRENT OF clause are allowed. |
| 4 | Попытки извлечения данных или закрытия (вызова оператора CLOSE) FOR SELECT курсора запрещены ! |
| 5 | Попытки открыть курсор, который уже открыт при помощи оператора OPEN, а равно, как и попытки [FETCH](/fetch/) из закрытого курсора, который не был открыт при помощи оператора OPEN или закрыт оператором CLOSE, будут неудачными. |
| 6 | Все курсоры, котрые не были явно закрыты при помощи оператора CLOSE при выходе из PSQL-блока/хранимой процедуры/триггера автоматически закрываются |
| 7 | Системная контекстная переменная [ROW_COUNT](/row_count/) может быть использована для проверки, вернул ли очередной FETCH строку |

## Пример
SQL: Следующая внедренная инструкция SQL выбирает столбец из активного набора курсора:
```sql
EXEC SQL
  FETCH PROJ_CNT INTO :department, :hcnt;
```

PSQL: Следующий пример показывает принципы работы с FETCH, [DECLARE CURSOR](/declare_cursor/), OPEN, CLOSE, [ROW_COUNT](/row_count/) в ProcedureSQL.
```sql
SET TERM !!;

CREATE OR ALTER PROCEDURE GET_RELATIONS_NAMES 
RETURNS(
  RNAME CHAR(31)
)AS
  DECLARE C CURSOR FOR (SELECT RDB$RELATION_NAME FROM RDB$RELATIONS);
BEGIN
  OPEN C;
  WHILE (1 = 1) DO
  BEGIN
    FETCH C INTO :RNAME;
    IF(ROW_COUNT = 0)THEN
      LEAVE;
    SUSPEND;
  END
  CLOSE C;
END!!

SET TERM ;!!
```

PSQL: Следующий пример показывает преимущество курсоров, так как можно проходить по нескольким курсорам параллельно.

```sql
execute block returns (id int, id1 int, id2 int)
as
declare variable master_id int;
declare variable rc int;
declare d1 cursor for (select id from detail1 where master_id=:master_id);
declare d2 cursor for (select id from detail2 where master_id=:master_id);
begin
  for select id from master into master_id
  do begin
    id=master_id;
    open d1; open d2;
    while (0=0) do begin
      rc=0;
      fetch d1 into id1;
      if (row_count=0) then id1=null;
      rc=row_count;

      fetch d2 into id2;
      if (row_count=0) then id2=null;
      rc=rc+row_count;


      if (rc=0) then begin
        if (id=master_id) then suspend; -- если нет деталей, всё равно вывод
        leave;
      end
      else suspend;
      if (id=master_id) then id=null;
    end
    close d1; close d2;
  end
end
```

## См. также
CLOSE,  [DECLARE CURSOR](/declare_cursor/),  [DELETE](/delete/),  FETCH(BLOB),  OPEN,  [SELECT](/select/)

## Источник
langref.pdf
