class Solution:
    def traversal_dfs(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return []
        
        DIRECTIONS = [
            [-1, 0], #up
            [0, 1], #right
            [1, 0], #down
            [0, -1] #left
        ]

        seen = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        
        def dfs(matrix, row, col, seen, result):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
                return
            
            result.append(matrix[row][col])
            seen[row][col] = True
            
            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc

                dfs(matrix, new_row, new_col, seen, result)

        result = []
        dfs(matrix, 0, 0, seen, result)
        return result

solution = Solution()
print(solution.traversal_dfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))