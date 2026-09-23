---
title: "DECLARE CURSOR"
old_id: declare_cursor
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DECLARE CURSOR

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [DSQL](/raznovidnosti_jazyka_sql/) | - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |
| [PSQL](/raznovidnosti_jazyka_sql/) | - | - | - | - | - | Да | Да | Да | Да | Да | Да |

## Формат
[SQL](/raznovidnosti_jazyka_sql/): 
```
DECLARE cursor CURSOR FOR <select> [FOR UPDATE OF <col> [, <col>...]];
```

[DSQL](/raznovidnosti_jazyka_sql/):
```
DECLARE cursor CURSOR FOR <statement_id>
```

BLOB: DECLARE CURSOR(BLOB)

[PSQL](/raznovidnosti_jazyka_sql/) (⚠️ Firebird v2.0 и выше):
```
DECLARE [VARIABLE] <cursor_name> CURSOR FOR (<select_statement>);
```
| Аттрибут | Значение |
|---|---|
| <cursor_name> | Имя переменной курсора. К нему применимы правила объявления локальных переменных в [PSQL](/raznovidnosti_jazyka_sql/) |
| <select_statement> | Оператор выбора набора данных [SELECT](/select/) |

## Описание
DECLARE CURSOR определяет набор данных, который может быть возвращен, при обращении к этому курсору. Это первая инструкция, из группы инструкций работы с курсором, которая должна быть использована в работе с ним.

<select> определяет инструкцию [SELECT](/select/), которая определяет, какой набор данных необходимо вернуть. Инструкция [SELECT](/select/) не должна включать предложения [INTO](/select/) и [ORDER BY](/select/).

Предложение FOR UPDATE OF необходимо, для модификации или удаления значений из набора данных.

Курсор это однонаправленный указатель на упорядоченный набор данных, возвращенных выражением [SELECT](/select/) в инструкции DECLARE CURSOR, позволяющий получить последовательный <u>однонаправленный</u> доступ к возвращенным даныым. 

Есть четыре связанных инструкции для работы с курсором:

| Стадия | Инструкция | Назначение |
|---|---|---|
| 1 | DECLARE CURSOR | Объявляет курсор. Инструкция [SELECT](/select/) определяет набор данных, возвращаемый для курсора. |
| 2 | OPEN | Открывает набор данных на последовательный <u>однонаправленный</u> доступ. |
| 3 | FETCH | Возвращает текущую строку из текущего набора данных, начиная с первой строки. |
| 4 | CLOSE | Закрывает курсор и освобождает системные ресурсы. |

Эта инструкция может быть использована в [SQL](/raznovidnosti_jazyka_sql/), [DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/).
⚠️ Для работы с курсорами в [PSQL](/raznovidnosti_jazyka_sql/) нужно использовать Firebird v2.0 и выше.

⚠️ Важные замечания для работы с FETCH, OPEN, CLOSE, DECLARE CURSOR в [PSQL](/raznovidnosti_jazyka_sql/):
| № | замечание |
|---|---|
| 1 | Объявление курсора как переменной DECLARE CURSOR разрешается только в области объявления переменных DECLARE VARIABLE [PSQL](/raznovidnosti_jazyka_sql/)-блока/хранимой процедуры/триггера. |
| 2 | Имена курсоров должны быть уникальны в текущем контексте. They cannot interfere with FOR SELECT cursor (declared via the AS CURSOR clause) names. But a cursor can share its name with any variable in this context, as possible operations are different. |
| 3 | Операция обновления и удаления в курсоре использует WHERE CURRENT OF clause are allowed. |
| 4 | Попытки извлечения данных или закрытия (вызова оператора CLOSE) FOR SELECT курсора запрещены ! |
| 5 | Попытки открыть курсор, который уже открыт при помощи оператора OPEN, а равно, как и попытки FETCH из закрытого курсора, который не был открыт при помощи оператора OPEN или закрыт оператором CLOSE, будут неудачными. |
| 6 | Все курсоры, котрые не были явно закрыты при помощи оператора CLOSE при выходе из [PSQL](/raznovidnosti_jazyka_sql/)-блока/хранимой процедуры/триггера автоматически закрываются |
| 7 | Системная контекстная переменная [ROW_COUNT](/row_count/) может быть использована для проверки, вернул ли очередной FETCH строку |
| 8 | SELECT запрос может содержать имена параметров, например: “select name from names where number = :num” Каждый параметр должен быть ранее объявленной переменной (включая входящие/выходящие параметры процедуры). Когда курсор открывается - параметры получают текущее значенее одноименных переменных. |

## Пример
Следующая внедренная инструкция SQL объявляет курсор с условиями поиска:
```
EXEC SQL
  DECLARE C CURSOR FOR
  SELECT CUST_NO, ORDER_STATUS
  FROM SALES
  WHERE ORDER_STATUS IN ("open", "shipping");
```

Следующая инструкция [DSQL](/raznovidnosti_jazyka_sql/) объявляет курсор для предварительно приготовленной инструкции QUERY1:
```
DECLARE Q CURSOR FOR QUERY1
```

[PSQL](/raznovidnosti_jazyka_sql/): Следующий пример показывает принципы работы с FETCH, DECLARE CURSOR, OPEN, CLOSE, [ROW_COUNT](/row_count/) в [PSQL](/raznovidnosti_jazyka_sql/).
```
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

## См. также
DECLARE CURSOR(BLOB),  PREPARE,  [SELECT](/select/)

## Источник
langref.pdf
