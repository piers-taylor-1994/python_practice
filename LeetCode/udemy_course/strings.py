class Solution:
    def typed_out_strings_bf(self, s:str, t:str):
        list_s = []
        list_t = []
        for i in range(len(s)):
            if s[i] != "#":
                list_s.append(s[i])
            elif len(list_s) > 0:
                list_s.pop()
        for j in range(len(t)):
            if t[j] != "#":
                list_t.append(t[j])
            elif len(list_t) > 0:
                list_t.pop()
        return list_s == list_t
    def typed_out_strings(self, s:str, t:str):
        p1 = len(s) - 1
        p2 = len(t) - 1
        while p1 >= 0 or p2 >= 0:
            if s[p1] == "#":
                back_count = 2
                while back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if p1 >= 0 and s[p1] == "#":
                        back_count += 2
                continue
            if t[p2] == "#":
                back_count = 2
                while back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if p2 >= 0 and t[p2] == "#":
                        back_count += 2
                continue
            else:
                if (p1 < 0 and p2 <= 0) or (p2 < 0 and p1 <= 0) or s[p1] != t[p2]:
                    return False
                p1 -= 1
                p2 -= 1
        return True
    
    def longest_substring_without_repeating_bf(self, s:str):
        max_substring_length = 0

        for i in range(len(s)):
            substring = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in substring:
                    break
                substring += s[j]
            max_substring_length = max(max_substring_length, len(substring))
        return max_substring_length
    def longest_substring_without_repeating(self, s:str):
        longest = 0
        left = 0
        letter_positions = {}
        for right in range(len(s)):
            if s[right] in letter_positions and left <= letter_positions[s[right]]:
                left = letter_positions[s[right]] + 1
            else:
                longest = max(longest, right - left + 1)
            letter_positions[s[right]] = right
        return longest
    def longest_substring_without_repeating_v2(self, s:str):
        left = 0
        substring = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longest = max(longest, right - left + 1)
        return longest         
    
    def is_palindrome(self, s:str):
        new_word = ''.join(letter.lower() for letter in s if letter.isalpha())
        left = 0
        right = len(new_word) - 1
        while left < right:
            if new_word[left] != new_word[right]:
                return False
            left += 1
            right -= 1
        return True
    def is_almost_palindrome(self, s:str):
        def palindrome_checker(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return palindrome_checker(s, left + 1, right) or palindrome_checker(s, left, right - 1)
            left += 1
            right -= 1
        return True
solution = Solution()
print(solution.typed_out_strings_bf("ab#z", "az#z"))
print(solution.typed_out_strings_bf("a##", "a##"))
print(solution.typed_out_strings("ab#c", "ad#c"))
print(solution.typed_out_strings("ab##", "c#d#"))
print(solution.typed_out_strings("xywrrmp", "xywrrmu#p"))
print(solution.typed_out_strings("a", "aa#a"))
print(solution.typed_out_strings("c#a#c", "c"))

print(solution.longest_substring_without_repeating_bf("abccbac"))
print(solution.longest_substring_without_repeating_bf(""))
print(solution.longest_substring_without_repeating_bf("ab"))
print(solution.longest_substring_without_repeating_bf("ccc"))
print(solution.longest_substring_without_repeating_bf("abcbda"))
print(solution.longest_substring_without_repeating_bf("pwwkew"))
print(solution.longest_substring_without_repeating("abcabcbb"))
# print(solution.longest_substring_without_repeating(""))
# print(solution.longest_substring_without_repeating("ab"))
# print(solution.longest_substring_without_repeating("ccc"))
# print(solution.longest_substring_without_repeating("abcbda"))
print(solution.longest_substring_without_repeating("pwwkew"))
print(solution.longest_substring_without_repeating("au"))
print(solution.longest_substring_without_repeating("tmmzuxt"))

print(solution.is_palindrome("A man, a plan, a canal: Panama"))
print(solution.is_palindrome("race car"))
# print(solution.is_almost_palindrome("abca"))
print(solution.is_almost_palindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))