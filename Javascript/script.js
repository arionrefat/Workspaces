'use strict';

const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti 23, Firenze, Italy',
    categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
    starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
    mainMenu: ['Pizza', 'Pasta', 'Risotto'],
    order: function (starterIndex, mainIndex) {
        return this.starterMenu[starterIndex], this.starterMenu[mainIndex];
    },
};

// let [first, , second] = (restaurant.categories[(first, second)] = [
//     second,
//     first,
// ]); // switch variables by destructuring
//
// console.log(first, second);
//
// console.log(restaurant.order(2, 0));

const {name, mainMenu, ...renew} = restaurant
console.log(renew)
