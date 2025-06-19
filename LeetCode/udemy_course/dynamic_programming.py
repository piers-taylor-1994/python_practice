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
        def dp(current_amount, memo):
            if current_amount == 0:
                return 0
            elif current_amount < 0:
                return float('inf')
            elif current_amount in memo:
                return memo[current_amount]

            memo[current_amount] = min([dp(current_amount - coin, memo) + 1 for coin in coins])
            return memo[current_amount]

        memo = {}
        result = dp(amount, memo)

        return result if result != float('inf') else -1
    
    def coin_change_tabular(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def knapsack_memo(self, capacity, profit, weight):
        def dp(i, current_capacity, memo):
            if i == len(profit) or capacity == 0:
                return 0
            elif (i, current_capacity) in memo:
                return memo[(i, current_capacity)]
            
            if current_capacity - weight[i] < 0:
                result = dp(i + 1, current_capacity, memo)
            else:
                take = profit[i] + dp(i + 1, current_capacity - weight[i], memo)
                skip = dp(i + 1, current_capacity, memo)
                result = max(take, skip)
            
            memo[(i, current_capacity)] = result
            return memo[(i, current_capacity)]

        return dp(0, capacity, {})
    
    def unique_paths_memo(self, m, n):
        def dp(m, n, memo):
            if m == 1 or n == 1:
                return 1
            elif (m, n) in memo:
                return memo[(m, n)]
            
            memo[(m, n)] = dp(m - 1, n, memo) + dp(m, n - 1, memo)
            return memo[(m, n)]

        return dp(m, n, {})
    
    def unique_paths_tabular(self, m, n):
        dp = {}

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]
        
        return dp[(m - 1, n - 1)]
    
    def min_path_sum_memo(self, grid):
        target_pos = (len(grid) - 1, len(grid[0]) - 1)
        memo = {}

        def dp(row, col):
            if row > target_pos[0] or col > target_pos[1]:
                return float('inf')
            if (row, col) == target_pos:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] = grid[row][col] + min(dp(row + 1, col), dp(row, col + 1))
            return memo[(row, col)]

        return dp(0, 0)
    
    def min_path_sum_tabular(self, grid):
        dp = {}
        dp[(0, 0)] = grid[0][0]
        dp[(1, 0)] = dp[(0, 0)] + grid[1][0]
        dp[(0, 1)] = dp[(0, 0)] + grid[0][1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) == (0, 0) or (i, j) == (1, 0) or (i, j) == (0, 1):
                    continue
                else:
                    first = dp[(i - 1, j)] if (i - 1, j) in dp else grid[i - 1][j] if i - 1 >= 0 and j >= 0 else float('inf')
                    second = dp[(i, j - 1)] if (i, j - 1) in dp else grid[i][j - 1] if i >= 0 and j - 1 >= 0 else float('inf')
                    dp[(i, j)] = grid[i][j] + min(first, second)
        
        return dp[(len(grid) - 1, len(grid[0]) - 1)]
    
    def longest_common_subsequence(self, text1, text2):
        memo = {}
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = (
                1 + dp(i + 1, j + 1) if text1[i] == text2[j]
                else max(dp(i + 1, j), dp(i, j + 1))
            )

            return memo[(i, j)]
        return dp(0, 0)
    
    def edit_distance(self, word1, word2):
        memo = {}
        
        def dp(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            elif (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = (
                dp(i - 1, j - 1) if word1[i - 1] == word2[j - 1]
                else 1 + min(
                    dp(i - 1, j),
                    dp(i, j - 1),
                    dp(i - 1, j - 1)
                )
            )
            return memo[(i, j)]

        return dp(len(word1), len(word2))
    
    def house_robber(self, nums):
        memo = {}

        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            elif i in memo:
                return memo[i]
            
            memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
            return memo[i]

        return dp(len(nums) - 1)
    
    def jump_game_memo(self, nums):
        memo = {}

        def dp(i):
            if i == len(nums) - 1:
                return True
            elif i >= len(nums):
                return False
            elif i in memo:
                return memo[i]
            
            for j in range(1, nums[i] + 1):
                if dp(i + j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dp(0)
    def jump_game_greedy(self, nums):
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
        return True
    
    def knight_probability_memo(self, n, k, row, column):
        moves = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
        memo = {}

        def dp(move, r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            elif move == k:
                return 1.00
            elif (r, c, move) in memo:
                return memo[(r, c, move)]
            
            total = sum([dp(move + 1, r + k_row, c + k_col) / 8 for k_row, k_col in moves])
            memo[(r, c, move)] = total
            return memo[(r, c, move)]
        
        return dp(0, row, column)
    
    def dice_roll(self, n, k, target):
        def dp(roll, number):
            if roll == n and number != target:
                return 0
            elif roll == n and number == target:
                return 1
            
            return sum([dp(roll + 1, number + i) for i in range(1, k + 1)])

        return dp(0, 0)


solution = Solution()
print(solution.min_cost_stairs_memo([20,15,30,5]))
print(solution.min_cost_stairs_tabular([20,15,30,5]))
print(solution.min_cost_stairs_tabular_v2([20,15,30,5]))

print(solution.knight_probability_memo(3, 2, 0, 0))

print(solution.fibonacci_memo(8))
print(solution.fibonacci_tabular(8))
print(solution.fibonacci_tabular_optimised(8))

#dp technique 1
print(solution.knapsack_memo(4, profit=[1,2,3], weight=[4,5,1]))
print(solution.coin_change_memo([1,2,5], 11))
print(solution.coin_change_memo([2], 3))
print(solution.coin_change_tabular([1,2,5], 11))
print(solution.coin_change_tabular([2], 3))

#dp technique 2
print(solution.unique_paths_memo(3, 2))
print(solution.unique_paths_memo(3, 7))
print(solution.unique_paths_tabular(3, 2))
print(solution.unique_paths_tabular(3, 7))
print(solution.min_path_sum_memo([[1,3,1],[1,5,1],[4,2,1]]))
print(solution.min_path_sum_memo([[1,2,3],[4,5,6]]))
print(solution.min_path_sum_tabular([[1,3,1],[1,5,1],[4,2,1]]))
print(solution.min_path_sum_tabular([[1,2,3],[4,5,6]]))

#dp technique 3
print(solution.longest_common_subsequence("abcde", "abc"))
print(solution.edit_distance("horse", "ros"))

#dp technique 4
print(solution.house_robber([1,2,3,1]))
print(solution.jump_game_memo([2,3,1,1,4]))

#dp technique 5
print(solution.knight_probability_memo(3, 2, 0, 0))
print(solution.dice_roll(2, 6, 7))