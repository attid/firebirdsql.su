---
title: "CREATE SEQUENCE"
old_id: create_sequence
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# CREATE SEQUENCE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/)

## Формат
```
CREATE {SEQUENCE | GENERATOR} seq_name
  [START WITH start_value]
  [INCREMENT [BY] increment]
```

## Описание
Оператор `CREATE SEQUENCE` создаёт новую последовательность (генератор) — объект базы данных, предназначенный для выдачи уникальных числовых значений, которые обычно используются в качестве суррогатных первичных ключей. Слова `SEQUENCE` и `GENERATOR` являются синонимами: можно использовать любое, однако рекомендуется применять `SEQUENCE`. Имя последовательности может содержать до 63 символов.

Необязательное предложение `START WITH` задаёт начальное значение (по умолчанию 1). В момент создания последовательности ей устанавливается значение, указанное в `START WITH`, минус значение приращения из `INCREMENT [BY]`. Если `START WITH` отсутствует, устанавливается значение 1. Таким образом, если начальное значение равно 100, а приращение 10, то первое значение, выданное оператором `NEXT VALUE FOR`, будет равно 100. До Firebird 4.0 первое значение, выданное `NEXT VALUE FOR`, было равно 110 — начальному значению плюс шаг приращения.

Необязательное предложение `INCREMENT [BY]` задаёт шаг приращения для `NEXT VALUE FOR`. По умолчанию шаг равен единице; значение приращения — 4-байтовое целое число. Для пользовательских последовательностей приращение не может быть нулём.

Значение последовательности изменяется также при обращении к функции `GEN_ID`, где параметрами указываются имя последовательности и значение приращения, которое может отличаться от заданного в `INCREMENT BY`.

## Пример
```sql
CREATE SEQUENCE seq_employee;

CREATE SEQUENCE seq_invoice
  START WITH 1000
  INCREMENT BY 10;

INSERT INTO EMPLOYEE (ID, NAME)
  VALUES (NEXT VALUE FOR seq_employee, 'Иванов');
```

## См. также
[CREATE GENERATOR](/create_generator/), [ALTER SEQUENCE](/alter_sequence/), [Типы данных](/tipy_dannyx/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
