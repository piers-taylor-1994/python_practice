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

solution = Solution()
print(solution.quick_sort([5, 2, 1, 9, 0, 3]))