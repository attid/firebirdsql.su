---
title: "GEN_ID()"
old_id: gen_id
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# GEN_ID()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | ? |

## Формат
```
GEN_ID (generator, step);
```

| Аргумент | Описание |
|---|---|
| generator | Имя существующего генератора. |
| step | Целое или выражение, определяющее увеличение или уменьшение текущего значения генератора. Значения могут быть в диапазоне от -2<sup>31</sup> до 2<sup>31</sup>- 1. |

## Описание
Функция GEN_ID():

1. Увеличивает текущее значение определенного генератора на step.
2. Возвращает текущее значение определенного генератора. 

GEN_ID() полезно использовать для автоматического создания уникальных ключей, чтобы вставлять в столбцы [UNIQUE](/constraint/) или [PRIMARY KEY](/constraint/). Чтобы вставить сгенерированное число в столбец, напишите триггер, процедуру или инструкцию SQL, которые вызывают GEN_ID().

⚠️ Генератор создан инструкцией [CREATE GENERATOR](/create_generator/). По умолчанию, значение генератора устанавливается в нуль. Оно может быть установлено в другое значение с помощью [SET GENERATOR](/set_generator/).

## Пример
Следующее определение триггера включает обращение к GEN_ID():
```
SET TERM !! ;

CREATE TRIGGER CREATE_EMPNO FOR EMPLOYEES
ACTIVE BEFORE INSERT POSITION 0 AS 
BEGIN
  NEW.EMPNO = GEN_ID (EMPNO_GEN, 1);
END!!

SET TERM ; !!
```
В первый раз, при выполнении триггера, NEW.EMPNO устанавливается к 1. В следующий раз, оно будет установлено к 2, и т.д.

## См. также
[CREATE GENERATOR](/create_generator/),  [DROP GENERATOR](/drop_generator/),  [SET GENERATOR](/set_generator/),  [NEXT VALUE FOR](/next_value_for/)

## Источник
langref.pdf
