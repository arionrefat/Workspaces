package com.teamToyoda;

public class Main4 {
    public static void main(String[] args) {
        System.out.println("Sum of digits in sumDigits is: " +sumDigits(32123));
    }

    private static int sumDigits(int number){
        if(number < 10){
            return -1;
        }
        else {
            int sum = 0;
            while (number > 0) {
                sum += number%10;
                number = number/10;
            }
            return sum;
        }
    }
}
