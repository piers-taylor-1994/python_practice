class Solution:
    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x * self.factorial(x - 1)

solution = Solution()
print(solution.factorial(4))