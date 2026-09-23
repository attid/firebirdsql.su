---
title: "ALTER DOMAIN"
old_id: alter_domain
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ALTER DOMAIN

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
```sql
ALTER DOMAIN name {
[SET DEFAULT {literal | NULL | USER}]
  | [DROP DEFAULT]
  | [ADD [CONSTRAINT] CHECK (<dom_search_condition>)]
  | [DROP CONSTRAINT]
  };

<dom_search_condition> = {
VALUE <operator> <val>
  | VALUE [NOT] BETWEEN <val> AND <val>
  | VALUE [NOT] LIKE <val> [ESCAPE <val>]
  | VALUE [NOT] IN (<val> [, <val> ...])
  | VALUE IS [NOT] NULL
  | VALUE [NOT] CONTAINING <val>
  | VALUE [NOT] STARTING [WITH] <val>
  | (<dom_search_condition>)
  | NOT <dom_search_condition>
  | <dom_search_condition> OR <dom_search_condition>
  | <dom_search_condition> AND <dom_search_condition>
  }

<operator> = {= | < | > | <= | >= | !< | !> | <> | !=}
```

| Аргумент | Описание |
|---|---|
| name | Имя существующего домена. |
| SET DEFAULT | Определяет значение столбца по умолчанию, которое будет введено, когда ни какой другой ввод не сделан. |
| DROP DEFAULT | Удаляет существующее значение по умолчанию. |
| ADD [CONSTRAINT] CHECK (<dom_search_condition>) | Добавляет CHECK ограничения в определение домена. Определение домена может включать только одно CHECK ограничение. |
| DROP CONSTRAINT | Удаляет CHECK ограничения из определения домена. |

## Описание
ALTER DOMAIN изменяет любые свойства существующего домена, кроме типа данных и установки NOT NULL. Изменения, над доменом воздействуют на все столбцы, основанные на домене, которые не были отменены на уровне таблицы.

Обратите внимание: Для изменения типа данных или установки NOT NULL, удалите домен и создаете его заново с желаемыми свойствами.

Домен может быть изменен его создателем или пользователем SYSDBA.

## Пример

Следующая инструкция создает домен с допустимыми значениями > 1000, за тем устанавливает его значение по умолчанию к 9999.

```sql
CREATE DOMAIN CUSTNO
  AS INTEGER
    CHECK (VALUE > 1000);

ALTER DOMAIN CUSTNO SET DEFAULT 9999;
```

## См. также
[CREATE DOMAIN](/create_domain/),  [DROP DOMAIN](/drop_domain/),  [CREATE TABLE](/create_table/)

## Источник
langref.pdf
