from collections import deque
import random
import heapq
 
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26 #Change to hashmap to decrease space (26 => how ever many letter in the words) and to allow non-alphabetical characters
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for letter in word:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                current_node.children[letter_idx] = TrieNode()
            
            current_node = current_node.children[letter_idx]
        
        current_node.end = True
    
    def search_word(self, word):
        current_node = self.root

        for letter in word:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                return False
            
            current_node = current_node.children[letter_idx]
        
        return current_node.end
    
    def search_prefix(self, prefix):
        current_node = self.root

        for letter in prefix:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                return False
            
            current_node = current_node.children[letter_idx]
        
        return True
    
class MinHeap():
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        self.heap.append(value)
        val_idx = len(self.heap) - 1

        while val_idx > 0:
            parent_idx = self.parent(val_idx)

            if self.heap[parent_idx] > self.heap[val_idx]:
                self.swap(val_idx, parent_idx)
                val_idx = parent_idx
            else:
                break
    
    def extract_minimum(self):
        self.swap(0, len(self.heap) - 1)

        min_value = self.heap.pop()

        root_idx = 0

        while root_idx < len(self.heap) - 1:
            left_child = self.left_child(root_idx)
            right_child = self.right_child(root_idx)
            smallest = root_idx

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
            if smallest == root_idx:
                break

            self.swap(root_idx, smallest)
            root_idx = smallest
        
        return min_value
    
    def peek_minimum(self):
        return self.heap[0] if self.heap else None
    
    def heapify(self, arr):
        self.heap = arr

        def heapify_function(root_idx):
            while root_idx < len(self.heap) - 1:
                left_child = self.left_child(root_idx)
                right_child = self.right_child(root_idx)
                smallest = root_idx

                if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                    smallest = left_child
                if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                    smallest = right_child
                if smallest == root_idx:
                    break

                self.swap(root_idx, smallest)
                root_idx = smallest

        for i in range(self.parent(len(arr) - 1), -1, -1):
            heapify_function(i)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def return_heap(self):
        return [-i for i in self.heap]

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def extract_max(self):
        return -heapq.heappop(self.heap)
    
    def peek_max(self):
        return -self.heap[0] if self.heap else None
    
    def heapify(self, arr):
        self.heap = [-i for i in arr]
        heapq.heapify(self.heap)

