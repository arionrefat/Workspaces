'use strict'

//importing json file
const dataOfCompanies = require("./index.json")
console.log(dataOfCompanies[1].name);

// This is called function declaration and you even call the function before the fuction declared
function age(birthyear){
    return 2077 - birthyear;
}
//This is called a anonymous function and also called function expression
const calcAge = function (birthyear) {
    return 2037 - birthyear;
}

// This is called arrow function
const calcAge3 = birthyear => 2037 - birthyear;
console.log(calcAge3(2000));

const yearUntillRetirement = birthyear => {
    const age = 2031 - birthyear;
    const retirement = 65 - age;
    return retirement;
}
