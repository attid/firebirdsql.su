<?php
declare(strict_types=1);

// PDO Firebird: dbname=хост:путь_к_базе. Хост firebird — имя сервиса compose.
$dsn = "firebird:dbname=firebird:/var/lib/firebird/data/employee.fdb;charset=UTF8";

$pdo = new PDO($dsn, "SYSDBA", "masterkey", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);

$stmt = $pdo->query(
    "SELECT FIRST_NAME, LAST_NAME, SALARY "
    . "FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5"
);

echo "Топ-5 сотрудников по зарплате:\n";
foreach ($stmt as $row) {
    printf("  %s %s — %.2f\n", $row["FIRST_NAME"], $row["LAST_NAME"], $row["SALARY"]);
}
