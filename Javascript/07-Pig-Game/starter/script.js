'use strict';

// Selecting Score elements so we can use them later
const player0EL = document.querySelector('.player--1')
const player1EL = document.querySelector('.player--0')
const score0El = document.querySelector('#score--0') // # is the selector or ID and . is the selector for class
const score1El = document.getElementById('score--1') //this is a bit faster
const current0EL = document.getElementById('current--0') //this is a bit faster
const current1EL = document.getElementById('current--1') //this is a bit faster
const diceEl = document.querySelector('.dice')
const diceRoll = document.querySelector('.btn--roll')
const diceNew = document.querySelector('.btn--new')
const diceHold = document.querySelector('.btn--hold')

score0El.textContent = 0;
score1El.textContent = 0;
diceEl.classList.add('hidden')

const scores = [0,0];
let currentScore = 0;
let activePlayer = 0;

// Rolling dice functionality
diceRoll.addEventListener('click', function() {
    //1. generating a random dice roll
    const dice = Math.trunc(Math.random() * 6) + 1;

    //2. display the dice
    diceEl.classList.remove('hidden');
    diceEl.src = `dice-${dice}.png`
    // if the dice is 1, then
    if (dice != 1) {
        // add the dice number to the currentscore
        currentScore += dice;
        document.getElementById(`current--${activePlayer}`).textContent = currentScore;
    }
    else {
        //switched to the next player
        document.getElementById(`current--${activePlayer}`).textContent = 0;
        currentScore = 0;
        activePlayer = activePlayer === 0 ? 1 : 0;
        player0EL.classList.toggle('player--active');
        player1EL.classList.toggle('player--active');
    }

})

diceHold.addEventListener('click', function(){
    //first add current score to active player's score
})