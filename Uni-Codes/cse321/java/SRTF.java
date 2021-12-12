import java.util.Scanner;

public class SRTF {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("enter no of process:");
        int n = input.nextInt();
        int[] proc = new int[n];
        int[] arrival_time = new int[n];
        int[] burst_time = new int[n];
        int[] complete_time = new int[n];
        int[] turnaround_time = new int[n];
        int[] waiting_time = new int[n];
        int[] f = new int[n];
        int[] k = new int[n];
        int i, st = 0, total = 0;
        float avgwt = 0, avgta = 0;

        for (i = 0; i < n; i++) {
            proc[i] = i + 1;
            System.out.println("Process " + (i + 1) + " arrival time:");
            arrival_time[i] = input.nextInt();
            System.out.println("Process " + (i + 1) + " burst time:");
            burst_time[i] = input.nextInt();
            k[i] = burst_time[i];
            f[i] = 0;
        }

        while (true) {
            int c = n;
            int min = 999;
            if (total == n) break;

            for (i = 0; i < n; i++) {
                if ((arrival_time[i] <= st) && (f[i] == 0) && (burst_time[i] < min)) {
                    min = burst_time[i];
                    c = i;
                }
            }

            if (c == n) st++;
            else {
                burst_time[c]--;
                st++;
                if (burst_time[c] == 0) {
                    complete_time[c] = st;
                    f[c] = 1;
                    total++;
                }
            }
        }
        for (i = 0; i < n; i++) {
            turnaround_time[i] = complete_time[i] - arrival_time[i];
            waiting_time[i] = turnaround_time[i] - k[i];
            avgwt += waiting_time[i];
            avgta += turnaround_time[i];
        }

        System.out.println("proc  arrival  burst  complete turn waiting");
        for(i=0;i<n;i++) System.out.println(proc[i] +"\t"+ arrival_time[i]+"\t"+ k[i] +"\t"+ complete_time[i] +"\t"+ turnaround_time[i] +"\t"+ waiting_time[i]);
        System.out.println("Average Turnaround time is " + (float) (avgta / n));
        System.out.println("Average Waiting time is " + (float) (avgwt / n));
        input.close();
    }
}