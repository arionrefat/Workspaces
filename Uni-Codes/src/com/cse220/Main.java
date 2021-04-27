public class Main {
    public static void main(String args[]) {
        int[] array = { 1, 4, 2, 11, 17, 2, 1, 3, 9, 2 };
        RecursiveSelection selectionsort = new RecursiveSelection();
        selectionsort.selectionSort(array, 0);
        selectionsort.print(array);
        System.out.println();
        RecursiveInsertion insertionsort = new RecursiveInsertion();
        insertionsort.insertionSort(array, array.length);
        insertionsort.print(array);
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

    void print(int[] array) {
        for (Integer val : array)
            System.out.println(val);
    }
}

class RecursiveBubble {
    void bubbleSort(int my_arr[], int len_arr) {
        if (len_arr == 1)
            return;

        for (int i = 0; i < len_arr - 1; i++) {
            if (my_arr[i] > my_arr[i + 1]) {
                int temp = my_arr[i];
                my_arr[i] = my_arr[i + 1];
                my_arr[i + 1] = temp;
            }
        }
        bubbleSort(my_arr, len_arr - 1);
    }

    class Node {
        int element;
        Node next;

        public Node(int e, Node n) {
            element = e;
            next = n;
        }
    }

    class MyList {
        Node head;
        Node tail = null;

        MyList(int[] a) {

            for (int j : a) {
                Node newNode = new Node(j, null);

                if (head == null) {
                    head = newNode;
                } else {
                    tail.next = newNode;
                }
                tail = newNode;
            }
        }

        void showList() {
            Node n = head;
            if (n == null)
                System.out.println("Empty List");
            else {
                while (n != null) {
                    System.out.println(n.element);
                    n = n.next;
                }
            }
            System.out.println();
        }

        int size() {
            int count = 0;
            Node n = head;

            while (n != null) {
                count = count + 1;
                n = n.next;
            }
            return count;
        }
    }
}
