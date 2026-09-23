---
title: "Полезные запросы"
old_id: polesnue_zaprosu
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# Полезные запросы

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

## Описание

полезные запросы, которые можно будет оформить в статью или просто создать страничку 

## Пример

если нужно отобрать записи по ключам, то
намного быстрее будет засунуть эти ID в строку,
распарсить и вытягивать каждую запись по по ключу по
отдельности в цикле:

```sql
CREATE PROCEDURE CONVERT_IDS_TO_ROWS(
    IDS VARCHAR(32700))
RETURNS (
    ID INTEGER)
AS
DECLARE I INTEGER = 1;
  DECLARE J INTEGER = 1;
BEGIN
  IDS = TRIM(IDS);
  WHILE (I <= CHAR_LENGTH(IDS)) DO
  BEGIN
    IF (',' = SUBSTRING(IDS FROM I FOR 1)) THEN
    BEGIN
      ID = SUBSTRING(IDS FROM J FOR I - J);
      SUSPEND;
      I = I + 1;
      J = I;
    END
    I= I + 1;
  END
  IF (I > J) THEN
  BEGIN
   ID = SUBSTRING(IDS FROM J FOR I - J);
   SUSPEND;
  END
END


CREATE OR ALTER PROCEDURE LIST_TO_ROWS(
    LST BLOB SUB_TYPE TEXT)
RETURNS (
    ID INTEGER)
AS
  declare i integer = 1;
  declare j integer = 1;
begin
  while (i <= char_length(lst)) do begin
    if (substring(lst from i for 1) = ',') then begin
      if (i > j) then
        id = substring(lst from j for i - j);
      else
        id = null;
      suspend;
      j = i+1;
    end
    i = i+1;
  end

  if (i > j) then
    id = substring(lst from j for i - j);
  else
    id = null;
  suspend;
end


CREATE OR ALTER PROCEDURE LIST_TO_ROWS(
    LST BLOB SUB_TYPE TEXT)
RETURNS (
    ID INTEGER)
AS
  declare pos_ int;
  declare offset int = 1;
  declare beg int;
  declare buf varchar(30100);
begin
  while (0=0) do begin
    buf = substring(lst from offset for 30100);
    pos_ = 1; beg = 1;
    while (pos_ <= char_length(buf) and pos_ <= 30000) do begin
      if (substring(buf from pos_ for 1) = ',') then begin
        if (pos_ > beg) then
          id = substring(buf from beg for pos_ - beg);
        else
          id = null;
        suspend;
        beg = pos_ + 1;
      end
      pos_ = pos_ + 1;
    end
    if (offset + pos_ - 2 = char_length(lst)) then leave;
    offset = offset + beg - 1;
    if (offset > char_length(lst)) then leave;
  end

  if (pos_ > beg) then
    id = substring(buf from beg for pos_ - beg);
  else
    id = null;
  suspend;
end
```

Если нужно проверить во входящей строке можно ли её считать числом можно использовать следующую процедуру
```sql
CREATE PROCEDURE IS_NUMBER (
    a_value varchar(32))
returns (
    result varchar(10))
as
declare variable i integer;
declare variable j integer;
begin
  result = 'Фиг';
  a_value = trim(a_value);
  if (a_value is null or char_length(a_value) = 0) then begin
    suspend;
    exit;
  end
  i = 1;
  j = CHAR_LENGTH(a_value);
  while (i <= j) do begin
    if (substring(a_value from i for 1) between '0' and '9'
     or (i =1 and substring(a_value from 1 for 1) in ('-', '+')
       and CHAR_LENGTH(a_value) > 1 )) then
      result = 'Это число';
    else begin
      result = 'Фиг';
      Break;
    end
    i = i + 1;
  end
  suspend;
end
```

