console.log("Task 1: " + task1(3, 2));
console.log("Task 3: " + task3(1));

console.log(task5(1, 4));

function task1(base, n) {
    if (n == 0) return 1;
    else return base * task1(base, n - 1);
}

function task3(height) {
    if (height != 0) {
        if (height == 1)
            return 8;
        else
            return 5 + task3(height - 1);
    }
    else return "Houes cann't be build";
}

function task5(row, input) {

}
