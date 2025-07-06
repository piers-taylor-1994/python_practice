import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 2
    
    def insert(self, val):
        # Append value and bubble it up
        self.heap.append(val)

        val_idx = len(self.heap) - 1

        while val_idx > 0:
            parent_idx = self.parent(val_idx)

            if self.heap[val_idx] < self.heap[parent_idx]:
                self.heap[val_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[val_idx]
                val_idx = parent_idx
            else:
                break
    
    def extract_min(self):
        # Swap root with last, remove last, bubble root down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        min_val = self.heap.pop()

        root_idx = 0

        while root_idx < len(self.heap):
            smallest = root_idx
            left_child_idx = self.left_child(root_idx)
            right_child_idx = self.right_child(root_idx)

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest]:
                smallest = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest]:
                smallest = right_child_idx
            if smallest == root_idx:
                break

            self.heap[root_idx], self.heap[smallest] = self.heap[smallest], self.heap[root_idx]
            root_idx = smallest
        
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None

    
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