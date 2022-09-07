let id: number = 5;

// tuple

let person: [string, number, boolean] = ['hello', 124, true];

// tuple array
let employee: [string, number][] = [
  ['hello', 123],
  ['suasd', 700],
];

// Union
let id1: string | number = 123;

// enumarated types

enum Direction {
  Up = 'up',
  down = 'down',
  left = 'left',
  right = 'right',
}

const user: {
  id: number;
  name: string;
} = {
  id: 1,
  name: 'refat',
};

// or we can do this instead

type User = {
  readonly id: number;
  name: string;
};

const anotherUser: User = {
  id: 12,
  name: 'refat',
};

// type assertion
let customer: any = 1;

// if want to use the customer variable as types
let customerId = <number>customer;
// or use as `type`
customerId = customer as number;

customerId = 1;

function log(message: number | string): void {
  console.log(message);
}

interface UserInterface {
  id: number;
  name: string;
  age?: number;
} // can't use union types on inteface

const newUser: UserInterface = {
  id: 12,
  name: 'refat',
  age: 12,
};

newUser.name = 'refat'; // can change values of respective keys but cannot the keys along with values

interface MathFunc {
  (x: number, y: number): number;
}

const add: MathFunc = (x: number, y: number): number => x + y; //shows error if y: string

interface PersonInterface {
  id: number;
  name: string;
  register(): number;
  age?: number;
} // can't use union types on inteface

class Person implements PersonInterface {
  readonly id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }
  register() {
    return id + 1;
  }
}

const refat = new Person(12, 'hello');
refat.name = 'asd';

// this employee class is call subclasses
class Employee extends Person {
  position: string;

  constructor(id: number, name: string, position: string) {
    super(id, name);
    this.position = position;
  }
}

const emp = new Employee(12, 'rfat', 'manager');

// now time for generics
function getArray(items: any[]): any[] {
  return new Array().concat(items);
}

let idArray = getArray([1, 12312, 12]);
let stringarray = getArray(['asd', 'asdsad']);

idArray.push('asdsa'); // I don't want string to be in a number array

// now time for generics
function getArray2<type>(items: type[]): type[] {
  return new Array().concat(items);
}

let idArray2 = getArray2<number>([1, 12312, 12]);
let stringarray2 = getArray2<string>(['asd', 'asdsad']);

idArray2.push(12);

function incomeTax(income: number, taxYear?: number): number {
  if ((taxYear || 2020) > 2022) return income * 1.6;
  return income * 12; // always need else otherwise it will return undefined
}

function incomeTax2(income: number, taxYear = 2020): number {
  if (taxYear > 12000) return income * 1.6;
  return income * 12; // always need else otherwise it will return undefined
} //better approach for functions

// Intersection types

type Dragable = {
  drag: () => void;
};

type resizeable = {
  resize: () => void;
};

type UIwidget = Dragable & resizeable;

let textBox: UIwidget = {
  drag: () => {},
  resize: () => {},
};

//literal types
let exo: 80 | 100 = 100;
type name = 'refat' | 'hamim';

const names: name = 'refat';

// nullable types
function greet(name: string | null | undefined) {
  if (name) console.log(name.toUpperCase());
  console.log('heloa');
}
greet(null);

// optional property access operator
type Customer12 = {
  birthday?: Date;
};

function getCustomer(id: number): Customer12 | null | undefined {
  return id === 0 ? null : { birthday: new Date() };
}

let customer1 = getCustomer(0);
console.log(customer1?.birthday?.getFullYear()); //will only show birthday if there is no null value
