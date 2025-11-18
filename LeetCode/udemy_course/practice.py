from collections import Counter, defaultdict, deque
import decimal
import math
from operator import indexOf
import random
import heapq
import bisect
 
class Node(object):
    def __init__(self, val = 0, prev = None, next = None, child = None):
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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = []

        for i in range(len(nums)):
            target_num = target - nums[i]

            if target_num in seen_nums:
                return [indexOf(seen_nums, target_num), i]
            
            seen_nums.append(nums[i])
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        lowest_value = float('inf')

        for price in prices:
            if price < lowest_value:
                lowest_value = price
            else:
                max_profit = max(max_profit, price - lowest_value)
        
        return max_profit
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_hash = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            
            anagram_hash[sorted_word] = anagram_hash.get(sorted_word, []) + [word]
        
        return [word_array for _, word_array in anagram_hash.items()]
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_hash = {i:set() for i in range(9)}
        col_hash = {i:set() for i in range(9)}
        grid_hash = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                grid_hash[(row // 3, col // 3)] = set()

        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]

                if value == ".":
                    continue

                grid_id = (row // 3, col // 3)

                if value in row_hash[row] or value in col_hash[col] or value in grid_hash[grid_id]:
                    return False
                
                row_hash[row].add(value)
                col_hash[col].add(value)
                grid_hash[grid_id].add(value)
        
        return True
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0
        hash_map = { prefix: 1 }
        result = 0

        for num in nums:
            prefix += num
            result += hash_map.get(prefix - k, 0)
            hash_map[prefix] = hash_map.get(prefix, 0) + 1
        
        return result
    
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        nums = list(nums_set)
        nums.sort()
        current_num = 0
        current_range = 0
        longest_range = 0

        for num in nums:
            if num - current_num == 1:
                current_range += 1
            else:
                current_range = 1

            longest_range = max(longest_range, current_range)
            current_num = num

        return longest_range
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])

        results = [intervals[0]]
        current_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
                results[-1][1] = current_end
            else:
                results.append([start,end])
                current_end = end
        
        return results
    
    def min_meeting_rooms(self, intervals):
        intervals.sort(key=lambda x:(x[0], x[1]))

        if not intervals:
            return 0

        rooms_booked_end = [intervals[0][1]]
        heapq.heapify(rooms_booked_end)

        for start, end in intervals[1:]:
            if start >= rooms_booked_end[0]:
                heapq.heappop(rooms_booked_end)
            
            heapq.heappush(rooms_booked_end, end)
        
        return len(rooms_booked_end)
    
    def search_rotated_array(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_target(is_left):
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] == target:
                    result = middle

                    if is_left:
                        right = middle - 1
                    else:
                        left = middle + 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            
            return result
        
        return [find_target(True), find_target(False)]
    
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        current_node = head
        prev = None

        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        
        return prev
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = Node()
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list2 if not list1 else list1
        return head.next
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        current_node = head
        tracked_nodes = set([current_node])

        while current_node:
            next = current_node.next

            if next in tracked_nodes:
                return True
            
            tracked_nodes.add(next)
            current_node = next
        
        return False
    
    def hasCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = l1
        num1 = ""
        while current_node:
            num1 += str(current_node.val)
            current_node = current_node.next
        
        num2 = ""
        current_node = l2
        while current_node:
            num2 += str(current_node.val)
            current_node = current_node.next
        
        result = (str(int(num1[::-1]) + int(num2[::-1])))[::-1]

        head = Node(int(result[0]))
        current_node = head

        for num in result[1:]:
            current_node.next = Node(int(num))
            current_node = current_node.next
        
        return head
    
    def addTwoNumbers_v2(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(node):
            prev = None

            while node:
                node_next = node.next
                node.next = prev
                prev = node
                node = node_next
            
            return prev
        
        head = Node()
        tail = head
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry
            carry = total // 10
            tail.next = Node(total % 10)
            
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
    
    def clean_json_list(self, arr):
        result = []

        for item in arr:
            if isinstance(item, list):
                arr += self.clean_json_list(item)
            elif item not in ("", {}):
                result.append(item)
        
        return result
    
    def clean_json_dict(self, json):
        if isinstance(json, dict):
            return {k:self.clean_json_dict(v) for k, v in json.items() if v not in ("", None, {})}
        elif isinstance(json, list):
            return [self.clean_json_dict(v) for v in json if v not in ("", None, {})]
        else:
            return json
        
    def levelOrder_BFS(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_order = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level_order.append(node.val)
            
            result.append(level_order)
        
        return result
        
    def levelOrder_DFS(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []

        def dfs(node, level):
            if not node:
                return

            if len(result) >= level + 1:
                result[level].append(node.val)
            else:
                result.append([node.val])
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result
    
    def isValidBST_BFS(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([(
            -float('inf'),
             root, 
             float('inf')
             )])

        while queue:
            min_val, node, max_val = queue.popleft()
            
            if not min_val < node.val < max_val:
                return False
            
            if node.left:
                queue.append((min_val, node.left, node.val))
            if node.right:
                queue.append((node.val, node.right, max_val))
        
        return True
    
    def isValidBST_DFS(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        result = True

        def dfs(min_val, node, max_val):
            nonlocal result
            if not node:
                return
            elif not min_val < node.val < max_val:
                result = False
                return
            
            if node.left:
                dfs(min_val, node.left, node.val)
            if node.right:
                dfs(node.val, node.right, max_val)
        
        dfs(-float('inf'), root, float('inf'))
        return result
    
    def numIslands_BFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        seen = set()
        islands_count = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            seen.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    new_row = dr + row
                    new_col = dc + col

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1" and (new_row, new_col) not in seen:
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    islands_count += 1
                    bfs(i, j)
        
        return islands_count
    
    def numIslands_DFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        seen = set()
        islands_count = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1" or (r, c) in seen:
                return
            
            seen.add((r, c))

            for dr, dc in DIRECTIONS:
                dfs(dr + r, dc + c)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    islands_count += 1
                    dfs(i, j)
        
        return islands_count
    
    def clone_graph_BFS(self, node):
        if not node:
            return None

        node_to_clone = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()

            for neigh in current_node.neighbors:
                if neigh not in node_to_clone:
                    node_to_clone[neigh] = Node(neigh.val)
                    queue.append(neigh)
                
                node_to_clone[current_node].neighbors.append(node_to_clone[neigh])
        
        return node_to_clone[node]

    def clone_graph_DFS(self, node):
        if not node:
            return None

        node_to_clone = {node: Node(node.val)}
        
        def dfs(current_node):
            for neigh in current_node.neighbors:
                if neigh not in node_to_clone:
                    node_to_clone[neigh] = Node(neigh.val)
                    dfs(neigh)
                
                node_to_clone[current_node].neighbors.append(node_to_clone[neigh])
        
        dfs(node)
        
        return node_to_clone[node]
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}

        for course, courseRequired in prerequisites:
            graph[courseRequired].append(course)
        
        for i in range(numCourses):
            seen = set([i])
            queue = deque(graph[i])

            while queue:
                node = queue.popleft()
                
                for edge in graph[node]:
                    if edge == i:
                        return False
                    elif edge not in seen:
                        queue.append(edge)
                        seen.add(edge)
        
        return True
    
    def shortestPathBinaryMatrix_BFS(self, grid):
        DIRECTIONS = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]

        if not grid or not grid[0]:
            return -1
        
        target = (len(grid) - 1, len(grid[0]) - 1)
        seen = set()
        queue = deque([(0,0)])
        moves = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if (row, col) == target:
                    return moves
                
                for dr, dc in DIRECTIONS:
                    new_row = dr + row
                    new_col = dc + col
                    
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0 and (new_row, new_col) not in seen:
                        queue.append((new_row, new_col))
            
            moves += 1
        
        return -1
    
    def shortestPathBinaryMatrix_DFS(self, grid):
        DIRECTIONS = [
            (1, 1),
            (0, 1),
            (1, 0),
            (-1, 0),
            (-1, 1),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]

        if not grid or not grid[0] or grid[0][0] != 0:
            return -1
        
        target = (len(grid) - 1, len(grid[0]) - 1)
        seen = set()
        
        def dfs(row, col, moves):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 1 or (row, col) in seen:
                return float('inf')
            elif (row, col) == target:
                return moves
            
            seen.add((row, col))
            
            return min([dfs(dr + row, dc + col, moves + 1) for dr, dc in DIRECTIONS])

        result = dfs(0, 0, 1)
        return result if result != float('inf') else -1
    
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        pacific_valid = set()
        atlantic_valid = set()

        def dfs(row, col, prev_height, group):
            if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]) or prev_height > heights[row][col] or (row, col) in group:
                return
            
            group.add((row, col))
            
            for dr, dc in DIRECTIONS:
                dfs(dr + row, dc + col, heights[row][col], group)

        max_row = len(heights)
        max_col = len(heights[0])
        
        for i in range(max_row):
            dfs(i, 0, -float('inf'), pacific_valid)
            dfs(i, max_col - 1, -float('inf'), atlantic_valid)
        for j in range(max_col):
            dfs(0, j, -float('inf'), pacific_valid)
            dfs(max_row - 1, j, -float('inf'), atlantic_valid)
                        
        return list(pacific_valid & atlantic_valid)
    
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        pacific_valid = set()
        atlantic_valid = set()

        def dfs(row, col, prev_height, group):
            if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]) or prev_height > heights[row][col] or (row, col) in group:
                return
            
            group.add((row, col))
            
            for dr, dc in DIRECTIONS:
                dfs(dr + row, dc + col, heights[row][col], group)

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 or j == 0: #pacific
                    dfs(i, j, -float('inf'), pacific_valid)
                if i == len(heights) - 1 or j == len(heights[0]) - 1: #atlantic
                    dfs(i, j, -float('inf'), atlantic_valid)

        return list(pacific_valid & atlantic_valid)
    
    def climbingStairs(self, n):
        memo = {}
        def rec(step):
            if step == 0:
                return 1
            elif step < 0:
                return 0
            elif step in memo:
                return memo[step]

            memo[step] = rec(step - 1) + rec(step - 2)
            return memo[step]

        return rec(n)
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        memo = {}
        
        def rec(current_amount):
            if current_amount == 0:
                return 0
            elif current_amount < 0:
                return float('inf')
            elif current_amount in memo:
                return memo[current_amount]
            
            memo[current_amount] = min([rec(current_amount - coin) for coin in coins]) + 1
            return memo[current_amount]
        
        result = rec(amount)
        return result if result != float('inf') else -1
                    
