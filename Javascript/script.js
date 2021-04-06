'use strict';
/*
document.querySelector('.message').textContent = '🎉Correct Number!';
console.log(document.querySelector('.message').textContent);

document.querySelector('.number').textContent = 13;
document.querySelector('.score').textContent = 10;
document.querySelector('.guess').value = 23;
console.log(document.querySelector('.guess').value);
*/

const clickValue = function(){
    console.log(document.querySelector('.guess').value);
    const guess = (document.querySelector('.guess').value);
    console.log(typeof guess);
}
document.querySelector('.check').addEventListener('click',clickValue);
