package com.teamToyoda;

public class Main3 {
    public static void main(String[] args) {
        int number = 4;
        int finishNumber = 20;
        int count = 0;
        while (number <= finishNumber){
            number ++;
            /*
            when number is passed in isEvenNumber then only
            even number is printed and others get skipped
            because of "Continue"
             */
            if (!isEvenNumber(number)) {
                continue;
            }
            count++;
            System.out.println("Even numbers :" + number);
            if(count >= 5) break;
        }
    }

    public static boolean isEvenNumber(int number) {
        return number % 2 == 0;
    }
}
