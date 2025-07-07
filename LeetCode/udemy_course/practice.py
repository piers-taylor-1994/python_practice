import random

class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] + nums[j] == target:
                    return [i, j]

# print(random.choice(["two-sum", "container-with-most-water", "trapping-rainwater"]))
solution = Solution()
print(solution.two_sum([3,2,4], 6))