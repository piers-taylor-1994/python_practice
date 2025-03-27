class Solution:
    def merge_alternatively(self, word1, word2) -> str:
        merged_word = ""

        for letter1, letter2 in zip(word1, word2):
            merged_word += letter1 + letter2
        
        if len(word1) != len(word2):
            merged_word += word1[len(word2):]
            merged_word += word2[len(word1):]
        return merged_word
    
    def gcd(self, num1, num2):
        while num2 > 0:
            num1, num2 = num2, num1 % num2
        return num1
    
    def gcdOfStrings(self, str1, str2) -> str:
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(len1, len2):
            while len2 > 0:
                len1, len2 = len2, len1 % len2
            return len1
        
        return str1[:gcd(len(str1), len(str2))]
    
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        return [True if c + extraCandies >= max_candy else False for c in candies]
    
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            left_is_free = i == 0 or flowerbed[i - 1] == 0
            right_is_free = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            if left_is_free and right_is_free and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
        

solution = Solution()
print(solution.merge_alternatively("abc", "pqr"))
print(solution.merge_alternatively("ab", "pqrs"))

print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("LEET", "CODE"))
print(solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
print(solution.gcdOfStrings("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
print(solution.gcd(1071, 462))
print(solution.kidsWithCandies([2,3,5,1,3], 3))
print(solution.kidsWithCandies([4,2,1,1,2], 1))
print(solution.canPlaceFlowers([1,0,0,0,1], 1))
print(solution.canPlaceFlowers([1,0,0,0,1], 2))
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))
print(solution.canPlaceFlowers([1,0,0,0,0,0,1], 2))