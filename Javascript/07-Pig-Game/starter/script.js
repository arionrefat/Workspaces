'use strict';

// Selecting Score elements so we can use them later
const score0El = document.querySelector('#score--0') // # is the selector or ID and . is the selector for class
const score1El = document.getElementById('score--1') //this is a bit faster
const diceEl = document.querySelector('.dice')
const diceRoll = document.querySelector('.btn--roll')
const diceNew = document.querySelector('.btn--new')
const diceHold = document.querySelector('.btn--hold')

score0El.textContent = 0;
score1El.textContent = 0;
diceEl.classList.add('hidden')

// Rolling dice functionality
diceRoll.addEventListener('click', function() {
    //1. generating a random dice roll
    const dice = Math.trunc(Math.random() * 6) + 1;

    //2. display the dice
    diceEl.classList.remove('hidden');
    diceEl.src = `dice-${dice}.png`
    // if the dice is 1, 
    if (dice == 1) {
        //switched to the next playerswitched to the next player

    }
    else {

    }

})
