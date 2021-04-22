const array = [10, 13, 14, 15, 2, 1];
console.log(array);

function minTermIndex(i, array) {
    let j = array.length - 1;
    let minNumber = array[i];
    let index = i;
    i++;

    for (i; i <= j; i++) {
        if (minNumber <= array[i]) continue;
        else {
            minNumber = array[i];
            index = i;
        }
    }
    return index;
}

console.log(minTermIndex(0, array));

function selectionSort(index, array){
    const indexOfMin = minTermIndex(index, array);

    if (index == array.length) return;

    if (indexOfMin != index){
        let temp = array[index];
        array[index] = array[indexOfMin];
        array[indexOfMin] = temp;
    }

    selectionSort(index+1,array);
    return array;
}

console.log(arr = selectionSort(0,array));