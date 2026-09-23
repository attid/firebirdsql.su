---
title: "SET TERM"
old_id: set_term
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# SET TERM

## Версии сервера
все 

## Доступно в
ISQL  PSQL

## Формат
```sql
SET TERM string;
```

Обратите внимание:
| Аргумент | Описание |
|---|---|
| string | Определяет символ или символы, чтобы использовать для завершения инструкции. По умолчанию: точка с запятой (;). |

## Описание
SET TERM определяет, какой символ или строка символов завершает команду.

По умолчанию, isql команды должны быть завершены точкой с запятой (;). Используйте SET TERM, чтобы изменить символ завершения.

SET TERM обычно используется совместно с [CREATE PROCEDURE](/create_procedure/) или [CREATE TRIGGER](/create_trigger/). Процедуры и триггеры определены, используя язык процедур и триггеров (PSQL), в котором инструкция всегда заканчивается точкой с запятой. Процедура или триггер непосредственно должна быть завершена символом отличным от точки с запятой.

Текстовый файл, содержащий определение [CREATE PROCEDURE](/create_procedure/) или [CREATE TRIGGER](/create_trigger/), должен включать одну команду SET TERM перед определением, и соответственно после определения. Начальный SET TERM определяет новый завершающий символ; конечный SET TERM восстанавливает точку с запятой (;), как по умолчанию.

Использование SET TERM изнутри isql сессии имеет тот же эффект, как использование терминатора из командной строки.

## Пример
Следующий пример показывает текстовый файл, который использует SET TERM при создании процедуры. Первый SET TERM определяет !!!, как завершающие символы; соответствующий SET TERM восстанавливает точку с запятой (;), как завершающий символ:

```sql
SET TERM !!! ;

CREATE PROCEDURE ADD_EMP_PROJ(
   A_EMP_NO SMALLINT
  ,A_PROJ_ID CHAR(5)
)AS
BEGIN
  INSERT INTO employee_project (EMP_NO, PROJ_ID) VALUES (:A_EMP_NO, :A_PROJ_ID);
  WHEN SQLCODE -530 DO
    EXCEPTION unknown_emp_id;
END
!!!

SET TERM ; !!!
```

## См. также
[CREATE PROCEDURE](/create_procedure/), [CREATE TRIGGER](/create_trigger/)

## Источник
langref.pdf
