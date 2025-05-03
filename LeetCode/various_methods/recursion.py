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
    
    def fibonacci_iterative(self, x):
        fibo = [0, 1]

        for i in range(2, x + 1):
            fibo.append(fibo[i - 1] + fibo[i - 2])
        
        return fibo[x]
    def fibonacci_recursive(self, x):
        if x <= 1:
            return x
        return self.fibonacci_recursive(x - 1) + self.fibonacci_recursive(x - 2)

solution = Solution()
print(solution.factorial_iterative(5))
print(solution.factorial_recursive(5))
print(solution.fibonacci_iterative(8))
print(solution.fibonacci_recursive(8))