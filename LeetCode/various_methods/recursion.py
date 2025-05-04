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
    
    def array_sorted_iterative(self, array):
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                return False 
        return True
    def array_sorted_recursive(self, array, index = 0):
        if index == len(array) - 1:
            return array[index]
        return array[index] <= self.array_sorted_recursive(array, index + 1)
    
    def is_palindrome_iterative(self, number):
        if not number:
            return False
        number = str(number)
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] != number[right]:
                return False
            left += 1
            right -= 1
        return True
    def is_palindrome_recursive(self, number):
        if not number:
            return False
        
        def recursive(str_number, left, right):
            if left >= right:
                return True
            return str_number[left] == str_number[right] and recursive(str_number, left + 1, right - 1)

        str_number = str(number)
        return recursive(str_number, 0, len(str_number) - 1)
    
    def reverse_linked_list_iterative(self, head):
        current_node = head
        prev = None

        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        return prev
    def reverse_linked_list_recursive(self, head, prev = None):
        #base case
        if not head:
            return prev
        
        next = head.next
        head.next = prev
        
        #recursive
        return self.reverse_linked_list_recursive(next, head)

solution = Solution()
print(solution.factorial_iterative(5))
print(solution.factorial_recursive(5))

print(solution.fibonacci_iterative(8))
print(solution.fibonacci_recursive(8))

print(solution.sum_of_digits_iterative(432))
print(solution.sum_of_digits_recursive(432))

print(solution.reverse_string_iterative("Hello"))
print(solution.reverse_string_recursive("Hello"))

print(solution.array_sorted_iterative([1,2,3,4,5]))
print(solution.array_sorted_recursive([1,2,3,4,5]))

print(solution.is_palindrome_iterative(123321))
print(solution.is_palindrome_recursive(123321))