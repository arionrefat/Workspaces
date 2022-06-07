package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

func main() {
	FileName := "input.txt"
	data, err := str(ioutil.ReadFile(FileName))
	if err != nil {
		fmt.Printf("Can't read file: %v\n", FileName)
		panic(err)
	}

	var regN int
	fmt.Scan(&regN)
	var r []*regexp.Regexp
	for i := 1; i <= regN; i++ {
		var s string
		fmt.Scan(&s)
		r = append(r, regexp.MustCompile(s))
	}

	var ins int
	fmt.Scan(&ins)
	for i := 1; i <= ins; i++ {
		var s string
		fmt.Scan(&s)
		regSerial := 0
		for i, v := range r {
			if v.MatchString(s) {
				regSerial = i + 1
				break
			}
		}
		if regSerial != 0 {
			fmt.Printf("YES, %v\n", regSerial)
		} else {
			fmt.Println("No, 0")
		}
	}
}
