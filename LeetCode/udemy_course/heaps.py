import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        ...
    
    def insert(self, val):
        # Append value and bubble it up
        ...
    
    def extract_min(self):
        # Swap root with last, remove last, bubble root down
        ...

    def peek(self):
        ...

    
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(2)
print(heap.heap)
heap.extract_min()
print(heap.heap)

heap_2 = []
heapq.heappush(heap_2, 5)
heapq.heappush(heap_2, 3)
heapq.heappush(heap_2, 8)
heapq.heappush(heap_2, 1)
heapq.heappush(heap_2, 2)
print(heap_2)
heapq.heappop(heap_2)
print(heap_2)