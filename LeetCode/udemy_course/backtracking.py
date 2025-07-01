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
        def is_valid(row, col, num):
            if num in board[row]:
                return False
            elif num in [board[i][col] for i in range(len(board))]:
                return False
            
            search_row = 3 * (row // 3)
            search_col = 3 * (col // 3)

            for r in range(3):
                for c in range(3):
                    if board[r + search_row][c + search_col] == num:
                        return False
            
            return True

        def rec():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if rec():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        rec()
        return board

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