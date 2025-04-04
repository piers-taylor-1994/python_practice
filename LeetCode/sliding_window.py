class Solution:
    """
    Maintain a subset of elements (the "window") that slides through a data structure, such as an array or string.
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
        current_average = max_average = float(sum(nums[:k]))

        for i in range(k, len(nums)):
            current_average = current_average + nums[i] - nums[i - k]
            max_average = max(max_average, current_average)
        return max_average / k
    
    def maxVowels(self, s: str, k: int):
        vowels = "aeiou"
        current_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        for j in range(k, len(s)):
            if s[j-k] in vowels:
                current_vowels -= 1
            if s[j] in vowels:
                current_vowels += 1
                max_vowels = max(max_vowels, current_vowels)
        return max_vowels

        
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
print(solution.findMaxAverage([5], 1))
print(solution.findMaxAverage([3,3,4,3,0], 3))
print(solution.findMaxAverage([0,1,1,3,3], 4))
print(solution.findMaxAverage([-1], 1))
print(solution.maxVowels("abciiidef", 3))