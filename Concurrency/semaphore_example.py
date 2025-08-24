import threading
import time

semaphore = threading.Semaphore(3)
lock = threading.Lock()
counter = 0

def increment_counter(thread_id):
    global counter
    print(f"Thread {thread_id} awaiting connection")

    with semaphore:
        print(f"Thread {thread_id} ready to work")
        time.sleep(0.1)
        
        with lock:
            print(f"Thread {thread_id} doing critical work")
            counter += 1

threads = [threading.Thread(target=increment_counter, args=(i, )) for i in range(9)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Threads all finished. Counter: {counter}")