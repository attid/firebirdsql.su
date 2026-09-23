---
title: "CREATE GENERATOR\\SEQUENCE"
old_id: create_generator
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CREATE GENERATOR\SEQUENCE

## Формат
```
CREATE {GENERATOR | SEQUENCE} <имя генератора>;
```

## Описание
Оператор CREATE GENERATOR используется для создания в базе данных объекта генератор (GENERATOR
или SEQUENCE). 
Ключевые слова GENERATOR и SEQUENCE являются синонимами.
Имя генератора должно быть уникальным среди имен всех генераторов базы данных и должно содержать до
31 символа. При создании генератора ему присваивается значение 0. Последующие обращения к функции
GEN_ID или использование конструкции NEXT VALUE FOR изменяют это значение на указанную при обра-
щении к функции величину.

## Пример
```sql
  CREATE SEQUENCE gen_employee_id;
```

## См. также
[SEQUENCE](/sequence/), [ALTER SEQUENCE](/alter_sequence/), [GEN_ID](/gen_id/), [NEXT VALUE FOR](/next_value_for/)
