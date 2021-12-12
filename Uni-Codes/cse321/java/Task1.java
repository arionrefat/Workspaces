import java.util.Scanner;

class Calcu extends Thread {
  int num1, num2;
  String calculation;

  public Calcu(int num, int num0, String calcs) {
    num1 = num;
    num2 = num0;
    calculation = calcs;
  }

  public int add(int number1, int number2) { return number1 + number2; }
  public int sub(int number1, int number2) { return number1 - number2; }
  public int mul(int number1, int number2) { return number1 * number2; }
  public int div(int number1, int number2) { return number1 / number2; }

  @Override
  public void run() {
    if (calculation.equals("add"))
      System.out.println(add(num1, num2));
    else if (calculation.equals("sub"))
      System.out.println(sub(num1, num2));
    else if (calculation.equals("div"))
      System.out.println(div(num1, num2));
    else if (calculation.equals("mul"))
      System.out.println(mul(num1, num2));
    else
      System.out.println("No Valid operation");
  }
}
public class Task1 {
  public static void main(String[] args) throws InterruptedException {
    Scanner input = new Scanner(System.in);
    int num1 = input.nextInt();
    int num2 = input.nextInt();
    Calcu Thread1 = new Calcu(num1, num2, "add");
    Calcu Thread2 = new Calcu(num1, num2, "sub");
    Calcu Thread3 = new Calcu(num1, num2, "mul");
    Calcu Thread4 = new Calcu(num1, num2, "div");
    Calcu Thread5 = new Calcu(num1, num2, "oth");
    Thread1.start();
    Thread2.start();
    Thread3.start();
    Thread4.start();
    Thread5.start();

    Thread1.join();
    Thread2.join();
    Thread3.join();
    Thread4.join();
    Thread5.join();

    input.close();
  }
}
