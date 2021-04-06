import java.util.*;

public class Hashset1 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        HashSet <String> set = new HashSet<>();

        set.add("hola");
        set.add("mundo");
        set.add("mundo");
        set.add("elgore");
        set.add("hola");

        System.out.println(set.size());
        set.remove("mundo");
        input.close();
    }
}
