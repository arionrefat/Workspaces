package main

import (
	"errors"
	"fmt"
)

func main() {

	var inputval string = "refat"
	fmt.Println(&inputval)

	var condition bool = true

	if condition {
		fmt.Println("")
	} else {
		fmt.Println("")
	}

	userExists, length, err := validatename("joha")

	fmt.Printf("User exists %v and the length is %v, and there is no %T", userExists, length, err)
}

func validatename(name string) (bool, int, error) {
	const user = "refat"

	if name == user {
		return true, len(name), nil
	} else {
		return false, 0, errors.New("USER DOESNOT EXIT")
	}
}
