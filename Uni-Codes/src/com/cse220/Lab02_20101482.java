package com.cse220;

class tester {
    public static void main(String[] args) {
        int[] a = { 10, 20, 30, 40, 50 };

        MyList list1 = new MyList(a);
        MyList list2 = new MyList(list1);
        list1.remove(10);
        list1.showList();
//        list1.insert(2,2);
        list1.insert(new Node(10,null));
        list1.rotate("left",2);
        list1.showList();
//        list1.clear();
//        list1.isEmpty();
        System.out.println(list1.findEle(10));
    }
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

    MyList() {
        head = null;
    }

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

    MyList(MyList a) {
        Node head2 = a.head;

        while (head2 != null) {
            Node newNode = new Node(head2.element, null);

            if (head == null)
                head = newNode;
            else
                tail.next = newNode;

            tail = newNode;
            head2 = head2.next;
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

    void isEmpty() {
        Node n = head;
        int count = 0;

        while (n != null) {
            count++;
            n = n.next;
        }
        if (count > 0) System.out.println(false);
        else System.out.println(true);
    }

    void clear() {
        head = null;
    }

    int size(){
        int count = 0;
        Node n = head;

        while (n != null){
            count = count + 1;
            n = n.next;
        }
        return count;
    }

    Node nodeAt(int index){
        Node n = head;

        for (int i = 0; i< index; i++)  n = n.next;

        return n;
    }

    void insert(Node newElement) {
        Node n = head;
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

            while (n.next != null){
                n = n.next;
            }
            n.next = newElement;
        }
    }


    void insert(int newElement, int index) {

        if (index < 0 || index > size())
            System.out.println("Invalid Index");

        Node n = head;
        boolean flag = true;

        while (n != null) {
            if (head.element == newElement) {
                flag = false;
                break;
            }
            n = n.next;
        }
        if (!flag)
            System.out.println("Element already exits");
        else {
            Node newNode = new Node(newElement, null);
            if (index == 0) {
                newNode.next = head;
                head = newNode;
            } else {
                Node pred = nodeAt(index - 1);
                newNode.next = pred.next;
                pred.next = newNode;
            }
        }
    }

    void remove(int deleteKey) {
        Node n = head;
        int index = 0;

        for (int i = 0; i < size(); i++) {
            if (n.element == deleteKey)
                break;
            else {
                n = n.next;
                index++;
            }
        }
        Node removedValue = nodeAt(index);
        Node removeNode = null;

        if (index == 0) {
            removeNode = head;
            head = head.next;
        } else {
            Node pred = nodeAt(index - 1);
            removeNode = pred.next;
            pred.next = removeNode.next;
        }

    }

    Node even(){
        Node n = head;
        Node nH = null;
        Node nT = null;
        Node temp = null;

        while (n != null){

            if (n.element %2 == 0){
                temp = new Node(n.element, null);

                if (nH == null){
                    nH = temp;
                }
                else{
                    nT.next = temp;
                }
                nT = temp;

                n = n.next;
            }
        }
        head = nH;

        return temp;
    }

    boolean findEle(int num){
        Node n = head;

        while(n != null){
            if (n.element == num) return true;
            n = n.next;
        }
        return false;
    }

    void reverse(){
        Node head_new = null, n = head, nextNode;

        while(n != null){
            nextNode = n.next;
            n.next = head_new;
            head_new = nextNode;
            n = nextNode;
        }
    }

    void printSum(){
        int sums = 0;
        Node n = head;

        while(n != null){
            sums += n.element;
            n = n.next;
        }
        System.out.println(sums);
    }

    void rotate(String instruction, int difference){
        Node oH = head;
        Node tail = null;
        if(instruction.equals("right")) difference = size() - difference;
        for (int i = 0; i <= difference; i++){
            oH = head;
            head = head.next;
            tail = head;
            while (tail.next != null) tail = tail.next;
            tail.next = oH;
            oH.next = null;
        }
    }

    void sorting(){
        int len = size();
        Node temp = null;
        Node n = head;
        int num = 0;

        while(n != null){
            temp = n;
            n = n.next;
        }

        for(int j = 0; j < len+1; j++){
            Node newHead = head;
            while(newHead != null){
                if (newHead != temp){
                    if (newHead.element > newHead.next.element){
                        num = newHead.element;
                        newHead.element = newHead.next.element;
                        newHead.next.element = num;
                    }
                    newHead= newHead.next;
                }
            }
        }
    }
}
