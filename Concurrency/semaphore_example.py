import random
import threading
import time

connection_pool = threading.Semaphore(3)
lock = threading.Lock()
counter = 0

def counter_increment(task_id):
    global counter
    print(f"Task {task_id} waiting for connection\n")
    
    with connection_pool:
        print(f"Task {task_id} ready to work\n")
        time.sleep(random.uniform(0.5, 1.5))
        with lock:
            print(f"Task {task_id} doing critical work\n")
            counter += 1

threads = [threading.Thread(target=counter_increment, args=(i,)) for i in range(9)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"All tasks complete, counter: {counter}")