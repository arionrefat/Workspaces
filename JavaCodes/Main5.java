package com.teamToyoda;

public class Main5 {
    public static void main(String[] args) {
        String numberAsString = "2018.125"; //if we put 2018a
        System.out.println("numberAsString= "+numberAsString);

        double number = Double.parseDouble(numberAsString);//But this cannot convert 2018'a' but since it is not valid integer
        System.out.println("number is : " + number);


        numberAsString += 1;
        number += 1;

        System.out.println("numberAsString : " + numberAsString);
        System.out.println("number : " + number);
    }
}
