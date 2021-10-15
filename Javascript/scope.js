'use script'

function calcAge(birthYear) {
    const age = 2037 - birthYear;

    function printAge() {
        const output = `You are ${age}, born is ${birthYear}`
        console.log(output)
    }
    printAge();
    return age;
}

const firstName = 'jonas';
calcAge(1991);
