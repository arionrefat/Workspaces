/* How to create a boolean variable with other variable */

const year1 = 2020;
const year2 = 2077;

const isLarger = year1 > year2;
console.log(isLarger);

const firstName = 'Jonas';
const job = 'teacher';
const birthyear = 2000;
const year = 2020;

const jonas = "I'm " + firstName + ', a ' + (year - birthyear) + ' year old ' + job + '!';
console.log(jonas);

console.log("This is called templete literal");
const jonasNew = `I'm ${firstName}, a ${year - birthyear} year old ${job}`
console.log(jonasNew);

console.log(`Just a regular string`);

console.log(`Use backticks for string alwasys hahaha `);
console.log(`String with \n\
multiple \n\
lines`);

console.log(`String
with
a
new line`);

// Can use blocks or not in else statement

console.log("This is called a control stucture");

const age = 10;

if (age >= 18) console.log("yes he is ready to drive");
else {
    yearsleft = 18 - age;
    console.log(`she cant drive because she is ${yearsleft} years left`);
}

console.log("Let's do type conversion ");

const inputYear = '1991';
console.log(Number(inputYear),inputYear);
console.log(Number(inputYear)+ 75);
console.log(Number('Jonas'));
console.log(typeof NaN);
console.log(String(23),23);

console.log("THis is Type Coercion");

console.log('I am ' +28 + ' years old');
console.log('I am ' +String(23)+ ' years old');
console.log('23' + '10' + 9); //It will produce 23109 since it has + operator
console.log('23' - '10' - 9); // But it will show 10 because it will
console.log('20' / '9');
console.log('23' > '18');

let n = '1' + 1;
n = n - 1;
console.log(n)


console.log("\n Five falsy values: 0, '', undefined, null, NoN");
console.log("----------------------");

console.log(Boolean(0));
console.log(Boolean(undefined));
console.log(Boolean(null));
console.log(Boolean('Jonas'));
console.log(Boolean({}));

const money = 0;

if (money) console.log(`Don't spend any money`);
else console.log(`Get a job you crap`);

let height;
if (height) console.log("Yes run it");
else console.log("It is undefined");

