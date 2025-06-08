class Solution:
    def min_cost_stairs_memo(self, cost):
        def dp(i, memo):
            if i in memo:
                return memo[i]
            elif i < 0:
                return 0
            elif i < 2:
                return cost[i]
            
            memo[i] = cost[i] + min(dp(i-1, memo), dp(i-2, memo))
            return memo[i]

        n = len(cost)
        return 0 + min(dp(n-1, {}), dp(n-2, {}))
    
    def min_cost_stairs_tabular(self, cost):
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[len(cost) - 1], dp[len(cost) - 2])


solution = Solution()
print(solution.min_cost_stairs_memo([20,15,30,5]))
print(solution.min_cost_stairs_tabular([20,15,30,5]))