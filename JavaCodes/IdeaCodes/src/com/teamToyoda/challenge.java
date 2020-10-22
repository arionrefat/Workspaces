package com.teamToyoda;

public class challenge {
    public static void main(String[] args) {
        char code = 'G';
        switch (code) {
            case 'A':
            case 'B':
            case 'C':
            case 'D':
            case 'E':
                System.out.println(code + " is found");
                break;
            default:
                System.out.println("nothing is found");
                break;
        }
        String month = "ulabreta";
        switch (month.toLowerCase()){
            case "january":
            case "february":
            case "march":
            case "april":
                System.out.println("It is " + month);
                break;
            default:
                System.out.println("wow " + month +" exits");
                break;
        }

    }
}
