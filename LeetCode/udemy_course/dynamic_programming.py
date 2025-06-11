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
    
    def fibonacci_memo(self, n):
        def dp(n, memo):
            if n <= 1:
                return n
            elif n in memo:
                return memo[n]
            
            memo[n] = dp(n - 1, memo) + dp(n - 2, memo)

            return memo[n]

        return dp(n, {})
            
    def fibonacci_tabular(self, n):
        dp = {}
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def fibonacci_tabular_optimised(self, n):
        first = 0
        second = 1

        for _ in range(2, n + 1):
            temp = first + second
            first = second
            second = temp

        return second
    
    def coin_change_memo(self, coins, amount):
        def dfs(current_amount, memo):
            if current_amount == 0:
                return 0
            elif current_amount < 0:
                return float('inf')
            elif current_amount in memo:
                return memo[current_amount]

            memo[current_amount] = min([dfs(current_amount - coin, memo) + 1 for coin in coins])
            return memo[current_amount]

        memo = {}
        result = dfs(amount, memo)

        return result if result != float('inf') else -1
    
    def coin_change_tabular(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def knapsack_bfs(self, w, profit, weight):
        n = len(profit)

        def dfs(i, current_weight, memo):
            if i == n or current_weight == 0:
                return 0
            elif (i, current_weight) in memo:
                return memo[(i, current_weight)]
            

            if weight[i] > current_weight:
                result = dfs(i + 1, current_weight, memo)
            
            else:
                take = profit[i] + dfs(i + 1, current_weight - weight[i], memo)
                skip = dfs(i + 1, current_weight, memo)
                result = max(take, skip)

            memo[(i, current_weight)] = result

            return memo[(i, current_weight)]

        return dfs(0, w, {})


solution = Solution()
print(solution.min_cost_stairs_memo([20,15,30,5]))
print(solution.min_cost_stairs_tabular([20,15,30,5]))
print(solution.min_cost_stairs_tabular_v2([20,15,30,5]))

print(solution.knight_probability_memo(3, 2, 0, 0))

print(solution.fibonacci_memo(8))
print(solution.fibonacci_tabular(8))
print(solution.fibonacci_tabular_optimised(8))

print(solution.coin_change_memo([1,2,5], 11))
print(solution.coin_change_memo([2], 3))
print(solution.coin_change_tabular([1,2,5], 11))
print(solution.coin_change_tabular([2], 3))

print(solution.knapsack_bfs(4, [1,2,3], [4,5,1]))