solution = Solution()

# print(solution.twoSum([2,7,11,15], 9))

# print(solution.maxProfit([7,1,5,3,6,4]))

# print(solution.lengthOfLongestSubstring("pwwkew"))

# print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

# print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

# print(solution.subarraySum([1,1,1], 2))

# print(solution.longestConsecutive([1,1,0,2]))
# print(solution.longestConsecutive([100, 0, 200, 1, 2, 3]))

# print(solution.merge([[1,3], [2,6], [8,10], [15,18]]))

# print(solution.min_meeting_rooms([(0,40), (5,10), (15,20)]))
# print(solution.min_meeting_rooms([(4,9)]))
# print(solution.min_meeting_rooms([]))

# print(solution.search_rotated_array([4,5,6,7,0,1,2,3], 4))

# print(solution.searchRange([5,7,7,8,8,10], 8))

# head = Node(1)
# node_1 = Node(2)
# node_2 = Node(3)
# node_3 = Node(4)
# node_4 = Node(5)
# head.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# solution.reverseList(head)

# head2 = Node(1)
# node_5 = Node(3)
# node_6 = Node(4)
# head2.next = node_5
# node_5.next = node_6
# solution.mergeTwoLists(head, head2)

# print(solution.clean_json_dict({
#     "user": {
#         "name": "Alice",
#         "age": None,
#         "emails": [None, "alice@example.com", ""],
#         "address": {
#             "city": "London",
#             "postcode": None
#         }
#     },
#     "active": True,
#     "metadata": {}
# }))
# print(solution.clean_json_list(["", "hello", 5, 10, {}, [1,2, ""]]))

