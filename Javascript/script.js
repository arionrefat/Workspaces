'use strict'

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

    orderDelivery: function ({
        time = '20:00',
        address,
        mainIndex,
        starterIndex = 1,
    }) {
        console.log(
            `Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`
        )
    },

    orderPasta: function (ing1, ing2, ing3) {
        console.log(`Here is your pastas with ${ing1}, ${ing2} and ${ing3}`)
    },
}

// SPREAD operator because on right side of the assignment operator ( = )
const arr = [1, 2, ...[3, 4]]

// REST operator because on left side of the assignment operator ( = )
const [a, b, ...others] = [1, 2, 3, 4, 5, 6]
console.log(a, b, others)
const [pizza, , rissoto, ...otherfood] = [
    ...restaurant.mainMenu,
    ...restaurant.starterMenu,
]
console.log(pizza, rissoto, otherfood)
