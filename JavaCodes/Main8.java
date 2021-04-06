package com.teamToyoda;

public class Main8 {
    public static void main(String[] args) {
        boolean t = false;

        first:{
            second: {
                third:{
                    System.out.println("This line1 should execute!");
                    if (t) break second;
                    System.out.println("This line should not execute!");
                }
                System.out.println("This should not execute!");
            }
            System.out.println("This line3 should execute");
        }
    }
}
