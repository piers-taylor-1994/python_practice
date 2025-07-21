import bisect

class Solution:
    def numberOfItems(self, s: str, startIndices: list[int], endIndices: list[int]) -> list[int]:
        pipe_indices = []
        prefix_items = [0] * len(s)
        count = 0
        inside = False
        results = []

        for i in range(len(s)):
            if s[i] == "|":
                pipe_indices.append(i)
                inside = True
            elif inside:
                count += 1
            prefix_items[i] = count

        for i in range(len(startIndices)):
            start = startIndices[i] - 1
            end = endIndices[i] - 1

            left_idx = bisect.bisect_left(pipe_indices, start)
            right_idx = bisect.bisect_right(pipe_indices, end) - 1

            if left_idx < len(pipe_indices) and right_idx >= 0 and left_idx < right_idx:
                left_pipe_pos = pipe_indices[left_idx]
                right_pipe_pos = pipe_indices[right_idx]

                left_items = prefix_items[left_pipe_pos]
                right_items = prefix_items[right_pipe_pos]
                items = right_items - left_items
            else:
                items = 0
            
            results.append(items)
        
        return results

    def subarraySum(self, nums, k):
        prefix = 0
        count_map = {0: 1}
        total = 0

        for num in nums:
            prefix += num
            #This works backwards. If this is > 0, there's a subarray with the current num that == k
            total += count_map.get(prefix - k, 0)
            count_map[prefix] = count_map.get(prefix, 0) + 1    
        
        return total

solution = Solution()

print(solution.numberOfItems("|**|*|", [1,1], [5,6]))

print(solution.subarraySum([1,2,3], 3))