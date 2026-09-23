---
title: "GDSCODES (Коды ошибок Firebird)"
old_id: gdscodes
section: errors
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# GDSCODES (Коды ошибок Firebird)

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Описание

| SQLCODE | GDSCODE | Сообщение |
|---|---|---|
| 101 | 335544366L | Выделенный буфер памяти меньше, чем требуется |
| 100 | 335544338L | No match for first value expression |
| 100 | 335544354L | Неверное значение RDB$DB_KEY |
| 100 | 335544367L | Attempted retrieval of more segments than exist |
| 100 | 335544374L | Attempt to fetch past the last record in a record stream |
| -84 | 335544554L | Table/procedure has non-SQL security class defined |
| -84 | 335544555L | Column has non-SQL security class defined |
| -84 | 335544668L | Процедура <string> не возвращает значений или столбцов |
| -103 | 335544571L | Datatype for constant unknown |
| -104 | 335544343L | Invalid request BLR at offset <long> |
| -104 | 335544390L | BLR syntax error: expected <string> at offset <long>, encountered <long> |
| -104 | 335544425L | Контекст уже используется (BLR error) |
| -104 | 335544426L | Контекст не определен (BLR error) |
| -104 | 335544429L | Bad parameter number |
| -104 | 335544440L |  |
| -104 | 335544456L | Invalid slice description language at offset <long> |
| -104 | 335544570L | Неверная команда |
| -104 | 335544579L | Внутрення ошибка |
| -104 | 335544590L | Option specified more than once |
| -104 | 335544591L | Unknown transaction option |
| -104 | 335544592L | Invalid array reference |
| -104 | 335544634L | Token unknown—line <long>, char <long> |
| -104 | 335544608L | Unexpected end of command |
| -104 | 335544612L | Token unknown |
| -150 | 335544360L | Attempted update of read-only table |
| -150 | 335544362L | Cannot update read-only view <string> |
| -150 | 335544446L | Notupdatable |
| -150 | 335544546L | Cannot define constraints on views |
| -151 | 335544359L | Attempted update of read-only column |
| -155 | 335544658L | <string> is not a valid base table of the specified view |
| -157 | 335544598L | Must specify column name for view select expression |
| -158 | 335544599L | Number of columns does not match select list |
| -162 | 335544685L | Dbkey not available for multi-table views |
| -170 | 335544512L | Parameter mismatch for procedure <string> |
| -170 | 335544619L | External functions cannot have more thaniO parameters |
| -171 | 335544439L | Function <string> could not be matched |
| -171 | 335544458L | Column not array or invalid dimensions (expected <long>, encountered <long>) |
| -171 | 335544618L | Return mode by value not allowed for this datatype |
| -172 | 335544438L | Function <string> is not defined |
| -204 | 335544463L | Generator <string> is not defined |
| -204 | 335544502L | Reference to invalid stream number |
| -204 | 335544509L | CHARACTER SET <string> is not defined |
| -204 | 335544511L | Procedure <string> is not defined |
| -204 | 335544515L | Status code <string> unknown |
| -204 | 335544516L | Exception <string> not defined |
| -204 | 335544532L | Name of Referential Constraint not defined in constraints table. |
| -204 | 335544551L | Could not find table/procedure for GRANT |
| -204 | 335544568L | Implementation of text subtype <digit> not located. |
| -204 | 335544573L | Datatype unknown |
| -204 | 335544580L | Table unknown |
| -204 | 335544581L | Procedure unknown |
| -204 | 335544588L | COLLATION <string> is not defined |
| -204 | 335544589L | COLLATION <string> is not valid for specified CHARACTER SET |
| -204 | 335544595L | Trigger unknown |
| -204 | 335544620L | Alias <string> conflicts with an alias in the same statement |
| -204 | 335544621L | Alias <string> conflicts with a procedure in the same statement |
| -204 | 335544622L | Alias <string> conflicts with a table in the same statement |
| -204 | 335544635L | There is no alias or table named <string> at this scope leveL |
| -204 | 335544636L | There is no index <string> for table <string> |
| -204 | 335544640L | Invalid use of CHARACTER SET ОГ COLLATE |
| -204 | 335544662L | BLOB SUB_TYPE <string> is not defined |
| -205 | 335544396L | Column <string> is not defined in table <string> |
| -205 | 335544552L | Could not find column for GRANT |
| -206 | 335544578L | Column unknown |
| -206 | 335544587L | Column is not a Blob |
| -206 | 335544596L | Subselect illegal in this context |
| -208 | 335544617L | Invalid ORDER BY clause |
| -219 | 335544395L | Table <string> is not defined |
| -239 | 335544691L | Cache length too smalL |
| -260 | 335544690L | Cache redefined |
| -281 | 335544637L | Table <string> is not referenced in plan |
| -282 | 335544638L | "Table <string> is referenced more than once in plan; use aliases to distinguish" |
| -282 | 335544643L | "The table <string> is referenced twice; use aliases to differentiate" |
| -282 | 335544659L | "Table <string> is referenced twice in view; use an alias to distinguish" |
| -282 | 335544660L | "View <string> has more than one base table; use aliases to distinguish" |
| -283 | 335544639L | Table <string> is referenced in the plan but not the from list |
| -284 | 335544642L | Index <string> cannot be used in the specified plan |
| -291 | 335544531L | Column used in a PRIMARY/UNIQUE constraint must be NOT NULL. |
| -292 | 335544534L | Cannot update constraints (RDB$REF_CONSTRAINTS). |
| -293 | 335544535L | Cannot update constraints (RDB$CHECK_CONSTRAINTS). |
| -294 | 335544536L | Cannot delete CHECK constraint entry (RDB$CHECK_CONSTRAINTS) |
| -295 | 335544545L | Cannot update constraints (RDB$RELATION_CONSTRAINTS). |
| -296 | 335544547L | Internal isc software consistency check (invalid RDB$CONSTRAINT_TYPE) |
| -297 | 335544558L | Operation violates CHECK constraint <string> on view or table |
| -313 | 335544669L | Count of column list and variable list do not match |
| -314 | 335544565L | Cannot transliterate character between character sets |
| -401 | 335544647L | Invalid comparison operator for find operation |
| -402 | 335544368L | Attempted invalid operation on a Blob |
| -402 | 335544414L | Blob and array datatypes are not supported for <string> operation |
| -402 | 335544427L | Data operation not supported |
| -406 | 335544457L | Subscript out of bounds |
| -407 | 335544435L | Null segment of UNIQUE KEY |
| -413 | 335544334L | "Conversion error from string ""<string>""" |
| -413 | 335544454L | Filter not found to convert type <long> to type <long> |
| -501 | 335544327L | Invalid request handle |
| -501 | 335544577L | Attempt to reclose a closed cursor |
| -502 | 335544574L | Declared cursor already exists |
| -502 | 335544576L | Attempt to reopen an open cursor |
| -504 | 335544572L | Cursor unknown |
| -508 | 335544348L | No current record for fetch operation |
| -510 | 335544575L | Cursor not updatable |
| -518 | 335544582L | Request unknown |
| -519 | 335544688L | The PREPARE statement identifies a prepare statement with an open cursor |
| -530 | 335544466L | "Violation of FOREIGN KEY constraint: ""<string>""" |
| -530 | 335544597L | Cannot prepare a CREATE DATABASE/SCHEMA statement |
| -532 | 335544469L | Transaction marked invalid by I/O error |
| -551 | 335544352L | No permission for <string> access to <string> <string> |
| -552 | 335544550L | Only the owner of a table can reassign ownership |
| -552 | 335544553L | User does not have GRANT privileges for operation |
| -553 | 335544529L | Cannot modify an existing user privilege |
| -595 | 335544645L | The current position is on a crack |
| -596 | 335544644L | Illegal operation when at beginning of stream |
| -597 | 335544632L | Preceding file did not specify length, so <string> must include starting page number |
| -598 | 335544633L | Shadow number must be a positive integer |
| -599 | 335544607L | Gen.c: node not supported |
| -600 | 335544625L | A node name is not permitted in a secondary, shadow, cache or log file name |
| -600 | 335544680L | Sort error: corruption in data structure |
| -601 | 335544646L | Файл базы данных или указанный файл уже существует. |
| -604 | 335544593L | Array declared with too many dimensions |
| -604 | 335544594L | Illegal array dimension range |
| -605 | 335544682L | Inappropriate self-reference of column |
| -607 | 335544351L | Unsuccessful metadata update |
| -607 | 335544549L | Cannot modify or erase a system trigger |
| -607 | 335544657L | Array/Blob/DATE/TIIMESTAMP datatypes not allowed in arithmetic |
| -615 | 335544475L | Lock on table <string> conflicts with existing lock |
| -615 | 335544476L | Requested record lock conflicts with existing lock |
| -615 | 335544507L | Refresh range number <long> already in use |
| -616 | 335544530L | Cannot delete PRIMARY KEY being used in FOREIGN KEY definition. |
| -616 | 335544539L | Cannot delete index used by an integrity constraint |
| -616 | 335544540L | Cannot modify index used by an integrity constraint |
| -616 | 335544541L | Cannot delete trigger used by a CHECK Constraint |
| -616 | 335544543L | Cannot delete column being used in an integrity constraint. |
| -616 | 335544630L | There are <long> dependencies |
| -616 | 335544674L | Last column in a table cannot be deleted |
| -617 | 335544542L | Cannot update trigger used by a CHECK Constraint |
| -617 | 335544544L | Cannot rename column being used in an integrity constraint. |
| -618 | 335544537L | Cannot delete index segment used by an integrity constraint |
| -618 | 335544538L | Cannot update index segment used by an integrity constraint |
| -625 | 335544347L | "Validation error for column <string>, value ""<string>""" |
| -637 | 335544664L | Duplicate specification of <string> not supported |
| -660 | 335544533L | Non-existent PRIMARY or UNIQUE KEY specified for FOREIGN KEY |
| -660 | 335544628L | Cannot create index <string> |
| -663 | 335544624L | Segment count of 0 defined for index <string> |
| -663 | 335544631L | Too many keys defined for index <string> |
| -663 | 335544672L | Too few key columns found for index <string> (incorrect column name?) |
| -664 | 335544434L | "key size exceeds implementation restriction for index ""<string>""" |
| -677 | 335544445L | <string> extension error |
| -685 | 335544465L | Invalid Blob type for operation |
| -685 | 335544670L | Attempt to index Blob column in index <string> |
| -685 | 335544671L | Attempt to index array column in index <string> |
| -689 | 335544403L | Page <long> is of wrong type (expected <long>, found <long>) |
| -689 | 335544650L | Wrong page type |
| -690 | 335544679L | Segments not allowed in expression index <string> |
| -691 | 335544681L | New record size of <long> bytes is too big |
| -692 | 335544477L | Maximum indexes per table (<digit>) exceeded |
| -693 | 335544663L | Too many concurrent executions of the same request |
| -694 | 335544684L | Cannot access column <string> in view <string> |
| -802 | 335544321L | Arithmetic exception, numeric overflow, or string truncation |
| -803 | 335544349L | "Attempt to store duplicate value (visible to active transactions) in unique index ""<string>""" |
| -803 | 335544665L | "Violation of PRIMARY or UNIQUE KEY constraint: ""<string>""" |
| -804 | 335544380L | Wrong number of arguments on calL |
| -804 | 335544583L | SQLDA missing or incorrect version, or incorrect number/type of variables |
| -804 | 335544584L | Count of columns not equal count of values |
| -804 | 335544586L | Function unknown |
| -806 | 335544600L | Only simple column names permitted for VIEW WITH CHECK OPTION |
| -807 | 335544601L | No where clause for VIEW WITH CHECK OPTION |
| -808 | 335544602L | Only one table allowed for VIEW WITH CHECK OPTION |
| -809 | 335544603L | DISTINCT, GROUP ОГ HAVING not permitted for VIEW WITH CHECK OPTION |
| -810 | 335544605L | No subqueries permitted for VIEW WITH CHECK OPTION |
| -811 | 335544652L | Multiple rows in singleton select |
| -816 | 335544651L | External file could not be opened for output |
| -817 | 335544361L | Attempted update during read-only transaction |
| -817 | 335544371L | Attempted write to read-only Blob |
| -817 | 335544444L | Operation not supported |
| -820 | 335544356L | Metadata is obsolete |
| -820 | 335544379L | "Unsupported on-disk structure for file <sf™g>;found</ong>, support <long>" |
| -820 | 335544437L | Wrong DYN version |
| -820 | 335544467L | Minor version too high found <long> expected <long> |
| -823 | 335544473L | Invalid bookmark handle |
| -824 | 335544474L | Invalid lock level <digit> |
| -825 | 335544519L | Invalid lock handle |
| -826 | 335544585L | Invalid statement handle |
| -827 | 335544655L | Invalid direction forfind operation |
| -828 | 335544678L | Invalid key position |
| -829 | 335544616L | Invalid column reference |
| -830 | 335544615L | Column used with aggregate |
| -831 | 335544548L | Attempt to define a second PRIMARY KEY for the same table |
| -832 | 335544604L | FOREIGN KEY column count does not match PRIMARY KEY |
| -833 | 335544606L | Expression evaluation not supported |
| -834 | 335544508L | Refresh range number <long> not found |
| -835 | 335544649L | Bad checksum |
| -836 | 335544517L | Exception <digit> |
| -837 | 335544518L | Restart shared cache manager |
| -838 | 335544560L | Database <string> shutdown in <digit> seconds |
| -839 | 335544686L | journal file wrong format |
| -840 | 335544687L | Intermediate journal file fulL |
| -841 | 335544677L | Too many versions |
| -842 | 335544697L | Precision should be greater than 0 |
| -842 | 335544698L | Scalecannot be greater than precision |
| -842 | 335544699L | Short integer expected |
| -842 | 335544700L | Long integer expected |
| -842 | 335544701L | Unsigned short integer expected |
| -901 | 335544322L | Invalid database key |
| -901 | 335544326L | Unrecognized database parameter block |
| -901 | 335544328L | Invalid Blob handle |
| -901 | 335544329L | Invalid Blob ID |
| -901 | 335544330L | Invalid parameter in transaction parameter block |
| -901 | 335544331L | Invalid format for transaction parameter block |
| -901 | 335544332L | Invalid transaction handle (expecting explicit transaction start) |
| -901 | 335544337L | Attempt to start more than <long> transactions |
| -901 | 335544339L | Information type inappropriate for object specified |
| -901 | 335544340L | No information of this type available for object specified |
| -901 | 335544341L | Unknown information item |
| -901 | 335544342L | Action cancelled by trigger (<long>) to preserve data integrity |
| -901 | 335544345L | Lock conflict on no wait transaction |
| -901 | 335544350L | Program attempted to exit without finishing database |
| -901 | 335544353L | Transaction is not in limbo |
| -901 | 335544355L | Blob was not closed |
| -901 | 335544357L | Cannot disconnect database with open transactions (<long> active) |
| -901 | 335544358L | Message length error (encountered <long>, expected <long>) |
| -901 | 335544363L | No transaction for request |
| -901 | 335544364L | Request synchronization error |
| -901 | 335544365L | Request referenced an unavailable database |
| -901 | 335544369L | Attempted read of a new, open Blob |
| -901 | 335544370L | Attempted action on blob outside transaction |
| -901 | 335544372L | Attempted reference to Blob in unavailable database |
| -901 | 335544376L | Table <string> was omitted from the transaction reserving list |
| -901 | 335544377L | Request includes a DSRI extension not supported in this implementation |
| -901 | 335544378L | Feature is not supported |
| -901 | 335544382L | <string> |
| -901 | 335544383L | Unrecoverable conflict with limbo transaction <long> |
| -901 | 335544392L | Internal error |
| -901 | 335544407L | Database handle not zero |
| -901 | 335544408L | Transaction handle not zero |
| -901 | 335544418L | Transaction in limbo |
| -901 | 335544419L | Transaction not in limbo |
| -901 | 335544420L | Transaction outstanding |
| -901 | 335544428L | Undefined message number |
| -901 | 335544431L | Blocking signal has been received |
| -901 | 335544442L | Database system cannot read argument <long> |
| -901 | 335544443L | Database system cannot write argument <long> |
| -901 | 335544450L | <string> |
| -901 | 335544468L | Transaction <long> is <string> |
| -901 | 335544485L | Invalid statement handle |
| -901 | 335544510L | Lock time-out on wait transaction |
| -901 | 335544559L | Invalid service handle |
| -901 | 335544561L | Wrong version of service parameter block |
| -901 | 335544562L | Unrecognized service parameter block |
| -901 | 335544563L | Service <string> is not defined |
| -901 | 335544609L | INDEX <string> |
| -901 | 335544610L | EXCEPTION <string> |
| -901 | 335544611L | Column <string> |
| -901 | 335544613L | Union not supported |
| -901 | 335544614L | Unsupported DSQL construct |
| -901 | 335544623L | Illegal use of keyword VALUE |
| -901 | 335544626L | Table <string> |
| -901 | 335544627L | Procedure <string> |
| -901 | 335544641L | Specified domain or source column does not exist |
| -901 | 335544656L | Variable <string> conflicts with parameter in same procedure |
| -901 | 335544666L | Server version too old to support all CREATE DATABASE options |
| -901 | 335544673L | Cannot delete |
| -901 | 335544675L | Sort error |
| -902 | 335544333L | Internal isc software consistency check (<string>) |
| -902 | 335544335L | Database file appears corrupt (<string>) |
| -902 | 335544344L | "I/O error during ""<string>"" operation tortile ""<string>""" |
| -902 | 335544346L | Corrupt system table |
| -902 | 335544373L | Operating system directive <string> failed |
| -902 | 335544384L | Internal error |
| -902 | 335544385L | Internal error |
| -902 | 335544387L | Internal error |
| -902 | 335544388L | Block size exceeds implementation restriction |
| -902 | 335544394L | Incompatible version of on-disk structure |
| -902 | 335544397L | Internal error |
| -902 | 335544398L | Internal error |
| -902 | 335544399L | Internal error |
| -902 | 335544400L | Internal error |
| -902 | 335544401L | Internal error |
| -902 | 335544402L | Internal error |
| -902 | 335544404L | Database corrupted |
| -902 | 335544405L | Checksum error on database page <long> |
| -902 | 335544406L | Index is broken |
| -902 | 335544409L | Transaction-request mismatch (synchronization error) |
| -902 | 335544410L | Bad handle count |
| -902 | 335544411L | Wrong version of transaction parameter block |
| -902 | 335544412L | Unsupported BLR version (expected <long>, encountered <long>) |
| -902 | 335544413L | Wrong version of database parameter block |
| -902 | 335544415L | Database corrupted |
| -902 | 335544416L | Internal error |
| -902 | 335544417L | Internal error |
| -902 | 335544422L | Internal error |
| -902 | 335544423L | Internal error |
| -902 | 335544432L | Lock manager error |
| -902 | 335544436L | SQL error code = <long> |
| -902 | 335544448L |  |
| -902 | 335544449L |  |
| -902 | 335544470L | Cache buffer for page <long> invalid |
| -902 | 335544471L | There is no index in table <string> with id <digit> |
| -902 | 335544472L | Your user name and password are not defined. Ask your database administrator to set up an InterBase login. |
| -902 | 335544478L | Enable journal for database before starting online dump |
| -902 | 335544479L | Online dump failure. Retry dump |
| -902 | 335544480L | An online dump is already in progress |
| -902 | 335544481L | No more disk/tape space. Cannot continue online dump |
| -902 | 335544483L | Maximum number of online dump files that can be specified is 16 |
| -902 | 335544506L | Database <string> shutdown in progress |
| -902 | 335544520L | Long-term journaling already enabled |
| -902 | 335544528L | Database <string> shutdown |
| -902 | 335544557L | Database shutdown unsuccessfuL |
| -902 | 335544653L | Cannot attach to password database |
| -902 | 335544654L | Cannot start transaction for password database |
| -902 | 335544564L | Long-term joumaling not enabled |
| -902 | 335544569L | Dynamic SQL Error |
| -904 | 335544324L | Invalid database handle (no active connection) |
| -904 | 335544375L | Unavailable database |
| -904 | 335544381L | Implementation limit exceeded |
| -904 | 335544386L | Too many requests |
| -904 | 335544389L | Buffer exhausted |
| -904 | 335544391L | Buffer in use |
| -904 | 335544393L | Request in use |
| -904 | 335544424L | No lock manager available |
| -904 | 335544430L | Unable to allocate memory from operating system |
| -904 | 335544451L | Update conflicts with concurrent update |
| -904 | 335544453L | Object <string> is in use |
| -904 | 335544455L | Cannot attach active shadow file |
| -904 | 335544460L | A file in manual shadow <long> is unavailable |
| -904 | 335544661L | Cannot add index, index root page is full. |
| -904 | 335544676L | Sort error: not enough memory |
| -904 | 335544683L | Request depth exceeded. (Recursive definition?) |
| -906 | 335544452L | Product <string> is not licensed |
| -909 | 335544667L | Drop database completed with errors |
| -911 | 335544459L | Record from transaction <long> is stuck in limbo |
| -913 | 335544336L | Deadlock |
| -922 | 335544323L | File <string> is not a valid database |
| -923 | 335544421L | Connection rejected by remote interface |
| -923 | 335544461L | Secondary server attachments cannot validate databases |
| -923 | 335544462L | Secondary server attachments cannot start joumaling |
| -924 | 335544325L | Bad parameters on attach or create database |
| -924 | 335544441L | Database detach completed with errors |
| -924 | 335544648L | Connection lost to pipe server |
| -926 | 335544447L | No rollback performed |
| -999 | 335544689L | InterBase error |

## Пример
```sql

```

## См. также
[GDSCODE](/gdscode/), SQLCODE, [WHEN](/when/), [EXCEPTION](/exception/), [Обработка ошибок](/obrabotka_oshibok/)

## Источник
Language Reference 56
