package main

import "fmt"

func main(){

    // slice is a reference type
    var sliceA [] string = [] string{"alo", "alo"}
    var arrayA := [10] string {"this"}

    ab := append(sliceA, "news", "shit")

    fmt.Println(ab)
}
