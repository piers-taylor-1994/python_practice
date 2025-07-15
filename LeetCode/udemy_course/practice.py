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
        ...

class Trie:
    def __init__(self):
        ...
    
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
    4. Linked lists
    5. Binary trees
    6. Tries
    7. Matrices
    8. Stack/queues
    9. Graphs
    10. Heaps
    11. DP
    12. Backtracking

    """
    def max_depth(self, root):
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            depth += 1
        
        return depth
    
# print(random.choice(["container-with-most-water"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating"]))
# print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list"]))
# print(random.choice(["level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["num_islands", "orange_rotting", "walls_gates"]))

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
print(solution.max_depth(root))

print("\nTrie")
# trie = Trie()
# trie.insert("appls")
# print(trie.search_word("apple"))
# print(trie.search_prefix("app"))

print("\nMatrix")
# matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

print("\nGraph")
# graph = {
#     0: [1, 3],
#     1: [0],
#     2: [3, 8],
#     3: [0, 4, 5, 2],
#     4: [3, 6],
#     5: [3],
#     6: [4, 7],
#     7: [6],
#     8: [2]
# }

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