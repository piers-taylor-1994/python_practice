import enum
import random
import math
from functools import reduce
import operator

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
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)

        new_word = [n for n in s[::-1] if n.lower() in vowels]
        count = 0
        for i,n in enumerate(s):
            if n.lower() in vowels:
                s[i] = new_word[count]
                count += 1
        return "".join(s)
    
    def reverseVowels_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        word = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not word[start].lower() in vowels:
                start += 1
            while start < end and not word[end].lower() in vowels:
                end -= 1

            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        return "".join(word)
    
    def reverse_words(self, s: str):
        s_list = s.split()
        s_list = s_list[::-1]
        return " ".join(s_list)
    
    def productExceptSelf(self, nums: list):
        if len(nums) <= 1:
            return []
        ans = [1] * len(nums)
        left_product, right_product = 1, 1

        for i in range(len(nums)):
            ans[i] *= left_product
            if i < len(nums) - 1:
                left_product *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right_product
            if i > 0:
                right_product *= nums[i]

        return ans      

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read, write = 0, 0
        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
    
    def moveZeroes(self, nums: list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            zero_count = nums.count(0)
            for _ in range(zero_count):
                nums.remove(0)
                nums.append(0)
        

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
print(solution.reverseVowels("IceCreAm"))
print(solution.reverseVowels_2("IceCreAm"))
print(solution.reverse_words("the sky is blue"))
print(solution.reverse_words("  hello world  "))
print(solution.reverse_words("a good   example"))
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))
print(solution.compress(["a","a","b","b","c","c","c"]))
print(solution.moveZeroes([0,1,0,3,12]))
