---
title: "DROP GENERATOR"
old_id: drop_generator
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DROP GENERATOR

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
```
DROP GENERATOR <наименование>;
```

## Описание
Оператор, удаляющий генератор <наименование> в текущей БД.

Удалить генератор может либо его владелец либо SYSDBA при условии что его нет в зависимостях других обьектов. Например, генератор не используется в триггерах/хранимых процедурах.

:?: Узнать список объектов где используется генератор (допустим с именем **MY_GENERATOR**) можно при помощи следующего скрипта:
```
SELECT D.RDB$DEPENDENT_NAME, T.RDB$TYPE_NAME
FROM   RDB$DEPENDENCIES D, RDB$TYPES T
WHERE  (D.RDB$DEPENDED_ON_NAME = 'MY_GENERATOR')
  AND  (T.RDB$TYPE = D.RDB$DEPENDENT_TYPE)
  AND  (T.RDB$FIELD_NAME = 'RDB$OBJECT_TYPE')
```

⚠️ Конструкция появилась только в Firebird v1.5. В ранних версиях сервера удалить созданный генератор [CREATE GENERATOR](/create_generator/) средствами DDL было невозможно. Для удаления генератора в более ранних версиях сервера использовался оператор DML 
```
DELETE FROM RDB$GENERATORS R WHERE (R.RDB$GENERATOR_NAME = 'GEN_CUSTOMERS_ID');
```

⚠️ Конструкция считается устаревшей. Для управления генераторами рекомендуется использовать конструкции CREATE SEQUENCE / DROP SEQUENCE

## Пример
```
DROP GENERATOR GEN_CUSTOMERS_ID;
```

## См. также
[CREATE GENERATOR](/create_generator/),  [SET GENERATOR](/set_generator/),  CREATE SEQUENCE,  [ALTER SEQUENCE](/alter_sequence/),  DROP SEQUENCE

## Источник
