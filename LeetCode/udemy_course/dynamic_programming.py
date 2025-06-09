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
    
    def min_cost_stairs_tabular_v2(self, cost):
        first = cost[0]
        second = cost[1]

        for i in range(2, len(cost)):
            temp = cost[i] + min(first, second)
            first = second
            second = temp

        return min(first, second)

    def knight_probability_memo(self, n, k, row, column):
        moves = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
        
        def dfs(r, c, memo, depth):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            elif depth == k:
                return 1
            elif (r, c, depth) in memo:
                return memo[(r, c, depth)]
            
            probability = 0
            for k_row, k_col in moves:
                probability += dfs(k_row + r, k_col + c, memo, depth + 1) / 8
            
            memo[(r, c, depth)] = probability

            return memo[(r, c, depth)]

        return dfs(row, column, {}, 0)

solution = Solution()
print(solution.min_cost_stairs_memo([20,15,30,5]))
print(solution.min_cost_stairs_tabular([20,15,30,5]))
print(solution.min_cost_stairs_tabular_v2([20,15,30,5]))

print(solution.knight_probability_memo(3, 2, 0, 0))