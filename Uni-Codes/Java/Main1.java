class TesterClass {
    public static void main(String args[]) {
        Assignment1 task = new Assignment1();
        System.out.println(task.task1(3, 1));
    }
}

class Assignment1 {

    int task1(int base, int n) {
        if (n != 0)
            return task1(base, n - 1);
        else
            return 1;
    }
}
