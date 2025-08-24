import random
import threading
import time

connection_pool = threading.Semaphore(3)

def db_process(task_id):
    print(f"Task {task_id} waiting for connection\n")

    with connection_pool:
        print(f"Task {task_id} acquired connection\n")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Task {task_id} releasing connection\n")

threads = [threading.Thread(target=db_process, args=(i,)) for i in range(8)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"All tasks complete")