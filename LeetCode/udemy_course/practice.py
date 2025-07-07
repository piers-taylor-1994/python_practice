import random

class Solution:
    def two_sum(self, nums, target):
        recorded_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in recorded_nums:
                return [recorded_nums[(target - nums[i])], i]
            recorded_nums[nums[i]] = i

# print(random.choice(["two-sum", "container-with-most-water", "trapping-rainwater"]))
solution = Solution()
print(solution.two_sum([3,2,4], 6))