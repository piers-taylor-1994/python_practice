import threading

# Shared mutable state
counter = 0

# Lock to protect the critical section
counter_lock = threading.Lock()

def increment_counter():
    """
    Increment the global counter in a thread-safe way.
    Demonstrates Lock (correctness) + Join (completion ordering).
    """
    global counter
    for _ in range(100_000):
        with counter_lock:  # critical section
            counter += 1

# Create worker threads
threads = [threading.Thread(target=increment_counter) for _ in range(2)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final counter: {counter}")