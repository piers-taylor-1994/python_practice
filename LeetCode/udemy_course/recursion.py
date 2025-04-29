import random


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
        
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        # Can use 1st, last, middle or median of three (1st, middle, last) as pivots
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)
    
    def kth_largest_element(self, arr, k):
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            return quicksort(left) + middle + quicksort(right)
        
        arr = quicksort(arr)
        return arr[-k]

solution = Solution()
print(solution.factorial(4))
print(solution.factorial_tail(4))
print(solution.quicksort([1,5,1,7,3,2]))
print(solution.kth_largest_element([1,5,1,7,3,2], 2))