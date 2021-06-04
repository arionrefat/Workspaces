'use strict';

let number = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

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
            document.querySelector('body').style.backgroundColor = '#60b347';
            document.querySelector('.number').style.width = '30rem';

            if (score > highscore) {
                highscore = score;
                document.querySelector('.highscore').textContent = highscore;
            }
        }
    }
}

const reset = function () {
    score = 20;
    number = Math.trunc(Math.random() * 20) + 1;

    document.querySelector('.message').textContent = 'Start guessing...';
    document.querySelector('.score').textContent = score;
    document.querySelector('.number').textContent = '?';
    document.querySelector('.guess').value = '';

    document.querySelector('body').style.backgroundColor = '#222';
    document.querySelector('.number').style.width = '15rem';
}

document.querySelector('.check').addEventListener('click', clickValue);
document.querySelector('.again').addEventListener('click', reset);
