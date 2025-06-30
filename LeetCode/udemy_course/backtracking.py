class Solution:
    def sudoku_solver(self, board):
        def is_valid(r, c, val):
            # Row check
            if val in board[r]:
                return False
            # Column check
            if val in [board[i][c] for i in range(9)]:
                return False
            # 3x3 grid check
            start_row, start_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val:
                        return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(r, c, num):
                                board[r][c] = num
                                if solve():
                                    return True
                                board[r][c] = "."  # backtrack
                        return False  # if no valid number found
            return True  # board is complete

        solve()
        return board


solution = Solution()
print(solution.sudoku_solver([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))