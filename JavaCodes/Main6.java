package com.teamToyoda;
import java.util.*;

public class Main6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter your year of birth: ");

        boolean hasnextint = input.hasNextInt(); //returns a bool if the number is not a integer

        if(hasnextint) {
            int BD_date = input.nextInt();
            input.nextLine(); //if you don't want to use this you put name after the date just like C++

            System.out.println("Enter your name: ");
            String name = input.nextLine();

            int age = 2020 - BD_date;

            if (age >= 0 && age <= 100)
                System.out.println("Your name is: " + name + " and you are " + age + " years old");
            else
                System.out.println("Invalid year of birth");
        }
        else System.out.println("unable to parse year of birth ");
        // input.nextLine(); // handles end of line (enter Key)

        input.close();
    }
}
