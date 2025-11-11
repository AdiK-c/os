import java.util.*;

class Process {
    String pid;
    int arrivalTime, burstTime, remainingTime, completionTime, turnaroundTime, waitingTime;

    public Process(String pid, int at, int bt) {
        this.pid = pid;
        this.arrivalTime = at;
        this.burstTime = bt;
        this.remainingTime = bt;
    }
}

public class RoundRobinScheduling {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int timeQuantum = 1;
        System.out.println("Round Robin CPU Scheduling (Time Quantum = " + timeQuantum + " sec)");

        // Given processes
        Process[] processes = {
            new Process("P1", 10, 2),
            new Process("P2", 0, 10),
            new Process("P3", 8, 4),
            new Process("P4", 5, 5)
        };

        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        Queue<Process> readyQueue = new LinkedList<>();
        int currentTime = 0;
        int completed = 0;
        double totalWT = 0, totalTAT = 0;
        List<String> gantt = new ArrayList<>();

        while (completed < processes.length) {
            // Add arrived processes to ready queue
            for (Process p : processes) {
                if (p.arrivalTime == currentTime)
                    readyQueue.add(p);
            }

            if (!readyQueue.isEmpty()) {
                Process current = readyQueue.poll();
                gantt.add(current.pid);
                current.remainingTime -= 1;
                currentTime++;

                // Add any process that arrived at this time
                for (Process p : processes) {
                    if (p.arrivalTime == currentTime)
                        readyQueue.add(p);
                }

                if (current.remainingTime > 0) {
                    readyQueue.add(current);
                } else {
                    completed++;
                    current.completionTime = currentTime;
                    current.turnaroundTime = current.completionTime - current.arrivalTime;
                    current.waitingTime = current.turnaroundTime - current.burstTime;
                    totalWT += current.waitingTime;
                    totalTAT += current.turnaroundTime;
                }
            } else {
                gantt.add("Idle");
                currentTime++;
            }
        }

        // Print process table
        System.out.println("\nProcess\tAT\tBT\tCT\tTAT\tWT");
        for (Process p : processes) {
            System.out.println(p.pid + "\t" + p.arrivalTime + "\t" + p.burstTime + "\t" +
                               p.completionTime + "\t" + p.turnaroundTime + "\t" + p.waitingTime);
        }

        System.out.println("\nAverage Turnaround Time: " + (totalTAT / processes.length));
        System.out.println("Average Waiting Time: " + (totalWT / processes.length));

        // Gantt Chart
        System.out.println("\nGantt Chart:");
        for (String pid : gantt)
            System.out.print(pid + " | ");
        System.out.println();
    }
}
