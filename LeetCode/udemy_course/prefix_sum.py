import bisect

from sortedcontainers import SortedDict, SortedList

class Solution:
    def basic_prefix(self, nums):
        results = [0] * len(nums)
        results[0] = nums[0]

        for i in range(1, len(nums)):
            results[i] = results[i-1] + nums[i]
        
        return results
    
    def range_sum(self, nums, i, j):
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for k in range(1, len(nums)):
            prefix_sum[k] = prefix_sum[k - 1] + nums[k]
        
        if i == 0:
            return prefix_sum[j]
        return prefix_sum[j] - prefix_sum[i - 1]
    
    def even_numbers_prefix(self, nums):
        prefix_sum = [0] * len(nums)
        count = 1 if nums[0] % 2 == 0 else 0
        prefix_sum[0] = count

        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                count += 1
            prefix_sum[i] = count
        
        return prefix_sum
    
    def even_numbers_prefix_range(self, nums, i, j):
        prefix_sum = [0] * len(nums)
        count = 1 if nums[0] % 2 == 0 else 0
        prefix_sum[0] = count

        for k in range(1, len(nums)):
            if nums[k] % 2 == 0:
                count += 1
            prefix_sum[k] = count
        
        if i == 0:
            return prefix_sum[j]
        return prefix_sum[j] - prefix_sum[i - 1]
    
    def numberOfItems(self, s: str, startIndices: list[int], endIndices: list[int]) -> list[int]:
        pipe_indices = []
        prefix_sum = [0] * len(s)
        inside = False
        results = []
        count = 0

        for i in range(len(s)):
            if s[i] == "|":
                pipe_indices.append(i)
                inside = True
            elif inside:
                count += 1
            prefix_sum[i] = count
        
        for i in range(len(startIndices)):
            start = startIndices[i] - 1
            end = endIndices[i] - 1

            start_idx = bisect.bisect_left(pipe_indices, start)
            end_idx = bisect.bisect_right(pipe_indices, end) - 1

            if start_idx < len(s) and end_idx >= 0 and start_idx < end_idx:
                start_pipe = pipe_indices[start_idx]
                end_pipe = pipe_indices[end_idx]

                left_prefix = prefix_sum[start_pipe]
                right_prefix = prefix_sum[end_pipe]

                results.append(right_prefix - left_prefix)
        
        return results

    def subarraySum(self, nums, k):
        prefix = 0
        count_map = {prefix:1}
        total = 0

        for num in nums:
            prefix += num
            total += count_map.get(prefix - k, 0)
            count_map[prefix] = count_map.get(prefix, 0) + 1
            
        return total
    
    def countSmaller(self, nums):
        sorted_list = SortedList()
        result = []

        for num in nums[::-1]:
            idx = bisect.bisect_left(sorted_list, num)
            result.append(idx)
            sorted_list.add(num)
        
        return result[::-1]

    def countGreater(self, nums):
        results = []
        sorted_list = []

        for num in nums[::-1]:
            idx = bisect.bisect_right(sorted_list, -num)
            results.append(idx)
            bisect.insort(sorted_list, -num)
        
        return results[::-1]
    
    def countRangeSum(self, nums, lower, upper):
        sorted_list = SortedList()
        prefix = 0
        count = 0

        sorted_list.add(0)

        for num in nums:
            prefix += num
            left = sorted_list.bisect_left(prefix - upper)
            right = sorted_list.bisect_right(prefix - lower)
            count += right - left
            sorted_list.add(prefix)

        return count

solution = Solution()

print(solution.basic_prefix([1,2,3,4,5]))

print(solution.range_sum([2,4,6,8,10], 1, 3))

print(solution.even_numbers_prefix([1,2,4,5,6]))

print(solution.even_numbers_prefix_range([1,2,4,5,6], 2, 4))

print(solution.numberOfItems("|**|*|", [1,1], [5,6]))

print(solution.subarraySum([1,2,3], 3))

print(solution.countSmaller([5,2,6,1]))
print(solution.countGreater([5,2,6,1]))

print(solution.countRangeSum([-2, 5, -1], -2, 2))