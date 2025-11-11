import java.util.*;

class Process {
    String pid;
    int arrivalTime, burstTime;
    int completionTime, turnaroundTime, waitingTime;

    Process(String pid, int at, int bt) {
        this.pid = pid;
        this.arrivalTime = at;
        this.burstTime = bt;
    }
}

public class FCFS_Scheduling {
    public static void main(String[] args) {
        // Given input
        Process[] processes = {
            new Process("P1", 10, 2),
            new Process("P2", 0, 10),
            new Process("P3", 8, 4),
            new Process("P4", 5, 5)
        };

        int n = processes.length;

        // Sort by Arrival Time
        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        int currentTime = 0;
        double totalTAT = 0, totalWT = 0;

        System.out.println("FCFS CPU Scheduling Algorithm\n");
        System.out.println("Process\tAT\tBT\tCT\tTAT\tWT");

        for (Process p : processes) {
            if (currentTime < p.arrivalTime)
                currentTime = p.arrivalTime; // CPU idle till process arrives

            p.completionTime = currentTime + p.burstTime;
            p.turnaroundTime = p.completionTime - p.arrivalTime;
            p.waitingTime = p.turnaroundTime - p.burstTime;

            currentTime = p.completionTime;

            totalTAT += p.turnaroundTime;
            totalWT += p.waitingTime;

            System.out.println(p.pid + "\t" + p.arrivalTime + "\t" + p.burstTime + "\t" +
                               p.completionTime + "\t" + p.turnaroundTime + "\t" + p.waitingTime);
        }

        System.out.printf("\nAverage Turnaround Time: %.2f", totalTAT / n);
        System.out.printf("\nAverage Waiting Time: %.2f\n", totalWT / n);

        // Gantt Chart
        System.out.println("\nGantt Chart:");
        for (Process p : processes) {
            System.out.print("| " + p.pid + " ");
        }
        System.out.println("|");
    }
}
