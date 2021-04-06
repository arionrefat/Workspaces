import java.util.*;

class ArrayList1 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
//        int arr1[] = new int[10];
//        only use when needed as it uses more memory
//        And it is ame as Vector in CPP;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(10);
        arr.add(20);
        arr.add(30);
        arr.add(50);
        arr.add(69);

        arr.remove(2);

        System.out.println("------------------------------");

        for (Integer i : arr) {
            System.out.println(i);
        }

        System.out.println("------------------------------");
        System.out.println(arr.contains(50));
        System.out.println("------------------------------");

        arr.add(0, 56);
        for (Integer integer : arr) {
            System.out.println(integer);
        }

        input.close();
    }
}
