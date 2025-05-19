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
        pass

solution = Solution()
print(solution.traversal_dfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))
print(solution.traversal_bfs([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]))