package main

import (
	"fmt"
)

type student struct {
	Id   int8
	cgpa int8
}

type Person struct {
	Name    string
	Phone   int
	address string
	job     string
	gender  string
	student student
}

func main() {

	// person1 := Person{ "Refatul", 1112, "1212", "asas", "TAAT" }
	person1 := Person{Name: "Refat", Phone: 1112, address: "asa"}

	person2 := struct {
		Name  string
		Id    int
		Phone int
	}{
		Name:  "Refat",
		Id:    1212131,
		Phone: 01201201,
	}

    defer fmt.Println("hello")
    // json.Unmarshal(&person2)
	fmt.Println(person1)
	fmt.Println(person2)
}
