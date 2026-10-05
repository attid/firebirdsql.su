package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/nakagami/firebirdsql"
)

func main() {
	// firebirdsql://user:password@host:port/path/to/database
	dsn := "SYSDBA:masterkey@firebird:3050/var/lib/firebird/data/employee.fdb?charset=UTF8"

	db, err := sql.Open("firebirdsql", dsn)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	rows, err := db.Query(
		"SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	fmt.Println("Топ-5 сотрудников по зарплате:")
	for rows.Next() {
		var first, last string
		var salary float64
		if err := rows.Scan(&first, &last, &salary); err != nil {
			log.Fatal(err)
		}
		fmt.Printf("  %s %s — %.2f\n", first, last, salary)
	}
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
}
