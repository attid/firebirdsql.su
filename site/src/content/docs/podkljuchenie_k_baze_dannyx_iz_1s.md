---
title: "Подлючение к базе данных из 1С"
old_id: podkljuchenie_k_baze_dannyx_iz_1s
section: install
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# Подлючение к базе данных из 1С

## Доступно в
1C7.x   1C8.x

## Описание
Пусть требуется подключиться к базе данных из системы 1С:Предприятие.

На ЭВМ, с которой будем подключаться должны быть соблюдены следующие условия:

1) Скачан и установлен [Firebird](http://www.firebirdsql.org/en/server-packages/) с настройками по умолчанию в любой конфигурации (ClassicServer / SuperServer / SuperClassicServer).

2) Скачан и установлен [Firebird ODBC Driver](http://www.firebirdsql.org/en/odbc-driver/) с настройками по умолчанию.

Требуется подключиться к удаленному серверу в локальной сети, например, имеющем: IP=192.168.1.200, Firebird настроен на порт 3050, база данных располагается в файле: D:\DB\MYDATABSE.FDB.
## Пример

```c
  // Формируем строку подключения
  Сonn = CreateObject("ADODB.Connection");
  Conn.ConnectionString = "Driver=Firebird/InterBase(r) driver;" +
     "Dbname=192.168.1.200/3050:D:\DB\MYDATABSE.FDB;" +  // Исправьте на свой IP, порт и путь к базе данных !
     "UID=SYSDBA;" +                                     // Исправьте на свое имя пользователя !
     "PWD=masterkey;" +                                  // Исправьте на правильный пароль ! 
     "CHARSET=WIN1251;" +                                // Исправьте на свою кодировку подключения !!!
     "client=C:\Program Files\Firebird\Firebird_2_5\bin\fbclient.dll";
  Conn.ConnectionTimeout = 180;
  Conn.CursorLocation = 3;
  // Подключаемся к базе данных
  Try
    Conn.Open(Conn.ConnectionString);
  Except
    Сообщить("Не удалось выполнить подключение " + ОписаниеОшибки());
    Return;
  EndTry;
	
  
  // Выполнение простого DML-запроса
  Try
    Conn.Execute("INSERT INTO MY_TABLE(ID,NAME)VALUES(0, 'Значение' ); ");
  Except
    Сообщить("Не удалось выполнить запрос " + ОписаниеОшибки());
    Conn.Close();
    Return;
  EndTry;
  

  
  // Выполнение селективного запроса
  RecordSet = CreateObject("ADODB.Recordset");
  RecordSet.ActiveConnection = Conn;
  RecordSet.CursorType = 1;
  RecordSet.LockType = 3;
  //Запрос к базе данных на языке SQL запросов
  Try
    RecordSet.Open("SELECT T.MY_FIELD1 FROM MY_TABLE T WHERE (T.FIELD = 'SomeValue')", Conn);
  Except  
    Сообщить("Не удалось выполнить запрос " + ОписаниеОшибки());
    Conn.Close();
    Return;
  EndTry;  
  // Обработка результатов запроса
  Пока(RecordSet.EOF() = 0)Цикл
    Сообщить("Значение домена = " + String(RecordSet.Fields("MY_FIELD1").Value));
    RecordSet.MoveNext();
  КонецЦикла;
  // Не забываем закрыть набор данных !!!
  RecordSet.Close(); 

  

  // Не забываем отключиться от базы данных !
  Conn.Close();
  
```
