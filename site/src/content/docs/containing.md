---
title: "CONTAINING"
old_id: containing
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CONTAINING

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Формат
<переменая> [NOT] CONTAINING <значение>

## Описание
Поиск строки содержащей text (аналог [LIKE](/like/) '%text%'). 
В отличие от [LIKE](/like/) результат не зависит от регистра

## Пример
1. Найти в таблице всех "Сидоров"
```sql
  SELECT S.* 
  FROM   sotrudnik S 
  WHERE  (S.full_fio_name CONTAINING 'Сидоров')
```

2.Исключить из набора данных всех "Сидоров", "Сидоренко", "Сидоридзе", "Сидорбаев"
```sql
  SELECT S.* 
  FROM   sotrudnik S 
  WHERE  (S.full_fio_name NOT CONTAINING 'Сидор')
```

## См. также
[LIKE](/like/)
