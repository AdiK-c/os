import java.util.*;

public class OptimalPageReplacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input reference string
        System.out.println("Enter the number of pages in reference string: ");
        int n = sc.nextInt();

        int[] pages = new int[n];
        System.out.println("Enter the reference string: ");
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }

        // Input number of frames
        System.out.println("Enter number of frames: ");
        int capacity = sc.nextInt();

        int[] frames = new int[capacity];
        Arrays.fill(frames, -1); // initialize all frames as empty
        int hit = 0, fault = 0;

        for (int i = 0; i < n; i++) {
            int currentPage = pages[i];
            boolean pageFound = false;

            // Check if page is already in frame
            for (int j = 0; j < capacity; j++) {
                if (frames[j] == currentPage) {
                    hit++;
                    pageFound = true;
                    break;
                }
            }

            // If not found => Page Fault
            if (!pageFound) {
                fault++;

                // Find empty frame
                boolean emptyFound = false;
                for (int j = 0; j < capacity; j++) {
                    if (frames[j] == -1) {
                        frames[j] = currentPage;
                        emptyFound = true;
                        break;
                    }
                }

                // If no empty frame, replace using Optimal logic
                if (!emptyFound) {
                    int indexToReplace = findOptimalIndex(frames, pages, i + 1);
                    frames[indexToReplace] = currentPage;
                }
            }

            // Display current frame status
            System.out.print("Step " + (i + 1) + " (Page " + currentPage + "): ");
            for (int f : frames) {
                if (f == -1)
                    System.out.print("- ");
                else
                    System.out.print(f + " ");
            }

            if (pageFound)
                System.out.println(" (HIT)");
            else
                System.out.println(" (FAULT)");
        }

        System.out.println("\nTotal Hits: " + hit);
        System.out.println("Total Faults: " + fault);
        System.out.println("Hit Ratio: " + ((float) hit / n));
        System.out.println("Fault Ratio: " + ((float) fault / n));
        sc.close();
    }

    // Function to find which page to replace using Optimal strategy
    public static int findOptimalIndex(int[] frames, int[] pages, int startIndex) {
        int farthest = startIndex, indexToReplace = -1;

        for (int i = 0; i < frames.length; i++) {
            int j;
            for (j = startIndex; j < pages.length; j++) {
                if (frames[i] == pages[j]) {
                    if (j > farthest) {
                        farthest = j;
                        indexToReplace = i;
                    }
                    break;
                }
            }

            // If page is never used again
            if (j == pages.length)
                return i;
        }

        if (indexToReplace == -1)
            return 0;
        else
            return indexToReplace;
    }
}

/*
 Enter the number of pages in reference string:
12
Enter the reference string:
2 3 2 1 5 2 4 5 3 2 5 2
Enter number of frames:
3
 */
