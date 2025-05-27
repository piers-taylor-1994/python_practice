from collections import deque

class Solution:
    def traversal_bfs(self, graph):
        if not graph:
            return []
        
        result = []
        seen = set()
        queue = deque([0])
        seen.add(0)

        while queue:
            node = queue.popleft()
            result.append(node)

            for edge in graph[node]:
                if edge not in seen:
                    queue.append(edge)
                    seen.add(edge)
        
        return result
    
    def traversal_dfs(self, graph):
        pass

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
print(solution.traversal_dfs([
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