```sql
CREATE OR ALTER PROCEDURE CURRENCYSTR(
    VAL NUMERIC(15,2),
    SHOWCURRENCY INTEGER)
RETURNS (
    CURR_STR VARCHAR(1000))
AS
declare razryad varchar(50);
declare razryad_idx varchar(28);
declare hundreds varchar(64);
declare hundreds_idx varchar(30);
declare tens varchar(69);
declare tens_idx varchar(40);
declare ones varchar(138);
declare ones_idx varchar(100);

declare sign_of_val varchar(6);
declare raz int;
declare cents varchar(3);
declare val_str varchar(20);
declare num varchar(20);
declare i int;
declare buf varchar(200);
declare buf1 varchar(200);

begin
  /* Константы */
  razryad_idx = /* 2.2 */ '0100010506071308210829114011';
  razryad = 'тысячмиллионмиллиардтриллионквадриллионквинтиллион';
  hundreds_idx = /* 2.1 */ '010013046106169257328407479569';
  hundreds = 'стодвеститристачетырестапятьсотшестьсотсемьсотвосемьсотдевятьсот';
  tens_idx = /* 2.2 */ '0100010001080908170522093110410950116109';
  tens = 'двадцатьтридцатьсорокпятьдесятшестьдесятсемьдесятвосемьдесятдевяносто';
  ones_idx = /* 3.2 */ '0010000100001000010300406010040140501904023060290603506041110521006210072120841009411105101151212712';
  ones = 'тричетырепятьшестьсемьвосемьдевятьдесятьодиннадцатьдвенадцатьтринадцатьчетырнадцатьпятнадцатьшестнадцатьсемнадцатьвосемнадцатьдевятнадцать';

  if (ShowCurrency is null) then ShowCurrency = 0;
  curr_str = '';

  /* Смотрим знак */
  if (val < 0) then begin
    sign_of_val = 'минус ';
    val = -val;
  end else
    sign_of_val = '';

  /* Выбираем и запоминаем копейки, убираем их из числа */
  val_str = cast(val as varchar(20));
  i = position('.' in val_str);
  cents = lpad(substring(val_str from i+1 for 2), 2, '0');
  val_str = lpad(substring(val_str from 1 for i-1), ((i+1)/3*3), '0');

  /* Разбираем число */
  raz = 0; curr_str = '';
  while (val_str != '') do begin
    /* Берём триаду символов */
    num = right(val_str, 3);
    /* Если не нулевое число */
    if (num != '000') then begin
      /* Берём сотни */
      i = cast(substring(num from 1 for 1) as int);
      buf = substring(hundreds from cast(substring(hundreds_idx from i*3+1 for 2) as int) for cast(substring(hundreds_idx from i*3+3 for 1) as int));

      /* Далее десятки */
      /* Для "десятнадцатых" упрощённая обработка */
      if (substring(num from 2 for 1) = '1') then begin
          /* Вставляем нужную "десятнадцать" */
          i = cast(substring(num from 2 for 2) as int);
          buf1 = substring(ones from cast(substring(ones_idx from i*5+1 for 3) as int) for cast(substring(ones_idx from i*5+4 for 2) as int));
          if (buf != '') then buf = buf || ' ';
          buf = buf || buf1;
      end else
      /* Для "нормальных" чисел своя обработка */
      begin
        /* Десятки */
        i = cast(substring(num from 2 for 1) as int);
        buf1 = substring(tens from cast(substring(tens_idx from i*4+1 for 2) as int) for cast(substring(tens_idx from i*4+3 for 2) as int));
        if (buf != '' and buf1 != '') then buf = buf || ' ';
        buf = buf || buf1;

        /* Единицы */
        i = cast(substring(num from 3 for 1) as int);
        /* Смотрим количество для нужного окончания */
        if (i = 1) then begin
          if (raz = 1) then buf1 = 'одна'; else buf1 = 'один';
        end else
        if (i = 2) then begin
          if (raz = 1) then buf1 = 'две'; else buf1 = 'два';
        end else
          buf1 = substring(ones from cast(substring(ones_idx from i*5+1 for 3) as int) for cast(substring(ones_idx from i*5+4 for 2) as int));
        if (buf != '' and buf1 != '') then buf = buf || ' ';
        buf = buf || buf1;
      end

      /* Разряд числа */
      buf1 = substring(razryad from cast(substring(razryad_idx from raz*4+1 for 2) as int) for cast(substring(razryad_idx from raz*4+3 for 2) as int));
      if (buf1 != '') then begin
        /* Подбор окончания для разряда */
        if (i = 1) then begin
          if (raz = 1) then buf1 = buf1 || 'а';
        end else
        if (i in (2,3,4)) then begin
          if (raz = 1) then buf1 = buf1 || 'и';
          else if (raz > 1) then buf1 = buf1 || 'а';
        end else
          if (raz > 1) then buf1 = buf1 || 'ов';
        buf = buf || ' ' || buf1;
      end
    end else
      buf = '';

    /* Присоединяем обработанную триаду к результату */
    if (curr_str != '' and buf != '') then buf = buf || ' ';
    curr_str = buf || curr_str;
    /* Переходим к следующей триаде */
    val_str = left(val_str, char_length(val_str)-3);
    /* Увеличиваем счётчик разряда */
    raz = raz + 1;
  end

  /* Припысываем знак */
  curr_str = sign_of_val || curr_str;
  /* Делаем первую букву прописной */
  curr_str = upper(substring(curr_str from 1 for 1)) || substring(curr_str from 2);

  /* Флаг "показать название валюты" */
  if (ShowCurrency = 1) then
    curr_str = curr_str || ' руб. ' || cents || ' коп.';

  suspend;
end
```

```sql
WITH RECURSIVE
  RELATIONS AS (
    SELECT DISTINCT
      RC_1.RDB$RELATION_NAME AS RN1, RC_2.RDB$RELATION_NAME AS RN2
    FROM RDB$RELATION_CONSTRAINTS RC_1
    JOIN RDB$REF_CONSTRAINTS REC_2 ON REC_2.RDB$CONST_NAME_UQ = RC_1.RDB$CONSTRAINT_NAME
      AND RC_1.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY'
    JOIN RDB$RELATION_CONSTRAINTS RC_2 ON RC_2.RDB$CONSTRAINT_NAME = REC_2.RDB$CONSTRAINT_NAME
      AND RC_2.RDB$CONSTRAINT_TYPE = 'FOREIGN KEY'
    WHERE RC_1.RDB$RELATION_NAME <> RC_2.RDB$RELATION_NAME
  ),

  RELATIONS_TREE AS (
    SELECT DISTINCT 1 AS LVL, RN1 AS RN_ID, CAST(NULL AS VARCHAR(32)) AS RN_PARENT
    FROM RELATIONS

    UNION ALL

    SELECT RT.LVL + 1, R.RN1, R.RN2
    FROM RELATIONS R
    JOIN RELATIONS_TREE RT ON R.RN2 = RT.RN_ID
  ),

  RELATION_REFS AS (
    SELECT RN_ID, SUM(LVL) AS REFS_COUNT
    FROM RELATIONS_TREE
    GROUP BY 1
  )

SELECT
  RR.RDB$RELATION_NAME AS RELATION_NAME, COALESCE(RT.REFS_COUNT, 0)
FROM RDB$RELATIONS RR
LEFT JOIN RELATION_REFS RT ON RT.RN_ID = RR.RDB$RELATION_NAME
WHERE RR.RDB$VIEW_BLR IS NULL
  AND COALESCE(RR.RDB$SYSTEM_FLAG, 0) = 0
ORDER BY 2 DESC
```

## См. также

## Источник
2008-05-12irebird%\doc\
