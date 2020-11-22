const firstName = 'Jonas';
const job = 'teacher';
const birthyear = 2000;
const year = 2020;

const jonas = "I'm " + firstName + ', a ' + (year - birthyear) + ' year old ' + job + '!';
console.log(jonas);

const jonasNew = `I'm ${firstName}, a (${year} - ${birthyear}) ${job}`
console.log(jonasNew);