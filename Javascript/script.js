'use strict';

const number = Math.trunc(Math.random() * 20) + 1;
console.log(number);

const clickValue = function () {
    const guess = (document.querySelector('.guess').value);

    if (!guess)
        document.querySelector('.message').textContent = 'No number';
    else {
        if (guess > number) document.querySelector('.message').textContent = 'Guessed a bit High';
        else if (guess < number) document.querySelector('.message').textContent = 'Guessed a bit Low';
        else {
            document.querySelector('.message').textContent = 'Correct answer!';
            document.querySelector('.number').textContent = guess;
        }
    }
}
document.querySelector('.check').addEventListener('click', clickValue);
