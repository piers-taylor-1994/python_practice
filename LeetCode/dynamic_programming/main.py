class Solution:
    #Each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    # #F(0) = 0, F(1) = 1
    # #F(n) = F(n - 1) + F(n - 2), for n > 1.
    def fibonacci(self, n, memo):
        if n <= 1:
            return n
        elif n in memo:
            return memo[n]
        
        memo[n] = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
        return memo[n]
    
    #The Tribonacci sequence Tn is defined as follows: 
    # T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    def tribonacci(self, n, memo = {}):
        if n in memo:
            return memo[n]
        elif n <= 2:
            if n == 0:
                return n
            return 1
        
        memo[n] = self.tribonacci(n - 1, memo) + self.tribonacci(n - 2, memo) + self.tribonacci(n - 3, memo)
        return memo[n]
    
    #You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
    # Once you pay the cost, you can either climb one or two steps.
    # You can either start from the step with index 0, or the step with index 1.
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
    
    def climbStairs(self, n, memo = {}):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        elif n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[2,7,9,3,1]
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        memo[0] = nums[0] #2
        memo[1] = max(nums[0], nums[1]) 

        for i in range (2, n):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
        return memo[n-1]

        
    
solution = Solution()
# print(solution.fibonacci(8, {}))
# print(solution.tribonacci(4, {}))
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(solution.climbStairs(4))
# print(solution.rob([1,2,3,1]))
print(solution.rob([2,7,9,3,1]))