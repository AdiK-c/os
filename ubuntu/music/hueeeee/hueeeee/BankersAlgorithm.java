import java.util.Scanner;

public class BankersAlgorithm {
    private int need[][], allocate[][], max[][], avail[][], np, nr;

    private void input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of processes and resources: ");
        np = sc.nextInt(); // number of processes
        nr = sc.nextInt(); // number of resources

        need = new int[np][nr];
        max = new int[np][nr];
        allocate = new int[np][nr];
        avail = new int[1][nr];

        System.out.println("Enter allocation matrix:");
        for (int i = 0; i < np; i++) {
            for (int j = 0; j < nr; j++) {
                allocate[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter maximum matrix:");
        for (int i = 0; i < np; i++) {
            for (int j = 0; j < nr; j++) {
                max[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter available resources:");
        for (int j = 0; j < nr; j++) {
            avail[0][j] = sc.nextInt();
        }

        sc.close();
    }

    private int[][] calc_need() {
        for (int i = 0; i < np; i++) {
            for (int j = 0; j < nr; j++) {
                need[i][j] = max[i][j] - allocate[i][j]; // Need = Max - Allocated
            }
        }
        return need;
    }

    private boolean check(int i) {
        // check if all resources for process i can be allocated
        for (int j = 0; j < nr; j++) {
            if (avail[0][j] < need[i][j])
                return false;
        }
        return true;
    }

    public void isSafe() {
        input();
        calc_need();
        boolean done[] = new boolean[np];
        int j = 0;

        while (j < np) { // until all processes are allocated
            boolean allocated = false;
            for (int i = 0; i < np; i++) {
                if (!done[i] && check(i)) { // try to allocate
                    for (int k = 0; k < nr; k++) {
                        avail[0][k] = avail[0][k] + allocate[i][k];
                    }
                    System.out.println("Allocated process: " + i);
                    allocated = done[i] = true;
                    j++;
                }
            }
            if (!allocated)
                break; // if no allocation possible
        }

        if (j == np)
            System.out.println("\nSafely allocated — System is in safe state.");
        else
            System.out.println("\nAll processes can’t be allocated safely — System is in unsafe state.");
    }

    public static void main(String[] args) {
        new BankersAlgorithm().isSafe();
    }
}


/*
    Enter number of processes and resources: 3 4
    Enter allocation matrix:
    1 2 2 1
    1 0 3 3
    1 2 2 1
    Enter maximum matrix:
    3 3 2 2
    1 1 3 4
    1 3 5 0
    Enter available resources:
    3 1 1 2
    Allocated process: 0
    Allocated process: 1
    Allocated process: 2

    Safely allocated ? System is in safe state.
 */