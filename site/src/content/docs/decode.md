---
title: "DECODE"
old_id: decode
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DECODE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | ? |

Функция DECODE реализует краткую запись "простого" оператора [CASE](/case/)

## Формат
```
DECODE ( <test-expr>,
         <expr>, result
         [, <expr>, result ...]
         [, defaultresult] )
```
Эквивалентная конструкция CASE:
```
CASE <test-expr>
   WHEN <expr> THEN result
   [WHEN <expr> THEN result ...]
   [ELSE defaultresult]
END
```

## Пример
Через DECODE
```sql
SELECT
    o.ID,
    o.Description,
    DECODE(o.STATUS, 
             1, 'confirmed',
             2, 'in production',
             3, 'ready',
             4, 'shipped',
                'unknown status ''' || o.STATUS || ''''
          )     
  FROM
    Orders o
```

Через [CASE](/case/)
```sql
SELECT
    o.ID,
    o.Description,
    CASE o.STATUS
      WHEN 1 THEN 'confirmed'
      WHEN 2 THEN 'in production'
      WHEN 3 THEN 'ready'
      WHEN 4 THEN 'shipped'
      ELSE 'unknown status ''' || o.STATUS || ''''
    END
  FROM
    Orders o
```
## См. также
[CASE](/case/)

## Источник
