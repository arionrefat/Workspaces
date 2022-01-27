package main

import "fmt"

type Student struct {
	Name   string
	Id     int32
	Course []Course
}

type Course struct {
	Department string
	Code       int16
	Section    string
}

func (addS *Student) addcourse( dept string, code int16, section string) {
    addS.Course = append(addS.Course, dept, code, section)
}

func (s *Student) Printdetails() {
	fmt.Printf("Name: %v\n", s.Name)
	fmt.Printf("ID: %v\n", s.Id)
	fmt.Println("-----------")
	fmt.Printf("Course Department: %v\n", s.Course.Department)
	fmt.Printf("Course Code: %v\n", s.Course.Code)
	fmt.Printf("Course Section: %v\n", s.Course.Section)
}

func main() {
	student := Student{}
	student.Name = "Safwan Hossein Rakin"
	student.Id = 20101033
	student.addcourse("CSE", 211, "A2")
	student.addcourse("CSE", 255, "A5")
	student.Printdetails()
}
