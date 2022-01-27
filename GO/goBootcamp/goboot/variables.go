package main

import "fmt"

func main() {
	var variable string = "this is a string"
	var nextVariable = 45 //inferred

	nextVariable2 := "his is a string " //only useable inside a function
	x, y := 8, 0

	var (
		a = 55
		b = 99
	)

	const (
		ip     = "10.12.1.3.3"
		dbname = "mongoDB"
	)

	fmt.Println(variable)
	fmt.Println(nextVariable2)
	fmt.Println(nextVariable)
	fmt.Println(a, b)
	fmt.Println(x, y)
}
