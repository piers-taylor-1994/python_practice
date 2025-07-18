class Solution:
    """
    -Usually have to do some kind of sorting at the beginning (not always obviously sorted ascending, can be descending, or sorted from end instead of start)
    -Greedy algorithms attempt to construct an optimal solution step-by-step by choosing the most beneficial 
        option at each point—without reconsidering previous choices.
    -Usually use a loop (for loops, pointers etc)
    -Usually initialise variable/s at the beginning to track current state, count etc
    """
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
    
    def jump_game(self, nums):
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
        
        return True
    
    def minimum_coins_change(self, coins:list[int], amount):
        coins.sort(reverse=True)

        total = 0
        count = 0
        marker = 0
        while total < amount:
            if coins[marker] + total <= amount:
                total += coins[marker]
                count += 1
            else:
                marker += 1

                if marker >= len(coins):
                    break
        
        return count
    
    def minimum_platforms_needed(self, arrival, departure):
        arrival.sort()
        departure.sort()
        i = 0
        j = 0
        platforms_needed = 0
        min_platforms = 0

        while i < len(arrival):
            if arrival[i] < departure[j]:
                platforms_needed += 1
                min_platforms = max(min_platforms, platforms_needed)
                i += 1
            else:
                platforms_needed -= 1
                j += 1
        
        return min_platforms
    
    def max_activities(self, start, end):
        start_end = [(start[i], end[i]) for i in range(len(start))]
        start_end.sort(key=lambda x:x[1])

        current_end = 0
        max_activities = 0

        for start, end in start_end:
            if start >= current_end:
                max_activities += 1
                current_end = end
        
        return max_activities



solution = Solution()

print(solution.coin_change([1, 5, 10, 25], 47))

print(solution.max_non_overlapping_meetings([[1, 4], [2, 3], [3, 5], [7, 9]]))

print(solution.max_number_of_coins_picked([2, 4, 1, 6, 3, 5]))

print(solution.assign_cookies([1,2,3], [1,1]))
print(solution.assign_cookies([1,2], [2,3,4]))

print(solution.jump_game([2,3,1,1,4]))

print(solution.minimum_coins_change([1, 3, 4], 6))

print(solution.minimum_platforms_needed([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))

print(solution.max_activities([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))