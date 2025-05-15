from collections import deque


class PriorityQueue:
    def __init__(self, queue, max_heap = True):
        self.heap = deque(queue)
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

        while self.heap[self.parent(self.heap.index(x))] < x:
            self.swap(self.heap.index(x), self.parent(self.heap.index(x)))

        return self.heap
    
    def pop(self):
        self.heap.popleft()

        x = self.heap.pop()
        self.heap.appendleft(x)

        while self.comparator(max(self.heap[self.left_child(self.heap.index(x))], self.heap[self.right_child(self.heap.index(x))] if self.right_child(self.heap.index(x)) < len(self.heap) else 0), x):
            self.swap(self.heap.index(x), self.heap.index(max(self.heap[self.left_child(self.heap.index(x))], self.heap[self.right_child(self.heap.index(x))])))

        return self.heap

priority_queue = PriorityQueue([50,25,45,35,10,15,20])
print("Insertion demo")
print(priority_queue.heap)
print(priority_queue.push(40))
print("\nDeletion demo")
priority_queue = PriorityQueue([75,50,25,45,35,10,15,20,40])
print(priority_queue.heap)
print(priority_queue.pop())