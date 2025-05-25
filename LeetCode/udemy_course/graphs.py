from collections import deque

class Solution:
    def traversal_bfs(self, graph):
        result = []
        seen = {}
        queue = deque([0])
        seen[0] = True

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for connection in graph[vertex]:
                if not connection in seen:
                    queue.append(connection)
                    seen[connection] = True
        
        return result

solution = Solution()
print(solution.traversal_bfs([
    [1, 3],
    [0],
    [3, 8],
    [0, 4, 5, 2],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]))