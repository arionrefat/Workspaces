'use strict';
/*
document.querySelector('.message').textContent = '🎉Correct Number!';
console.log(document.querySelector('.message').textContent);

document.querySelector('.number').textContent = 13;
document.querySelector('.score').textContent = 10;
document.querySelector('.guess').value = 23;
console.log(document.querySelector('.guess').value);
*/

const clickValue = function() {
    const guess = (document.querySelector('.guess').value);
    if (!guess) document.querySelector('.message').textContent = 'No number';
    else document.querySelector('.message').textContent = guess;
}
document.querySelector('.check').addEventListener('click', clickValue);
