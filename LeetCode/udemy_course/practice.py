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
    def subarrays_equal_k(self, nums, k):
        prefix = 0
        subarray_count = {prefix: 1}
        total = 0

        for num in nums:
            prefix += num
            total += subarray_count.get(prefix - k, 0)
            subarray_count[prefix] = subarray_count.get(prefix, 0) + 1
        
        return total
    
    def minimum_size_subarray_sum(self, target, nums):
        window_total = 0
        window_range = 0
        left = 0

        for right in range(len(nums)):
            window_total += nums[right]

            while left <= right and window_total >= target:
                current_range = right - left + 1

                if window_range == 0 or current_range < window_range:
                    window_range = current_range
                
                window_total -= nums[left]
                left += 1
        
        return window_range
    
    def binary_tree_paths_dfs(self, root):
        if not root:
            return []
        
        results = []

        def dfs(node, current_path):
            if not node.left and not node.right:
                results.append(current_path + [node.val])
                return
            
            if node.left:
                dfs(node.left, current_path + [node.val])
            if node.right:
                dfs(node.right, current_path + [node.val])
        
        dfs(root, [])
        return results
    
    def binary_tree_paths_bfs(self, root):
        if not root:
            return []
        
        results = []
        queue = deque()

        if root.left:
            queue.append((root.left, [root.val]))
        if root.right:
            queue.append((root.right, [root.val]))
        
        while queue:
            node, path = queue.popleft()

            if not node.left and not node.right:
                results.append(path + [node.val])
            else:
                if node.left:
                    queue.append((node.left, path + [node.val]))
                if node.right:
                    queue.append((node.right, path + [node.val]))
        
        return results
    
    def partition_labels(self, s):
        s_count = Counter(s)
        current_letters = set()
        results = []

        for i in range(len(s)):
            if s[i] not in current_letters:
                current_letters.add(s[i])
            
            s_count[s[i]] -= 1

            if s_count[s[i]] == 0:
                current_letters.remove(s[i])

            if not current_letters:
                results.append(i - sum(results) + 1)
        
        return results
    
    def find_right_interval(self, intervals):
        results = []

        for interval in intervals:
            right_interval = bisect.bisect_right(intervals, interval)

            if right_interval == len(intervals):
                results.append(-1)
            else:
                results.append(right_interval)
        
        return results
    
    def combination_sum_2(self, candidates, target):
        candidates.sort()
        results = []
        used = set()

        def rec(index, subarray, total):
            if total == target:
                if tuple(subarray) not in used:
                    results.append(subarray[:])
                    used.add(tuple(subarray[:]))
                return
            elif total > target:
                return
            
            for i in range(index, len(candidates)):
                subarray.append(candidates[i])
                rec(i + 1, subarray, total + candidates[i])
                subarray.pop()

        rec(0, [], 0)
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
print(solution.subarrays_equal_k([1,2,3], 3))
print(solution.subarrays_equal_k([1,-1, 0], 0))

print(solution.minimum_size_subarray_sum(7, [2,3,1,2,4,3]))

root = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_5 = TreeNode(5)
root.left = node_2
root.right = node_3
node_2.left = node_5
print(solution.binary_tree_paths_dfs(root))
print(solution.binary_tree_paths_bfs(root))

print(solution.partition_labels("ababcbacadefegdehijhklij"))

print(solution.find_right_interval([[1,2], [2,3], [3,4]]))

print(solution.combination_sum_2([10,1,2,7,6,1,5], 8))

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