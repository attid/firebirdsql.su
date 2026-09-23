---
title: "AUTONOMOUS TRANSACTION"
old_id: autonomous_transaction
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# AUTONOMOUS TRANSACTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
IN AUTONOMOUS TRANSACTION DO
  { <simple statement> | <compound statement> }
```

## Описание

Данный оператор позволяет выполнять некоторый блок [PSQL](/raznovidnosti_jazyka_sql/)-кода в автономной транзакции. Основной областью применения данной конструкции может служить те случаи, когда Вам необходимо вызвать исключение, но Вы не хотите, чтобы изменения в базе данных были отменены в связи с откатом транзакции.

Новая транзакция, вызываемая оператором IN AUTONOMOUS TRANSACTION DO, стартует с тем же уровнем изоляции, с каким выполняется основной [PSQL](/raznovidnosti_jazyka_sql/)-блок, вызвавший этот оператор. Любое исключение, вызванное или появившееся в блоке кода автономной транзакции приведет к откату автономной транзакции и отмене всех внесенных изменений. Если код будет выполнен успешно, то автономная транзакция будет подтверждена.

## Пример
```sql
CREATE TABLE LOG (
   LOGDATE  TIMESTAMP
  ,MSG      VARCHAR(60)
);

CREATE EXCEPTION EX_CONN 'Отказано в доступе к базе данных !';

SET TERM !;

CREATE TRIGGER TRIG_CONN01 ON CONNECT
AS
BEGIN
  IF (CURRENR_USER = 'НеверныйПользователь')THEN  
  BEGIN
    IN AUTONOMOUS TRANSACTION DO
    BEGIN
      /* 
      Этот кусок кода будет выполнен в автономной транзакции и 
      вставка записи в таблицу протокола LOG будет произведена.
      */
      INSERT INTO LOG (LOGDATE, MSG) VALUES (CURRENT_TIMESTAMP, 
         'Отказано в подключении пользователю '||CURRENR_USER );
    END
    /*
    В основном PSQL-блоке вызываем исключение и транзакция 
    завершится откатом.
    */
    EXCEPTION EX_CONN;
  END
END!

SET TERM ;!
```

## См. также

[EXECUTE PROCEDURE](/execute_procedure/),  [EXECUTE STATEMENT](/execute_statement/),   [EXECUTE BLOCK](/execute_block/),  [PROCEDURE](/procedure/),  TRIGGER

## Источник
Firebird 2.5 Realise Notes http://firebirdsql.org/devel/doc/rlsnotes/html/rlsnotes25.html

Пожелание пользователей № CORE-1409 http://tracker.firebirdsql.org/browse/CORE-1409
