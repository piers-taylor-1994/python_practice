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
    def flatten_doubly_linked_list(self, head):
        if not head:
            return None
        
        current = head

        def rec(node):
            if not node:
                return
            
            if node.child:
                child = node.child
                next = node.next

                child.prev = node
                node.next = child

                if next:
                    while child.next:
                        child = child.next
                    child.next = next
                    next.prev = child

                node.child = None
            
            rec(node.next)
            
        rec(current)
        
        return head
    
# print(random.choice(["container-with-most-water"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating"]))
# print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list"]))
# print(random.choice(["max-depth", "level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["num_islands", "orange_rotting", "walls_gates"]))

solution = Solution()

print("Arrays")

print("\nStrings")

print("\nSorts/searches")

print("\nLinked lists")
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node3.child = node7
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node7.next = node8
node8.prev = node7
node8.next = node9
node8.child = node11
node9.prev = node8
node9.next = node10
node10.prev = node9
node11.next = node12
node12.prev = node11
new_head = solution.flatten_doubly_linked_list(head)
results = []
while new_head:
    results.append(new_head.val)
    new_head = new_head.next
print(results)

print("\nBinary tree")
# root = TreeNode(1)
# tree_node_2 = TreeNode(2)
# tree_node_3 = TreeNode(3)
# tree_node_4 = TreeNode(4)
# tree_node_5 = TreeNode(5)
# tree_node_6 = TreeNode(6)
# root.left = tree_node_2
# root.right = tree_node_3
# tree_node_2.left = tree_node_4
# tree_node_2.right = tree_node_5
# tree_node_3.left = tree_node_6

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