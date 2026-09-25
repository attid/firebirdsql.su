---
title: "DELETE"
old_id: delete
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# DELETE

## Версии сервера
Firebird v0.9       Firebird v1.0       Firebird v1.5       Firebird v2.0 

## Формат
DELETE FROM table [WHERE <search_condition>];

| Аргумент | Описание |
|---|---|
| table | Имя таблицы из которой удаляются строки. |
| <search_condition> | Условия поиска, которые определяют строки для удаления. Если это предложение не используется, DELETE воздействует на все строки в определенной таблице или представлении. |

## Описание
DELETE определяет одну или более строк, чтобы удалить из таблицы или редактируемого (updatable) вида. DELETE - одна из привилегий, которые контролируются инструкциями [GRANT](/grant/) и [REVOKE](/revoke/).

Для определения строк, которые следует удалить, может быть использовано факультативное предложение WHERE.

⚠️ Если не используется предложение WHERE,будут удалены все строки из таблицы.

## Пример
Следующая инструкция удаляет все строки из таблицы:
```
DELETE FROM EMPLOYEE_PROJECT;
```

Следующая инструкция удаляет строку для служащего #141:
```
DELETE FROM SALARY_HISTORY
WHERE EMP_NO = 141;
```
⚠️ EMP_NO это PRIMARY KEY для таблицы EMPLOYEE и по этому гарантирует уникальную идентификацию строки.

## См. также
[INSERT](/insert/),  [UPDATE](/update/),  [GRANT](/grant/),  [REVOKE](/revoke/),  [SELECT](/select/)

## Источник
langref.pdf
