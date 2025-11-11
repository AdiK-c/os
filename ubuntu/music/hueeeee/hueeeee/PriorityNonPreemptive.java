import java.util.*;

class Process {
    String pid;
    int arrivalTime, burstTime, priority;
    int completionTime, turnaroundTime, waitingTime;
    boolean isCompleted = false;

    Process(String pid, int at, int bt, int pr) {
        this.pid = pid;
        this.arrivalTime = at;
        this.burstTime = bt;
        this.priority = pr;
    }
}

public class PriorityNonPreemptive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Given input
        Process[] processes = {
            new Process("P1", 10, 2, 3),
            new Process("P2", 0, 10, 1),
            new Process("P3", 8, 4, 4),
            new Process("P4", 5, 5, 2)
        };

        int n = processes.length;
        int currentTime = 0, completed = 0;
        double totalTAT = 0, totalWT = 0;

        List<String> gantt = new ArrayList<>();

        // Sort by arrival time
        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        while (completed < n) {
            // Find process with highest priority (lowest number)
            int idx = -1;
            int highestPriority = Integer.MAX_VALUE;

            for (int i = 0; i < n; i++) {
                if (processes[i].arrivalTime <= currentTime && !processes[i].isCompleted) {
                    if (processes[i].priority < highestPriority) {
                        highestPriority = processes[i].priority;
                        idx = i;
                    }
                    // If same priority → choose one with earlier arrival time
                    else if (processes[i].priority == highestPriority &&
                             processes[i].arrivalTime < processes[idx].arrivalTime) {
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

        // Display table
        System.out.println("Priority Scheduling (Non-Preemptive)\n");
        System.out.println("Process\tAT\tBT\tPR\tCT\tTAT\tWT");
        for (Process p : processes) {
            System.out.println(p.pid + "\t" + p.arrivalTime + "\t" + p.burstTime + "\t" +
                               p.priority + "\t" + p.completionTime + "\t" +
                               p.turnaroundTime + "\t" + p.waitingTime);
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
