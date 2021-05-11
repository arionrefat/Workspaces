// The following code has been written in Javascript
// Please use node.js or any modern browser to test it

class SinglyListNode {
  constructor(data, next) {
    this.data = data;
    this.next = next;
  }
}

class DoublyListNode {
  constructor(data, next, prev) {
    this.data = data;
    this.next = next;
    this.prev = prev;
  }
}

function showList(list) {
  let elements = [];
  let node = list.head;
  while (node !== null) {
    elements = [...elements, node.data];
    node = node.next;
  }
  console.log(elements);
}

function selectionSortArrayRecursively(array, start, end) {
  if (start === end) return array;
  else {
    let minIndex = start;
    for (let index = start + 1; index < end; index++) {
      if (array[index] < array[minIndex]) minIndex = index;
    }
    const temp = array[start];
    array[start] = array[minIndex];
    array[minIndex] = temp;
    return selectionSortArrayRecursively(array, start + 1, end);
  }
}

function testSelectionSortArrayRecursively() {
  console.log("Selection Sort Array Recursively");
  console.log(selectionSortArrayRecursively([4, 6, 1, 3, 2, 5], 0, 6));
  console.log();
}

testSelectionSortArrayRecursively();

function insertionSortArrayRecursively(array, size) {
  if (size <= 0) return array;
  else {
    insertionSortArrayRecursively(array, size - 1);
    const last = array[size];
    let idx = size - 1;
    while (idx >= 0 && array[idx] > last) {
      array[idx + 1] = array[idx];
      idx--;
    }
    array[idx + 1] = last;
    return array;
  }
}

function testInsertionSortArrayRecursively() {
  console.log("Insertion Sort Array Recursively");
  console.log(insertionSortArrayRecursively([4, 6, 1, 3, 2, 5], 5));
  console.log();
}

testInsertionSortArrayRecursively();

function bubbleSortList(list) {
  let current = list.head;
  while (current !== null) {
    let next = current.next;

    while (next !== null) {
      if (current.data > next.data) {
        const temp = current.data;
        current.data = next.data;
        next.data = temp;
      }
      next = next.next;
    }
    current = current.next;
  }
}

function testBubbleSortList() {
  console.log("Bubble Sort Singly Linked List sequentially");
  const sll = {
    head: new SinglyListNode(
      4,
      new SinglyListNode(
        2,
        new SinglyListNode(
          6,
          new SinglyListNode(
            1,
            new SinglyListNode(3, new SinglyListNode(5, null))
          )
        )
      )
    )
  };
  bubbleSortList(sll);
  showList(sll);
  console.log();
}

testBubbleSortList();

function selectionSortList(list) {
  let current = list.head;
  while (current !== null) {
    let min = current;
    let next = current.next;

    while (next !== null) {
      if (min.data > next.data) min = next;
      next = next.next;
    }

    const x = current.data;
    current.data = min.data;
    min.data = x;
    current = current.next;
  }
}

function testSelectionSortList() {
  console.log("Selection Sort Singly Linked List sequentially");
  const sll = {
    head: new SinglyListNode(
      4,
      new SinglyListNode(
        2,
        new SinglyListNode(
          6,
          new SinglyListNode(
            1,
            new SinglyListNode(3, new SinglyListNode(5, null))
          )
        )
      )
    )
  };
  selectionSortList(sll);
  showList(sll);
  console.log();
}

testSelectionSortList();

function insertionSortList(list) {
  let node = list.head.next;
  while (node !== null) {
    const last_value = node.data;
    let prev_node = node.prev;
    while (prev_node !== null && last_value < prev_node.data) {
      prev_node.next.data = prev_node.data;
      prev_node = prev_node.prev;
    }
    if (prev_node !== null) prev_node.next.data = last_value;
    else list.head.data = last_value;
    node = node.next;
  }
  return list;
}

function testInsertionSortList() {
  console.log("Insertion Sort Doubly Linked List Sequentially");
  const node_1 = new DoublyListNode(5),
    node_2 = new DoublyListNode(2),
    node_3 = new DoublyListNode(4),
    node_4 = new DoublyListNode(1);

  node_1.next = node_2;
  node_1.prev = null;
  node_2.next = node_3;
  node_2.prev = node_1;
  node_3.prev = node_2;
  node_3.next = node_4;
  node_4.next = null;
  node_4.prev = node_3;

  const dll = {
    head: node_1
  };

  insertionSortList(dll);
  showList(dll);
  console.log();
}

testInsertionSortList();

function binarySearchArrayRecursively(array, start, end, key) {
  if (start > end) return false;
  else {
    const mid = array[((start + end) / 2) >> 0];
    if (array[mid] === key) return true;
    else if (key > array[mid])
      return binarySearchArrayRecursively(array, mid + start, end, key);
    else return binarySearchArrayRecursively(array, start, mid - start, key);
  }
}

function testBinarySearchArrayRecursively() {
  console.log("Binary Search Array Recursively");
  console.log(
    "Item found",
    binarySearchArrayRecursively([4, 6, 1, 3, 2, 5], 0, 5, 2)
  );
  console.log(
    "Item not found",
    binarySearchArrayRecursively([4, 6, 1, 3, 2, 5], 0, 5, 9)
  );
  console.log();
}

testBinarySearchArrayRecursively();

function fibonacciRecursiveWithMemoization(num, cache = {}) {
  if (num === 0) return 0;
  else if (num === 1) return 1;
  else if (cache[num]) return cache[num];
  const output =
    fibonacciRecursiveWithMemoization(num - 1, cache) +
    fibonacciRecursiveWithMemoization(num - 2, cache);
  cache[num] = output;
  return output;
}

function testFibonacciRecursiveWithMemoization() {
  console.log("Recursive Fibonacci with memoization");
  console.log("1", fibonacciRecursiveWithMemoization(1));
  console.log("10", fibonacciRecursiveWithMemoization(10));
  console.log("40", fibonacciRecursiveWithMemoization(40));
  console.log();
}

testFibonacciRecursiveWithMemoization();
