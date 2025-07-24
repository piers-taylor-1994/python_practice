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
    6. Greedy
    7. Matrices
    8. Graphs
    9. Heaps
    10. Bitmask
    11. DP
    12. Backtracking
    13. Prefix sum ✓ (22/07)
    14. Sliding window ✓ (22/07)
    """

    def reverse_partially_linked_list(self, head, left, right):
        if not head or not head.next:
            return head

        current = head
        node_before_reverse = head
        idx = 1

        while idx < left:
            node_before_reverse = current
            current = current.next
            idx += 1

        tail = current
        prev = None
        
        while left <= idx <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            idx += 1

        node_before_reverse.next = prev
        tail.next = current

        return head if left > 1 else prev
    
# print(random.choice([]))
# print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice([]))
# print(random.choice(["right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["orange_rotting", "walls_gates"]))
# print(random.choice(["can_finish", "network_delay_time"]))
# print(random.choice(["subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"]))

solution = Solution()

head = Node(1)
node_1 = Node(2)
node_2 = Node(3)
node_3 = Node(4)
node_4 = Node(5)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

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