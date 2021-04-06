import java.util.*;

public class Stack1 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        Stack <Integer> s = new Stack<>();
        s.push(6);
        s.push(9);
        s.push(3);
        s.push(6);

//        System.out.println(s.peek());
//        s.pop();
        System.out.println(s.search(6));
//        System.out.println(s.empty());
        System.out.println("-------------------");

        Iterator <Integer> it = s.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }
        System.out.println("-------------------");
        System.out.println(s.size());
        input.close();
    }
}
