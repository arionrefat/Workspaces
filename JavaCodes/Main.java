 package com.teamToyoda;

 public class Main {

     public static void main(String[] args) {
         int switchValue = 8;
         switch (switchValue){
             case 7:
                 System.out.println("Value was 1");
                 break;
             case 8:
                 System.out.println("Value was 2");
                 break;
             case 9:
                 System.out.println("Value was 3");
                 break;
             case 1: case 2: case 3:
                 System.out.println("value was either 3 2 1 ");
                 break;
             default:
                 System.out.println("was not following numbers");
                 break;
         }

     }
 }
