class Solution():
    def show_answer(self, output, answer):
        return f"{output} Answer correct: {output == answer}"
    
    def two_sum(self, nums, target) -> list[int]:
        if len(nums) == 2:
            return [0, 1]
        pos_idx = {}
        for i, num in enumerate(nums):
            number_to_find = target - num
            if number_to_find in pos_idx:
                return [pos_idx[number_to_find], i]
            pos_idx[num] = i
    def three_sum(self, nums) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    while True:
                        left += 1
                        if left >= right or nums[left] != nums[left - 1]:
                            break
                    while True:
                        right -= 1
                        if left >= right or nums[right] != nums[right + 1]:
                            break

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return ans
    def four_sum(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        while True:
                            left += 1
                            if left >= right or nums[left] != nums[left - 1]:
                                break
                        while True:
                            right -= 1
                            if left >= right or nums[right] != nums[right + 1]:
                                break
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return ans



solution = Solution()

#two sum always only 1 answer
print(f"{solution.show_answer(solution.two_sum([2,7,11,15], 9), [0, 1])}")
print(f"{solution.show_answer(solution.two_sum([3,2,4], 6), [1, 2])}")
print(f"{solution.show_answer(solution.two_sum([3,3], 6), [0, 1])}")

#three sum distinct tripletser right ans)
print(f"{solution.show_answer(solution.three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])}")
print(f"{solution.show_answer(solution.three_sum([0, 1, 1]), [])}")
print(f"{solution.show_answer(solution.three_sum([0,0,0]), [[0,0,0]])}")

#four sum unique quadruplets
print(f"{solution.show_answer(solution.four_sum([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])}")
print(f"{solution.show_answer(solution.four_sum([2,2,2,2,2], 8), [[2,2,2,2]])}")