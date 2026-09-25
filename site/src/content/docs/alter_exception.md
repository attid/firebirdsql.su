---
title: "ALTER EXCEPTION"
old_id: alter_exception
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ALTER EXCEPTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
```
ALTER EXCEPTION name "<message>";
```
| Аргумент | Описание |
|---|---|
| name | Имя существующей исключительной ситуации. |
| "<message>" | Заключенная в кавычки строка, содержащая ASCII:?: значения. |

## Описание
ALTER EXCEPTION изменяет текст в сообщении об ошибке исключительной ситуации.

Исключительная ситуация может быть изменена ее создателем и пользователем SYSDBA.

## Пример
Следующий пример изменяет сообщение исключительной ситуации.
```
ALTER EXCEPTION CUSTOMER_CHECK 'Hold shipment for customer remittance.';
```
## См. также
[CREATE EXCEPTION](/create_exception/),  [DROP EXCEPTION](/drop_exception/),  RECREATE EXCEPTION

## Источник
langref.pdf
