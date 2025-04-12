class Solution:
    def two_sum(self, nums, target):
        for left in range(len(nums) - 1):
            number_to_find = target - nums[left]
            for right in range(left + 1, len(nums)):
                if nums[right] == number_to_find:
                    return [left, right]
solution = Solution()
print(solution.two_sum([1,3,7,9,2], 11))
print(solution.two_sum([3,2,4], 6))