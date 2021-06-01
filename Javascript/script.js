'use strict';

const number = Math.trunc(Math.random() * 20) + 1;
let score = 20;
console.log(number);

const clickValue = function () {
    const guess = (document.querySelector('.guess').value);

    if (!guess)
        document.querySelector('.message').textContent = 'No number 😓';
    else {
        if (guess > number) {
            if (score > 0) {
                document.querySelector('.message').textContent = 'Guessed High';
                score--;
                document.querySelector('.score').textContent = score;
            }
            else
                document.querySelector('.message').textContent = 'You Lose!🤯';
        }
        else if (guess < number) {
            if (score > 0) {
                document.querySelector('.message').textContent = 'Guessed low';
                score--;
                document.querySelector('.score').textContent = score;
            }
            else
                document.querySelector('.message').textContent = 'You Lose!🤯';
        }
        else {
            document.querySelector('.message').textContent = 'Correct answer!🎉';
            document.querySelector('.number').textContent = guess;
        }
    }
}
document.querySelector('.check').addEventListener('click', clickValue);
