class TesterClass {

    Assignment1 task = new Assignment1();
    task.task1(3 , 2);
}

class Assignment1 {

    int task1(int base, int n) {
        if (n == 0)
            return 1;
        else
            return task1(base, n - 1);
    }
}
