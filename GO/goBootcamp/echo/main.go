package main

import (
	"example.com/echo-rest-api/handlers"
	"github.com/labstack/echo/v4"
)

func main(){
    server := echo.New()

    server.GET("/getDetails/:userID", handlers.GetUserDetails)
    server.Start(":9000")
}
