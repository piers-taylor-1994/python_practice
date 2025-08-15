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

    #Wednesday
    #2787. Ways to Express an Integer as Sum of Powers (Medium)
    #70. Climbing Stairs (Easy)
    #46. Permutations (Medium)
    
    def integer_sum_powers(self, n, x):        
        memo = {}

        def rec(last_number, total):
            if total == 0:
                return 1
            elif total < 0:
                return 0
            elif (last_number, total) in memo:
                return memo[(last_number, total)]
            
            memo[(last_number, total)] = sum([rec(i + 1, (total - (i ** x))) for i in range(last_number, n + 1)])
            return memo[(last_number, total)]
        
        return rec(1, n) % ((10**9) + 7)

    def climbing_stairs_memo(self, n):
        memo = {}

        def rec(steps):
            if steps <= 2:
                return steps
            elif steps in memo:
                return memo[steps]
            
            memo[steps] = rec(steps - 1) + rec(steps - 2)
            return memo[steps]
        
        return rec(n)
    def climbing_stairs_tab(self, n):
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def permutations(self, nums):
        results = []
        used = set()

        def rec(index, subarray):
            if len(subarray) == len(nums):
                results.append(subarray[:])
                return

            for num in nums:
                if num not in used:
                    subarray.append(num)
                    used.add(num)

                    rec(index + 1, subarray)

                    subarray.pop()
                    used.remove(num)
        
        rec(0, [])
        return results

    #Thursday
    #869. Reordered Power of 2 (Medium)
    #343. Integer Break (Medium)
    #191. Number of 1 Bits (Easy)

    def hamming_weight(self, n):
        return bin(n).count("1")
    
    def reorderedPowerOf2(self, n):
        def reorder(x):
            return sorted(str(x))
        
        n_ordered = reorder(n)
        
        for i in range(30):
            if reorder(2 ** i) == n_ordered:
                return True
        return False
    
    def int_break(self, n):
        memo = {}

        def rec(num):
            if num <= 3:
                return num
            elif num in memo:
                return memo[num]
            
            memo[num] = rec(num // 2) * rec(num - (num // 2))
            return memo[num]
        
        return rec(n // 2) * rec(n - (n // 2))
    
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

print(solution.climbing_stairs_memo(5))
print(solution.climbing_stairs_tab(5))

print(solution.permutations([1,2,3]))

print(solution.integer_sum_powers(4, 1))
print(solution.integer_sum_powers(2, 1))

print(solution.hamming_weight(11))

print(solution.reorderedPowerOf2(16))

print(solution.int_break(2))

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