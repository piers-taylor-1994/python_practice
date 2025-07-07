import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    1. Arrays
    2. Strings
    3. Sorts/searches
    4. Linked lists
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

# print(random.choice(["container-with-most-water", "trapping-rainwater"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating", "is_almost_palindrome"]))
# print(random.choice(["quick_sort", "binary_search"]))
print(random.choice(["reverse_partial_linked_list", "flatten_double_linked_list"]))

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