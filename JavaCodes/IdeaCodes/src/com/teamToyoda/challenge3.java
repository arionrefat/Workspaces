package com.teamToyoda;

import java.util.Scanner;

public class challenge3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int count = 1, sum = 0, number = 0;
        while(count <= 10) {
            System.out.println("Enter number #" + count);
            number = input.nextInt();
            boolean correctScanner = input.hasNextInt();
            if (correctScanner) {
                sum += number;
                count++;
            } else System.out.println("Invalid number");
        }

        input.close();
    }
}
