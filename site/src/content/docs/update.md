---
title: "UPDATE"
old_id: update
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# UPDATE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| + | + | + | + | + | + | + | + | + | + | + |
## Формат
```
UPDATE {table | view} SET 
  col = <val> [, col = <val> ...]
[WHERE <search_condition>
[PLAN plan_items]
[ORDER BY sort_items]
[ROWS <m> [TO <n>]]
[RETURNING <values> [INTO <variables>]];

<val> = {
col [<array_dim>] | <constant> | <expr> | <function>
  | NULL | USER
  }

<array_dim> = [x:y [, x:y ...]]
```
⚠️ Внешние скобки должны присутствовать в ссылке на массив.
```
<constant> = num | "string" | charsetname "string"

<expr> = Допустимое выражение SQL, которое возвращает одиночное значение.

<function> = {
CAST (<val> AS <datatype>)
  | UPPER (<val>)
  | GEN_ID (generator, <val>)
  }

<search_condition> = Смотри SELECT, для полного описания.
```

| Аргумент | Описание |
|---|---|
| table (view) | Имя существующей таблицы или вида для модификции. |
| SET col = <val> | Определяет столбцы для изменения и значения, которые требуется присвоить этим столбцам. |
| WHERE <search_cond> | Модифицировать только найденное. Определяет условия, которым строка должна удовлетворять, чтобы изменится. |

## Описание
UPDATE изменяет одну или более существующих строк в таблице или виде. UPDATE одна из привилегий базы данных контролируемых [GRANT](/grant/) и [REVOKE](/revoke/).

Факультативное предложение WHERE может быть использовано, чтобы ограничить UPDATE к некоторому подмножеству строк таблицы. Модификации не могут модифицировать секторы массива.

⚠️ Если предложение WHERE упущено, UPDATE изменяет все строки в таблице.

⚠️ Когда модифицируются BLOB столбцы, UPDATE заменяет весь BLOB целиком новым значением.

## Пример
Следующая инструкция изменяет столбцы для всех строк таблицы:
```
UPDATE CITIES SET 
  POPULATION = POPULATION * 1.03;
```

Следующая инструкция использует предложение WHERE, чтобы ограничить модификацию столбцов подмножеством строк:
```
UPDATE COUNTRY SET 
  CURRENCY = 'USDollar'
WHERE COUNTRY = 'USA';
```

## См. также
[SELECT](/select/), [INSERT](/insert/),  [UPDATE OR INSERT](/update_or_insert/),  [DELETE](/delete/),  [GRANT](/grant/),  [REVOKE](/revoke/)

## Источник
langref.pdf

[https://www.firebirdsql.org/refdocs/langrefupd25-update.html](https://www.firebirdsql.org/refdocs/langrefupd25-update.html)
