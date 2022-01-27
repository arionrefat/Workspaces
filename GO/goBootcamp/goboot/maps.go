package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type CSVReader struct {
	Path string
}

// func (c *CSVReader) ReadFile() {

// 	clients := []*Client{}
// 	clientFile, err = os.OpenFile(c.path, os.O_RDWR|os.O_CREATE, os.ModeAppend)
// 	if err != nil {
// 		fmt.Println(err)
// 	}
// 	defer clientFile.Close()

// 	gocsv.UnmarshalFile(clientFile, &clients)
// 	for _, client := range clients {
// 		fmt.Println("Hello", client.Name)
// 	}
// }

// var(
// 	Clients []*Client{}
// )

type JsonReader struct {
	Path string
}

func (j *JsonReader) ReadFile() {
	clients := []*Client{}
	jsonFile, _ := os.Open(j.Path)
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	json.Unmarshal([]byte(byteValue), &clients)
	for _, client := range clients {
		fmt.Println("Hello", client.Name)
	}
}

type Client struct {
	Id   string `csv:"client_id" json:"client_id"`
	Name string `csv:"client_name" json:"client_name"`
	Age  string `csv:"client_age" json:"client_age"`
}

func main() {
	// csvreader := CSVReader{"people.csv"}
	// csvreader.ReadFile()
	jsonReader := JsonReader{"people.json"}
	jsonReader.ReadFile()
}
