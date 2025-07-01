class Solution:
    """
    function backtrack(current_state):
        if is_goal(current_state):
            record_solution(current_state)
            return

        for choice in get_valid_choices(current_state):
            make_choice(current_state, choice)
            backtrack(current_state)
            undo_choice(current_state, choice)
    """
    def generate_all_subsets(self, nums):
        solutions = []

        def rec(position, path):
            solutions.append(path[:])

            for i in range(position, len(nums)):
                path.append(nums[i])
                rec(i + 1, path)
                path.pop()

        rec(0, [])
        return solutions

    def sudoku_solver(self, board):
        pass

solution = Solution()

print(solution.generate_all_subsets([1,2,3]))

print(solution.sudoku_solver([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))