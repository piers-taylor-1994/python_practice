class Solution:
    #Space complexity: O(N)
    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x * self.factorial(x - 1)
    
    #Space complexity: 0(1)
    def factorial_tail(self, x, total_so_far = 1):
        if x == 1:
            return total_so_far
        else:
            return self.factorial_tail(x - 1, total_so_far * x)

solution = Solution()
print(solution.factorial(4))
print(solution.factorial_tail(4))