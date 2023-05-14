package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

var (
	DB *sql.DB
)

type User struct {
	Name string
	Age  int
}

func connect() {
	connStr := "postgres://postgres:admin123@localhost/test?sslmode=disable"
	DB, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	var name string
	err = DB.QueryRow("SELECT * FROM pg_catalog.pg_tables;").Scan(&name)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(name)
}

func query() {

	// txn, err := DB.Begin()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// stmt, err := txn.Prepare(pq.CopyIn("users", "name", "age"))
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// _, err = stmt.Exec("alif", int64(21))
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// err = stmt.Close()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// err = txn.Commit()
	// if err != nil {
	// 	log.Fatal(err)
	// }
}

func main() {
	connect()
	// query()
}
