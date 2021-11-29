package java;

class MyThread extends Thread {
    public MyThread(String name){
        super(name);
    }
    @Override
    public void run(){
        System.out.println("hello world");
        System.out.println(Thread.currentThread().getName());
    }
}
class MyThreadfromRunnable implements Runnable {
    @Override
    public void run(){
        System.out.println("hello world");
        System.out.println(Thread.currentThread().getName());
    }
}
public class TheadTest{
    public static void main(String[] args) {
        MyThread myThread = new MyThread("myThread-1");
        myThread.start(); //runable state
        Thread MyTheadfromRunnable = new Thread(new MyThreadfromRunnable(), "myThread-2");
        MyTheadfromRunnable.start();
    }
}