class Solution:
    """
    1. Arrays ✓ (07/07)
    2. Strings ✓ (07/07)
    3. Sorts/searches ✓ (07/07)
    4. Linked lists ✓ (07/07)
    5. Binary trees ✓ (07/07)
    6. Tries ✓ (07/07)
    7. Matrices ✓ (07/07)
    8. Stack/queues ✓ (08/07)
    9. Graphs ✓ (08/07)
    10. Heaps ✓ (08/07)
    11. DP
    12. Backtracking

    """
    def two_sum(self, nums, target):
        recorded_nums = {}
        def rec(i):
            if (target - nums[i]) in recorded_nums:
                return [recorded_nums[target - nums[i]], i]
            
            recorded_nums[nums[i]] = i
            return rec(i + 1)
        return rec(0)
    
    def is_palindrome(self, s):
        word = "".join([letter for letter in s if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]).lower()
        
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def linked_list_has_cycle(self, head):
        if not head or not head.next:
            return False
        
        visited_nodes = set()
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next

    def binary_tree_bfs(self, root):
        if not root:
            return []
        
        queue = deque([root])
        tree = []

        while queue:
            current_node = queue.popleft()
            tree.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return tree
    
    def binary_tree_dfs(self, root, dfs_type):
        tree = []

        def dfs(node):
            if not node:
                return
            
            if dfs_type == "preorder":
                tree.append(node.val)
                dfs(node.left)
                dfs(node.right)
            elif dfs_type == "inorder":
                dfs(node.left)
                tree.append(node.val)
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)
                tree.append(node.val)
            
        dfs(root)
        return tree
    
    def matrix_bfs(self, matrix):
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        if not matrix or not matrix[0]:
            return []

        result = []
        queue = deque([(0,0)])
        seen = set([(0, 0)])

        while queue:
            row, col = queue.popleft()
            result.append(matrix[row][col])

            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc

                if new_row >= 0 and new_row < len(matrix) and new_col >= 0 and new_col < len(matrix[0]) and (new_row, new_col) not in seen:
                    queue.append((new_row, new_col))
                    seen.add((new_row, new_col))
        
        return result

    def matrix_dfs(self, matrix):
        DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        if not matrix or not matrix[0]:
            return []

        result = []
        seen = set()

        def dfs(row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (row, col) in seen:
                return
            
            result.append(matrix[row][col])
            seen.add((row, col))

            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc
                dfs(new_row, new_col)

        dfs(0, 0)
        return result
    
    def valid_parentheses(self, s):
        mappings = {"{":"}", "(":")", "[":"]"}
        stack = []

        for bracket in s:
            if bracket in mappings.keys():
                stack.append(bracket)
            elif stack:
                open_bracket = stack.pop()

                if bracket != mappings[open_bracket]:
                    return False
            else:
                return False
        
        return len(stack) == 0
    
    def graph_bfs(self, graph):
        if not graph:
            return []
        
        tree = []
        seen = set([0])
        queue = deque([0])

        while queue:
            node = queue.popleft()
            tree.append(node)

            for edge in graph[node]:
                if edge not in seen:
                    queue.append(edge)
                    seen.add(edge)
        
        return tree
            
    
    def graph_dfs(self, graph):
        if not graph:
            return []
        
        tree = []
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            tree.append(node)
            seen.add(node)

            for edge in graph[node]:
                dfs(edge)

        dfs(0)
        return tree
    
    def fibonacci_sequence_memo(self, n):
        memo = {}

        def rec(i):
            if i < 2:
                return i
            elif i in memo:
                return memo[i]
            
            memo[i] = rec(i - 1) + rec(i - 2)
            return memo[i]

        return rec(n)
    
    def fibonacci_sequence_tabular(self, n):
        dp = {}
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
# print(random.choice(["container-with-most-water", "trapping-rainwater"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating", "is_almost_palindrome"]))
# print(random.choice(["quick_sort", "binary_search"]))
# print(random.choice(["reverse_partial_linked_list", "flatten_double_linked_list"]))
# print(random.choice(["max-depth", "level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["num_islands", "orange_rotting", "walls_gates"]))

solution = Solution()

print(solution.two_sum([3,2,4], 6))

print(solution.is_palindrome("A man, a plan, a canal: Panama"))

head = ListNode(3)
node_1 = ListNode(2)
node_2 = ListNode(0)
node_3 = ListNode(-4)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_1
print(solution.linked_list_has_cycle(head))

root = TreeNode(1)
tree_node_2 = TreeNode(2)
tree_node_3 = TreeNode(3)
tree_node_4 = TreeNode(4)
tree_node_5 = TreeNode(5)
tree_node_6 = TreeNode(6)
root.left = tree_node_2
root.right = tree_node_3
tree_node_2.left = tree_node_4
tree_node_2.right = tree_node_5
tree_node_3.left = tree_node_6
print(solution.binary_tree_bfs(root))
print("/// dfs ///")
print(solution.binary_tree_dfs(root, "preorder"))
print(solution.binary_tree_dfs(root, "inorder"))
print(solution.binary_tree_dfs(root, "postorder"))

trie = Trie()
trie.insert("appls")
print(trie.search_word("apple"))
print(trie.search_prefix("app"))

print(solution.matrix_bfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))
print(solution.matrix_dfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))

graph = {
    0: [1, 3],
    1: [0],
    2: [3, 8],
    3: [0, 4, 5, 2],
    4: [3, 6],
    5: [3],
    6: [4, 7],
    7: [6],
    8: [2]
}
print(solution.graph_bfs(graph))
print(solution.graph_dfs(graph))

min_heap = MinHeap()
min_heap.insert(0)
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(9)
print(min_heap.heap)
min_heap.extract_minimum()
print(min_heap.heap)
min_heap.heapify([0, 10, 5, 3, 7, 9])
print(min_heap.heap)

max_heap = MaxHeap()
max_heap.insert(0)
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(7)
max_heap.insert(9)
print(max_heap.return_heap())
max_heap.extract_max()
print(max_heap.return_heap())
max_heap.heapify([0, 10, 5, 3, 7, 9])
print(max_heap.return_heap())

print(solution.fibonacci_sequence_memo(4))
print(solution.fibonacci_sequence_tabular(4))