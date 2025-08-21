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

    def pacificAtlantic(self, heights):
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        row_max = len(heights)
        col_max = len(heights[0])
        pacific_access = set()
        atlantic_access = set()

        def dfs(row, col, ocean, height):
            if row < 0 or row >= row_max or col < 0 or col >= col_max or heights[row][col] < height or (row, col) in ocean:
                return
            ocean.add((row, col))

            for dr, dc in DIRECTIONS:
                dfs(dr + row, dc + col, ocean, heights[row][col])

        for i in range(col_max):
            dfs(0, i, pacific_access, heights[0][i]) #top
            dfs(row_max - 1, i, atlantic_access, heights[row_max - 1][i]) #bottom

        for j in range(row_max):
            dfs(j, 0, pacific_access, heights[j][0]) #left
            dfs(j, col_max - 1, atlantic_access, heights[j][col_max - 1]) #right
        
        return list(pacific_access & atlantic_access)
    
    def longest_substring(self, s):
        letter_count = {}
        longest_length = 0
        left = 0

        for right in range(len(s)):
            right_letter = s[right]
            letter_count[right_letter] = letter_count.get(right_letter, 0) + 1

            while letter_count[right_letter] > 1:
                left_letter = s[left]
                letter_count[left_letter] -= 1

                if letter_count[left_letter] == 0:
                    del letter_count[left_letter]
                left += 1
            
            longest_length = max(longest_length, right - left + 1)
        
        return longest_length
    
    def min_size_subarray_greaterequal_target(self, nums, target):
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = nums[i] + prefix[i]
        
        q = deque()
        min_subarray = float('inf')

        for j in range(len(prefix)):
            while q and prefix[j] - prefix[q[0]] >= target:
                min_subarray = min(min_subarray, j - q.popleft())
            
            while q and prefix[j] <= prefix[q[-1]]:
                q.pop()

            q.append(j)
        
        return min_subarray if min_subarray != float('inf') else 0
    
    def merge_intervals(self, intervals:list):
        if not intervals:
            return []
        
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
        
        return merged


    
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

# print(solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(solution.pacificAtlantic([[1,1],[1,1],[1,1]]))

print(solution.longest_substring("abcabcbb"))

print(solution.min_size_subarray_greaterequal_target([2,3,1,2,4,3], 7))

print(solution.merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

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