import java.util.*;

class Process {
    String pid;
    int arrivalTime, burstTime, remainingTime;
    int completionTime, turnaroundTime, waitingTime;
    boolean isCompleted = false;

    Process(String pid, int at, int bt) {
        this.pid = pid;
        this.arrivalTime = at;
        this.burstTime = bt;
        this.remainingTime = bt;
    }
}

public class SJF_Preemptive {
    public static void main(String[] args) {
        // Given input
        Process[] processes = {
            new Process("P1", 10, 2),
            new Process("P2", 0, 10),
            new Process("P3", 8, 4),
            new Process("P4", 5, 5)
        };

        int n = processes.length;
        int completed = 0, currentTime = 0, prev = -1;
        double totalTAT = 0, totalWT = 0;
        List<String> gantt = new ArrayList<>();

        // Sort by arrival time
        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        while (completed < n) {
            int idx = -1;
            int minRT = Integer.MAX_VALUE;

            // Find process with smallest remaining time among arrived ones
            for (int i = 0; i < n; i++) {
                if (processes[i].arrivalTime <= currentTime && !processes[i].isCompleted) {
                    if (processes[i].remainingTime < minRT) {
                        minRT = processes[i].remainingTime;
                        idx = i;
                    }
                }
            }

            if (idx != -1) {
                Process p = processes[idx];

                // If CPU switches to a new process, log it in Gantt chart
                if (prev != idx) gantt.add(p.pid);

                // Execute for 1 unit of time
                p.remainingTime--;
                currentTime++;
                prev = idx;

                // If completed
                if (p.remainingTime == 0) {
                    p.isCompleted = true;
                    p.completionTime = currentTime;
                    p.turnaroundTime = p.completionTime - p.arrivalTime;
                    p.waitingTime = p.turnaroundTime - p.burstTime;
                    completed++;

                    totalTAT += p.turnaroundTime;
                    totalWT += p.waitingTime;
                }
            } else {
                gantt.add("Idle");
                currentTime++;
            }
        }

        // Display process info
        System.out.println("SJF (Preemptive / SRTF) Scheduling\n");
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
