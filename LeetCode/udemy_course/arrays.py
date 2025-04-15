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
            max_area = max(max_area, current_area)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area
    
    def trapping_rainwater_bf(self, heights:list[int]):
        trapped_water = 0
        
        for p1 in range(1, len(heights) - 1):
            max_left = 0
            max_right = 0
            left = p1
            right = p1
            while left > 0:
                max_left = max(max_left, heights[left])
                left -= 1
            while right < len(heights):
                max_right = max(max_right, heights[right])
                right += 1
            current_water = min(max_left, max_right) - heights[p1]
            if current_water > 0:
                trapped_water += current_water
        return trapped_water
    
    def trapping_rainwater(self, heights:list[int]):
        trapped_water = 0
        left = 0
        right = len(heights) - 1
        max_left = heights[left]
        max_right = heights[right]

        while left < right:
            if heights[left] <= heights[right]:
                if heights[left] > max_left:
                    max_left = heights[left]
                else:
                    trapped_water += max_left - heights[left]
                left += 1
            else:
                if heights[right] > max_right:
                    max_right = heights[right]
                else:
                    trapped_water += max_right - heights[right]
                right -= 1
        return trapped_water            


    
solution = Solution()
print(solution.two_sum_bf([1,3,7,9,2], 11))
print(solution.two_sum_bf([3,2,4], 6))
print(solution.two_sum([1,3,7,9,2], 11))
print(solution.two_sum([3,2,4], 6))

print(solution.container_with_most_water_bf([7,1,2,3,9]))
print(solution.container_with_most_water([7,1,2,3,9]))

print(solution.trapping_rainwater_bf([0,1,0,2,1,0,3,1,0,1,2]))
print(solution.trapping_rainwater_bf([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trapping_rainwater([0,1,0,2,1,0,3,1,0,1,2]))
print(solution.trapping_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]))