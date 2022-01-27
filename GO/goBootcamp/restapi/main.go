package main

import (
	"net/http"

	"github.com/gorilla/mux"
)

func serverHello(rw http.ResponseWriter, r *http.Request) {
    mux.Vars(r)
	rw.Write([]byte("Hello"))
}

func main() {
    router := mux.NewRouter()
	router.HandleFunc("/ping/server{id}", serverHello)
	http.ListenAndServe(":8000", nil)
}
