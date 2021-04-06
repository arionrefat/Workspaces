package com.karina;
//this is the use of constructor
class Box1{
    double width;
    double height;
    double depth;

    Box1(){
        System.out.println("Constructing box");
        width = 10;
        height = 21;
        depth = 6;
    }
    double volume(){
        return width*height*depth;
    }

}
class Box2{
    double height;
    double breadth;
    double depth;
    // And this is called parameterized constructor
    Box2(double w, double h, double d){
        height = h;
        breadth = d;
        depth = w;
    }
    double volume(){
        return breadth*height*depth;
    }
}
class Boxclass1{
    public static void main(String[] args) {
        Box1 mybox1 = new Box1();
        Box1 mybox2 = new Box1();

        double vol;
        vol = mybox1.volume();
        System.out.println("Volume is " + vol);

        vol = mybox2.volume();
        System.out.println("Volume is " + vol);
    }
}
