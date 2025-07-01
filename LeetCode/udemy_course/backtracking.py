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
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_spaces = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(num)
                else:
                    empty_spaces.append((r, c))

        def rec():
            for row, col in empty_spaces:
                for num in map(str, range(1, 10)):
                    box_index = (row // 3) * 3 + (col // 3)
                    if num not in rows[row] and num not in cols[col] and num not in boxes[box_index]:
                        board[row][col] = num
                        rows[row].add(num)
                        cols[col].add(num)
                        boxes[box_index].add(num)
                        empty_spaces.remove((row, col))

                        if rec():
                            return True
                                
                        board[row][col] = "."
                        rows[row].remove(num)
                        cols[col].remove(num)
                        boxes[box_index].remove(num)
                        empty_spaces.append((row, col))
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