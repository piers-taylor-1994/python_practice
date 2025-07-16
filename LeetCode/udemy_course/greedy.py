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
    
    def max_non_overlapping_meetings(self, meetings:list[int, int]):
        meetings.sort(key=lambda meeting: meeting[1])
        count = 0
        end_time = 0

        for start, end in meetings:
            if start >= end_time:
                count += 1
                end_time = end
        
        return count
    
    def max_number_of_coins_picked(self, piles):
        piles.sort(reverse=True)
        coins = 0

        while len(piles) >= 3:
            coins += piles.pop(0)
            piles.pop(0)
            piles.pop()
        
        return coins
    
    def assign_cookies(self, children, cookies):
        children.sort()
        cookies.sort()
        count = 0
        child_num = 0

        for cookie in cookies:
            if cookie >= children[child_num]:
                count += 1
                child_num += 1

                if child_num >= len(children):
                    break
        
        return count


solution = Solution()

print(solution.coin_change([1, 5, 10, 25], 47))

print(solution.max_non_overlapping_meetings([[1, 4], [2, 3], [3, 5], [7, 9]]))

print(solution.max_number_of_coins_picked([2, 4, 1, 6, 3, 5]))

print(solution.assign_cookies([1,2,3], [1,1]))
print(solution.assign_cookies([1,2], [2,3,4]))