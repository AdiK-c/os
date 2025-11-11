import java.util.*;

public class LRU_PageReplacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input: reference string
        System.out.println("Enter the number of frames: ");
        int frames = sc.nextInt();

        System.out.println("Enter the reference string (space separated): ");
        sc.nextLine(); // consume newline
        String[] refStr = sc.nextLine().trim().split("\\s+");
        int[] reference = new int[refStr.length];
        for (int i = 0; i < refStr.length; i++)
            reference[i] = Integer.parseInt(refStr[i]);

        // Initialize
        ArrayList<Integer> memory = new ArrayList<>(frames);
        int pageFaults = 0;
        int pageHits = 0;

        System.out.println("\nPage Replacement Process (LRU):\n");

        // Simulation
        for (int page : reference) {
            if (memory.contains(page)) {
                pageHits++;
                // Move the page to the end to mark it as most recently used
                memory.remove((Integer) page);
                memory.add(page);
            } else {
                pageFaults++;
                if (memory.size() == frames) {
                    // Remove least recently used (first element)
                    memory.remove(0);
                }
                memory.add(page);
            }

            // Print current frame status
            System.out.printf("Reference: %2d => ", page);
            for (int i = 0; i < frames; i++) {
                if (i < memory.size())
                    System.out.print(memory.get(i) + " ");
                else
                    System.out.print("- ");
            }
            System.out.println();
        }

        // Results
        System.out.println("\nTotal Page Faults: " + pageFaults);
        System.out.println("Total Page Hits: " + pageHits);
        System.out.printf("Hit Ratio: %.2f\n", (float) pageHits / reference.length);
        System.out.printf("Fault Ratio: %.2f\n", (float) pageFaults / reference.length);
    }
}


/*
    Enter the number of frames:
    3
    Enter the reference string (space separated):
    2 3 2 1 5 2 4 5 3 2 5 2
 */