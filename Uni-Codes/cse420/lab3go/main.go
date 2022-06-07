package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	lineEnding := "\n" // put it as "\r\n" for CRLF, "\n" for LF
	FileName := "inputs.txt"
	dataInByte, err := ioutil.ReadFile(FileName)
	if err != nil {
		fmt.Printf("Can't read file: %v\n", FileName)
		panic(err)
	}
	data := strings.Split(string(dataInByte), lineEnding)

	regN, err := strconv.ParseInt(data[0], 10, 32)
	if err != nil {
		fmt.Printf("Can't Parse Int: %v\n", data[0])
		panic(err)
	}
	var r []*regexp.Regexp
	for i := 1; i <= int(regN); i++ {
		r = append(r, regexp.MustCompile(data[i]))
	}

	ins, err := strconv.ParseInt(data[1+regN], 10, 32)
	if err != nil {
		fmt.Printf("Can't Parse Int: %v\n", data[1+regN])
		panic(err)
	}
	for i := 2 + regN; i < 2+regN+ins; i++ {
		regSerial := 1 + regN
		for indx, v := range r {
			if v.MatchString(data[i]) {
				regSerial = int64(indx) + 1
				break
			}
		}
		if regSerial <= regN {
			fmt.Printf("YES, %v\n", regSerial)
		} else {
			fmt.Println("NO, 0")
		}
	}
}
