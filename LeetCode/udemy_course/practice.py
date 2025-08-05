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
    def __init__(self):
        self.DIRECTIONS = [
            (-1, 0), #up
            (0, 1), #right
            (1, 0), #down
            (0, -1) #left
        ]

        self.DIRECTIONS_2 = [
            (1, 1), #down-right
            (0, 1), #right
            (1, 0), #down
        ]

    def num_islands(self, matrix):
        def dfs(row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == "0":
                return
            
            matrix[row][col] = "0"

            for dr, dc in self.DIRECTIONS:
                dfs(dr + row, dc + col)

        num_islands = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
    
    def largest_island(self, matrix):
        largest_island = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            island_total = 0

            while queue:
                r, c = queue.popleft()

                matrix[r][c] = 0
                island_total += 1

                for dr, dc in self.DIRECTIONS:
                    new_row = dr + r
                    new_col = dc + c

                    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
            
            return island_total
                

        def dfs(row, col):
            nonlocal total
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == 0:
                return
            
            total += 1
            matrix[row][col] = 0

            [dfs(dr + row, dc + col) for dr, dc in self.DIRECTIONS]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    largest_island = max(largest_island, bfs(i, j))
                    total = 0
                    # dfs(i, j)
                    # largest_island = max(largest_island, total)
        
        return largest_island

    #0 - empty 1 - orange 2 - rotten
    def rotten_oranges(self, matrix):
        rotten_oranges = []
        oranges = 0

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                item = matrix[i][j]

                if item == 2:
                    rotten_oranges.append((i, j))
                elif item == 1:
                    oranges += 1
        
        if not rotten_oranges:
            return 0

        queue = deque(rotten_oranges)
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in self.DIRECTIONS:
                    new_row = dr + row
                    new_col = dc + col

                    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1:
                        oranges -= 1
                        matrix[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            
            minutes += 1
        
        return minutes if oranges == 0 else -1


    #0 - open 1 - blocked (can use diagonal!)
    def shortest_path_bfs(self, matrix):
        target = (len(matrix) - 1, len(matrix[0]) - 1)
        shortest_path = 0

        queue = deque([(0, 0)])
        seen = set([(0, 0)])        

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in self.DIRECTIONS_2:
                    new_row = dr + row
                    new_col = dc + col

                    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and (new_row, new_col) not in seen and matrix[new_row][new_col] == 0:
                        if (new_row, new_col) == target:
                            return shortest_path + 1
                        
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))

            shortest_path += 1

    #0 - open 1 - blocked (can use diagonal!)
    def shortest_path_dfs(self, matrix):
        target = (len(matrix) - 1, len(matrix[0]) - 1)

        def dfs(row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == 1:
                return float('inf')
            if (row, col) == target:
                return 0
            
            matrix[row][col] = 1

            return 1 + min([dfs(dr + row, dc + col) for dr, dc in self.DIRECTIONS_2])
        
        return dfs(0, 0)

    
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

print(solution.num_islands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))

print(solution.largest_island([
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
)) #-> 6

print(solution.rotten_oranges([
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
)) #-> 4

print(solution.shortest_path_bfs([
    [0,1],
    [1,0]])) #->1
print(solution.shortest_path_bfs([
  [0,0,0],
  [1,1,0],
  [1,1,0]])) #-> 4
print(solution.shortest_path_dfs([
    [0,1],
    [1,0]])) #->1
print(solution.shortest_path_dfs([
  [0,0,0],
  [1,1,0],
  [1,1,0]])) #-> 4

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