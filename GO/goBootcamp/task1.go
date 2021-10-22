package main;

import ( "encoding/json"; "fmt"; "os"; "io/ioutil")

type SocialMedia struct{
    Facebook string `json:"facebook"`
    Twitter string `json:"twitter"`
}

type Person struct {
    Name string `json:"name"`
    Persontype string `json:"type"`
    Age int `json:"age"`
    Social SocialMedia `json:"social"`
}

type Users struct{
    User []Person `json:"users"`
}

func main(){
    Jsondata, err := os.Open("data.json") /// path of the file
	defer Jsondata.Close()

    if err != nil{
        fmt.Println(err);
    }

    // var result map[string]interface{} // Without using struct
    result := Users{};  //  using struct

    byteValue, _ := ioutil.ReadAll(Jsondata)
    json.Unmarshal([]byte(byteValue), &result)
    fmt.Println(result)
}
