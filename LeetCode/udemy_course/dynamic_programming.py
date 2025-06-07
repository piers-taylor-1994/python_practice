class Solution:
    def min_cost_stairs(self, cost):
        def dp(i):
            if i < 0:
                return 0
            elif i < 2:
                return cost[i]
            
            return cost[i] + min(dp(i-1), dp(i-2))

        n = len(cost)
        return 0 + min(dp(n-1), dp(n-2))


solution = Solution()
print(solution.min_cost_stairs([20,15,30,5]))