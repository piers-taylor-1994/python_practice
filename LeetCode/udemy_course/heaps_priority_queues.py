import heapq


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        # Append value and bubble it up
        self.heap.append(val)
        val_idx = len(self.heap) - 1

        while val_idx > 0:
            parent_idx = (self.heap.index(val) - 1) // 2
            if self.heap[parent_idx] > val:
                (self.heap[parent_idx], self.heap[val_idx]) = (self.heap[val_idx], self.heap[parent_idx])
                val_idx = parent_idx
            else:
                break
    
    def extract_min(self):
        # Swap root with last, remove last, bubble root down
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        idx = 0
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

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