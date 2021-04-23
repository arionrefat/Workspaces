class ListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }

}

class LinkedList {
    constructor(array) {
        let head = new ListNode();

        if (array.length != 0) {
            let head = new ListNode(array[0]);
            let tail = new ListNode();
            tail = head;

            for (let i = 0; i < array.length; i++) {
                tail.next = new ListNode(array[i]);
                tail = tail.next;
            }

        }
    }

    size() {
        let count = 0;
        let node = this.head;
        while (node) {
            count++;
            node = node.next
        }
        return count;
    }
}

const array = [1, 4, 4, 8, 11, 19, 1];
let linked1 = new LinkedList(array);
console.log(linked1.size());


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

function selectionSort(index, array) {
    const indexOfMin = minTermIndex(index, array);

    if (index == array.length) return;

    if (indexOfMin != index) {
        let temp = array[index];
        array[index] = array[indexOfMin];
        array[indexOfMin] = temp;
    }

    selectionSort(index + 1, array);
    return array;
}

console.log(arr = selectionSort(0, array));
