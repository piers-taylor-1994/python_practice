import threading
import time

#Like a library:
# Readers can read books simultaneously.
# Writers (editors) need exclusive access to update a book.
# Readers wait if a writer is editing. Writers wait if readers are reading.

class ReaderWriterLock:
    def __init__(self):
        self.readers = 0
        self.reader_lock = threading.Lock()
        self.writer_lock = threading.Lock()

    def acquire_read(self):
        with self.reader_lock:
            self.readers += 1

            if self.readers == 1:
                self.writer_lock.acquire()
    
    def release_read(self):
        with self.reader_lock:
            self.readers -= 1

            if self.readers == 0:
                self.writer_lock.release()
    
    def acquire_write(self):
        self.writer_lock.acquire()
    
    def release_write(self):
        self.writer_lock.release()

rw_lock = ReaderWriterLock()

def reader(id):
    rw_lock.acquire_read()
    print(f"Reader {id} is reading")
    time.sleep(0.25)
    print(f"Reader {id} finished")
    rw_lock.release_read()

def writer(id):
    rw_lock.acquire_write()
    print(f"Writer {id} is writing")
    time.sleep(0.5)
    print(f"Writer {id} finished")
    rw_lock.release_write()

threads = []
for i in range(3):
    t = threading.Thread(target=reader, args=(i,))
    threads.append(t)
for i in range(2):
    t = threading.Thread(target=writer, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()