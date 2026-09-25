---
title: "MON$ATTACHMENTS"
old_id: mon_attachments
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# MON$ATTACHMENTS
Эта виртуальная таблица содержит записи с информацией о активных подключениях БД.

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | ? |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Описание

| Поле | Тип | Описание | Пример |
|---|---|---|---|
| MON$ATTACHMENT_ID | [INTEGER](/integer/) | Номер подключения с момента начала работы сервера |  |
| MON$SERVER_PID | [INTEGER](/integer/) | ID процесса сервера |  |
| MON$STATE | [SMALLINT](/tipy_dannyx/) | состояние подключения (0:idle/1: active) |  |
| MON$ATTACHMENT_NAME | [VARCHAR](/tipy_dannyx/)(253) | Полное имя файла БД (алиас из aliases.conf) | D:\EMPLOYEE.FDB |
| MON$USER | [CHAR](/tipy_dannyx/)(31) | Имя юзера | SYSDBA |
| MON$ROLE | [CHAR](/tipy_dannyx/)(31) | Роль, под которой зашел юзер | NONE |
| MON$REMOTE_PROTOCOL | [VARCHAR](/tipy_dannyx/)(8) | Протокол соединения | TCPv4 |
| MON$REMOTE_ADDRESS | [VARCHAR](/tipy_dannyx/)(253) | IP машины юзера | 192.168.0.1 |
| MON$REMOTE_PID | [INTEGER](/integer/) | ID процесса клиента |  |
| MON$REMOTE_PROCESS | [VARCHAR](/tipy_dannyx/)(253) | Полное имя файла клиентского ПО | c:\client.exe |
| MON$CHARACTER_SET_ID | [SMALLINT](/tipy_dannyx/) | Код набора символов по умолчанию при подключении к БД |  |
| MON$TIMESTAMP | [TIMESTAMP](/tipy_dannyx/) | дата/время подключения | 25.06.2008 15:20:33 |
| MON$GARBAGE_COLLECTION | [SMALLINT](/tipy_dannyx/) | :?:garbage collection flag |  |
| MON$STAT_ID | [INTEGER](/integer/) | :?:statistics ID |  |

⚠️ SYSDBA и владелец базы могут просматривать информацию обо всех подключениях, обычным пользователям доступна информация только о своих подключениях.

⚠️ При использовании Embedded-подключения поля MON$REMOTE_PROTOCOL и MON$REMOTE_ADDRESS будут иметь значение null.

## Пример
```sql
  SELECT * FROM MON$ATTACHMENTS
```

## См. также
[Таблицы мониторинга](/tablicy_monitoringa/)

## Источник
README.monitoring_tables.txt
