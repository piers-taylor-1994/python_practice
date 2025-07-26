from collections import Counter, deque
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
        self.heap = []
        heapq.heapify(self.heap)

    def return_heap(self):
        return [-val for val in self.heap]

    def insert(self, value):
        heapq.heappush(self.heap, -value)
    
    def extract_max(self):
        return -heapq.heappop(self.heap)
    
    def heapify(self, arr):
        arr_to_heap = [-val for val in arr]
        heapq.heapify(arr_to_heap)
        self.heap = arr_to_heap

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
    8. Graphs ✓ (25/07)
    9. Heaps ✓ (25/07)
    10. Bitmask ✓ (25/07)
    11. DP
    12. Backtracking
    13. Prefix sum ✓ (22/07)
    14. Sliding window ✓ (22/07)
    """
    # [1,2,3] 3 => [[1,2], [3]]
    def subarrays_equal_k(self, nums, k):
        prefix = 0
        hash_map = {0: 1}
        total = 0

        for i in range(len(nums)):
            prefix += nums[i]
            total += hash_map.get(prefix - k, 0)
            hash_map[prefix] = hash_map.get(prefix, 0) + 1
        
        return total
    
    # "cbaebabacd", "abc" => [0, 6]
    def find_all_anagrams(self, s, p):
        results = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])

        for i in range(len(p) - 1, len(s)):
            start_idx = (i - len(p)) + 1

            if start_idx > 0:
                s_count[s[i]] = s_count.get(s[i], 0) + 1

                if s_count[s[start_idx - 1]] == 1:
                    del s_count[s[start_idx - 1]]
                else:
                    s_count[s[start_idx - 1]] -= 1
            

            if p_count == s_count:
                results.append(start_idx)
        
        return results
    
    # "ADOBECODEBANC", "ABC" => "BANC"
    def minimum_window_substring(self, s, t):
        t_count = Counter(t)
        s_count = Counter()
        result = ""
        min_length = float('inf')
        left = 0

        for right in range(len(s)):
            s_count[s[right]] += 1

            while s_count >= t_count:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    result = s[left:right + 1]
                
                if s_count[s[left]] == 1:
                    del s_count[s[left]]
                else:
                    s_count[s[left]] -= 1
                
                left += 1
        
        return result

    
# print(random.choice([]))
# print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice([]))
# print(random.choice(["right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["walls_gates"]))
# print(random.choice(["network_delay_time"]))

#"subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"
# print(random.choice(["subset sum/partition", "string manipulation", "decision based", "probability and counting", "bitmask"]))

solution = Solution()
print(solution.subarrays_equal_k([1,2,3], 3))
print(solution.subarrays_equal_k([1,-1, 0], 0))

print(solution.find_all_anagrams("cbaebabacd", "abc"))

print(solution.minimum_window_substring("ADOBECODEBANC", "ABC"))

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