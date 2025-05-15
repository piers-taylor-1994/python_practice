from collections import deque


class PriorityQueue:
    def __init__(self, max_heap = True):
        self.heap = deque([50,25,45,35,10,15,20])
        self.max_heap = max_heap
        pass

    def comparator(self, a, b):
        if self.max_heap:
            return a > b
        else:
            return a < b
        
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def parent(self, idx):
        return (idx - 1) // 2
    
    def left_child(self, idx):
        return (idx * 2) + 1
    
    def right_child(self, idx):
        return (idx * 2) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def peek(self):
        return self.heap[0]
    
    def push(self, x):
        self.heap.append(x)

        while(self.heap[self.parent(self.heap.index(x))] < x):
            self.swap(self.heap.index(x), self.parent(self.heap.index(x)))

        return self.heap

priority_queue = PriorityQueue()
print(priority_queue.heap)
print(priority_queue.push(40))