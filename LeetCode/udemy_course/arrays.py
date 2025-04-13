class Solution:
    def two_sum_brute_force(self, nums, target):
        for left in range(0, len(nums) - 1):
            number_to_find = target - nums[left]
            for right in range(left + 1, len(nums)):
                if nums[right] == number_to_find:
                    return [left, right]
    def two_sum(self, nums, target):
        numbers_to_find_dict = {target-nums[0]: 0}
        for i in range(1, len(nums)):
            current_number = nums[i]
            if current_number in numbers_to_find_dict:
                number_index = numbers_to_find_dict.get(current_number)
                return [number_index, i]
            number_to_find = target - nums[i]
            numbers_to_find_dict[number_to_find] = i
solution = Solution()
print(solution.two_sum_brute_force([1,3,7,9,2], 11))
print(solution.two_sum_brute_force([3,2,4], 6))
print(solution.two_sum([1,3,7,9,2], 11))
print(solution.two_sum([3,2,4], 6))