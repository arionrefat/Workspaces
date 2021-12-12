import java.util.*;

public class SJF {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("enter no of process:");

        int n = input.nextInt();
        int[] proc = new int[n];
        int[] arrival_time = new int[n];
        int[] brust_time = new int[n];
        int[] completion_time = new int[n];
        int[] turnaround_time = new int[n];
        int[] waiting_time = new int[n];
        int[] flags = new int[n];
        int start_time = 0, total = 0;
        float avg_waitingT = 0, avg_turnaroundT = 0;

        for (int i = 0; i < n; i++) {
            System.out.println("enter process " + (i + 1) + " arrival time:");
            arrival_time[i] = input.nextInt();
            System.out.println("enter process " + (i + 1) + " brust time:");
            brust_time[i] = input.nextInt();
            proc[i] = i + 1;
            flags[i] = 0;
        }

        while (true) {
            int c = n, min = 999;
            if (total == n) break;

            for (int i = 0; i < n; i++) {
                if ((arrival_time[i] <= start_time) && (flags[i] == 0) && (brust_time[i] < min)) {
                    min = brust_time[i];
                    c = i;
                }
            }
            if (c == n) start_time++;
            else {
                completion_time[c] = start_time + brust_time[c];
                start_time += brust_time[c];
                turnaround_time[c] = completion_time[c] - arrival_time[c];
                waiting_time[c] = turnaround_time[c] - brust_time[c];
                flags[c] = 1;
                total++;
            }
        }
        System.out.println("proc   arrival  brust   complete turn waiting");
        for (int i = 0; i < n; i++) {
            avg_waitingT += waiting_time[i];
            avg_turnaroundT += turnaround_time[i];
            System.out.println(proc[i] + "\t\t" + arrival_time[i] + "\t\t" + brust_time[i] + "\t\t" + completion_time[i] + "\t\t" + turnaround_time[i] + "\t\t" + waiting_time[i]);
        }
        System.out.println("\naverage tat is " + (float) (avg_turnaroundT / n));
        System.out.println("average waiting_time is " + (float) (avg_waitingT / n));
        input.close();
    }
}
