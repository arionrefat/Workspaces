package com.teamToyoda;

import java.util.*;

public class Main7{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;

        while(true){
            System.out.println("Enter a number ");
            boolean isAnInt = input.hasNextInt();

            if(isAnInt){
                int number = input.nextInt();
                if (number  > max ) max = number;
                if (number < min) min = number;
            }
            else break;
        }
    }

}
