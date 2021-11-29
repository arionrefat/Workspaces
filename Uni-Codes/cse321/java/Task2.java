import static java.lang.Thread.sleep;

class housesGOT implements Runnable {
    String houseName;
    public housesGOT(String name){
        houseName = name;
    }

    @Override
    public void run() {
        System.out.println("The House is: " + houseName);

        if (houseName.equals("House Stark") || houseName.equals("House Targaryen")) {
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else if (houseName.equals("House Lannister") || houseName.equals("House Bolton")) {
            try {
                sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else {
            try {
                sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
public class Task2{
    public static void main(String[] args) throws InterruptedException {
        Thread houseStark = new Thread(new housesGOT("House Stark"));
        Thread houseTargaryen = new Thread(new housesGOT("House Targaryen"));
        Thread houseBolton = new Thread(new housesGOT("House Bolton"));
        Thread houseLannister = new Thread(new housesGOT("House Lannister"));
        Thread houseTyrell = new Thread(new housesGOT("House Tyrell"));

        houseStark.setPriority(Thread.MAX_PRIORITY);
        houseBolton.setPriority(Thread.MIN_PRIORITY);

        houseStark.run();
        houseTargaryen.run();
        houseLannister.run();
        houseBolton.run();

        houseStark.start();
        houseTyrell.start();
        houseLannister.start();
        houseBolton.start();

        houseStark.join();
        houseTargaryen.join();
        houseLannister.join();
        houseBolton.join();
        houseTyrell.join();

        if (houseStark.isAlive()){
            System.out.println("Not Today!");
        }
        if (!houseBolton.isAlive()){
            System.out.println("You Know nothing!");
        }
    }
}
