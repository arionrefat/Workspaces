"use strict";
let id;
id = 5;
let company = 'reinforz';
let isPublished = true;
let x = 'hello';
let ids = [1, 2, 3, 4, 5, 6];
let arr = [1, true, 'hello'];
let person = [1, 'refat', true];
let employe;
employe = [
    [1, 'refat'],
    [2, 'refatul'],
    [3, 'arion'],
];
let pid = 22;
pid = '22';
var Direction1;
(function (Direction1) {
    Direction1[Direction1["up"] = 1] = "up";
    Direction1[Direction1["Down"] = 2] = "Down";
    Direction1[Direction1["Left"] = 3] = "Left";
    Direction1[Direction1["Right"] = 4] = "Right";
})(Direction1 || (Direction1 = {}));
var Direction2;
(function (Direction2) {
    Direction2["up"] = "up";
    Direction2["Down"] = "down";
    Direction2["Left"] = "left";
    Direction2["Right"] = "right";
})(Direction2 || (Direction2 = {}));
const user = {
    id: 2,
    name: 'Refatul',
};
let cid = 1;
let customerID = cid;
function addNum(x, y) {
    return x + y;
}
function log(message) {
    console.log(message);
}
const user1 = {
    id: 20101482,
    name: 'Refatul',
};
user1.age = 22;
const add = (x, y) => x + y;
const sub = (x, y) => x - y;
class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        console.log(`here I and doing nothing but ${id} and ${name}`);
    }
    add(idnum) {
        idnum = this.id + idnum;
        return idnum;
    }
    register() {
        return `${this.name} is register, along with his id:${this.id}`;
    }
}
let newPerson = new Person(20101482, 'Refatul');
class Employee extends Person {
    constructor(id, name, position) {
        super(id, name);
        this.position = position;
    }
}
const emp = new Employee(3, 'Refatul', 'Developer');
console.log(emp.register());
function getArray(items) {
    return new Array().concat(items);
}
let numArray = getArray([1, 3, 4, 5, 6, 7]);
let strArray = getArray(['refat', 'tafer', 'ferta']);
