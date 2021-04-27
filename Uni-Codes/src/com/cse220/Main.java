public class Main {
    public static void main(String args[]) {
        int[] array = { 1, 4, 2, 1, 2, 29, 9, 5, 11, 1, 5, 61 };
        MyListo list = new MyListo(array);
        RecursiveSelection selectionsort = new RecursiveSelection();
        selectionsort.selectionListSort(list, 0);
        // selectionsort.selectionSort(array, 0);
        // selectionsort.print(array);
        // System.out.println();
        // RecursiveInsertion insertionsort = new RecursiveInsertion();
        // insertionsort.insertionSort(array, array.length);
        // insertionsort.print(array);
        // list.showList();
        // RecursiveBubble bubblesort = new RecursiveBubble();
        // bubblesort.bubbleSort(list, list.size());
        // list.size();
        // System.out.println();
        // list.insert(69, 9);
        list.showList();
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

class Node0 {
    int element;
    Node0 next;

    public Node0(int e, Node0 n) {
        element = e;
        next = n;
    }
}

class MyListo {
    Node0 head;
    Node0 tail = null;

    MyListo(int[] a) {

        for (int j : a) {
            Node0 newNode0 = new Node0(j, null);

            if (head == null) {
                head = newNode0;
            } else {
                tail.next = newNode0;
            }
            tail = newNode0;
        }
    }

    void showList() {
        Node0 n = head;
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
        Node0 n = head;

        while (n != null) {
            count = count + 1;
            n = n.next;
        }
        return count;
    }

    Node0 nodeAt(int index) {
        Node0 n = head;

        for (int i = 0; i < index; i++)
            n = n.next;

        return n;
    }

    void insert(Node0 newElement) {
        Node0 n = head;
        boolean flag = true;

        while (n != null) {
            if (n.element == newElement.element) {
                flag = false;
                break;
            }
            n = n.next;
        }

        if (!flag)
            System.out.println("Element already exists");
        else {
            n = head;

            while (n.next != null) {
                n = n.next;
            }
            n.next = newElement;
        }
    }

    void insert(int newElement, int index) {

        if (index < 0 || index > size())
            System.out.println("Invalid Index");

        Node0 n = head;
        boolean flag = true;

        while (n != null) {
            if (head.element == newElement) {
                flag = false;
                break;
            }
            n = n.next;
        }
        if (flag) {
            Node0 newNode = new Node0(newElement, null);
            Node0 pred = nodeAt(index - 1);
            Node0 nextOne = nodeAt(index + 1);

            if (index == 0) {
                newNode.next = head.next;
                head = newNode;
            } else {
                pred.next = newNode;
                newNode.next = nextOne;
            }
        }
    }
}

class DublyListo {

    Node01 head = new Node01(null, null, null);

    public DublyListo(int[] a) {
        head.next = head.prev = head;
        Node01 tail = head;

        for (int i = 0; i < a.length; i++) {
            Node01 newNode = new Node01(a[i], null, null);
            newNode.prev = tail;
            newNode.next = tail.next;
            tail.next = newNode;
            newNode.next.prev = newNode;
            tail = newNode;
        }
    }

    void showList() {
        if (head.next == null)
            System.out.println("Empty List");
        else {
            for (Node01 n1 = head.next; n1 != head; n1 = n1.next) {
                System.out.println(n1.element);
            }
        }
    }

    int size() {
        int count = 0;

        for (Node01 n = head.next; n != head; n = n.next)
            count++;

        return count;
    }

    Node01 nodeAt(int index) {
        Node01 n = head.next;

        for (int i = 0; i < index; i++)
            n = n.next;

        return n;
    }

    void insert(int newElement, int index) {
        Node01 n = new Node01(newElement, null, null);

        boolean flag = true;

        for (Node01 n1 = head.next; n1 != head; n1 = n1.next) {
            if (n1.element == n.element) {
                flag = false;
                break;
            }
        }
        if (flag) {
            Node01 temp = nodeAt(index - 1);
            Node01 q = temp.next;
            n.next = q;
            n.prev = temp;
            temp.next = n;
            q.prev = n;
        }
    }
}

class Node01 {
    public Object element;
    public Node01 prev;
    public Node01 next;

    public Node01(Object e, Node01 n, Node01 p) {
        element = e;
        next = n;
        prev = p;
    }
}