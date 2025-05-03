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
    
    def sum_of_digits_iterative(self, x):
        return sum([int(num) for num in str(x)])
    def sum_of_digits_recursive(self, x):
        if x < 10:
            return x
        # % returns reminder so anything % 10 will be the unit
        return x % 10 + self.sum_of_digits_recursive(x // 10) # // 10 will just decrease everything by 1 digital and round down
    
    def reverse_string_iterative(self, word):
        output = ""

        for i in range(len(word) - 1, -1, -1):
            output += word[i]
        return output
    def reverse_string_recursive(self, word):
        #base
        if len(word) == 1:
            return word
        return self.reverse_string_recursive(word[1:]) + word[0]

solution = Solution()
print(solution.factorial_iterative(5))
print(solution.factorial_recursive(5))
print(solution.fibonacci_iterative(8))
print(solution.fibonacci_recursive(8))
print(solution.sum_of_digits_iterative(432))
print(solution.sum_of_digits_recursive(432))
print(solution.reverse_string_iterative("Hello"))
print(solution.reverse_string_recursive("Hello"))