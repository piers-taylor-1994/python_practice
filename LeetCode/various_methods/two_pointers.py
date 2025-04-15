class Solution:
    """
    -These pointers can start:
        - At opposite ends of the array (e.g., left = 0, right = array.length - 1).
        - At the same position (e.g., both at the beginning for sliding window problems).
    -Loops to use:
        -Sliding window, for loop
        -Opposite ends, while loop
    -The pointers move based on a predefined logic (e.g., towards each other, away from each other, or in a specific pattern).
    -The movement depends on the problem you're solving, such as skipping invalid elements or searching for specific conditions.
    -You evaluate a condition as the pointers move, such as checking if the sum of elements equals a target value, or finding subsequences that satisfy a constraint.
    """
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
    
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        left = 0

        for right in range(len(t)):
            if s[left] == t[right]:
                left += 1
            if left == len(s):
                return True
        return False
    
    def maxArea(self, height):
        left = max_area = 0
        right = len(height) - 1

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
    def maxOperations(self, nums, k):
        nums.sort()
        left = operations = 0
        right = len(nums) - 1

        while left < right:
            num_left = nums[left]
            num_right = nums[right]
            total = num_left + num_right

            if total == k:
                operations += 1
                left += 1
                right -= 1
            elif total < k:
                while left < right and nums[left] == num_left:
                    left += 1
            else:
                while left < right and nums[right] == num_right:
                    right -= 1
        return operations
        
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isSubsequence("abc", "adebasdc"))
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,2,1]))
print(solution.maxOperations([1,2,3,4], 5))
print(solution.maxOperations([3,1,3,4,3], 6))
print(solution.maxOperations([63,10,28,31,90,53,75,77,72,47,45,6,49,13,77,61,68,43,33,1,14,62,55,55,38,54,8,79,89,14,50,68,85,12,42,57,4,67,75,6,71,8,61,26,11,20,22,3,70,52,82,70,67,18,66,79,84,51,78,23,19,84,46,61,63,73,80,61,15,12,58,3,21,66,42,55,7,58,85,60,23,69,41,61,35,64,58,84,61,77,45,14,1,38,4,8,42,16,79,60,80,39,67,10,24,15,6,37,68,76,30,53,63,87,11,71,86,82,77,76,37,21,85,7,75,83,80,8,19,25,11,10,41,66,70,14,23,74,33,76,35,89,68,85,83,57,6,72,34,21,57,72,79,29,65,3,67,8,24,24,18,26,27,68,78,64,57,55,68,28,9,11,38,45,61,37,81,89,38,43,45,26,84,62,22,37,51,15,30,67,75,24,66,40,81,74,48,43,78,14,33,19,73,5,1,2,53,29,49,73,23,5], 59))