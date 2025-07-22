from collections import deque
import random
import heapq
 
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        ...

class MinHeap():
    def __init__(self):
        ...

class MaxHeap:
    def __init__(self):
        ...

class Solution:
    """
    1. Arrays ✓ (14/07)
    2. Strings ✓ (14/07)
    3. Sorts/searches ✓ (14/07)
    4. Linked lists ✓ (15/07)
    5. Binary trees ✓ (15/07)
    6. Tries ✓ (15/07)
    7. Greedy ✓ (17/07)
    7. Matrices ✓ (16/07)
    8. Stack/queues ✓ (16/07)
    9. Graphs ✓ (17/07)
    10. Heaps ✓ (17/07)
    11. Bitmask ✓ (17/07)
    12. DP ✓ (18/07)
    13. Backtracking ✓ (18/07)

    """
    
# print(random.choice(["container-with-most-water"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating"]))
# print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list"]))
# print(random.choice(["level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["orange_rotting", "walls_gates"]))
# print(random.choice(["can_finish", "network_delay_time"]))
# print(random.choice(["min_cost_stairs", "coin_change", "knapsack", "unique_paths", "min_path", "longest_common_subsequence", "edit_distance", "knight_probability", "dice_roll", "travelling_salesman", "job_assignment"]))

solution = Solution()

# print("\nTrie")
# trie = Trie()
# trie.insert("appls")
# print(trie.search_word("apple"))
# print(trie.search_prefix("app"))

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

print(solution.prefix_sum([1,5,7,12,15,30]))