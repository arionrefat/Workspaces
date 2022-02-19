package main

import (
	"fmt"
	"io/ioutil"
)

func isDelimiter(ch byte) bool {
	if ch == ' ' || ch == '+' || ch == '-' || ch == '*' ||
		ch == '/' || ch == ',' || ch == ';' || ch == '>' ||
		ch == '<' || ch == '=' || ch == '(' || ch == ')' ||
		ch == '[' || ch == ']' || ch == '{' || ch == '}' {
		return true
	}
	return false
}

func isOperator(ch byte) bool {
	if ch == '+' || ch == '-' || ch == '*' ||
		ch == '/' || ch == '>' || ch == '<' ||
		ch == '=' {
		return true
	}
	return false
}

func isValididentifier(str *byte) bool {
	if str == '0' || str == '1' || str == '2' ||
		str == '3' || str == '4' || str == '5' ||
		str == '6' || str == '7' || str == '8' ||
		str == '9' || isDelimiter(str) == true {
		return (false)
	}
	return (true)
}

func main() {
	fileinput, _ := ioutil.ReadFile("input.txt")
	file := string(fileinput)

	fmt.Print(file)
	fmt.Println("------")
	fmt.Println(isDelimiter('a'))
}