# root = TreeNode(1)
# treeNode_1 = TreeNode(2)
# treeNode_2 = TreeNode(3)
# treeNode_3 = TreeNode(4)
# treeNode_4 = TreeNode(5)
# root.left = treeNode_1
# root.right = treeNode_2
# treeNode_1.left = treeNode_3
# treeNode_1.right = treeNode_4
# print(solution.levelOrder(root))

# root = TreeNode(5)
# treeNode_1 = TreeNode(1)
# treeNode_4 = TreeNode(4)
# treeNode_3 = TreeNode(3)
# treeNode_6 = TreeNode(6)
# root.left = treeNode_1
# root.right = treeNode_4
# treeNode_4.left = treeNode_3
# treeNode_4.right = treeNode_6
# print(solution.isValidBST_BFS(root))

# class GraphNode(object):
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# print(solution.clone_graph_BFS([[2,4], [1,3], [2,4], [1,3]]))

# print(solution.canFinish(2, [[0, 1], [1, 0]]))

# print(solution.shortestPathBinaryMatrix_DFS([[0,1],[1,0]]))

print(solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))




















# print(random.choice([]))
# print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice([]))
# print(random.choice(["right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["walls_gates"]))
# print(random.choice(["network_delay_time"]))

#"subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"
# print(random.choice(["subset sum/partition", "string manipulation", "decision based", "probability and counting", "bitmask"]))

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