class Solution:
    def factorial_iterative(self, x):
        output = 1
        for i in range(2, x + 1):
            output *= i
        # while x > 1:
        #     output *= x
        #     x -= 1
        return output
    
    def factorial_recursive(self, x):
        if x <= 1:
            return 1
        return x * self.factorial_recursive(x - 1)

solution = Solution()
print(solution.factorial_iterative(5))
print(solution.factorial_recursive(5))