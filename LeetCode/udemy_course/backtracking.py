class Solution:
    def soduku_solver(self, board):
        def grid_check(value, r, c):
            if 0 <= r <= 2:
                if 0 <= c <= 2:
                    #grid 0
                    return value not in board[0][0:3] and value not in board[1][0:3] and value not in board[2][0:3]
                elif 3 <= c <= 5:
                    #grid 1
                    pass
                else:
                    #grid 2
                    pass
            elif 3 <= r <= 5:
                if 0 <= c <= 2:
                    #grid 3
                    pass
                elif 3 <= c <= 5:
                    #grid 4
                    pass
                else:
                    #grid 5
                    pass
            else:
                if 0 <= c <= 2:
                    #grid 6
                    pass
                elif 3 <= c <= 5:
                    #grid 7
                    pass
                else:
                    #grid 8
                    pass

        def recursion(row, col):
            if (row, col) == (8, 8):
                return board
            elif board[row][col] != ".":
                if col == 8:
                    return recursion(row + 1, 0)
                else:
                    return recursion(row, col + 1)

            for i in range(1, 10):
                if str(i) not in board[row] and (str(i) not in board[0][col] or str(i) not in board[1][col] or str(i) not in board[2][col] or str(i) not in board[3][col] or str(i) not in board[4][col] or str(i) not in board[5][col] or str(i) not in board[6][col] or str(i) not in board[7][col] or str(i) not in board[8][col]): #and grid_check(str(i), row, col):
                    board[row][col] = str(i)
                    if col == 8:
                        return recursion(row + 1, 0)
                    else:
                        return recursion(row, col + 1)

        return recursion(0, 0)

solution = Solution()
print(solution.soduku_solver([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))