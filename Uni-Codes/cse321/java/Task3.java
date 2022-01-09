class Fibo extends Thread {
    int n1, n2;
    String action;
    public static long sum;

    public Fibo(int number1, int number2, String act) {
        n1 = number1;
        n2 = number2;
        action = act;
    }

    public static long fib[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
            6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
            5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
            701408733, 1134903170, 1836311903, 2971215073L, 4807526976L, 7778742049L };

    @Override
    public void run() {
        if (action.equals("evM"))
            sum += evenMean(n1, n2);
        else if (action.equals("odM"))
            sum += oddMean(n1, n2);
        else if (action.equals("avg"))
            System.out.println("The average is : " + sum / 4);
        else
            System.out.println("Choose either evM, odM, avg");
    }

    public static long evenMean(int n1, int n2) {
        long evenSum = 0;
        int count = 0;
        for (int i = n1; i <= n2; i++) {
            if (fib[i] % 2 == 0) {
                evenSum += fib[i];
                count++;
            }
        }
        return (evenSum / count);
    }

    public static long oddMean(int n1, int n2) {
        long oddSum = 0;
        int count = 0;
        for (int i = n1; i <= n2; i++) {
            if (fib[i] % 2 != 0) {
                oddSum += fib[i];
                count++;
            }
        }
        return (oddSum / count);
    }
}

public class Task3 {
    public static void main(String[] args) throws InterruptedException {
        Fibo Thread1 = new Fibo(0, 24, "odM");
        Fibo Thread2 = new Fibo(0, 24, "evM");
        Fibo Thread3 = new Fibo(25, 49, "odM");
        Fibo Thread4 = new Fibo(25, 49, "evM");
        Fibo Thread5 = new Fibo(0, 0, "avg");

        Thread1.start();
        Thread2.start();
        Thread3.start();
        Thread4.start();
        Thread5.start();

        Thread1.join(); // waits one thead to complete
        Thread2.join();
        Thread3.join();
        Thread4.join();
        Thread5.join();
    }
}

// Wait for some time, it takes a little time and this is the output
// 403599659
