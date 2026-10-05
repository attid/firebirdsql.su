#!/usr/bin/env bash
# Инициализация employee.fdb — штатной демо-базы Firebird.
# Идемпотентно: повторный запуск ничего не ломает.
set -euo pipefail
cd "$(dirname "$0")"

docker compose up -d firebird
echo "Ждём готовности firebird..."
for i in $(seq 1 30); do
  if docker compose exec -T firebird sh -c \
    "echo 'SELECT 1 FROM RDB\$DATABASE;' | isql -user SYSDBA -password masterkey localhost:/var/lib/firebird/data/employee.fdb >/dev/null 2>&1"; then
    break
  fi
  [ "$i" = "30" ] && { echo "firebird не поднялся за 150с"; exit 1; }
  sleep 5
done

# Уже инициализирована?
if docker compose exec -T firebird sh -c \
  "echo \"SELECT COUNT(*) FROM EMPLOYEE;\" | isql -user SYSDBA -password masterkey localhost:/var/lib/firebird/data/employee.fdb 2>/dev/null" \
  | grep -qE '[0-9]'; then
  echo "employee.fdb уже инициализирована — пропускаю."
  exit 0
fi

echo "Создаю каноническую демо-базу employee (DDL + данные из Firebird ${FB_VER:-5.0.4})..."
docker compose exec -T firebird isql -user SYSDBA -password masterkey \
  -i /scripts/empddl.sql localhost:/var/lib/firebird/data/employee.fdb
docker compose exec -T firebird isql -user SYSDBA -password masterkey \
  -i /scripts/empdml.sql localhost:/var/lib/firebird/data/employee.fdb
echo "employee.fdb готова."
