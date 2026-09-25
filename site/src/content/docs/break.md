---
title: "break"
old_id: break
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# break

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| X | X | X | X | X | X | X | X | X | X | X |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
break

## Описание

Оператор прерывания цикла.

## Пример
```sql
  while (0=0) do
  begin
    if (:i>5000) then
      break;
  end
```

## См. также

## Источник
