---
title: "OVERLAY()"
old_id: overlay
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# OVERLAY()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
OVERLAY( <string1> PLACING <string2> FROM <start> [ FOR <length> ] )

## Описание
Возвращает string1 заменяя подстроку, начиная  с позиции start длиной length строкой string2.
Стартовая позиция начинается с 1, а не с 0.
Если стартовая позиция <start> или длина <length> не целочисленные, то будет применено банковское округление.
Если длина <length> не указана, то подразумевается CHAR_LENGTH( <string2> ).

Функция OVERLAY эквивалентна:
SUBSTRING(<string1>, 1 FOR <start> - 1) || <string2> ||
SUBSTRING(<string1>, <start> + <length>)

## Пример
```sql
 a = OVERLAY( str1 PLACING str2 FROM 1);
```

## См. также
[SUBSTRING](/substring/)

## Источник
2008-12-02irebird\doc\
Firebird 2.1 Release Notes Helen Borrie (Collator/Editor) 24 May 2008 - Document v.0211_00 - for Firebird 2.1.1
