import java.util.Scanner;

public class Priority {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of Process: ");
        int n = input.nextInt();
        int[] burstTime = new int[n];
        int[] priority = new int[n];
        int[] arrivalTime = new int[n];
        int[] processId = new int[n];
        int[] finishTime = new int[n];
        int[] waitingTime = new int[n];
        int[] turnAroundTime = new int[n];
        int temp, temp2 = 0;

        for (int i = 0; i < n; i++) {
            processId[i] = i+1;
            System.out.print("Enter the burst time   for Process - " + (i) + " : ");
            burstTime[i] = input.nextInt();
//            System.out.print("Enter the arrival time for Process - " + (i) + " : ");
//            arrivalTime[i] = input.nextInt();
            System.out.print("Enter the priority     for Process - " + (i) + " : ");
            priority[i] = input.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (priority[j] > priority[j + 1]) {
                    temp = burstTime[j];
                    burstTime[j] = burstTime[j + 1];
                    burstTime[j + 1] = temp;

                    temp = priority[j];
                    priority[j] = priority[j + 1];
                    priority[j + 1] = temp;

                    temp2 = processId[j];
                    processId[j] = processId[j + 1];
                    processId[j + 1] = temp2;
                }
            }
        }
        finishTime[0] = arrivalTime[0] + burstTime[0];
        turnAroundTime[0] = finishTime[0] - arrivalTime[0];
        waitingTime[0] = turnAroundTime[0] - burstTime[0];

        for (int i = 1; i < n; i++) {
            finishTime[i] = burstTime[i] + finishTime[i - 1];
            turnAroundTime[i] = finishTime[i] - arrivalTime[i];
            waitingTime[i] = turnAroundTime[i] - burstTime[i];
        }

        float sum = 0;
        for(int i=0;i<n;i++) sum+=waitingTime[i];
        float averageWaitingTime = sum / n;
        sum = 0;
        for(int i=0;i<n;i++) sum+=turnAroundTime[i];
        float averageTurnAroundTime = sum / n;

        System.out.println("ProcessId       " + "BurstTime      " + "Priority       " + "FinishTime         " + "WaitingTime        " + "TurnAroundTime     ");
        for (int i = 0; i < n; i++) System.out.println(processId[i] + "       "+ burstTime[i] + "         " + priority[i] + "       " + finishTime[i] + "       " +  waitingTime[i] + "         " + turnAroundTime[i]);
        System.out.println("Average Waiting Time:   " + averageWaitingTime + "   Average Turnaround Time :   " + averageTurnAroundTime);
    }
}