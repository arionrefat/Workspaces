package main

import "fmt"

func main() {

	type student struct{
		Id int8
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

	// person1 := Person{ "Refatul", 1112, "1212", "asas", "TAAT" }
	person1 := Person{Name: "Refat", Phone: 1112, address: "asa"}
	fmt.Println(person1)
}
