from typing import Counter

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
        freq = {}
        for n in set(arr):
            if arr.count(n) in freq.values():
                return False
            freq[n] = arr.count(n)
        return True
    
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        
        freq1 = [word1.count(l) for l in set1]
        freq2 = [word2.count(l) for l in set2]

        freq1.sort()
        freq2.sort()

        return freq1 == freq2
    
    def closeStrings_2(self, word1, word2):
        if set(word1) != set(word2):
            return False
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values())
    
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_tuples = [tuple(row) for row in grid]
        row_count = Counter(row_tuples)

        match_count = 0
        for col_id in range(len(grid)):
            col_tuple = tuple(grid[row_id][col_id] for row_id in range(len(grid)))

            if col_tuple in row_tuples:
                match_count += row_count.get(col_tuple)
        return match_count
                
        

solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))
print(solution.findDifference([1,2,3,3], [1,1,2,2]))
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print(solution.uniqueOccurrences([1,2]))
print(solution.closeStrings("cabbba", "abbccc"))
print(solution.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
print(solution.closeStrings_2("cabbba", "abbccc"))
print(solution.closeStrings_2("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
# print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))