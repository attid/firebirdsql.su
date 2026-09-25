---
title: "RECREATE VIEW"
old_id: recreate_view
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# RECREATE VIEW

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
RECREATE VIEW viewname [<full_column_list>]
AS <select_statement>
[WITH CHECK OPTION];

<full_column_list> ::= (colname [, colname ...])
```

## Описание
`RECREATE VIEW` создаёт новое представление или пересоздаёт существующее под тем же именем. По сути это последовательное выполнение `DROP VIEW` и `CREATE VIEW` одной операцией: если представление с именем `viewname` уже существует, сервер пытается удалить его и создать заново по определению из `select_statement`.

Имя представления может содержать до 63 символов. Необязательный список `full_column_list` задаёт имена столбцов представления; дубликаты в нём не допускаются. Предложение `WITH CHECK OPTION` контролирует изменения данных через представление.

Ключевое отличие от `ALTER VIEW` — в природе операции. Поскольку это удаление с последующим созданием, оператор не выполнится, если существующее представление имеет зависимости (другие представления, процедуры, триггеры, ссылающиеся на него). Даже при успешном пересоздании привязанные к старому объекту свойства теряются и должны быть восстановлены.

Удобен, когда представление создаётся с нуля или определение полностью меняется и зависимостей гарантированно нет: не нужно отслеживать существование объекта. Для точечной корректировки определения представления с зависимостями используйте `ALTER VIEW`.

## Пример
```sql
RECREATE VIEW ACTIVE_CLIENTS (ID, NAME, CITY)
AS
SELECT CLIENT_ID, CLIENT_NAME, CITY
FROM CLIENTS
WHERE STATUS = 'ACTIVE';
```

## См. также
[CREATE VIEW](/create_view/), [RECREATE TABLE](/recreate_table/), [DISTINCT](/distinct/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
