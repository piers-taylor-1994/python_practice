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
        ...
class Trie:
    def __init__(self):        ...

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
    # target=7 nums=[2,3,1,2,4,3] => 2 (4[4], 3[5])
    def minimum_size_subarray_sum(self, target, nums):
        minimum_window_range = float('inf')
        current_window_total = 0
        left = 0

        for right in range(len(nums)):
            current_window_total += nums[right]

            while current_window_total >= target:
                minimum_window_range = min(minimum_window_range, right - left + 1)

                current_window_total -= nums[left]
                left += 1
        
        return minimum_window_range
    
    def longest_substring_k_distinct_chars(self, s, k):
        current_chars = {}
        longest_substring_length = 0
        left = 0

        for right in range(len(s)):
            right_char = s[right]
            current_chars[right_char] = current_chars.get(right_char, 0) + 1

            if len(current_chars) <= k:
                longest_substring_length = max(longest_substring_length, right - left + 1)
            
            while len(current_chars) > k:
                left_char = s[left]
                current_chars[left_char] -= 1
                if current_chars[left_char] == 0:
                    del current_chars[left_char]
                left += 1
        
        return longest_substring_length
    
    def jump_game_2(self, nums):
        target = len(nums) - 1
        queue = deque([0])
        jumps = -1

        if target == 0:
            return 0

        while queue:
            jumps += 1
            for _ in range(len(queue)):
                position = queue.popleft()
                if position == target:
                    return jumps
                
                queue += [position + i for i in range(nums[position], 0, -1)]
        
        return jumps
    
    def jump_game_2_2(self, nums):
        target = len(nums) - 1
        jumps_map = {0:0} #index = jumps

        for position in range(len(nums)):
            if target in jumps_map:
                break

            if position not in jumps_map:
                continue
            else:
                for jump in range(1, nums[position] + 1):
                    new_position = position + jump
                    
                    if new_position not in jumps_map:
                        jumps_map[new_position] = jumps_map[position] + 1
        
        return jumps_map[target]
            
    def max_events_can_attend(self, events):
        sorted_events = sorted(events, key=lambda x:(x[1] - x[0], x[0]))
        attended_events = set()
        events = 0

        for start, end in sorted_events:
            if start not in attended_events:
                attended_events = attended_events.union(set([day for day in range(start, end)]))
                events += 1
        
        return events
    
    def sliding_window_max(self, nums, k):
        window = nums[:k]
        current_max = max(window)
        results = [current_max]

        for i in range(1, len(nums) - k + 1):
            dropped_value = window.pop(0)
            new_value = nums[i + k - 1]
            window.append(new_value)

            if new_value > current_max:
                results.append(new_value)
                current_max = new_value
            elif dropped_value != current_max:
                results.append(current_max)
            else:
                results.append(max(window))
        
        return results
    
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

print(solution.minimum_size_subarray_sum(7, [2,3,1,2,4,3]))

print(solution.longest_substring_k_distinct_chars("eceba", 2))

print(solution.jump_game_2([2,3,1,1,4]))
print(solution.jump_game_2([2,0,1,3,1,1,4]))
print(solution.jump_game_2_2([2,3,1,1,4]))
print(solution.jump_game_2_2([2,0,1,3,1,1,4]))

# print(solution.max_events_can_attend([[1,5], [1,2], [2,3], [3,4]]))

# print(solution.sliding_window_max([1,3,-1,-3,5,3,6,7], 3))

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