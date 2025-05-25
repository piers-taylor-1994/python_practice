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
        
    def min_max(self, a, b):
        if self.max_heap:
            return max(a, b)
        return min(a, b)
        
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

        while self.comparator(x, self.heap[self.parent(self.heap.index(x))]):
            self.swap(self.heap.index(x), self.parent(self.heap.index(x)))
            if self.heap.index(x) == 0:
                break

        return self.heap
    
    def pop(self):
        self.heap.popleft()

        x = self.heap.pop()
        self.heap.appendleft(x)

        while self.comparator(self.min_max(self.heap[self.left_child(self.heap.index(x))], self.heap[self.right_child(self.heap.index(x))] if self.right_child(self.heap.index(x)) < len(self.heap) else 0), x):
            self.swap(self.heap.index(x), self.heap.index(self.min_max(self.heap[self.left_child(self.heap.index(x))], self.heap[self.right_child(self.heap.index(x)) if self.right_child(self.heap.index(x)) < len(self.heap) else 0])))
            if self.left_child(self.heap.index(x)) >= len(self.heap):
                break

        return self.heap

print("Insertion demo max_heap")
priority_queue = PriorityQueue([50,25,45,35,10,15,20])
print(priority_queue.heap)
print(priority_queue.push(40))

print("\nInsertion demo min_heap")
priority_queue = PriorityQueue([10,15,25,20,35,30,50], False)
print(priority_queue.heap)
print(priority_queue.push(8))

print("\nDeletion demo max_heap")
priority_queue = PriorityQueue([75,50,25,45,35,10,15,20,40])
print(priority_queue.heap)
print(priority_queue.pop())

print("\nDeletion demo min_heap")
priority_queue = PriorityQueue([10,15,25,20,35,30,50,28], False)
print(priority_queue.heap)
print(priority_queue.pop())