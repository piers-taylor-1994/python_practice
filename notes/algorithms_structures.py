from collections import deque
import heapq
import random
from typing import Counter

## Structures

# Array
# - O(1) index access, O(n) search, mutable and ordered
# - Sequential storage, dynamic resizing/appending, useful for stacks/queues
# - Insert/delete in middle is O(n)
arr = []
arr.append("Hello")
arr[0]

# Stack
# - Push/Pop/Peek O(1), Last in, Last Out
# - Useful when you want whatevers last to be the first thing out (valid parentheses)
stack = [1,2,3,4]
stack.append(5)
stack.pop()

# Queue
# - Push/Pop/Peek O(1), First in, First out
# - Useful when order must be preserved, BFS
queue = deque([1,2,3,4,5])
queue.append(5)
queue.popleft()

# Set
# - O(1) lookup/insertion/deletion, disallows duplicates, no index access
# - Fast lookup, removes duplicates, track visited nodes in tree problems
# - Unordered
set_list = set()
set_list.add("Hello")
set_list.add("Hello")

# Dictionary (HashMap)
# - O(1) lookup/insertion/deletion, key-value pairs (keys must be hashable), value can be anything
# - Count frequencies, matching ids to objects, caching for memoization in DP
dict = {}
dict["test"] = "results"
dict[("key1", "key2")] = ["value1", "value2"]
counter = Counter("abc")

# Tuple
# - Immutable/ordered, dictionary keys, supports indexing
# - Fixed collection of values, hashable keys for sets/dictionaries
# - Cannot be modified, inflexible
key = ("h", "e", "l", "l", "o")

# Heaps
# - Root always contains smallest/larget element, insert/pop is O(log n), implemented via heapq
# - Priority queues, scheduling tasks, finding k smallest elements
# - No O(1) look up for arbitrary elements, max_heap requires negation
min_heap = [1, 5, 2, 0, -5, 10, 3]
heapq.heapify(min_heap)
print(heapq.heappop(min_heap))

max_heap = [10, 100, 1000, 2, 3, 10000]
max_heap = [-num for num in max_heap]
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))

## Algorithms

# Binary search -> Find a number in a sorted array. If it isn't quite sorted, you need to make it so/tweak the algorithm to make it work
def binary_search():
    nums = [1,2,3,4,5,6]
    target = 2
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

# Quicksort -> sort numbers
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = random.choice(nums)

    lower = [num for num in nums if num < mid]
    middle = [num for num in nums if num == mid]
    upper = [num for num in nums if num > mid]

    return quick_sort(lower) + middle + quick_sort(upper)

print(quick_sort([1, 5, 2, 3, 2, 10, -1]))

# Sliding window -> Find a range of values according to some logic. 
def sliding_window(s):
    longest_sub = 0
    char_counter = Counter()
    left = 0

    for right in range(len(s)):
        char_right = s[right]
        char_counter[char_right] += 1

    while char_counter[char_right] > 1:
        char_left = s[left]
        char_counter[char_left] -= 1
        left += 1
        longest_sub = max(longest_sub, right - left + 1)
        
    return longest_sub

# Two pointers -> Start two pointers at both extremes of a range, and the close one in at a time depending on logic
def two_pointers(height):
    max_water = 0
        
    left = 0
    right = len(height) - 1

    while left < right:
        lower_edge = min(height[left], height[right])
        max_water = max(max_water, (right - left) * lower_edge)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
        
    return max_water

# Linked lists -> ListNode() that has .next, and sometimes .children and .prev
class Node(object):
    def __init__(self, val = 0, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
def reverse_linked_list(head:Node):
    if not head:
        return None
    
    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

# Binary tree -> TreeNode() that has .left and .right
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_traversal_bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def binary_tree_traversal_dfs(root):
    if not root:
        return []
    
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    
    return result

# Matrix -> 2D array that we use DIRECTIONS (4 or 8) to navigate
def matrix_traversal_bfs(matrix):
    if not matrix or not matrix[0]:
        return []
    
    DIRECTIONS = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    seen = set()
    result = []
    queue = deque([0, 0])

    while queue:
        row, col = queue.popleft()

        result.append((row, col))

        for dr, dc in DIRECTIONS:
            new_row = dr + row
            new_col = dc + col

            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and (new_row, new_col) not in seen:
                queue.append((new_row, new_col))
    
    return result

def matrix_traversal_dfs(matrix):
    if not matrix or not matrix[0]:
        return []
    
    DIRECTIONS = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    seen = set()
    result = []
    
    def dfs(row, col):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (row, col) in seen:
            return
        
        result.append((row, col))
        seen.add((row, col))

        for dr, dc in DIRECTIONS:
            dfs(dr + row, dc + col)
    
    dfs(0, 0)
    return result

# Graphs -> adjacency lists/strange tree nodes that we use to navigate
def graph_traversal_bfs(self, graph):
        if not graph:
            return []
        
        result = []
        queue = deque([0])
        seen = set([0])

        while queue:
            node = queue.popleft()
            result.append(node)
            
            for edge in graph[node]:
                if edge not in seen:
                    queue.append(edge)
                    seen.add(edge)
        
        return result
    
def graph_traversal_dfs(self, graph):
    if not graph:
        return []
        
    def dfs(node, seen, result):
        if node in seen:
            return
            
        result.append(node)
        seen.add(node)

        for edge in graph[node]:
            dfs(edge, seen, result)

    result = []
    seen = set()
    dfs(0, seen, result)
    return result

#Dynamic programming -> useful when a problem has a ton of repeating subproblems
def fibonacci_memo(n):
    memo = {}

    def dp(number):
        if number <= 1:
            return number
        elif number in memo:
            return memo[number]

        memo[number] = dp(number - 1) + dp(number - 2)
        return memo[number]
    
    return dp(n)

def fibonacci_tab(n):
    dp = [0] * (len(n) + 1)
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n - 1]