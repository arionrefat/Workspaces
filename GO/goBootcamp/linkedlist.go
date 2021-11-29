package main

import "fmt"

type Node struct {
	Data int
	Next *Node
}

type List struct {
	Head *Node
}

func (l *List) PrintList() {
	list := l.Head
	for list != nil {
		fmt.Printf("%v ->", list.Data)
		list = list.Next
	}
}

func (l *List) Insert(data int) {
	head := l.Head
	if head == nil {
		l.Head = &Node{Data: data}
		return
	}
	for head.Next != nil {
		head = head.Next
	}
	head.Next = &Node{Data: data}
}

func main() {
	list := List{}
	list.Insert(4)
	list.Insert(8)
	list.Insert(9)
	list.Insert(7)
	list.Insert(1)
	list.Insert(12)
	list.PrintList()
}
