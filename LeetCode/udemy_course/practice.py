from collections import Counter, deque
import random
import heapq
import bisect
 
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
        self.end = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.end = True
    
    def search_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return node.end
    
    def search_prefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True


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

    def longest_subarray_sum_equalorless_target(self, nums, target):
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        longest_arr = 0
        q = deque([])

        for i in range(len(prefix)):
            while q and prefix[i] - prefix[q[0]] > target:
                q.popleft()
            
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)
            
            if q:
                longest_arr = max(longest_arr, i - q[0])
        
        return longest_arr
    
    def max_in_each_window(self, nums, k):
        q = deque([])
        results = []

        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                results.append(nums[q[0]])
        
        return results
    
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        shortest_subarray = float('inf')
        q = deque()

        for i in range(len(prefix)):
            while q and prefix[i] - prefix[q[0]] >= k:
                shortest_subarray = min(shortest_subarray, i - q.popleft())
            
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()
            
            q.append(i)
        
        return shortest_subarray if shortest_subarray != float('inf') else -1

    
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

print(solution.longest_subarray_sum_equalorless_target([2,-1,2], 3))

# print(solution.shortest_subarray_equal_k([1], 1))
# print(solution.shortest_subarray_equal_k([1,2], 4))
# print(solution.shortest_subarray_equal_k([2,-1,2], 3))

# print(solution.jump_game_2([2,3,1,1,4]))

# print(solution.task_schedule_max_profit([(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]))

# trie = Trie()
# trie.insert_word("appls")
# print(trie.search_word("apple"))
# print(trie.search_prefix("app"))

print(solution.max_in_each_window([1,3,-1,-3,5,3,6,7], 3))

print(solution.shortestSubarray([2, -1, 2], 3))

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