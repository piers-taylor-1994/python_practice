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
    3. Sorts/searches
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
    def trapping_rainwater(self, height):
        """Starting from 1 and ending before len - 1, calculate the max of left/right then use the minimum against the current value"""
        height_length = len(height)

        minimum_heights_hash = {i: [None, None] for i in range(0, height_length)}

        max_left = 0
        for i in range(0, height_length):
            if height[i] > max_left:
                max_left = height[i]
            
            minimum_heights_hash[i][0] = max_left
        
        max_right = 0
        for j in range(height_length - 1, -1, -1):
            if height[j] > max_right:
                max_right = height[j]
            
            minimum_heights_hash[j][1] = max_right
 
        collected_rainfall = 0

        for i in range(1, height_length - 1):
            min_height = min(minimum_heights_hash[i])

            if min_height - height[i] > 0:
                collected_rainfall += min_height - height[i]
        
        return collected_rainfall
    
    def is_almost_palindrome(self, s):
        def rec(left, right, skipped):
            if left >= right:
                return True
            if s[left] != s[right] and skipped:
                return False
            if s[left] == s[right]:
                return rec(left + 1, right - 1, skipped)
            
            if rec(left + 1, right, True) or rec(left, right - 1, True):
                return True
            return False
        
        return rec(0, len(s) - 1, False)
    
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] < target:
                left = middle + 1
            elif arr[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
    
# print(random.choice(["container-with-most-water"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating"]))
print(random.choice(["quick_sort"]))
# print(random.choice(["reverse_partial_linked_list", "flatten_double_linked_list"]))
# print(random.choice(["max-depth", "level-order", "right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["num_islands", "orange_rotting", "walls_gates"]))

solution = Solution()

print("Arrays")
print(solution.trapping_rainwater([4,2,0,3,2,5]))

print("\nStrings")
print(solution.is_almost_palindrome("abc"))

print("\nSorts/searches")
print(solution.binary_search([1,2,3,5,7,8,9,19,50,108], 19))

print("\nLinked lists")

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