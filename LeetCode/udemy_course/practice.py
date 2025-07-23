from collections import deque
import random
import heapq
 
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class MinHeap():
    def __init__(self):
        ...

class MaxHeap:
    def __init__(self):
        ...

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for character in word:
            character_idx = ord(character) - ord("a")

            if not node.children[character_idx]:
                node.children[character_idx] = TrieNode()
            
            node = node.children[character_idx]
        
        node.end = True
    
    def search_word(self, word):
        node = self.root

        for character in word:
            character_idx = ord(character) - ord("a")

            if not node.children[character_idx]:
                return False
            
            node = node.children[character_idx]
        
        return node.end

    def search_prefix(self, prefix):
        node = self.root

        for character in prefix:
            character_idx = ord(character) - ord("a")

            if not node.children[character_idx]:
                return False
            
            node = node.children[character_idx]
        
        return True

class Solution:
    """
    1. Arrays ✓ (22/07)
    2. Strings ✓ (22/07)
    3. Linked lists ✓ (23/07)
    4. Binary trees ✓ (23/07)
    5. Tries ✓ (23/07)
    6. Greedy
    7. Matrices
    8. Graphs
    9. Heaps
    10. Bitmask
    11. DP
    12. Backtracking
    13. Prefix sum ✓ (22/07)
    14. Sliding window ✓ (22/07)
    """
    
# print(random.choice([]))
# print(random.choice(["typed-out-strings"]))
# print(random.choice(["quick_sort"]))
# print(random.choice([]))
# print(random.choice(["right-side-view", "count-nodes", "is_valid_bst"]))
# print(random.choice(["orange_rotting", "walls_gates"]))
# print(random.choice(["can_finish", "network_delay_time"]))
# print(random.choice(["subset sum/partition", "grid/pathfinding", "string manipulation", "decision based", "probability and counting", "bitmask"]))

solution = Solution()

print("\nTrie")
trie = Trie()
trie.insert("appls")
print(trie.search_word("apple"))
print(trie.search_prefix("app"))

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