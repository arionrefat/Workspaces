package com.cse220;

//Lab3 is tester class
public class Lab3 {
    public static void main(String[] args) {
        int [] arr = {10,20,30,40,50};
        DublyList dublist = new DublyList(arr);

        // =====================================//
        dublist.showList();
//        dublist.insert(new Node1(68,null,null));
        System.out.println();
        dublist.insert(69,1);
        System.out.println();
        dublist.showList();
        dublist.remove(2);
        System.out.println();
//        dublist.remove(9);
        System.out.println(dublist.removeKey(50));
        System.out.println();
        dublist.showList();
        System.out.println();
        dublist.printSum();
    }
}

class DublyList{

    Node1 head = new Node1(null,null,null);

    public DublyList(int []a){
        head.next=head.prev=head;
        Node1 tail = head;

        for (int i = 0; i < a.length; i++){
            Node1 newNode = new Node1(a[i],null,null);
            newNode.prev = tail;
            newNode.next = tail.next;
            tail.next = newNode;
            newNode.next.prev = newNode;
            tail = newNode;
        }
    }

    void showList(){
        if (head.next == null) System.out.println("Empty List");
        else {
            for (Node1 n1 = head.next; n1 != head; n1 = n1.next) {
                System.out.println(n1.element);
            }
        }
    }
    void printSum(){
        int sums = 0;

        for(Node1 n = head.next; n!= head; n = n.next)
            sums += (int)n.element;

        System.out.println(sums);
    }
    int size(){
        int count = 0;

        for (Node1 n = head.next; n != head; n = n.next) count++;

        return count;
    }

    Node1 nodeAt(int index){
        Node1 n = head.next;

        for (int i = 0; i< index; i++)  n = n.next;

        return n;
    }

    void insert(Node1 newElement){

        boolean flag = true;

        for (Node1 n1 = head.next; n1 != head; n1 = n1.next) {
            if (n1.element == newElement.element) {
                flag = false;
                break;
            }
        }

        if(!flag)
            System.out.println("Element already exists");
        else {
                Node1 temp = nodeAt(size() - 1);
                Node1 q = temp.next;
                newElement.next = q;
                newElement.prev = temp;
                temp.next = newElement;
                q.prev = newElement;
        }
    }

    void insert(int newElement, int index){
        Node1 n = new Node1(newElement,null,null);

        boolean flag = true;

        for (Node1 n1 = head.next; n1 != head; n1 = n1.next) {
            if (n1.element == n.element) {
                flag = false;
                break;
            }
        }
        if(!flag)
            System.out.println("Element already exists");
        else {
            if (index >= size()) System.out.println("Out of range");
            else{
                Node1 temp = nodeAt(index - 1);
                Node1 q = temp.next;
                n.next = q;
                n.prev = temp;
                temp.next = n;
                q.prev = n;
            }
        }
    }
    void remove(int index){

        if (index >= size()) System.out.println("Out of range");
        else{
            Node1 temp = nodeAt(index);
            Node1 p = temp.prev;
            Node1 q = temp.next;

            p.next = q;
            q.prev = p;

        }
    }
    int removeKey(int deleteKey){
        Node1 n = head.next;
        int index = 0;

        for (int i = 0; i < size(); i++){
            if ((int)n.element == deleteKey) break;
            else{
                n = n.next;
                index++;
            }
        }
        int removedVal = (int)nodeAt(index).element;
        Node1 temp = nodeAt(index);
        Node1 p = temp.prev;
        Node1 q = temp.next;

        p.next = q;
        q.prev = p;

        return removedVal;
    }
}
class Node1{
    public Object element;
    public Node1 prev;
    public Node1 next;

    public Node1(Object e, Node1 n, Node1 p){
        element = e;
        next = n;
        prev =  p;
    }
}
