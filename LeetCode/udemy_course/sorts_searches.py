import random

class Solution:
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        pivot = random.choice(nums)

        left = [i for i in nums if i < pivot]
        middle = [i for i in nums if i == pivot]
        right = [i for i in nums if i > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1

solution = Solution()
print(solution.quick_sort([5, 2, 1, 9, 0, 3]))
print(solution.binary_search([0,1,5,6,9], 6))