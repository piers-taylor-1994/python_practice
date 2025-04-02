class Solution:
    """
    Maintain a subset of elements (the "window") that slides through a data structure, such as an array or string.
    Optimize problems involving contiguous subarrays or substrings by reducing time complexity, often from \(O(n^2)\) to \(O(n)\).
    The window can be fixed-size or variable-size, expanding or contracting based on problem-specific conditions.
    Use two pointers to define the window's boundaries, adjusting them as needed to meet the problem's criteria.
    Continuously update results (e.g., maximum sum, minimum length) as the window slides.
    """
    def findMaxAverage(self, nums:list, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = max_sum = float(sum(nums[:k]))
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k

        
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
print(solution.findMaxAverage([5], 1))
print(solution.findMaxAverage([3,3,4,3,0], 3))
print(solution.findMaxAverage([0,1,1,3,3], 4))
print(solution.findMaxAverage([-1], 1))