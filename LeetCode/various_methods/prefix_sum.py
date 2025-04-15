from operator import indexOf


class Solution:
    """
    The prefix sum for an array is a new array where each element at index i 
    contains the sum of the elements of the original array from index 0 to i.
    """
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum = [0] * (len(gain) + 1)
        
        for i in range(len(gain)):
            prefix_sum[i + 1] = prefix_sum[i] + gain[i]
        return max(prefix_sum)
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        total_sum = prefix_sum[-1]

        for j in range(len(prefix_sum)):
            left_sum = prefix_sum[j-1] if j > 0 else 0
            right_sum = total_sum - prefix_sum[j]

            if left_sum == right_sum:
                return j
        return -1

solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
print(solution.pivotIndex([1,7,3,6,5,6]))
print(solution.pivotIndex([1,2,3]))
print(solution.pivotIndex([2,1,-1]))