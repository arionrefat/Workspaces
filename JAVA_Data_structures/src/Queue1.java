import java.util.*;

public class Queue1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();

        q.add(2);
        q.add(3);
        q.add(7);
        q.add(8);
        q.add(1);
        q.add(101);

        System.out.println(q.peek());
        System.out.println("________________________");
        q.poll();
        System.out.println(q.peek());
        System.out.println(q.isEmpty());
        System.out.println("________________________");
        System.out.println(q.contains(8));
        System.out.println(q.contains(69));
        System.out.println("________________________");

        for (Integer i : q)
            System.out.println(i);
      
        System.out.println("hekl");
        input.close();
    }
}
