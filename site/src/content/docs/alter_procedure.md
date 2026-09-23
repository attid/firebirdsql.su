---
title: "ALTER PROCEDURE"
old_id: alter_procedure
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ALTER PROCEDURE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
Для Firebird версии ниже 2.0
```
ALTER PROCEDURE name
  [(param <datatype> [, param <datatype> ...])]
  [RETURNS (param <datatype> [, param <datatype> ...])]
  AS <procedure_body> [terminator]
```

Для Firebird версии выше 2.0
```
ALTER PROCEDURE name
  [(param <datatype> [= <default_value>]  [, param <datatype> [= <default_value>] ...])]
  [RETURNS (param <datatype> [, param <datatype> ...])]
  AS <procedure_body> [terminator]
```

| Аргумент | Описание |
|---|---|
| name | Имя существующей процедуры. |
| param <datatype> | Входные параметры, используемые процедурой. Допустимые типы данных перечисленны в Типы данных. |
| RETURNS param <datatype> | Выходные параметры, используемые процедурой. Допустимые типы данных перечислены в Типы данных. |
| <procedure_body> | Тело процедуры. Включает: 1.Объявления локальных переменных. 2 Блок инструкций на языке процедур и триггеров. Смотри CREATE PROCEDURE, для полного описания. |
| <default_value> | Значение параметра по умолчанию, если он не указан при вызове процедуры. ⚠️ для использования возможности требуется Firebird v2.0 и выше |
| terminator | Терминатор, определенный для ISQL командой SET TERM, указывающий конец тела процедуры. |

## Описание
ALTER PROCEDURE изменяет существующую сохраненную процедуру. Эта инструкция может изменять входные параметры, выходные параметры и тело процедуры.

Заголовок и тело процедуры должны быть включены в инструкцию ALTER PROCEDURE полнонстью. Синтаксис точно такой же, как у инструкции [CREATE PROCEDURE](/create_procedure/) за исключением ключевого слова CREATE, которое заменено на ALTER.

Процедуры, использующиеся в настоящий момент, не могут быть изменены, пока не завершится их использование.

Изменения созданные инструкцией ALTER PROCEDURE, дают эффект, как только они произведены. Изменения распространяются на все приложения, которые используют процедуру, без необходимости их перекомпиляции и сборки.

⚠️ Будте внимательны при изменении типов и числа входных и выходных параметров процедуры, так как существующий код может предполагать, что процедура имеет оригинальный формат.

Процедура может быть изменена ее создателем или пользователем SYSDBA.

## Пример
Эта инструкция изменяет процедуру GET_EMP_PROJ, изменяя возвращаемый параметр, чтобы он имел тип данных VARCHAR(20):
```
SET TERM !! ;

ALTER PROCEDURE GET_EMP_PROJ (
  EMP_NO SMALLINT
)RETURNS(
  PROJ_ID VARCHAR(20)
)AS
BEGIN
  FOR 
    SELECT PR.PROJ_ID
    FROM   EMPLOYEE_PROJECT PR
    WHERE  PR.EMP_NO = :emp_no
    INTO   :proj_id
  DO
    SUSPEND;
END !!

SET TERM ; !!
```

## См. также
[CREATE PROCEDURE](/create_procedure/),  [DROP PROCEDURE](/drop_procedure/),  [EXECUTE PROCEDURE](/execute_procedure/),  [SET TERM](/set_term/)

## Источник
langref.pdf
