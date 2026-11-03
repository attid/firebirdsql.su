---
title: "Триггеры в Firebird: типы, события, NEW и OLD"
old_id: triggery
section: sql
type: article
date: "2026-11-03"
firebird:
  since: 
  until: 
  deprecated: false
---

# Триггеры в Firebird

Триггер — код на [PSQL](/raznovidnosti_jazyka_sql/), который сервер выполняет
автоматически при наступлении события: изменении данных, подключении
пользователя, выполнении DDL. Типичный наследник любой рабочей базы Firebird —
аудит изменений, проверка бизнес-правил и заполнение полей `MODIFIED_AT`/
`MODIFIED_BY` живут именно в триггерах.

## DML-триггеры

Основной вид: срабатывают на `INSERT`, `UPDATE` или `DELETE` в таблице, до
(`BEFORE`) или после (`AFTER`) операции. Объявляются через
[CREATE TRIGGER](/create_trigger/), меняются [ALTER TRIGGER](/alter_trigger/),
удаляются [DROP TRIGGER](/drop_trigger/).

Внутри DML-триггера доступны контекстные записи [NEW и OLD](/new_old/):
`NEW` — строка после изменения, `OLD` — до него. В `INSERT` есть только `NEW`,
в `DELETE` — только `OLD`. Значения `NEW.xxx` осмысленно менять в
`BEFORE`-триггере: в `AFTER`-фазе данные уже записаны. Если один триггер
обрабатывает несколько событий, текущую операцию подскажут контексты
[INSERTING, UPDATING, DELETING](/inserting_updating_deleting/).

Классика жанра — аудит-триггер:

```sql
CREATE TRIGGER ORDERS_AU FOR ORDERS AFTER UPDATE
AS
BEGIN
  IF (OLD.STATUS <> NEW.STATUS) THEN
    INSERT INTO ORDERS_LOG (ORDER_ID, OLD_STATUS, NEW_STATUS)
    VALUES (NEW.ID, OLD.STATUS, NEW.STATUS);
END
```

На одно событие можно навесить несколько триггеров; порядок выполнения задаётся
предложением `POSITION` (меньший номер срабатывает раньше). Несколько событий в
одном триггере перечисляются через `OR` — `BEFORE INSERT OR UPDATE OR DELETE`;
такой синтаксис работает начиная с Firebird 1.5, то есть во всех актуальных
версиях.

## Триггеры событий базы данных

С Firebird 2.1 появились триггеры уровня сервера и транзакций: `ON CONNECT`,
`ON DISCONNECT`, `ON TRANSACTION START`, `ON TRANSACTION COMMIT`,
`ON TRANSACTION ROLLBACK`. Это штатный способ вести журнал подключений или
запретить вход определённым пользователям — без перехватчиков на стороне
клиента.

## DDL-триггеры

С Firebird 3.0 — триггеры на изменение метаданных (`BEFORE DDL`, `AFTER DDL`):
можно запретить изменение структур в рабочей базе или вести журнал того, кто и
что менял в схеме.

## Сводка

| Тип | События | Версия |
|---|---|---|
| DML (таблицы и представления) | BEFORE/AFTER INSERT, UPDATE, DELETE; несколько — через OR | все версии |
| События БД | ON CONNECT, ON DISCONNECT, ON TRANSACTION START/COMMIT/ROLLBACK | 2.1+ |
| DDL | BEFORE/AFTER DDL | 3.0+ |

## Грабли

- **COMMIT и ROLLBACK внутри триггера недопустимы** — операторы управления
  транзакциями в PSQL запрещены, чтобы не ломать атомарность вызвавшей
  операции. Исключение — блок `IN AUTONOMOUS TRANSACTION`
  ([автономные транзакции](/autonomous_transaction/), с 2.5), который
  выполняется в отдельной транзакции и переживёт откат основной.
- Ошибка в триггере отменяет всю операцию: неперехваченное
  [исключение](/exception/) в `BEFORE INSERT` не даст строке вставиться.
  Это и мощь, и ответственность.
- Триггер на триггер: `AFTER`-триггер изменил таблицу — сработают её триггеры.
  Цепочки имеют предел глубины, но лучше в них не попадать.
- Триггеры могут быть и у представлений — именно так реализуются обновляемые
  представления (updatable views).
- Список всех триггеров базы — в системной таблице [RDB$TRIGGERS](/rdb_triggers/),
  тексты сообщений об ошибках — в [RDB$TRIGGER_MESSAGES](/rdb_trigger_messages/).

## Что почитать дальше

- [CREATE TRIGGER](/create_trigger/) — полный синтаксис объявления
- [NEW и OLD](/new_old/) — доступ к строке до и после изменения
- [INSERTING, UPDATING, DELETING](/inserting_updating_deleting/) — определение операции
- [Исключения](/exception/) — как триггер отменяет недопустимое
- [Автономные транзакции](/autonomous_transaction/) — журнал, который переживёт откат основной
