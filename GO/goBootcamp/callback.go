package main

import "fmt"

type fun func(int, int) int

// func main() {
//     Arithmetic(1,3, "sum" ,func (a int,b int) int {
//         return a + b;
//     })
// }

func main() {
	Arithmetic(1, 3, "sum", sum)
}

func sum(a int, b int) int {
	return a + b
}

func Arithmetic(a int, b int, optype string, f fun) {

	var res int

	if optype == "sum" {
		res = f(a, b)
	}
	// fmt.Println(f(a, b));
	fmt.Println(res)
}
