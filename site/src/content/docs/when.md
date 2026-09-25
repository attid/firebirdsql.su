---
title: "WHEN"
old_id: when
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# WHEN

используется в конструкции запросов [select](/select/) или [case](/case/)

и как самостоятельный оператор:?: для вылавливания исключений что и будет рассмотрено в этой заметке

## Версии сервера
Firebird 1.5 Firebird 2.0 

## Формат
WHEN < SQLCODE код | GDSCODE код | ANY > DO <выражение> ;

## Описание
Встроенная функция

Для обработки исключений в процедуре или тригере смотрите также [exception](/exception/)

GDSCODE - это номера ошибок из ibase.h, подробнее см. [GDSCODES](/gdscodes/)

## Пример
```sql
  BEGIN
    ...
  WHEN SQLCODE -802 DO
    EXCEPTION E_ARITH_EXCEPT;
  WHEN SQLCODE -803 DO
    EXCEPTION E_KEY_VIOLATION;
  WHEN ANY DO
    EXCEPTION;
  END
```

## См.также
SQLCODE, [GDSCODE](/gdscode/), [GDSCODES](/gdscodes/), [EXCEPTION](/exception/)

## Источник
%Firebird%\doc\sql.extensions\README.exception_handling

%Firebird%\doc\sql.extensions\README.context_variables
