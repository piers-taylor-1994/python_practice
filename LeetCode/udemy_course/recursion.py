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
    
    def kth_largest_element_quicksort(self, arr, k):
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
    
    def kth_largest_element_quickselect(self, arr, k):
        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]
            
            pivot = random.choice(arr)
            left = [x for x in arr if x > pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x < pivot]

            if k < len(left):
                return quickselect(left, k)
            elif k < len(left) + len(middle):
                return middle[0]
            else:
                return quickselect(right, k - len(middle) - len(left))
        return quickselect(arr, k-1)
    
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] < target:
                left = middle + 1
            elif arr[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1
    
    def start_end_index_target(self, arr, target):
        if len(arr) == 0:
            return [-1, -1]

        def binary_search(arr, left, right, target):
            while left <= right:
                middle = (left + right) // 2

                if arr[middle] < target:
                    left = middle + 1
                elif arr[middle] > target:
                    right = middle - 1
                else:
                    return middle
            return -1

        first_position = binary_search(arr, 0, len(arr) - 1, target)
        if first_position == -1:
            return [-1, -1]
        
        start_position = first_position
        end_position = first_position
        temp_start = first_position
        temp_end = first_position

        while start_position != -1:
            temp_start = start_position
            start_position = binary_search(arr, 0, start_position - 1, target)
        
        start_position = temp_start

        while end_position != -1:
            temp_end = end_position
            end_position = binary_search(arr, end_position + 1, len(arr) - 1, target)
        
        end_position = temp_end

        return [start_position, end_position]
        

        
solution = Solution()
print(solution.factorial(4))
print(solution.factorial_tail(4))
print(solution.quicksort([1,5,1,7,3,2]))
print(solution.kth_largest_element_quicksort([1,5,1,7,3,2], 2))
print(solution.kth_largest_element_quickselect([1,5,1,7,3,2], 2))
print(solution.binary_search([1,2,3,4,5,6,7], 5))
print(solution.start_end_index_target([1,3,3,5,5,5,8,9], 5))
print(solution.start_end_index_target([1,2,3,4,5,6], 4))
print(solution.start_end_index_target([1,2,3,4,5], 9))
print(solution.start_end_index_target([], 3))
# print(solution.start_end_index_target_v2([1,3,3,5,5,5,8,9], 5))
# print(solution.start_end_index_target_v2([1,2,3,4,5,6], 4))
# print(solution.start_end_index_target_v2([1,2,3,4,5], 9))
# print(solution.start_end_index_target_v2([], 3))
# print(solution.start_end_index_target_v2([5,7,7,8,8,10], 8))