package com.cse220;

public class Main {
    public static void main(String args[]) {
        int[] array = { 1, 4, 2, 11, 17, 2, 1, 3, 9 };
        RecursiveSelection selectionsort = new RecursiveSelection();
        selectionsort.selectionSort(array, 0);
        selectionsort.print(array);
    }
}

class RecursiveSelection {
    void selectionSort(int[] array, int start) {
        int size = array.length - 1;

        if (start > size)
            return;

        int min = start;

        for (int i = start + 1; i < size; i++) {
            if (array[i] < array[min])
                min = i;
        }

        int temp = array[start];
        array[start] = array[min];
        array[min] = temp;
        selectionSort(array, start + 1);
    }

    void print(int[] array) {
        for (Integer val : array)
            System.out.println(val);
    }
}
