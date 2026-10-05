---
title: "Системные таблицы"
old_id: sistemnye_tablicy
section: groups
type: landing
firebird:
  since: 
  until: 
  deprecated: false
---

# Системные таблицы

| Таблица | Описание |
|---|---|
| RDB$BACKUP_HISTORY |  |
| RDB$CHARACTER_SETS | описывает доступные наборы символов |
| [RDB$CHECK_CONSTRAINTS](/rdb_check_constraints/) | содержит перекрестные ссылки имен и триггеров для ограничений СНЕСК и NOT NULL |
| RDB$COLLATIONS | содержит данные о порядке (последовательности) сравнения символьных данных |
| [RDB$DATABASE](/rdb_database/) | содержит описание базы данных |
| RDB$DEPENDENCIES | содержит описание зависимостей между объектами базы данных |
| RDB$EXCEPTIONS | содержит описание исключений в базе данных |
| [RDB$FIELDS](/rdb_fields/) | содержит информацию о всех доменах базы данных |
| RDB$FIELD_DIMENSIONS | содержит описание размерностей данных типа массив |
| RDB$FILES | содержит описание файлов базы данных |
| RDB$FILTERS | содержит описание фильтров BLOB |
| RDB$FORMATS | содержит описание истории изменения форматов столбцов таблицы |
| RDB$FUNCTIONS | содержит описание пользовательских функций (UDF) |
| RDB$FUNCTION_ARGUMENTS | содержит описание параметров пользовательских функций (UDF) |
| [RDB$GENERATORS](/rdb_generators/) | содержит информацию о всех генераторах в базе данных |
| [RDB$INDEX_SEGMENTS](/rdb_index_segments/) | хранит сегменты и позиции составных индексов |
| [RDB$INDICES](/rdb_indices/) | хранит определения всех индексов |
| RDB$LOG_FILES |  |
| RDB$PAGES | хранит историю выделения страниц в базе данных |
| RDB$PROCEDURES | содержит описание хранимых процедур |
| RDB$PROCEDURE_PARAMETERS | содержит описание параметров хранимых процедур |
| [RDB$REF_CONSTRAINTS](/rdb_ref_constraints/) | хранит действия для ссылочных ограничений |
| [RDB$RELATIONS](/rdb_relations/) | хранит информацию заголовка таблиц и просмотров |
| [RDB$RELATION_CONSTRAINTS](/rdb_relation_constraints/) | хранит информацию об ограничениях целостности на уровне таблицы |
| [RDB$RELATION_FIELDS](/rdb_relation_fields/) | хранит определения столбцов |
| [RDB$ROLES](/rdb_roles/) | содержит информацию о ролях доступа к базе данных |
| [RDB$SECURITY_CLASSES](/rdb_security_classes/) | хранит и отслеживает списки управления доступом к базе данных |
| [RDB$TRANSACTIONS](/rdb_transactions/) | отслеживает транзакции с несколькими базами данных |
| [RDB$TRIGGERS](/rdb_triggers/) | содержит информацию о всех триггерах в базе данных |
| [RDB$TRIGGER_MESSAGES](/rdb_trigger_messages/) | хранит определения сообщений триггеров (для системного использования) |
| RDB$TYPES | содержит перечень типов данных и алиасов символьных наборов и последовательностей сравнения символьных наборов |
| RDB$USER_PRIVILEGES | содержит сведения о выдачи прав пользователям на основе команд GRANT |
| RDB$VIEW_RELATIONS | описывает обзоры - для каждого обзора содержит перечень, используемых ими таблиц |
