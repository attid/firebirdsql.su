---
title: "CASE"
old_id: case
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CASE

## Версии сервера
| 0.9 | 1.0 | 1.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да |

## Формат

case [<переменная>]

when <условие> then <значение>

[when <условие> then <значение>]

[when <условие> then <значение>]

[else <значение>]

end

## Описание
Встроенная функция,
разным значениям переменой возвращает заданное значение. В случае одновременной истинности нескольких условий, функция вернет результат первого вхождения.

## Пример
# Простой case
select sl.po_number,
case sl.order_status
when 'open' then 'открыт'
when 'waiting' then 'в ожидании'
when 'shipped' then 'отгруженный'
else 'ошибка определения!!'
end
from sales sl

Поисковый case

select sl.po_number,
case
when sl.order_status = 'open' then 'открыт'
when sl.order_status = 'waiting' then 'в ожидании'
when sl.order_status = 'shipped' then 'отгруженный'
else 'ошибка определения!!' 
end
from sales sl

## См. также
[DECODE](/decode/)

[COALESCE](/coalesce/)

[IIF](/iif/)
