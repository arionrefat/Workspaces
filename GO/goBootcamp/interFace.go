package main

type fn func(int, string) int

type resolve interface {
	Gresolver()
}
