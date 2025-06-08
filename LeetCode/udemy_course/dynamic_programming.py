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


solution = Solution()
print(solution.min_cost_stairs_memo([20,15,30,5]))