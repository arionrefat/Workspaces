package main

import (
	"fmt"
)

func main() {
	// array declarartion
	var arr2 [5]int
	// pointer
	// var arr2 *[5]int
	// var arr3 = new([5]string)

	arr2[2] = 69

	fmt.Println(arr2[2])
}
