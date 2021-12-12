import java.util.Scanner;

class RoundRobin {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int quantumValue, sum = 0;

        System.out.println("Enter number of process:");
        int n = input.nextInt();
        int[] brusttime = new int[n];
        int[] waitingtime = new int[n];
        int[] turnaroundTime = new int[n];
        int[] proc = new int[n];

        System.out.println("Enter Brust Time:");

        for (int i = 0; i < n; i++) {
            System.out.println("Enter Brust Time for :" + (i + 1));
            brusttime[i] = input.nextInt();
        }

        System.out.println("Enter Time quantum: ");
        quantumValue = input.nextInt();

        for (int i = 0; i < n; i++) proc[i] = brusttime[i];
        for (int i = 0; i < n; i++) waitingtime[i] = 0;

        while (sum == 0){
            for (int i = 0; i < n; i++) {
                if (brusttime[i] > quantumValue) {
                    brusttime[i] -= quantumValue;
                    for (int j = 0; j < n; j++) if ((j != i) && (brusttime[j] != 0)) waitingtime[j] += quantumValue;
                } else {
                    for (int j = 0; j < n; j++) if ((j != i) && (brusttime[j] != 0)) waitingtime[j] += brusttime[i];
                    brusttime[i] = 0;
                }
            }
            for (int k = 0; k < n; k++)
                sum = sum + brusttime[k];
        }

        for (int i = 0; i < n; i++) turnaroundTime[i] = waitingtime[i] + proc[i];
        System.out.println("process\t\t BT\tWT\tTAT\tCT");
        for (int i = 0; i < n; i++) System.out.println("Process: " + (i + 1) + "\t" + proc[i] + "\t" + waitingtime[i] + "\t" + turnaroundTime[i] + "\t" + turnaroundTime[i]);

        float avg_wt = 0;
        float avg_turnaroundTime = 0;

        for (int j = 0; j < n; j++) avg_wt += waitingtime[j];
        for (int j = 0; j < n; j++) avg_turnaroundTime += turnaroundTime[j];

        System.out.println("average waiting time : " + (avg_wt / n) + "\n Average turn around time: " + (avg_turnaroundTime / n));
        input.close();
    }
}