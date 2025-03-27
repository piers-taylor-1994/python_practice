# class Solution:
#     #Each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#     # #F(0) = 0, F(1) = 1
#     # #F(n) = F(n - 1) + F(n - 2), for n > 1.
#     def fibonacci(self, n, memo):
#         if n <= 1:
#             return n
#         elif n in memo:
#             return memo[n]
        
#         memo[n] = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
#         return memo[n]
    
#     #The Tribonacci sequence Tn is defined as follows: 
#     # T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#     def tribonacci(self, n, memo = {}):
#         if n in memo:
#             return memo[n]
#         elif n <= 2:
#             if n == 0:
#                 return n
#             return 1
        
#         memo[n] = self.tribonacci(n - 1, memo) + self.tribonacci(n - 2, memo) + self.tribonacci(n - 3, memo)
#         return memo[n]
    
#     #You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
#     # Once you pay the cost, you can either climb one or two steps.
#     # You can either start from the step with index 0, or the step with index 1.
#     def minCostClimbingStairs(self, cost: list[int]) -> int:
#         cost.append(0)

#         for i in range(len(cost) - 4, -1, -1):
#             cost[i] += min(cost[i + 1], cost[i + 2])
#         return min(cost[0], cost[1])
    
#     def climbStairs(self, n, memo = {}):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n <= 3:
#             return n
#         elif n in memo:
#             return memo[n]
        
#         memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
#         return memo[n]
    
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         #[2,7,9,3,1]
#         def rob_dp(nums, n, memo):
#             if n in memo:
#                 return memo[n]
#             elif n == 0:
#                 return nums[0]
#             elif n == 1:
#                 return max(nums[0], nums[1])
#             memo[n] = max(rob_dp(nums, n-1, memo), nums[n] + rob_dp(nums, n-2, memo))
#             return memo[n]
#         return rob_dp(nums, len(nums) - 1, {})
    
#     def rob_2(self, nums, memo = {}):
#         def rob_dp(nums, n, memo):
#             if n in memo:
#                 return memo[n]
#             elif n == 0:
#                 return nums[0]
#             elif n == 1:
#                 return max(nums[0], nums[1])
            
#             memo[n] = max(rob_dp(nums, n - 1, memo), nums[n] + rob_dp(nums, n - 2, memo))
#             return memo[n]

#         for i in range(2, len(nums)):
#             memo[i] = rob_dp(nums, i, {})
#         return memo[len(nums) - 1]
    
#     def unique_paths(self, m, n):
#         above_row = [1] * n

#         #Skip 1st row
#         for _ in range(1, m):
#             current_row = [1] * n
#             #Skip 1st column 
#             for i in range(1, n):
#                 current_row[i] = current_row[i-1] + above_row[i]
#             above_row = current_row
#         return above_row[-1]

        
    
# solution = Solution()
# # print(solution.fibonacci(8, {}))
# # print(solution.tribonacci(4, {}))
# print(solution.minCostClimbingStairs([10,15,20]))
# print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
# print(solution.climbStairs(4))
# # print(solution.rob([1,2,3,1]))
# print(solution.rob([2,7,9,3,1]))
# print(solution.rob_2([2,7,9,3,1]))
# print(solution.unique_paths(3, 2))

class Solution:
    def fibo(self, n, memo = {}):
        #0, 1, 1, 2, 3, 5, 8...
        #n = n - 1 + n - 2!
        #base cases
        if n <= 1:
            return n
        elif n not in memo:
            memo[n] = self.fibo(n-1, memo) + self.fibo(n-2, memo) #n = n-1 + n-2
        return memo[n]
    def climbing_stairs(self, n, memo={}):
        #n(0) = 1 n(1) = 1 n(2) = 2 n(3) = 3
        #Therefore n = n-1 + n-2
        #Base case
        if n <= 1:
            return 1
        elif not n in memo:
            memo[n] = self.climbing_stairs(n-1) + self.climbing_stairs(n-2)
        return memo[n]
    def coin_change(self, coins, amount):
        #Effectively we need to try taking away each coin away from the total
        #We then re-use the new total minusing that coin and then recursively go until we get to 0
        #We then return the minimum coin route to the top
        #We add 1 every time is we account for the coin used in each sub problem
        #As we use that coin to take away from the total so we need to add that 1 coin back to the calc
        def dp(amount: int, memo: dict):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            if not amount in memo:
                #Add the coin count back after taking it away from the amount
                memo[amount] = min(dp(amount - c, memo) + 1 for c in coins)
            return memo[amount]
        #Have to structure it like this or the exception case (-1) doesn't work as memo doesn't get reset
        res = dp(amount, memo = {})
        return res if res != float('inf') else -1
    
    def unique_paths(self, m, n, memo={}):
        if m <= 1 or n <= 1:
            return 1  # Base case: Only one path in the first row or column
        if (m, n) in memo:
            return memo[(m, n)]  # Use cached result if available
        
        # Recursive calculation for paths
        memo[(m, n)] = self.unique_paths(m - 1, n, memo) + self.unique_paths(m, n - 1, memo)
        return memo[(m, n)]
     
solution = Solution()
print(solution.fibo(8))
print(solution.climbing_stairs(20))
print(solution.coin_change([1,2], 4))
print(solution.coin_change([1,2,5], 11))
print(solution.coin_change([2], 3))
print(solution.unique_paths(3, 3))