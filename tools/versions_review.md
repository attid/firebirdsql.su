# Разбор версий: страницы без автоматического since

Авто-заполнение (tools/apply_versions.py) покрывает доказанные случаи.
Ниже — остальное, разбито по категориям с решениями (2026-09-24).

## Не применимо: статьи, лендинги, дайджесты (флаг версии не ставится)

1glossarij, chto_takoe_firebird, indices_maintenance, istochniki_i_avtory,
matematicheskie_operacii_s_datoj, novosti-2026-*, o_sajte, odbc,
operatory_konstrukcii_select, oshibki_pri_sozdanii_metadannyx,
podkljuchenie_k_baze_dannyx_iz_1s, polesnue_zaprosu, port_3050, pravila,
python_async, samostojatelnaja_sborka_snapshota_firebird,
script_alert_script, skript_dlja_rezervirovanija_*,
soglashenija_sintaksisa, sql0xx.*, start, sidebar, sistemnye_tablicy,
tablicy_monitoringa, tipy_dannyx, transfer_table, ustanovka_*, utils,
vstroennye_funkcii, vstroennye_funkcii_po_gruppam

## Не применимо: утилиты и isql-директивы (не серверные конструкции)

autoddl (isql-опция), gbak, gfix, gsec, instclient.exe, set_term, sweep,
gdscodes (коды ошибок)

## Базовые конструкции SQL: есть во всех версиях, точная дата — InterBase-эра

join, returns, distinct, constraint, interval, if (PSQL), new_old
(NEW/OLD в триггерах), connect.
Пока since пуст — страница показывается при любом фильтре. Ставить
доказанное «≤2.5» как точный бейдж нельзя (ввело бы в заблуждение).

## EXTRACT-семейство: ключевые слова EXTRACT, присутствуют во всех версиях

hour, minute, month, second, year, weekday. Родственная страница day
получила since 0.9 по своей таблице; у этих таблицы в другом формате
(список версий без Да/−) — при желании привести к общему виду.

## Есть в LR 2.5+, точная дата требует release notes (оставлено пустым)

create_generator, rdb_generators, rdb_index_segments, rdb_ref_constraints.
CREATE GENERATOR / RDB$GENERATORS — InterBase-эра, но доказательства в
наших источниках только «≤2.5».

## Разобрано вручную

- comment → since: "2.0" (Firebird 2.0 release notes, DDL раздел)
- autonomous_transaction → since: "2.5" (таблица в теле страницы +
  синтаксис WITH {AUTONOMOUS | COMMON} TRANSACTION в книге 2.5)
