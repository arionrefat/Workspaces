package com.cse220;

class Node0 {
    Object element;
    Node next;

    Node0(Object e, Node n) {
        element = e;
        next = n;
    }
}

class Recursion {
    public int length(Node head) {
        if (head == null)
            return 0;
        else
            return 1 + length(head.next);
    }
}