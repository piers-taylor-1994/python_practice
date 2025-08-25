import threading
import queue
import time
import random

# Shared queue, acts as a buffer that decouples production and consumption speeds
# It's thread safe, the queue will lock off a task if a producer/consumer is working on it
task_queue = queue.Queue()

def producer(pid, num_items):
    for i in range(num_items):
        item = f"Task-{pid}-{i}"
        task_queue.put(item)
        print(f"[Producer {pid}] produced {item}")
        time.sleep(random.uniform(0.1, 0.3))
    print(f"[Producer {pid}] finished producing.")

def consumer(cid):
    while True:
        try:
            item = task_queue.get(timeout=1)  # blocks until item or timeout
        except queue.Empty:
            print(f"[Consumer {cid}] no more items, exiting.")
            break
        print(f"[Consumer {cid}] consumed {item}")
        task_queue.task_done()
        time.sleep(random.uniform(0.2, 0.4))

# Config
NUM_PRODUCERS = 2
NUM_CONSUMERS = 3
ITEMS_PER_PRODUCER = 5

# Start producers
producers = [
    threading.Thread(target=producer, args=(pid, ITEMS_PER_PRODUCER))
    for pid in range(NUM_PRODUCERS)
]

# Start consumers
consumers = [
    threading.Thread(target=consumer, args=(cid,))
    for cid in range(NUM_CONSUMERS)
]

for t in producers + consumers:
    t.start()

for t in producers:
    t.join()

task_queue.join()  # Wait until all tasks are processed

for t in consumers:
    t.join()