class Solution:
    """
    -These pointers can start:
        - At opposite ends of the array (e.g., left = 0, right = array.length - 1).
        - At the same position (e.g., both at the beginning for sliding window problems).

    -The pointers move based on a predefined logic (e.g., towards each other, away from each other, or in a specific pattern).
    -The movement depends on the problem you're solving, such as skipping invalid elements or searching for specific conditions.

    -You evaluate a condition as the pointers move, such as checking if the sum of elements equals a target value, or finding subsequences that satisfy a constraint.
    """
    def isPalindrome(self, s:str):
        s = "".join([c.lower() for c in s if c.isalnum()])
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def moveZeroes(self, nums: list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        right = 0
        for left in range(len(s)):
            while right < len(t) and s[left] != t[right]:
                right += 1
            if right >= len(t) or len(s[left:]) > len(t[right:]):
                return False
            right += 1
        return True
    
    def maxArea(self, height:list[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area                

        
solution = Solution()
print(solution.moveZeroes([0,1,0,12,13]))
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isSubsequence("abc", "adebasdc"))
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,2,1]))