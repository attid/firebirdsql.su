---
title: "RETURNING"
old_id: returning
section: glossary
type: term
firebird:
  since: "2.0.3"
  until: 
  deprecated: false
---

# RETURNING

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Частично | Да | Да | Да | Да | ? |

## Доступно
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
INSERT INTO ... VALUES (...) [RETURNING <column_list> [INTO <variable_list>]]
INSERT INTO ... SELECT ... [RETURNING <column_list> [INTO <variable_list>]]
UPDATE OR INSERT INTO ... VALUES (...) ... [RETURNING <column_list> [INTO <variable_list>]]
UPDATE ... [RETURNING <column_list> [INTO <variable_list>]]
DELETE FROM ... [RETURNING <column_list> [INTO <variable_list>]]
```

## Описание
Позволяет вернуть значения доменов таблицы, которые были изменены в результате работы операторов [INSERT](/insert/), [UPDATE OR INSERT](/update_or_insert/), [UPDATE](/update/), [DELETE](/delete/)

Самое популярное практическое применение этого оператора - получить значение первичного ключа вновь вставленной в таблицу записи, которое было сгенерировано внутри триггера BEFORE INSERT. 

⚠️ В версии 2.0 работает только с оператором [INSERT](/insert/)

## Замечания
1. INTO часть оператора - список переменных(<variable_list>), - разрешена к использованию только в [PSQL](/raznovidnosti_jazyka_sql/) для присваивания значений локальных переменных, и запрещена в [DSQL](/raznovidnosti_jazyka_sql/).

2. В [DSQL](/raznovidnosti_jazyka_sql/) значения полей записи возвращаются в том же порядке следования, в каком они перечислены в операторе [INSERT](/insert/).

3. Если в операторе изменения данных ([INSERT](/insert/), [UPDATE OR INSERT](/update_or_insert/), [UPDATE](/update/), [DELETE](/delete/)) присутствует оператор RETURNING, то оператор представляется как процедура, следовательно программная прослойка для работы с сервером должна поддерживать оператор [EXECUTE PROCEDURE](/execute_procedure/).

//Замечания переводчика:

Внимание Delphi-разработчиков: текущие на момент написания статьи версии компонентов доступа к серверу

  1. IBX x.11 не поддерживает эту особенность;
  1. IBDAC 2.20 не поддерживает эту особенность;
  1. FIBPlus 6.80 поддерживает эту особенность

//

4. Любое изменение записи и/или удаление записи, произведенное AFTER-триггером, игнорируется оператором RETURNING. То есть Вы получите значение модифицированной записи на момент выполнения всех BEFORE-триггеров и до выполнения всех AFTER-триггеров.

5. В операторах [UPDATE](/update/) и [UPDATE OR INSERT](/update_or_insert/) в части RETURNING могут использоваться переменные [OLD](/new_old/) и [NEW](/new_old/), хранящие соответственно старое и новое значение записи.

6. В операторах [UPDATE](/update/) и [UPDATE OR INSERT](/update_or_insert/) не указанные или указанные явно при помощи имени таблицы(пседвонима) значения полей заносятся в переменную [NEW](/new_old/).

## Ограничения использования
1. Оператор изменения данных ([INSERT](/insert/), [UPDATE OR INSERT](/update_or_insert/), [UPDATE](/update/), [DELETE](/delete/)) не должен оперировать более чем с одной записью. 

//Примечание от переводчика: если в результате выполнения оператора [DELETE](/delete/) будет удалено несколько записей, то выполнение RETURNING части оператора приведет к ошибке.//

2. Оператор RETURNING в [DSQL](/raznovidnosti_jazyka_sql/) всегда возвращает одну запись, даже если не было фактически вставлено/изменено/удалено ни одной записи. Возможно, такое поведение оператора RETURNING будет изменено в будущем.

3. Недопустимо использование "*" ("звездочки") как указателя на все поля таблицы.
## Пример
Допустим, в базе данных существуют следующие объекты:
```sql
CREATE SEQUENCE MY_GENERATOR_ID;
ALTER SEQUENCE MY_GENERATOR_ID RESTART WITH 0;

CREATE TABLE MY_TABLE(
  ID   INTEGER NOT NULL PRIMARY KEY,
  NAME VARCHAR(255) DEFAULT ''
);

SET TERM !!;

CREATE OR ALTER TRIGGER TRIG_MY_TABLE_BI_000 FOR MY_TABLE
ACTIVE BEFORE INSERT POSITION 0
AS
BEGIN
  NEW.ID = GEN_ID(MY_GENERATOR_ID, 1);
END!!

SET TERM ; !!
```

Пример использования в [DSQL](/raznovidnosti_jazyka_sql/): 
* ⚠️Внимание Delphi-разработчиков: текущая на момент написания статьи версия IBX x.11 корректное выполнение оператора не поддерживает, см. выше "Замечания" п.3*
```sql
-- 1. INSERT
INSERT INTO MY_TABLE(NAME) VALUES ('Значение записи') RETURNING ID, NAME;

-- 2. UPDATE
UPDATE MY_TABLE T1 SET
  T1.NAME = 'Новое значение'
WHERE (T1.ID = 4)
RETURNING OLD.NAME, NEW.NAME;

-- 3. DELETE
DELETE FROM MY_TABLE T1 WHERE (T1.ID = 2)RETURNING NAME;
```
Пример использования в [PSQL](/raznovidnosti_jazyka_sql/):
```sql
SET TERM !!;

CREATE OR ALTER PROCEDURE MY_TABLE_INS(
  A_NAME VARCHAR(255)
)RETURNS(
  ID INTEGER,
  DESCR VARCHAR(255)
)AS
BEGIN
  INSERT INTO MY_TABLE(NAME)VALUES(:A_NAME)RETURNING ID INTO :ID;
  DESCR = 'Вставленной записи присвоен код "' || :ID || '".';
  SUSPEND;
END !!

SET TERM; !!
```

## См. также
[INSERT](/insert/),  [UPDATE](/update/), [UPDATE OR INSERT](/update_or_insert/),  [DELETE](/delete/),  [CREATE TRIGGER](/create_trigger/),  [ALTER TRIGGER](/alter_trigger/)

## Источник
($FIREBIRD)/doc/README.returning.txt
