kimi version 2.0.2
• Just write the page in Russian. The facts got cut off at the end but I have enough. Write the reference page directly in the reply (they said "напиши справочную страницу" — probably output as markdown). No file path given, so output in the message.

• # BLOB_APPEND

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```sql
  BLOB_APPEND(<blob> [, <value1>, ... <valueN>])
  ```

  **Параметры:**

  | Параметр | Описание |
  |---|---|
  | blob | BLOB или NULL. |
  | value | Значение любого типа. |

  **Тип возвращаемого результата:** временный не закрытый BLOB с флагом `BLB_close_on_read`.

  ## Описание

  Функция `BLOB_APPEND` предназначена для конкатенации BLOB без создания промежуточных BLOB. Обычная операция конкатенации с аргументами типа BLOB всегда создаёт столько временных BLOB, сколько раз она используется; `BLOB_APPEND` позволяет этого избежать.

  Поведение функции для первого аргумента зависит от его значения:

  - **NULL** — будет создан новый пустой не закрытый BLOB;
  - **постоянный BLOB** (из таблицы) или временный уже закрытый BLOB — будет создан новый пустой не закрытый BLOB, и содержимое первого BLOB будет в него добавлено;
  - **временный не закрытый BLOB** — он будет использован далее (дописан);
  - **другие типы данных** преобразуются в строку, будет создан временный не закрытый BLOB с содержимым этой строки.

  Остальные аргументы могут быть любого типа:

  - **NULL** игнорируется;
  - **не BLOB** преобразуются в строки (по обычным правилам) и добавляются к содержимому результата;
  - **BLOB** при необходимости транслитерируются к набору символов первого аргумента, и их содержимое добавляется к результату.

  Возвращаемое значение — временный не закрытый BLOB с флагом `BLB_close_on_read`: либо новый BLOB, либо тот же, что был в первом аргументе. Поэтому последовательность операций вида `blob = BLOB_APPEND(blob, ...)` приводит к созданию не более одного BLOB (если не пытаться добавить BLOB к самому себе). Такой BLOB автоматически закрывается движком при попытке прочитать его клиентом, записать в таблицу или использовать в других выражениях, требующих чтения содержимого.

  > **Примечание.** Проверка BLOB на значение NULL с помощью оператора `IS [NOT] NULL` не читает его, а следовательно, временный BLOB не будет закрыт при таких проверках.

  > **Совет.** Используйте функции `LIST` и `BLOB_APPEND` для конкатенации BLOB. Это позволит сэкономить объём потребляемой памяти, дисковый ввод/вывод, а также предотвратит разрастание базы данных из-за создания множества временных BLOB при использовании операторов конкатенации.

  ## Пример

  Пошаговое наращивание текстового BLOB без промежуточных объектов:

  ```sql
  execute block
  returns (b blob sub_type text)
  as
  begin
    -- создаст новый временный не закрытый BLOB
    -- и запишет в него строку из 2-ого аргумента
    b = blob_append(null, 'Hello ');
    -- добавляет во временный BLOB две строки, не закрывая его
    b = blob_append(b, 'World', '!');
    -- сравнение BLOB со строкой закроет его, ибо для этого надо прочитать BLOB
    if (b = 'Hello World!') then
    begin
    -- ...
    end
    -- создаст временный закрытый BLOB, добавив в него строку
    b = b || 'Close';
    suspend;
  end
  ```

  Сборка JSON на стороне сервера (с использованием PSQL-пакета `JSON_UTILS` для преобразования элементарных типов данных в JSON-нотацию):

  ```sql
  EXECUTE BLOCK
  RETURNS (
      JSON_STR BLOB SUB_TYPE TEXT CHARACTER SET UTF8)
  AS
    DECLARE JSON_M BLOB SUB_TYPE TEXT CHARACTER SET UTF8;
  BEGIN
    FOR
        SELECT
            HORSE.CODE_HORSE,
            HORSE.NAME,
            HORSE.BIRTHDAY
        FROM HORSE
        WHERE HORSE.CODE_DEPARTURE = 15
        FETCH FIRST 1000 ROW ONLY
        AS CURSOR C
    DO
    BEGIN
      SELECT
        LIST(
            '{' ||
            JSON_UTILS.NUMERIC_PAIR('age', MEASURE.AGE) ||
            ',' ||
            JSON_UTILS.NUMERIC_PAIR('height', MEASURE.HEIGHT_HORSE) ||
            ',' ||
            JSON_UTILS.NUMERIC_PAIR('length', MEASURE.LENGTH_HORSE) ||
            ',' ||
            JSON_UTILS.NUMERIC_PAIR('chestaround', MEASURE.CHESTAROUND) ||
            ',' ||
            JSON_UTILS.NUMERIC_PAIR('wristaround', MEASURE.WRISTAROUND) ||
            ',' ||
            JSON_UTILS.NUMERIC_PAIR('weight', MEASURE.WEIGHT_HORSE) ||
            '}'
        ) AS JSON_M
      FROM MEASURE
      WHERE MEASURE.CODE_HORSE = :C.CODE_HORSE
      INTO JSON_M;

      JSON_STR = BLOB_APPEND(
        JSON_STR,
        IIF(JSON_STR IS NULL, '[', ',' || ascii_char(13)),
        '{',
        JSON_UTILS.INTEGER_PAIR('code_horse', C.CODE_HORSE),
        ...
  ```

  Пояснения к примерам:

  - В первом примере цепочка присваиваний `b = blob_append(b, ...)` не создаёт промежуточных BLOB — дописывается один и тот же временный не закрытый BLOB, пока его не прочитают (в примере — при сравнении со строкой).
  - Во втором примере показан типичный сценарий: `LIST` собирает внутренний массив, а `BLOB_APPEND` дописывает элементы в результирующий JSON-BLOB, избегая разрастания временных BLOB в цикле по курсору.

  Замечание: переданный фрагмент официального руководства обрывается на втором примере (после `JSON_UTILS.INTEGER_PAIR('code_horse', C.CODE_`), поэтому пример JSON приведён в том же усечённом виде — хвост можно восстановить из полной версии руководства при публикации.

To resume this session: kimi -r session_6b85b5fe-6293-4b2f-889a-27b7cc45e026
