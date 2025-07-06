import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def parent(self, i):
        return (i-1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, val):
        # Append value and bubble it up
        self.heap.append(val)

        val_idx = self.__len__() - 1

        while val_idx > 0:
            parent_idx = self.parent(val_idx)

            if self.heap[val_idx] < self.heap[parent_idx]:
                self.swap(val_idx, parent_idx)
                val_idx = parent_idx
            else:
                break
    
    def extract_min(self):
        # Swap root with last, remove last, bubble root down
        self.swap(0, self.__len__() - 1)

        min_value = self.heap.pop()

        root_idx = 0

        while root_idx < self.__len__():
            smallest_idx = root_idx
            left_child_idx = self.left_child(root_idx)
            right_child_idx = self.right_child(root_idx)

            if left_child_idx < self.__len__() and self.heap[left_child_idx] < self.heap[smallest_idx]:
                smallest_idx = left_child_idx
            if right_child_idx < self.__len__() and self.heap[right_child_idx] < self.heap[smallest_idx]:
                smallest_idx = right_child_idx
            if smallest_idx == root_idx:
                break

            self.swap(root_idx, smallest_idx)
            root_idx = smallest_idx
        
        return min_value

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def heapify(self, arr):
        self.heap = arr

        for i in range(len(arr) - 1, -1, -1):
            idx = i

            while idx < self.__len__():
                smallest_idx = idx
                left_child_idx = self.left_child(idx)
                right_child_idx = self.right_child(idx)

                if left_child_idx < self.__len__() and self.heap[left_child_idx] < self.heap[smallest_idx]:
                    smallest_idx = left_child_idx
                if right_child_idx < self.__len__() and self.heap[right_child_idx] < self.heap[smallest_idx]:
                    smallest_idx = right_child_idx
                if smallest_idx == idx:
                    break

                self.swap(idx, smallest_idx)
                idx = smallest_idx

class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def parent(self, i):
        return (i-1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, val):
        self.heap.append(val)

        val_idx = self.__len__() - 1

        while val_idx > 0:
            parent_idx = self.parent(val_idx)

            if self.heap[val_idx] > self.heap[parent_idx]:
                self.swap(val_idx, parent_idx)
                val_idx = parent_idx
            else:
                break
    
    def extract_max(self):
        self.swap(0, self.__len__() - 1)
        max_value = self.heap.pop()

        root_idx = 0
        while root_idx < self.__len__():
            greatest_idx = root_idx
            left_child = self.left_child(root_idx)
            right_child = self.right_child(root_idx)

            if left_child < self.__len__() and self.heap[greatest_idx] < self.heap[left_child]:
                greatest_idx = left_child
            if right_child < self.__len__() and self.heap[greatest_idx] < self.heap[right_child]:
                greatest_idx = right_child
            if greatest_idx == root_idx:
                break

            self.swap(root_idx, greatest_idx)
            root_idx = greatest_idx
        
        return max_value

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def heapify(self, arr):
        self.heap = arr

        for i in range(self.parent(self.__len__()), -1, -1):
            idx = i
            while idx < self.__len__():
                greatest_idx = idx
                left_child = self.left_child(idx)
                right_child = self.right_child(idx)

                if left_child < self.__len__() and self.heap[greatest_idx] < self.heap[left_child]:
                    greatest_idx = left_child
                if right_child < self.__len__() and self.heap[greatest_idx] < self.heap[right_child]:
                    greatest_idx = right_child
                if greatest_idx == idx:
                    break

                self.swap(idx, greatest_idx)
                idx = greatest_idx
    
# heap = MinHeap()
# heap.insert(5)
# heap.insert(3)
# heap.insert(8)
# heap.insert(1)
# heap.insert(2)
# print(heap.heap)
# heap.extract_min()
# print(heap.heap)
# heap.heapify([5,3,8,1,2])
# print(heap.heap)

# print("///")

# heap_2 = []
# heapq.heappush(heap_2, 5)
# heapq.heappush(heap_2, 3)
# heapq.heappush(heap_2, 8)
# heapq.heappush(heap_2, 1)
# heapq.heappush(heap_2, 2)
# print(heap_2)
# heapq.heappop(heap_2)
# print(heap_2)
# heap_2 = [5,3,8,1,2]
# heapq.heapify(heap_2)
# print(heap_2)

max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(1)
max_heap.insert(2)
print(max_heap.heap)
max_heap.extract_max()
print(max_heap.heap)
max_heap.heapify([5,3,8,1,2])
print(max_heap.heap)

max_heap_2 = []
heapq.heappush(max_heap_2, -5)
heapq.heappush(max_heap_2, -3)
heapq.heappush(max_heap_2, -8)
heapq.heappush(max_heap_2, -1)
heapq.heappush(max_heap_2, -2)
print([i * -1 for i in max_heap_2])
heapq.heappop(max_heap_2)
print([i * -1 for i in max_heap_2])
max_heap_2 = [-5,-3,-8,-1,-2]
heapq.heapify(max_heap_2)
print([i * -1 for i in max_heap_2])