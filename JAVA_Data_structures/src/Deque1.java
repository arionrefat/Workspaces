import java.util.*;

public class Deque1 {
    public static void main(String[] args) {
        Deque<Integer> d = new LinkedList<>();
        d.offerFirst(4);
        d.offerFirst(5);
        d.offerLast(2);
        d.offerLast(9);
        System.out.println(d);

//        Iterator it = d.iterator();
//        while (it.hasNext()) System.out.println(it.next());

        for (Integer integer : d) System.out.println(integer);
        System.out.println("_______________________");
        d.pollFirst();
        System.out.println(d.peekFirst());
        d.pollLast();
        System.out.println(d.peekLast());
    }
}
