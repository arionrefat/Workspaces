package com.teamToyoda;

public class Car {
    private int doors;
    private int wheels;
    private String model;
    private String engine;
    private String color;

    public void setModel(String model){    //set_ and get_ are known as setters and getters in java
        this.model = model;
    }
    public String getModel(){
        return this.model;
    }
}
