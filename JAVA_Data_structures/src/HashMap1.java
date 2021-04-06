import java.util.*;

public class HashMap1 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);

/*
automatic shorted hoye jai that is lexicographically
same as MAP or python's dictionary
same key hole value update hoye jabe
 */
        HashMap <String, String> map = new HashMap<>();
        map.put("STL1", "MAP");
        map.put("STL2", "SET");

//      have same size method that is .size()
//      Also if we want to know the keys we can use
        System.out.println(map.keySet());
        System.out.println(map.containsKey("STL1"));
        System.out.println(map.containsValue("SET"));
        System.out.println("-----------------------");
        for (String i: map.keySet()) {
            System.out.println(map.get(i));
        }


       input.close();
    }
}
