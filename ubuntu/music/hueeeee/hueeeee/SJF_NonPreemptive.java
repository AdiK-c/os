import java.util.*;

class Process {
    String pid;
    int arrivalTime, burstTime;
    int completionTime, turnaroundTime, waitingTime;
    boolean isCompleted = false;

    Process(String pid, int at, int bt) {
        this.pid = pid;
        this.arrivalTime = at;
        this.burstTime = bt;
    }
}

public class SJF_NonPreemptive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Given input
        Process[] processes = {
            new Process("P1", 10, 2),
            new Process("P2", 0, 10),
            new Process("P3", 8, 4),
            new Process("P4", 5, 5)
        };

        int n = processes.length;
        int currentTime = 0, completed = 0;
        double totalTAT = 0, totalWT = 0;

        List<String> gantt = new ArrayList<>();

        // Sort by arrival time first
        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        while (completed < n) {
            int idx = -1;
            int minBT = Integer.MAX_VALUE;

            // Find process with smallest burst time among arrived ones
            for (int i = 0; i < n; i++) {
                if (processes[i].arrivalTime <= currentTime && !processes[i].isCompleted) {
                    if (processes[i].burstTime < minBT) {
                        minBT = processes[i].burstTime;
                        idx = i;
                    }
                }
            }

            if (idx != -1) {
                Process p = processes[idx];
                gantt.add(p.pid);
                currentTime += p.burstTime;
                p.completionTime = currentTime;
                p.turnaroundTime = p.completionTime - p.arrivalTime;
                p.waitingTime = p.turnaroundTime - p.burstTime;
                p.isCompleted = true;
                completed++;

                totalTAT += p.turnaroundTime;
                totalWT += p.waitingTime;
            } else {
                gantt.add("Idle");
                currentTime++;
            }
        }

        // Display process info
        System.out.println("SJF (Non-Preemptive) Scheduling\n");
        System.out.println("Process\tAT\tBT\tCT\tTAT\tWT");
        for (Process p : processes) {
            System.out.println(p.pid + "\t" + p.arrivalTime + "\t" + p.burstTime + "\t" +
                               p.completionTime + "\t" + p.turnaroundTime + "\t" + p.waitingTime);
        }

        System.out.println("\nAverage Turnaround Time: " + (totalTAT / n));
        System.out.println("Average Waiting Time: " + (totalWT / n));

        // Gantt chart
        System.out.println("\nGantt Chart:");
        for (String pid : gantt)
            System.out.print(pid + " | ");
        System.out.println();
    }
}
