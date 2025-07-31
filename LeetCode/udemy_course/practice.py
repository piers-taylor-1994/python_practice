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
        nums_length = len(nums)

        prefix = [0] * (nums_length + 1)
        for i in range(nums_length):
            prefix[i + 1] = prefix[i] + nums[i]
        
        queue = deque([0])
        max_length = 0

        for i in range(1, len(prefix)):
            while queue and prefix[i] - prefix[queue[0]] > target:
                queue.popleft()
            
            if queue:
                max_length = max(max_length, i - queue[0])
            
            #incoming value is smaller so pop all that are bigger
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        return max_length
    
    def jump_game_2(self, nums):
        furthest = 0
        current_furthest = 0
        jumps = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == current_furthest:
                current_furthest = furthest
                jumps += 1
        
        return jumps
    
    def task_schedule_max_profit(self, tasks):
        sorted_tasks = sorted(tasks, key=lambda x:-x[1])
        days_taken = set()
        total_profit = 0

        for deadline, profit in sorted_tasks:
            for day in range(deadline, 0, -1):
                if day not in days_taken:
                    total_profit += profit
                    days_taken.add(day)
                    break
        
        return total_profit
    
    def max_in_each_window(self, nums, k):
        q = deque()
        results = []

        for i in range(len(nums)):
            #out of range
            while q and q[0] < i - k + 1:
                q.popleft()
            
            #incoming value is bigger so pop all that are smaller
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            #this value must be smaller thus if there are any values they must be bigger than what's going in
            q.append(i)

            #if first window has developed i.e i >= 3 - 1(2)
            if i >= k - 1:
                results.append(nums[q[0]])
        
        return results
    
    def longest_subarray_sum_equalorless_target_2(self, nums, target):
        total = 0
        max_longest = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total > target:
                total -= nums[left]
                left += 1
            
            max_longest = max(max_longest, right - left + 1)
        
        return max_longest
    
    def shortest_subarray_equal_k(self, nums, k):
        total = 0
        min_shortest = float('inf')
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= k:
                min_shortest = min(min_shortest, right - left + 1)

                total -= nums[left]
                left += 1
        
        return min_shortest if min_shortest != float('inf') else -1

    
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
print(solution.longest_subarray_sum_equalorless_target_2([2,-1,2], 3))

print(solution.shortest_subarray_equal_k([1], 1))
print(solution.shortest_subarray_equal_k([1,2], 4))
print(solution.shortest_subarray_equal_k([2,-1,2], 3))

# print(solution.jump_game_2([2,3,1,1,4]))

# print(solution.task_schedule_max_profit([(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]))

# trie = Trie()
# trie.insert_word("appls")
# print(trie.search_word("apple"))
# print(trie.search_prefix("app"))

# print(solution.max_in_each_window([1,3,-1,-3,5,3,6,7], 3))

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