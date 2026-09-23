---
title: "RDB$GET_CONTEXT"
old_id: rdb_get_context
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$GET_CONTEXT

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Да | Да | Да | Да | Да | Да |

## Формат
RDB$GET_CONTEXT( "пространство имён", переменная)
## Описание
Встроенная функция
Дает доступ к информации о текущем подключении и текущей транзакции.
Так же позволяет получать пользовательские переменые внутри транзакции или подключения заданые с помощью RDB$SET_CONTEXT.

⚠️ "Пространства имен" и переменые являются регистро зависимыми 

⚠️ Для продотвращения DoS атак, существует ограничение на 1000 переменых в одном "пространстве имен".

RDB$GET_CONTEXT возращает текущее значение переменой, если переменой нет то возращается NULL.

в настоящий момент есть всего 3 "пространства имен" которые можно использовать:

**USER_SESSION** для пользовательских переменых, заданые через RDB$SET_CONTEXT в течении подключения.

**USER_TRANSACTION** для пользовательских переменых, заданые через RDB$SET_CONTEXT в течении транзакции.

**SYSTEM** предостовляют доступ к определеным переменым, описанных в следующей таблице

| Переменая | описание | возможное значение |
|---|---|---|
| ENGINE_VERSION | Возвращает текущую версию SQL-сервера | Например, "2.5.0" |
| NETWORK_PROTOCOL | Сетевой протокол, используемый клиентом. | "TCPv4", "WNET", "XNET" , NULL |
| CLIENT_ADDRESS | Сетевой адрес клиента | для TCPv4 - "xxx.xxx.xxx.xxx", для XNET - ID процесса, для остальных NULL |
| DB_NAME | Имя базы данных, в зависимости от подключения возвращает алиас или путь к файлу, указанные в строке подключения к базе данных. |  |
| ISOLATION_LEVEL | Уровень изолированности текущей транзакции. | "READ COMMITTED", "CONSISTENCY", "SNAPSHOT" |
| READ_ONLY | Режим транзакции для чтения с 2.5.3 или 2.5.2 | "TRUE", "FALSE" |
| TRANSACTION_ID | Номер текущей транзакции, тоже самое что [CURRENT_TRANSACTION](/current_transaction/) |  |
| SESSION_ID | Номер текущего подключения, тоже самое что [CURRENT_CONNECTION](/current_connection/) |  |
| CURRENT_USER | Текущий пользователь, тоже самое что [CURRENT_USER](/current_user/) |  |
| CURRENT_ROLE | Текущая роль, тоже самое что [CURRENT_ROLE](/current_role/) |  |

## Пример
```sql
-- Получить текущую версию сервера
SELECT RDB$GET_CONTEXT('SYSTEM','ENGINE_VERSION') FROM RDB$DATABASE

-- Создание пользовательской переменной в рамках контекста
SELECT RDB$SET_CONTEXT('USER_SESSION','MY','Значение Моей Переменной') FROM RDB$DATABASE
-- Получить потом значение этой переменной
SELECT RDB$GET_CONTEXT('USER_SESSION','MY') FROM RDB$DATABASE
-- Но вот таким образом получить потом значение этой переменной нельзя,
-- т.к. пространство имен регистро-зависимое
SELECT RDB$GET_CONTEXT('USER_SESSION','My') FROM RDB$DATABASE
```

С помощью контекстных переменных можно сделать нумерацию строк в запросе
```sql
SELECT RDB$GET_CONTEXT('USER_TRANSACTION','ROW') AS ROWNUM,
       E.*,
       RDB$SET_CONTEXT('USER_TRANSACTION','ROW', CAST(COALESCE(RDB$GET_CONTEXT('USER_TRANSACTION','ROW'),0) AS INTEGER)+1) AS X
FROM   EMPLOYEE E
```

Чтобы перезапуск вышеприведенного запроса (без commit'a или rollback'a) не приводил к увеличению счетчика строк, можно "проинициализировать" CONTEXT-переменную холостой выборкой из rdb$database с null-значениями всех полей. Эта "null-строка" далее отсеивается where-предикатом.
Чтобы не отображался столбец 'X', нельзя удалять его из select-списка. Вместо этого надо включить его в выражение вычисления другого числового столбца, но так, чтобы это не повлияло на итоговый результат. Например, можно умножить 'X' на ноль и добавить к rownum - на результат это не повлияет:
```sql
select rownum+0*x rownum, emp_no, emp_name
from(
  select 
    rdb$set_context('USER_TRANSACTION','row',0) rownum,
    null emp_no,
    null emp_name,
    null x
  from rdb$database

  union all

  select 
    1+cast(rdb$get_context('USER_TRANSACTION','row') as int) as rownum,
    e.emp_no,
    e.last_name emp_name,
  rdb$set_context('USER_TRANSACTION','row', cast(coalesce(rdb$get_context('USER_TRANSACTION','row'),0) as integer)+1) as x
  from   
  employee e
)t
where emp_no is not null
;
```
## См. также
RDB$SET_CONTEXT

## Источник
%Firebird%\doc\sql.extensions\README.context_variables2.txt
