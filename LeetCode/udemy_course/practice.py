from collections import deque
import random
import heapq
 
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.end = True

    def search_word(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return node.end

    def search_prefix(self, prefix):
        node = self.root

        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return True

class MinHeap():
    def __init__(self):
        ...

class MaxHeap:
    def __init__(self):
        ...

class Solution:
    """
    1. Arrays ✓ (14/07)
    2. Strings ✓ (14/07)
    3. Sorts/searches ✓ (14/07)
    4. Linked lists ✓ (15/07)
    5. Binary trees ✓ (15/07)
    6. Tries ✓ (15/07)
    7. Greedy ✓ (16/07)
    7. Matrices ✓ (16/07)
    8. Stack/queues ✓ (16/07)
    9. Graphs
    10. Heaps
    11. DP
    12. Backtracking

    """

    def num_of_minutes(self, n, headID, manager, informTime):
        graph = {i: [] for i in range(n)}
        for i in range(len(manager)):
            if manager[i]!= -1:
                graph[manager[i]].append(i)

        def dfs(employee_id):
            if not graph[employee_id]:
                return 0
            
            return max([dfs(edge) for edge in graph[employee_id]]) + informTime[employee_id]
        
        return dfs(headID)

    
# print(random.choice(["container-with-most-water"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating"]))
# print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list"]))
# print(random.choice(["level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["orange_rotting", "walls_gates"]))
print(random.choice(["can_finish", "network_delay_time"]))

solution = Solution()

print("Arrays")

print("\nStrings")

print("\nSorts/searches")

print("\nLinked lists")
# new_head = solution.flatten_doubly_linked_list(head)
# results = []
# while new_head:
#     results.append(new_head.val)
#     new_head = new_head.next
# print(results)

print("\nBinary tree")
root = TreeNode(3)
tree_node_2 = TreeNode(9)
tree_node_3 = TreeNode(20)
tree_node_4 = TreeNode(15)
tree_node_5 = TreeNode(7)
root.left = tree_node_2
root.right = tree_node_3
tree_node_3.left = tree_node_4
tree_node_3.right = tree_node_5

print("\nTrie")
trie = Trie()
trie.insert("appls")
print(trie.search_word("apple"))
print(trie.search_prefix("app"))

print("\nMatrix")
matrix = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# print(solution.num_islands(matrix))

print("\nStack")

print("\nGraph")
print(solution.num_of_minutes(7, 0, [-1,0,0,0,3,3,5], [1,0,0,2,0,3,0]))

print("\nHeaps")
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
# min_heap.heapify([0, 10, 5, 3, 7, 9])
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

print("\nDP")

print("\nBacktracking")