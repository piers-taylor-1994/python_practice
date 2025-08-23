import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    """Increment shared mutable counter in a thread-safe way"""
    global counter
    for _ in range(100000):
        #Critical section
        with lock:
            counter += 1
    
threads = []
for _ in range(2):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter: {counter}")