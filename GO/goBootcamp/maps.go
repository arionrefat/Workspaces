package main

import ("fmt"; "json")

func main() {
	var map1 map[string]interface{}
	// var map1 map[string]interface{} = map[string]interface{}
	map1 = make(map[string]interface{})
    // data := `{"data" : "haha"}`

	map1["this"] = 21
	map1["that"] = 69

	fmt.Println(map1)

}
