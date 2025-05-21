from collections import deque


class Solution:
    def __init__(self):
        self.DIRECTIONS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

    def traversal_bfs(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return []
        
        seen = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        result = []
        queue = deque([(0, 0)])
        seen[0][0] = True

        while queue:
            row, col = queue.popleft()
            result.append(matrix[row][col])

            for dr, dc in self.DIRECTIONS:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and not seen[new_row][new_col]:
                    queue.append((new_row, new_col))
                    seen[new_row][new_col] = True

        return result

    def traversal_dfs(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return []
        
        def dfs(row, col, seen, result):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
                return
            
            result.append(matrix[row][col])
            seen[row][col] = True

            for dr, dc in self.DIRECTIONS:
                new_row = row + dr
                new_col = col + dc
                dfs(new_row, new_col, seen, result)

        seen = []
        for _ in range(len(matrix)):
            inner_seen = []
            for _ in range(len(matrix[0])):
                inner_seen.append(False)
            seen.append(inner_seen)

        result = []
        dfs(0, 0, seen, result)
        return result

    def num_islands(self, matrix):
        def traversal(row, col, seen, matrix):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == "0" or seen[row][col]:
                return
            
            seen[row][col] = True

            for dr, dc in self.DIRECTIONS:
                traversal(dr + row, dc + col, seen, matrix)

        seen = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        num_of_islands = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1" and not seen[i][j]:
                    num_of_islands += 1
                    traversal(i, j, seen, matrix)
        return num_of_islands


solution = Solution()
print(solution.traversal_bfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))
print(solution.traversal_dfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))

print(solution.num_islands([
    ["1","1","1","1","0"], 
    ["1","1","0","1","0"], 
    ["1","1","0","0","0"], 
    ["0","0","0","0","0"]
    ]))
print(solution.num_islands([
    ["1","1","0","0","0"], 
    ["1","1","0","0","0"], 
    ["0","0","1","0","0"], 
    ["0","0","0","1","1"]
    ]))