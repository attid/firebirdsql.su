---
title: "ALTER TRIGGER"
old_id: alter_trigger
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ALTER TRIGGER

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Формат
Для Firebird v0.9, Firebird v1.0
```
ALTER TRIGGER name
[ACTIVE | INACTIVE]
  [{BEFORE | AFTER} {DELETE | INSERT | UPDATE}]
  [POSITION number]
  [AS <trigger_body>] [terminator]
```

Для Firebird v1.5 и выше
```
ALTER TRIGGER name
[ACTIVE | INACTIVE]
  [{BEFORE | AFTER} {DELETE | INSERT | UPDATE [OR {DELETE | INSERT | UPDATE} [OR {DELETE | INSERT | UPDATE}]]} ]
  [POSITION number]
  [AS <trigger_body>] [terminator]
```

| Аргумент | Описание |
|---|---|
| name | Имя существующего триггера. |
| ACTIVE | Определяет, что действие триггера дает эффект, когда тот запускается (по умолчанию). |
| INACTIVE | Определяет, что действие триггера не дает эффекта. |
| BEFORE | Определяет, что триггер срабатывает перед ассоциированной операцией. |
| AFTER | Определяет, что триггер срабатывает после ассоциированной операцией. |
| DELETE, INSERT, UPDATE | Определяет операцию над таблицей, при которой срабатывает триггер. |
| POSITION number | Определяет порядок в котором срабатывают триггеры перед или после того же самого действия. number должен быть целым от 0 до 32767. Триггер с меньшим номером срабатывает раньше. Триггеры для того же самого действия, с тем же самым позиционным номером, будут запущены в случайном порядке. |
| trigger_body | Тело триггера, блок инструкций на языке процедур и триггеров. Смотри [CREATE TRIGGER](/create_trigger/) для полного описания. |
| terminator | Терминатор, определенный для ISQL командой [SET TERM](/set_term/), указывающий на конец тела триггера. Необязателен, при изменении только заголовка триггера. |

## Описание
ALTER TRIGGER изменяет определение существующего триггера. Если какие-либо аргументы инструкции ALTER TRIGGER пропущены, тогда они, по умолчанию, принимают текущие значения, которые определены инструкцией [CREATE TRIGGER](/create_trigger/) или последующей ALTER TRIGGER.

ALTER TRIGGER может изменить:

  - Только информацию заголовка, заключенную в activation status триггера, when it performs its actions, событие, которое запускает триггер и порядок, в котором триггеры запускаются.
  - Только информацию тела: инструкции которые следуют за предложением AS.
  - Информацию заголовка и тела триггера. В этом случае новое определение триггера заменяет старое определение. 

Триггер может быть изменен его создателем и пользователем SYSDBA.

⚠️ Изменение триггера определено автоматически для CHECK ограничения таблицы, используйте [ALTER TABLE](/alter_table/), чтобы изменить определение ограничения.

## Пример
Cледующая инструкция изменяет триггер SET_CUST_NO, делая его не активным. (а пассивным :))
```
ALTER TRIGGER SET_CUST_NO INACTIVE;
```

Следующая инструкция изменяет триггер SET_CUST_NO, чтобы вставлять строку в таблицу NEW_CUSTOMER для каждого нового заказчика:
```
SET TERM !! ;

ALTER TRIGGER SET_CUST_NO FOR CUSTOMER
BEFORE INSERT AS
BEGIN
  NEW.CUST_NO = GEN_ID(CUST_NO_GEN, 1);
  INSERT INTO NEW_CUSTOMERS(NEW.CUST_NO, TODAY)
END !!

SET TERM ; !!
```

Следующая инструкция изменяет триггер AFTER_CUST_INS, чтобы он срабатывал после любого действия над таблицей:
```
SET TERM !! ;

ALTER TRIGGER AFTER_CUST_INS FOR CUSTOMER
AFTER INSERT OR UPDATE OR DELETE POSITION 200 
AS
BEGIN
  POST_EVENT 'CUSTOMER_CHANGED';
END !!

SET TERM ; !!
```
## См. также
[CREATE TRIGGER](/create_trigger/), [DROP TRIGGER](/drop_trigger/), RDB$TRIGGERS, [SET TERM](/set_term/), [CREATE PROCEDURE](/create_procedure/)

## Источник
langref.pdf
