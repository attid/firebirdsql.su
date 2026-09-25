---
title: "COALESCE"
old_id: coalesce
section: glossary
type: term
firebird:
  since: "1.5.3"
  until: 
  deprecated: false
---

# COALESCE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | ? |

## Формат
COALESCE ( значение1, значение2[,значение3[,значение4]])

## Описание
Встроенная функция.
Возвращает первое не NULL значение из списка

COALESCE упрощенная форма CASE к примеру
COALESCE (V1, V2)
можно заменить : 
CASE WHEN V1 IS NOT NULL THEN V1 ELSE V2 END

COALESCE (V1, V2,…, Vn)
можно заменить : 
CASE WHEN V1 IS NOT NULL THEN V1 ELSE COALESCE (V2,…,Vn) END
и так далее

## Пример
select c.customer, coalesce(c.address_line2,'не задан')
from customer c

## См. также
[IF](/if/), [CASE](/case/), [IIF](/iif/)
