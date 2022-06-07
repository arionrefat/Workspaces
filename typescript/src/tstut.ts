let id: number
id = 5
let company: string = 'reinforz'
let isPublished: boolean = true
let x: any = 'hello'

let ids: number[] = [1, 2, 3, 4, 5, 6]
let arr: any[] = [1, true, 'hello'] //if I don't know what will be the types

// Tuple

let person: [number, string, boolean] = [1, 'refat', true] // this has to be in exact spot

let employe: [number, string][]

employe = [
    [1, 'refat'],
    [2, 'refatul'],
    [3, 'arion'],
]

//union
let pid: string | number = 22
pid = '22'

// Enum
enum Direction1 {
    up = 1,
    Down,
    Left,
    Right,
}

enum Direction2 {
    up = 'up',
    Down = 'down',
    Left = 'left',
    Right = 'right',
}

type User = {
    id: number
    name: string
}

// type User = number | string

// objects
const user: User = {
    id: 2,
    name: 'Refatul',
}

// Type assertion
let cid: any = 1
// let customerID = <string> cid
let customerID = cid as boolean

//function
function addNum(x: number, y: number): number {
    return x + y
}

function log(message: string | number): void {
    console.log(message)
}

// Interface
interface Userinterface {
    readonly id: number
    name: string
    age?: number
}

// objects
const user1: Userinterface = {
    id: 20101482,
    name: 'Refatul',
}

user1.age = 22

interface MathFunc {
    (x: number, y: number): number
}

const add: MathFunc = (x: number, y: number): number => x + y
const sub: MathFunc = (x: number, y: number): number => x - y

interface Personinterface {
    id: number
    name: string
    register(): string
}

// Classes
class Person implements Personinterface {
    id: number
    name: string

    constructor(id: number, name: string) {
        this.id = id
        this.name = name
        console.log(`here I and doing nothing but ${id} and ${name}`)
    }
    add(idnum: number): number {
        idnum = this.id + idnum
        return idnum
    }
    register() {
        return `${this.name} is register, along with his id:${this.id}`
    }
}

let newPerson = new Person(20101482, 'Refatul')
// if not private
// newPerson.id = 69
// console.log(newPerson.add(10))


//subclasses
class Employee extends Person {
    position: string

    constructor(id: number, name: string, position: string) {
        super(id, name)
        this.position = position
    }
}

const emp = new Employee(3, 'Refatul', 'Developer')
console.log(emp.register()) //this is also calling the constructor from Person

//Generics
function getArray<T>(items: T[]): T[]{
    return new Array().concat(items)
}

let numArray = getArray<number>([1,3,4,5,6,7])
let strArray = getArray<String>(['refat','tafer','ferta'])

// numArray.push(11)
