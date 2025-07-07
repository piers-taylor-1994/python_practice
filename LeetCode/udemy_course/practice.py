import random

class Solution:
    def two_sum(self, nums, target):
        recorded_nums = {}
        def rec(i):
            if (target - nums[i]) in recorded_nums:
                return [recorded_nums[target - nums[i]], i]
            
            recorded_nums[nums[i]] = i
            return rec(i + 1)
        return rec(0)

# print(random.choice(["two-sum", "container-with-most-water", "trapping-rainwater"]))
solution = Solution()
print(solution.two_sum([3,2,4], 6))