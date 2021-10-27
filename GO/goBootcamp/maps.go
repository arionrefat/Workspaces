package main

import "fmt"

func main() {
	// var map2 map[string]string = make(map[string]string)
	var map3 map[string]string = map[string]string{}
	var map2 map[string]string = map[string]string{"thisi": "thias ", "bisch": "bita"}

	var map1 map[string]interface{}
	// var map1 map[string]interface{} = map[string]interface{}
	map1 = make(map[string]interface{})
	// data := `{"data" : "haha"}`

	map1["this"] = 21
	map1["that"] = 69

	data := `    {
      "name": "Elliot",
      "type": "Reader",
      "age": 23,
      "social": {
        "facebook": "https://facebook.com",
        "twitter": "https://twitter.com"
      }
    }, `
	fmt.Println(map1)
	fmt.Println(map2)
	fmt.Println(map3)
}
