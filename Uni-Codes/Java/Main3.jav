//Disclaimer:

//Run this file in terminal by renaming the file into Main.java and
//running Following the command in terminal
// ``java Main.java``

public class Main {
    public static void main(String args[]) {
        int[] array = { 3, 1, 5, 9, 10, 68 };
        MyListo list = new MyListo(array);
        RecursiveSelection selectionsort = new RecursiveSelection();
        selectionsort.selectionListSort(list, 0);
        selectionsort.selectionSort(array, 0);
        selectionsort.print(array);
        // System.out.println();

        DublyListo list0 = new DublyListo(array);
        RecursiveInsertion insertionsort = new RecursiveInsertion();
        insertionsort.insertionDubListSort(list0, list0.size());
        insertionsort.insertionSort(array, array.length);
        insertionsort.print(array);
        list.showList();
        list0.showList();

        RecursiveBubble bubblesort = new RecursiveBubble();
        bubblesort.bubbleSort(list, list.size());

        RecursiveBinary binarysearch = new RecursiveBinary();
        System.out.println(binarysearch.binarySort(array, 0, array.length, 3));

        fibonacciMemoization fibM = new fibonacciMemoization();
        System.out.println(fibM.fibMemoi(7));
    }
}

class RecursiveSelection {
    void selectionSort(int[] array, int start) {
        int size = array.length - 1;

        if (start > size)
            return;

        int min = start;

        for (int i = start + 1; i <= size; i++) {
            if (array[i] < array[min])
                min = i;
        }

        int temp = array[start];
        array[start] = array[min];
        array[min] = temp;

        selectionSort(array, start + 1);
    }

    void selectionListSort(MyListo list, int start) {
        int size = list.size() - 1;

        if (start > size)
            return;

        int min = start;

        for (int i = start + 1; i <= size; i++)
            if (list.nodeAt(i).element < list.nodeAt(min).element)
                min = i;

        int temp = list.nodeAt(start).element;
        list.insert(list.nodeAt(min).element, start);
        list.insert(temp, min);

        selectionListSort(list, start + 1);
    }

    void print(int[] array) {
        for (Integer val : array)
            System.out.println(val);
    }
}

class RecursiveInsertion {
    void insertionSort(int[] array, int size) {
        if (size <= 1)
            return;

        insertionSort(array, size - 1);

        int number = array[size - 1];
        int index = size - 2;

        while (index >= 0 && array[index] > number) {
            array[index + 1] = array[index];
            index--;
        }

        array[index + 1] = number;
    }

    void insertionDubListSort(DublyListo array, int size) {
        if (size <= 1)
            return;

        insertionDubListSort(array, size - 1);

        int number = (int) array.nodeAt(size - 1).element;
        int i = size - 2;

        while (i >= 0 && (int) array.nodeAt(i).element > number) {
            array.insert((int) array.nodeAt(i).element, i + 1);
            i--;
        }

        array.insert(number, i + 1);
    }

    void print(int[] array) {
        for (Integer val : array)
            System.out.println(val);
    }
}

class RecursiveBubble {
    void bubbleSort(MyListo list, int size) {
        if (size == 1)
            return;

        for (int i = 0; i < size - 1; i++) {
            if (list.nodeAt(i).element > list.nodeAt(i + 1).element) {
                int temp = list.nodeAt(i).element;
                list.insert(list.nodeAt(i + 1).element, i);
                list.insert(temp, i + 1);
            }
        }
        bubbleSort(list, size - 1);
    }
}

class fibonacciMemoization {
    int array[];

    fibonacciMemoization() {
        array = new int[10001];
    }

    fibonacciMemoization(int n) {
        array = new int[n + 1];
    }

    // starts from 0

    // int fibMemoi(int number) {
    // if (array[number] > 0)
    // return array[number];
    // if (number == 1 || number == 2)
    // return array[number] = 1;
    // else if (number == 0)
    // return array[number] = 0;
    // else
    // return array[number] = fibMemoi(number - 1) + fibMemoi(number - 2);
    // }

    // Starts from 1

    int fibMemoi(int number) {
        if (array[number] > 0)
            return array[number];
        if (number == 0 || number == 1)
            return array[number] = 1;
        else
            return array[number] = fibMemoi(number - 1) + fibMemoi(number - 2);
    }
}

class RecursiveBinary {
    int binarySort(int[] array, int i, int size, int target) {

        if (size >= i && i < array.length - 1) {

            int middleTerm = i + (size - i) / 2;

            if (array[middleTerm] == target)
                return middleTerm;

        }
    }
}
