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

console.log("Let's do type conversion and type coercion");

const inputYear = '1991';
console.log(Number(inputYear),inputYear);
console.log(Number(inputYear)+ 75);
console.log(Number('Jonas'));
console.log(typeof NaN);
