class Solution:
    def two_sum_bf(self, nums, target):
        for left in range(0, len(nums) - 1):
            number_to_find = target - nums[left]
            for right in range(left + 1, len(nums)):
                if nums[right] == number_to_find:
                    return [left, right]
    def two_sum(self, nums, target):
        numbers_to_find_dict = {target - nums[0]: 0}
        for i in range(1, len(nums)):
            current_number = nums[i]
            if current_number in numbers_to_find_dict:
                number_index = numbers_to_find_dict.get(current_number)
                return [number_index, i]
            number_to_find = target - nums[i]
            numbers_to_find_dict[number_to_find] = i

    def container_with_most_water_bf(self, heights:list[int]):
        max_area = 0
        for p1 in range(len(heights) - 1):
            for p2 in range(p1 + 1, len(heights)):
                min_height = min(heights[p1], heights[p2])
                width = p2 - p1
                current_area = min_height * width
                max_area = max(max_area, current_area)
        return max_area
    def container_with_most_water(self, heights:list[int]):
        max_area = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            height = min(heights[p1], heights[p2])
            width = p2 - p1
            current_area = height * width
            if current_area > max_area:
                max_area = current_area

            if max(heights[p1:p2]) * (p2 - p1 - 1) < max_area:
                break

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area
    
solution = Solution()
print(solution.two_sum_bf([1,3,7,9,2], 11))
print(solution.two_sum_bf([3,2,4], 6))
print(solution.two_sum([1,3,7,9,2], 11))
print(solution.two_sum([3,2,4], 6))

print(solution.container_with_most_water_bf([7,1,2,3,9]))
print(solution.container_with_most_water([7,1,2,3,9]))