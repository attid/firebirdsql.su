import firebirdsql

# Чистый Python-драйвер (без нативных библиотек).
# dsn: host:path — хост firebird это имя сервиса docker compose.
# Нюанс (проверено): с явным портом (firebird/3050:...) драйвер 1.4.7
# против Firebird 5 падает "unavailable database" — порт опускаем,
# 3050 используется по умолчанию.
con = firebirdsql.connect(
    dsn="firebird:/var/lib/firebird/data/employee.fdb",
    user="SYSDBA",
    password="masterkey",
    charset="utf-8",
)

cur = con.cursor()
cur.execute(
    "SELECT FIRST_NAME, LAST_NAME, SALARY "
    "FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5"
)

print("Топ-5 сотрудников по зарплате:")
for first, last, salary in cur.fetchall():
    print(f"  {first} {last} — {salary:.2f}")

con.close()
