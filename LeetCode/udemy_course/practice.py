from collections import deque
import random
import heapq
from re import sub
 
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
    1. Arrays ✓ (22/07)
    2. Strings
    3. Linked lists
    4. Binary trees
    5. Tries
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

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        subarray = []
        longest = 0

        for right in range(len(s)):
            while s[right] in subarray:
                subarray.remove(s[left])
                left += 1
            subarray.append(s[right])
            longest = max(longest, right - left + 1)
        
        return longest
    
# print(random.choice([]))
print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list"]))
# print(random.choice(["level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["orange_rotting", "walls_gates"]))
# print(random.choice(["can_finish", "network_delay_time"]))
# print(random.choice(["subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"]))

solution = Solution()

print(solution.lengthOfLongestSubstring("pwwkew"))

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