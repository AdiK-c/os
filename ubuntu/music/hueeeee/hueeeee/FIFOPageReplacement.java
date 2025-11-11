import java.util.*;

public class FIFOPageReplacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of pages in reference string: ");
        int n = sc.nextInt();

        int[] pages = new int[n];
        System.out.println("Enter the reference string:");
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }

        System.out.print("Enter number of frames: ");
        int framesCount = sc.nextInt();

        int[] frames = new int[framesCount];
        Arrays.fill(frames, -1); // initialize with -1 (empty)

        int pointer = 0, hits = 0, faults = 0;

        System.out.println();
        for (int i = 0; i < n; i++) {
            int page = pages[i];
            boolean hit = false;

            // Check if page is already in frame
            for (int j = 0; j < framesCount; j++) {
                if (frames[j] == page) {
                    hit = true;
                    hits++;
                    break;
                }
            }

            // If not hit -> page fault
            if (!hit) {
                frames[pointer] = page;
                pointer = (pointer + 1) % framesCount;
                faults++;
            }

            // Display current step
            System.out.print("Step " + (i + 1) + " (Page " + page + "): ");
            for (int f = 0; f < framesCount; f++) {
                if (frames[f] != -1)
                    System.out.print(frames[f] + " ");
                else
                    System.out.print("- ");
            }
            if (hit)
                System.out.println(" (HIT)");
            else
                System.out.println(" (FAULT)");
        }

        double hitRatio = (double) hits / n;
        double faultRatio = (double) faults / n;

        System.out.println("\nTotal Hits: " + hits);
        System.out.println("Total Faults: " + faults);
        System.out.println("Hit Ratio: " + hitRatio);
        System.out.println("Fault Ratio: " + faultRatio);
    }
}

/*
 Enter the number of pages in reference string: 12
Enter the reference string:
2 3 2 1 5 2 4 5 3 2 5 2
Enter number of frames: 3
 */