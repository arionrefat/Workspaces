package main

import (
    "fmt"
    "github.com/gocarina/gocsv"
)

type CSVReader struct{
    Path string
}

var Clients []*Client{}

func (c *CSVReader) ReadFile(){
    Clients := []*Clients{}
    clienFile , err := os.Open(c.Path, os.O_RDWR|os.O_CREATE, os.ModePerm)
    if err != nil {
        fmt.Println(err)
    }
    defer clientFile.close()
    gocsv.Unmarshal(clientFile,&clients)

    for _,clients := range clients{
        fmt.Println("Hello", client.name)
    }
}


type Client struct{
    Id string `csv:"client_id"`
    Name string `csv:"client_name"`
    Age string `csv:"client_age"`
}

func main(){
    csvreader := CCSVReader("people.csv")
    csvreader.ReadFile()
}
