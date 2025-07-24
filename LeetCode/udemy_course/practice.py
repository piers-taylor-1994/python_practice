from collections import deque
import random
import heapq
 
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class MinHeap():
    def __init__(self):
        ...

class MaxHeap:
    def __init__(self):
        ...

class TrieNode:
    def __init__(self):
        ...
class Trie:
    def __init__(self):
        ...

class Solution:
    """
    1. Arrays ✓ (22/07)
    2. Strings ✓ (22/07)
    3. Linked lists ✓ (24/07)
    4. Binary trees ✓ (23/07)
    5. Tries ✓ (23/07)
    6. Greedy ✓ (24/07)
    7. Matrices ✓ (24/07)
    8. Graphs
    9. Heaps
    10. Bitmask
    11. DP
    12. Backtracking
    13. Prefix sum ✓ (22/07)
    14. Sliding window ✓ (22/07)
    """

    def oranges_rotting(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        rotten_oranges = set()
        fresh_oranges = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    fresh_oranges += 1
                elif matrix[i][j] == 2:
                    rotten_oranges.add((i, j))
        
        if fresh_oranges == 0:
            return 0
        
        seen = rotten_oranges
        queue = deque(rotten_oranges)
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    new_row = row + dr
                    new_col = col + dc

                    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and (new_row, new_col) not in seen and matrix[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))
                        fresh_oranges -= 1
            minutes += 1
        
        return minutes if fresh_oranges == 0 else -1


    
# print(random.choice([]))
# print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice([]))
# print(random.choice(["right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["walls_gates"]))
# print(random.choice(["can_finish", "network_delay_time"]))
# print(random.choice(["subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"]))

solution = Solution()

print(solution.oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))
print(solution.oranges_rotting([[0, 1]]))

# head = Node(1)
# node_1 = Node(2)
# node_2 = Node(3)
# node_3 = Node(4)
# node_4 = Node(5)
# head.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4

# print("\nHeaps")
# min_heap = MinHeap()
# min_heap.insert(0)
# min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(3)
# min_heap.insert(7)
# min_heap.insert(9)
# print(min_heap.heap)
# min_heap.extract_minimum()
# print(min_heap.heap)

# max_heap = MaxHeap()
# max_heap.insert(0)
# max_heap.insert(10)
# max_heap.insert(5)
# max_heap.insert(3)
# max_heap.insert(7)
# max_heap.insert(9)
# print(max_heap.return_heap())
# max_heap.extract_max()
# print(max_heap.return_heap())
# max_heap.heapify([0, 10, 5, 3, 7, 9])
# print(max_heap.return_heap())