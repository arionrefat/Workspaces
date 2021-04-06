package com.cse220;

public class MyQueue {
    public static void main(String[] args) {

    }
}

//class ArrayQueue implements Queue{
//
//}
interface Queue{
    public void enqueue(Object e);
    public Object dequeue();
    public Object peek();
}