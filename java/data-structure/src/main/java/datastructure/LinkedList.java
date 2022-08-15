package datastructure;

public class LinkedList {
    Node head; // Initializing head as Node type object

    public static class Node { // Constructor
        int data;
        Node next;

        public Node(int d) {
            data = d;
            next = null;
        }
    }

    public void printList() {
        Node n = head;

        while (n != null) {
            System.out.println(n.data + " ");
            n = n.next;
        }
    }

    public void push(int d) {
        Node newNode = new Node(d);

        newNode.next = head;
        head = newNode;
    }

    public void insertAfter(Node pre_node, int d) {
        Node newNode = new Node(d);
        if (pre_node == null) {
            System.out.println("Null value given");
        } else {
            newNode.next = pre_node.next;
            pre_node.next = newNode;
        }
    }

    public void insertBefore(Node next_node, int d) {
        Node newNode = new Node(d);
        if (next_node == null) {
            System.out.println("Null value given");
        } else {
            newNode.next = pre_node.next;
            pre_node.next = newNode;
        }
    }

    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        llist.head = new Node(10);
        Node second = new Node(20);
        Node third = new Node(30);
        llist.head.next = second;
        second.next = third;

        llist.push(5);
        llist.insertAfter(second, 15);
        llist.printList();
    }
}
