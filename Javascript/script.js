'use strict';

const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti 23, Firenze, Italy',
    categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
    starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
    mainMenu: ['Pizza', 'Pasta', 'Risotto'],
    order: function(starterIndex, mainMenuIndex) {
        return [this.starterMenu[starterIndex], this.mainMenu[mainMenuIndex]]
    }
};

const arr = [1, 2, 4, 5];
const a = arr[0];
const b = arr[1];
const c = arr[2];

// destructuring array
const [x, y, z] = arr;
console.log(x, y, z);

let [first, , second] = restaurant.categories;

// const temp = first
// first = second
// second = temp
// console.log(first, second)

[first, second] = [second, first]
console.log(first, second)

const [starter, maincourse] = (restaurant.order(2, 0))
console.log(starter, maincourse)

// nested destructuring
const numbers = [1, 4, [5, 6, 7]]
const [i, , [j, , k]] = numbers
