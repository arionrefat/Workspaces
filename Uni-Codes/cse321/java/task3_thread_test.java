class Fibo extends Thread {
    int n1, n2;
    String action;
    public static long totalSum = 0;

    public Fibo(int number1, int number2, String act) {
        n1 = number1;
        n2 = number2;
        action = act;
    }

    @Override
    public void run() {

        long fibonacci[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
                10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
                5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
                701408733, 1134903170, 1836311903, 2971215073L, 4807526976L, 7778742049L
        };

        if (action.equals("th1")) {
            long sum = 0;
            int count = 0;
            for (int i = n1; i <= n2; i++) {
                if (fibonacci[i] % 2 == 1) {
                    sum += fibonacci[i];
                    count += 1;
                }
            }
            long mean = sum / count;
            totalSum += mean;
            System.out.println(mean);
        } else if (action.equals("th2")) {
            long sum = 0;
            int count = 0;
            for (int i = n1; i <= n2; i++) {
                if (fibonacci[i] % 2 == 0) {
                    sum += fibonacci[i];
                    count += 1;
                }
            }
            long mean = sum / count;
            totalSum += mean;
            System.out.println(mean);
        } else if (action.equals("th3")) {
            long sum = 0;
            int count = 0;

            for (int i = n1; i <= n2; i++) {
                if (fibonacci[i] % 2 == 1) {
                    sum += fibonacci[i];
                    count += 1;
                }
            }
            long mean = sum / count;
            totalSum += mean;
            System.out.println(mean);
        } else if (action.equals("th4")) {
            long sum = 0;
            int count = 0;

            for (int i = n1; i <= n2; i++) {
                if (fibonacci[i] % 2 == 0) {
                    sum += fibonacci[i];
                    count += 1;
                }
            }
            long mean = sum / count;
            totalSum += mean;
            System.out.println(mean);
        } else if (action.equals("avg")) {
            long finalRes = totalSum / 4;
            System.out.println(finalRes);
        }
    }
}

public class task3_thread_test {
    public static void main(String[] args) {
        Fibo t1 = new Fibo(0, 24, "th1");
        Fibo t2 = new Fibo(0, 24, "th2");
        Fibo t3 = new Fibo(25, 49, "th3");
        Fibo t4 = new Fibo(25, 49, "th4");
        Fibo t5 = new Fibo(0, 0, "avg");

        t1.start();
        t2.start();
        t3.start();
        t4.start();

        try {
            t1.join();
            t2.join();
            t3.join();
            t4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t5.start();

        // For Thread 1 :3793
        // For Thread 4 :786634227
        // For Thread 3 :827753874
        // For Thread 2 :6744
        // The Final Result is : 403599659
    }
}
