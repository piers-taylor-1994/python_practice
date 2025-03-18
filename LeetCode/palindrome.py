
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_string = str(x)
        x_string_length = len(x_string)
        if x_string_length % 2 == 0: #even
            if x_string[:(int(x_string_length / 2))] == x_string[int(x_string_length / 2):][::-1]:
                return True
            else:
                return False
        else: #odd
            if x_string[:(int(x_string_length // 2))] == x_string[int(x_string_length // 2 + 1):][::-1]:
                return True
            else:
                return False
    def isPalindrome2(self, x):
            """
            :type x: int
            :rtype: bool
            """
            if x < 0:
                return False
            x_list = list(map(int, str(x)))
            x_list_length = len(x_list)
            if x_list_length % 2 == 0: #even
                if x_list[:(int(x_list_length / 2))] == x_list[int(x_list_length / 2):][::-1]:
                    return True
                else:
                    return False
            else: #odd
                if x_list[:(int(x_list_length // 2))] == x_list[int(x_list_length // 2 + 1):][::-1]:
                    return True
                else:
                    return False
Solution.isPalindrome("", 121)
Solution.isPalindrome("", -121)
Solution.isPalindrome("", 10)

print(Solution.isPalindrome2("", 121))
print(Solution.isPalindrome2("", -121))
print(Solution.isPalindrome2("", 10))