class Solution:
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
    
    def uniqueOccurrences(self, arr:list):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurences_count = set()
        for n in set(arr):
            number_count = arr.count(n)
            if number_count in occurences_count:
                return False
            occurences_count.add(number_count)
        return True

solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print(solution.uniqueOccurrences([1,2]))