import java.util.Scanner;

public class MemoryPlacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numBlocks, numProcesses;

        System.out.print("Enter number of memory blocks: ");
        numBlocks = sc.nextInt();
        int[] blockSize = new int[numBlocks];

        System.out.println("Enter sizes of memory blocks:");
        for (int i = 0; i < numBlocks; i++) {
            System.out.print("Block " + (i + 1) + ": ");
            blockSize[i] = sc.nextInt();
        }

        System.out.print("\nEnter number of processes: ");
        numProcesses = sc.nextInt();
        int[] processSize = new int[numProcesses];

        System.out.println("Enter sizes of processes:");
        for (int i = 0; i < numProcesses; i++) {
            System.out.print("Process " + (i + 1) + ": ");
            processSize[i] = sc.nextInt();
        }

        System.out.println("\n===== MEMORY ALLOCATION =====");
        System.out.println("1. Best Fit");
        System.out.println("2. Worst Fit");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                bestFit(blockSize.clone(), processSize);
                break;
            case 2:
                worstFit(blockSize.clone(), processSize);
                break;
            default:
                System.out.println("Invalid choice!");
        }

        sc.close();
    }

    // ---------------- BEST FIT ----------------
    static void bestFit(int[] blockSize, int[] processSize) {
        int[] allocation = new int[processSize.length];

        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;

        for (int i = 0; i < processSize.length; i++) {
            int bestIdx = -1;
            for (int j = 0; j < blockSize.length; j++) {
                if (blockSize[j] >= processSize[i]) {
                    if (bestIdx == -1 || blockSize[j] < blockSize[bestIdx])
                        bestIdx = j;
                }
            }

            if (bestIdx != -1) {
                allocation[i] = bestIdx;
                blockSize[bestIdx] -= processSize[i];
            }
        }

        System.out.println("\n--- Best Fit Allocation ---");
        displayResult(processSize, allocation);
    }

    // ---------------- WORST FIT ----------------
    static void worstFit(int[] blockSize, int[] processSize) {
        int[] allocation = new int[processSize.length];

        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;

        for (int i = 0; i < processSize.length; i++) {
            int worstIdx = -1;
            for (int j = 0; j < blockSize.length; j++) {
                if (blockSize[j] >= processSize[i]) {
                    if (worstIdx == -1 || blockSize[j] > blockSize[worstIdx])
                        worstIdx = j;
                }
            }

            if (worstIdx != -1) {
                allocation[i] = worstIdx;
                blockSize[worstIdx] -= processSize[i];
            }
        }

        System.out.println("\n--- Worst Fit Allocation ---");
        displayResult(processSize, allocation);
    }

    // ---------------- DISPLAY FUNCTION ----------------
    static void displayResult(int[] processSize, int[] allocation) {
        System.out.println("\nProcess No.\tProcess Size\tBlock No.");
        for (int i = 0; i < processSize.length; i++) {
            System.out.print("   " + (i + 1) + "\t\t" + processSize[i] + "\t\t");
            if (allocation[i] != -1)
                System.out.println((allocation[i] + 1));
            else
                System.out.println("Not Allocated");
        }
    }
}
