from collections import Counter, defaultdict, deque
import decimal
import math
from operator import indexOf
import random
import heapq
import bisect

from numpy import kaiser
 
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
    def reverse_string(self, s):
        new_string = ""

        for letter in s[::-1]:
            new_string += letter
        
        return new_string
    
    def check_balanced_brackets(self, s):
        brackets = { "(":")", "{":"}", "[":"]" }
        stack = []

        for letter in s:
            if letter in brackets or letter in brackets.values():
                if letter in brackets:
                    stack.append(letter)
                elif not stack or brackets[stack.pop()] != letter:
                    return False
        
        return len(stack) == 0
    
    def find_longest_word(self, s):
        s_array = s.split(" ")
        longest_word = s_array[0]

        for word in s_array[1:]:
            if len(word) > len(longest_word):
                longest_word = word
        
        return longest_word
    

    def factiorial(self, n):
        def rec(number):
            if number == 1:
                return 1
            
            return number * rec(number - 1)
        
        return rec(n)
    
    def sum_prime_numbers(self, n):
        def is_prime(number):
            if number < 2:
                return False
            
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True 
        
        return sum([i for i in range(2, n) if is_prime(i)])
    
    def activity_selections(self, activities):
        activities.sort(key=lambda x:x[1])

        activities_taken = 0
        current_end = -float('inf')

        for start, end in activities:
            if start >= current_end:
                activities_taken += 1
                current_end = end
        
        return activities_taken
    
    def coin_change(self, coins, amount):
        memo = {}

        def rec(current_amount):
            if current_amount == amount:
                return 0
            elif current_amount > amount:
                return float('inf')
            elif current_amount in memo:
                return memo[current_amount]
            
            memo[current_amount] = min([1 + rec(current_amount + coin) for coin in coins])
            return memo[current_amount]
        
        result = rec(0)
        return result if result != float('inf') else -1



                    
solution = Solution()

print(solution.reverse_string("helllo"))

print(solution.check_balanced_brackets("(a + b)*(c + d)"))
print(solution.check_balanced_brackets("((a + b)"))

print(solution.find_longest_word("The quick brown fox jumped over the lazy dog"))

print(solution.sum_prime_numbers(10))

print(solution.factiorial(5))

print(solution.activity_selections([(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))

print(solution.coin_change([1,2,5], 11))

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