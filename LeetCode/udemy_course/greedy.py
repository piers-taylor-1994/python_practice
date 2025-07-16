class Solution:
    def coin_change(self, coins: list[int], target):
        coins.sort(reverse=True)
        coins_used = []

        while target > 0:
            for coin in coins:
                if target - coin >= 0:
                    target -= coin
                    coins_used.append(coin)
                    break
        
        return coins_used


solution = Solution()

print(solution.coin_change([1, 5, 10, 25], 47))