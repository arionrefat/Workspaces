package com.karina;

class Box{
    void volume(double width,double height, double depth){
        System.out.print("Volume is ");
        System.out.println(width*height*depth);
    }
}

class BoxClass{
    public static void main(String[] args) {
        Box box1 = new Box();
        Box box2 = new Box();
        //Here Box() is already the constructor if we want to add anything to the box class we add the following the Boxclass1

        box1.volume(10, 20 , 60);
        box2.volume(20, 5 ,6);
    }
}
