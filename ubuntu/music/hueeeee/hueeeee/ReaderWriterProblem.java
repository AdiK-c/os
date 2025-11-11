import java.util.concurrent.Semaphore;

// Shared resource
class Shared {
    static int data = 0; // shared data
}

// Reader-Writer Problem using Semaphore and Mutex
class ReaderWriter {
    // Semaphore to ensure mutual exclusion for writers
    static Semaphore wrt = new Semaphore(1);
    // Mutex to protect reader count updates
    static Semaphore mutex = new Semaphore(1);
    static int readCount = 0; // Number of active readers
}

// Reader class
class Reader implements Runnable {
    private int readerId;

    Reader(int id) {
        this.readerId = id;
    }

    @Override
    public void run() {
        try {
            // Entry Section
            ReaderWriter.mutex.acquire();
            ReaderWriter.readCount++;
            if (ReaderWriter.readCount == 1)
                ReaderWriter.wrt.acquire(); // First reader locks writer
            ReaderWriter.mutex.release();

            // Critical Section
            System.out.println("Reader " + readerId + " is READING. Data = " + Shared.data);
            Thread.sleep(1000);

            // Exit Section
            ReaderWriter.mutex.acquire();
            ReaderWriter.readCount--;
            if (ReaderWriter.readCount == 0)
                ReaderWriter.wrt.release(); // Last reader unlocks writer
            ReaderWriter.mutex.release();

            System.out.println("Reader " + readerId + " has FINISHED READING.");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

// Writer class
class Writer implements Runnable {
    private int writerId;

    Writer(int id) {
        this.writerId = id;
    }

    @Override
    public void run() {
        try {
            ReaderWriter.wrt.acquire(); // Request exclusive access
            System.out.println("Writer " + writerId + " is WRITING...");
            Shared.data++;
            Thread.sleep(1000);
            System.out.println("Writer " + writerId + " has FINISHED WRITING. Data = " + Shared.data);
            ReaderWriter.wrt.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class ReaderWriterProblem {
    public static void main(String[] args) {
        System.out.println("=== Reader Writer Problem Simulation using Mutex and Semaphore ===");

        Thread w1 = new Thread(new Writer(1));
        Thread r1 = new Thread(new Reader(1));
        Thread r2 = new Thread(new Reader(2));
        Thread w2 = new Thread(new Writer(2));
        Thread r3 = new Thread(new Reader(3));

        // Start threads in interleaved order
        r1.start();
        w1.start();
        r2.start();
        w2.start();
        r3.start();
    }
}
