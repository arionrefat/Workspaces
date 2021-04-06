package com.timbuchalka;

public class Main {

  public static void main(String[] args) {
    Car porsche = new Car();
    Car holden_rip = new Car();
    porsche.setModel("911_Targa");
    System.out.println("Model is " + porsche.getModel());
  }
}
