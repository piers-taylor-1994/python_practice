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
        number_of_occurences = []
        for n in set(arr):
            n_count = 0
            for j in arr:
                if n == j:
                    n_count += 1
            if n_count in number_of_occurences:
                return False
            number_of_occurences.append(n_count)
        return True
    
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1) != set(word2):
            return False
        
        freq1 = {n:word1.count(n) for n in word1}
        freq2 = {n:word2.count(n) for n in word2}
        
        freq1_list = [i for i in freq1.values()]
        freq2_list = [i for i in freq2.values()]
        freq1_list.sort()
        freq2_list.sort()

        return freq1_list == freq2_list
    
    def closeStrings_2(self, word1, word2):
        if set(word1) != set(word2):
            return False
        
        #More efficient way of turning list -> dict
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        #Basically .sort() but for any iterable thing
        return sorted(freq1.values()) == sorted(freq2.values())

        

solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))
print(solution.findDifference([1,2,3,3], [1,1,2,2]))
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print(solution.uniqueOccurrences([1,2]))
print(solution.closeStrings("cabbba", "abbccc"))
print(solution.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
print(solution.closeStrings_2("cabbba", "abbccc"))
print(solution.closeStrings_2("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))