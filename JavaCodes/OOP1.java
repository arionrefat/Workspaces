class Box{

    double length;
    double width;
    double height;

    }

class OOP1{
    public static void main(String[] args) {
        Box mybox = new Box();
        double vol;

        mybox.length = 10;
        mybox.width = 20;
        mybox.height = 10;

        vol = mybox.length * mybox.width * mybox.height;

        System.out.println("The volume is "+ vol);

        }
    }
