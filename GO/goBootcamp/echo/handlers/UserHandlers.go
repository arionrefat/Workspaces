package handlers

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

type User struct {
	Name string
	Id   string
	Addr string
	Job  string
}

type ErrMsg struct {
	Msg string
}

var userList map[string]User = map[string]User{
	"a": {"shudin", "a", "1254/1 malibag", "Frontend developer"},
	"b": {"shudin1", "b", "uttora", "Android developer"},
	"c": {"shahriar", "c", "dhanmondi", "Backend developer"},
	"d": {"prisoner", "d", "mugda", "Scala developer"},
	"e": {"alex", "e", "USA", "Elixr developer"},
	"f": {"robert", "f", "Unknown", "Rust developer"},
}

func GetUserDetails(c echo.Context) error {
	user_id := c.Param("userID")
	data, ok := userList[user_id]

	if !ok {
		msg := ErrMsg{"User does not exist"}
		c.JSON(http.StatusBadRequest, msg)
		return nil
	}
	c.JSON(http.StatusOK, data)
	return nil
}
