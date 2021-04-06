package com.teamToyoda;

public class Main2 {
    public static void main(String[] args) {

//        for (int i = 8 ; i >= 2; i--) {
//            System.out.println(String.format("%.2f",calculateInterest(10000,i)));
//        }
        System.out.println(isPrime(5));
        int count = 0;

        // i<= (long) Math.sqrt(n); more effcient
        for (int i = 10; i < 50; i++) {
            if(isPrime(i)){
                count++;
                System.out.println("Number is " +i);
                if(count==10){
                    System.out.println("Exiting the loop");
                    break;
                }
            }
        }
    }

    public static boolean isPrime(int n){
        if (n == 1) return false;
        for(int i = 2; i <= n/2; i++){
            if(n%i == 0) return false;
        }
        return true;
    }

    public static double calculateInterest(double amount, double interestRate){
        return (amount*(interestRate)/100);
    }
}