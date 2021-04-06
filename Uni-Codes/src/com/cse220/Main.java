package com.cse220;

public class Main {
    public static void main(String[] args) {
        String source = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14";
        ParenBalance pb = new ParenBalance();
        pb.parenthesisBalancing(source);
    }
}

class ParenBalance {
    ArrayStack stack = new ArrayStack();
    boolean flag = false;
    int index = 0;
    String openClose;

    public void parenthesisBalancing(String source) {
        for (int i = 0; i < source.length(); i++) {
            if (source.charAt(i) == '(' || source.charAt(i) == '{' || source.charAt(i) == '[')
                stack.push(source.charAt(i));
            else if (source.charAt(i) == ')' || source.charAt(i) == '}' || source.charAt(i) == ']') {
                if (stack.size == 0) {
                    stack.push(source.charAt(i));
                    break;
                } else {
                    if ((source.charAt(i) == ')' && stack.peek().equals('('))
                            || (source.charAt(i) == '}' && stack.peek().equals('{'))
                            || (source.charAt(i) == ']' && stack.peek().equals('[')))
                        stack.pop();
                }
            }
        }

        // index = (source.indexOf((char) stack.peek()) + 1);

        for (int i = 0; i < source.length(); i++) {
            if (source.charAt(i) == (char) stack.peek()) {
                index = i + 1;
                break;
            }
        }

        if (stack.size == 0)
            flag = true;
        else if (stack.peek().equals('(') || stack.peek().equals('{') || stack.peek().equals('['))
            openClose = "closed";
        else
            openClose = "opened";

        if (flag == true)
            System.out.println("The expression is correct");
        else
            System.out.println("The expression is NOT correct. \n" + "Error at character # " + index + ". " + "‘"
                    + stack.peek() + "‘- not " + openClose + ".");
    }
}

class ParenBalanceList {
    ListStack stack = new ListStack();
    boolean flag = false;
    int index = 0;
    String openClose;

    public void parenthesisBalancing(String source) {
        for (int i = 0; i < source.length(); i++) {
            if (source.charAt(i) == '(' || source.charAt(i) == '{' || source.charAt(i) == '[')
                stack.push(source.charAt(i));
            else if (source.charAt(i) == ')' || source.charAt(i) == '}' || source.charAt(i) == ']') {
                if (stack.size == 0) {
                    stack.push(source.charAt(i));
                    break;
                } else {
                    if ((source.charAt(i) == ')' && stack.peek().equals('('))
                            || (source.charAt(i) == '}' && stack.peek().equals('{'))
                            || (source.charAt(i) == ']' && stack.peek().equals('[')))
                        stack.pop();
                }
            }
        }

        // index = (source.indexOf((char) stack.peek()) + 1);

        for (int i = 0; i < source.length(); i++) {
            if (source.charAt(i) == (char) stack.peek()) {
                index = i + 1;
                break;
            }
        }

        if (stack.size == 0)
            flag = true;
        else if (stack.peek().equals('(') || stack.peek().equals('{') || stack.peek().equals('['))
            openClose = "closed";
        else
            openClose = "opened";

        if (flag == true)
            System.out.println("The expression is correct");
        else
            System.out.println("The expression is NOT correct. \n" + "Error at character # " + index + ". " + "‘"
                    + stack.peek() + "‘- not " + openClose + ".");
    }
}


    class ListStack implements Stack {
        Node head;

        public void push(Object e) {

            Node n = new Node(e, head);
            head = n;

        }

        public Object peek() {
            if (head == null)
                return null;

            return head.element;
        }

        public Object pop() {
            if (head == null)
                return null;

            Node remove = head;
            head = head.next;
            remove.next = null;
            return remove.element;
        }

        public void print() {
            for (Node n = head; n != head; n = n.next)
                System.out.println(n.element);
        }
    }


    class ArrayStack implements Stack {
        Object[] a;
        int size;

        public ArrayStack() {
            a = new Object[100];
            size = 0;
        }

        public void push(Object e) {
            if (size == a.length) {
                return;
            }
            a[size] = e;
            size++;
        }

        public Object peek() {
            if (size == 0) {
                return null;
            }
            return a[size - 1];
        }

        public Object pop() {
            if (size == 0) {
                return null;
            }
            Object val = a[size - 1];
            a[size - 1] = null;
            size--;
            return val;
        }

        public void print() {
            if (size == 0)
                return;
            else
                for (int i = 0; i < size; i++)
                    System.out.println(a[i]);
        }
}

class Node {
    Object element;
    Node next;

    Node(Object e, Node n) {
        element = e;
        next = n;
    }
}

interface Stack {
    void push(Object e);

    Object pop();

    Object peek();
}
