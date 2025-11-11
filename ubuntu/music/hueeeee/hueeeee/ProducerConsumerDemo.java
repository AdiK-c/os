import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.Semaphore;

// Shared class for Producer–Consumer logic
class ProducerConsumer {
    private final Queue<Integer> buffer = new LinkedList<>();
    private final int maxSize;

    // Semaphores
    private final Semaphore empty; // Tracks empty slots
    private final Semaphore full;  // Tracks filled slots
    private final Semaphore mutex = new Semaphore(1); // Ensures mutual exclusion

    // Constructor
    public ProducerConsumer(int size) {
        this.maxSize = size;
        this.empty = new Semaphore(size); // Initially, all slots are empty
        this.full = new Semaphore(0);     // Initially, no slots are full
    }

    // Producer method
    public void produce(int item) throws InterruptedException {
        empty.acquire();   // Wait if buffer is full
        mutex.acquire();   // Enter critical section

        buffer.add(item);
        System.out.println("Produced: " + item);

        mutex.release();   // Exit critical section
        full.release();    // Signal that an item has been produced
    }

    // Consumer method
    public int consume() throws InterruptedException {
        full.acquire();    // Wait if buffer is empty
        mutex.acquire();   // Enter critical section

        int item = buffer.poll();
        System.out.println("Consumed: " + item);

        mutex.release();   // Exit critical section
        empty.release();   // Signal that a slot is now empty
        return item;
    }
}

// Main class
public class ProducerConsumerDemo {
    public static void main(String[] args) {
        ProducerConsumer pc = new ProducerConsumer(5); // Buffer size = 5

        // Producer thread
        Thread producer = new Thread(() -> {
            int item = 1;
            try {
                for (int i = 0; i < 10; i++) { // Produce 10 items
                    pc.produce(item++);
                    Thread.sleep(500); // Simulate production time
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // Consumer thread
        Thread consumer = new Thread(() -> {
            try {
                for (int i = 0; i < 10; i++) { // Consume 10 items
                    pc.consume();
                    Thread.sleep(1000); // Simulate consumption time
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // Start both threads
        producer.start();
        consumer.start();

        // Wait for both threads to finish
        try {
            producer.join();
            consumer.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("\nAll items produced and consumed successfully!");
    }
}
