from collections import Counter, defaultdict, deque
import math
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
    def mergeKLists(self, lists:list):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or all(node is None for node in lists):
            return None

        min_heap = []
        counter = 1

        for node in lists:
            current_node = node

            while current_node:
                heapq.heappush(min_heap, (current_node.val, counter, current_node))
                current_node = current_node.next
                counter += 1

        _, _, head = heapq.heappop(min_heap)
        current_node = head
        while min_heap:
            _, _, next_node = heapq.heappop(min_heap)
            current_node.next = next_node
            current_node = next_node
        
        return head
    
class MedianFinder(object):
    def __init__(self):
        self.heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.heap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        heap_length = len(self.heap)
        heap_copy = self.heap[:]
        
        #even
        if heap_length % 2 == 0:
            idx_1 = int((heap_length / 2) - 1)
            idx_2 = int(idx_1 + 1)

            num_1 = 0
            num_2 = 0

            for i in range(idx_2 + 1):
                if i == idx_1:
                    num_1 = heapq.heappop(heap_copy)
                elif i == idx_2:
                    num_2 = heapq.heappop(heap_copy)
                else:
                    heapq.heappop(heap_copy)
            
            return (num_1 + num_2) / 2.0 
        #odd
        else:
            middle_value = 0
            target_position = heap_length // 2
            
            for _ in range(target_position + 1):
                middle_value = heapq.heappop(heap_copy)
            
            return middle_value

solution = Solution()

medianFinder = MedianFinder()
medianFinder.addNum(-1)
print(medianFinder.findMedian())
medianFinder.addNum(-2)
print(medianFinder.findMedian())
medianFinder.addNum(-3)
print(medianFinder.findMedian())
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())

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