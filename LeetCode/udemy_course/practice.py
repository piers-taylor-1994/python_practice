import random

class Solution:
    """
    1. Arrays
    2. Strings
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

# print(random.choice(["container-with-most-water", "trapping-rainwater"]))
print(random.choice(["typed-out-strings", "longest-substring-without-repeating", "is_almost_palindrome"]))

solution = Solution()
print(solution.two_sum([3,2,4], 6))

print(solution.is_palindrome("A man, a plan, a canal: Panama"))