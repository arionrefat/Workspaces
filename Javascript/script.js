'use strict';

// Data needed for a later exercise
const flights =
    '_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30';

const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti 23, Firenze, Italy',
    categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
    starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
    mainMenu: ['Pizza', 'Pasta', 'Risotto'],
    order: function (starterIndex, mainMenuIndex) {
        return [this.starterMenu[starterIndex], this.mainMenu[mainMenuIndex]]
    },
    openingHours: {
        thu: {
            open: 12,
            close: 22,
        },
        fri: {
            open: 11,
            close: 23,
        },
        sat: {
            open: 0, // Open 24 hours
            close: 24,
        },
    },

    orderDelivery: function ({time = '20:00', address, mainIndex, starterIndex = 1}) {
        console.log(`Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`);
    }
};

restaurant.orderDelivery({
    time: '22:30',
    address: 'Via del sel, 21',
    mainIndex: 2,
    starterIndex: 2,
})

restaurant.orderDelivery({
    address: 'viva la vida',
    mainIndex: 1
})

const arr = [1, 2, 4, 5];

// destructuring array
const [x, y, z] = arr;
console.log(x, y, z);

let [first, , second] = restaurant.categories;

// const temp = first
// first = second
// second = temp
// console.log(first, second)

// mutating varibables
[first, second] = [second, first]
console.log(first, second)

const [starter, maincourse] = (restaurant.order(2, 0))
console.log(starter, maincourse)

// nested destructuring
const numbers = [1, 4, [5, 6, 7]]
const [i, , [j, , k]] = numbers

//Default Values

const [p = 1, q, r = 69] = [, 8, 9]
console.log(p, r)

const {name, openingHours, catagories} = restaurant;
const {name: restaurantName, openingHours: hours, categories: tags} = restaurant;
const {menu = [], starterMenu: starters = []} = restaurant;

console.log(menu, starters)
// console.log(restaurantName, hours, tags);

// Mutating vars for objects
let val1 = 101;
let val2 = 102;
const obj = {val1: 23, val2: 7, val3: 14};
({val1, val2} = obj);
console.log(val1, val2);

//nested objects
const {fri: {open: o, close: cl}} = openingHours;
console.log(o, cl);
