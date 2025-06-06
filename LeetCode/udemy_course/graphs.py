from collections import deque
import heapq

class Solution:
    def traversal_bfs(self, graph):
        if not graph:
            return []
        
        result = []
        queue = deque([0])
        seen = set([0])

        while queue:
            node = queue.popleft()
            result.append(node)
            
            for edge in graph[node]:
                if edge not in seen:
                    queue.append(edge)
                    seen.add(edge)
        
        return result
    
    def traversal_dfs(self, graph):
        if not graph:
            return []
        
        def dfs(node, seen, result):
            if node in seen:
                return
            
            result.append(node)
            seen.add(node)

            for edge in graph[node]:
                dfs(edge, seen, result)

        result = []
        seen = set()
        dfs(0, seen, result)
        return result
    
    def num_of_minutes(self, n, headID, manager, informTime):
        if not n:
            return 0
        
        graph = {i:[] for i in range(n)}
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append((i, informTime[i]))

        def dfs(node, time):
            if not time:
                return 0
            
            max_time = 0
            for edge, iTime in graph[node]:
                max_time = max(max_time, dfs(edge, iTime))
            
            return informTime[node] + max_time
        
        return dfs(headID, informTime[headID])

    def can_finish(self, numCourses, prerequisites):
        if numCourses == 1:
            return True
        
        graph = {i:[] for i in range(numCourses)}
        inDegree = {i:0 for i in range(numCourses)}
        for courseA, courseB in prerequisites:
            graph[courseB].append(courseA)
            inDegree[courseA] += 1

        stack = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                stack.append(i)

        count = 0
        while stack:
            node = stack.pop()
            count += 1

            for edge in graph[node]:
                inDegree[edge] -= 1

                if inDegree[edge] == 0:
                    stack.append(edge)
        
        return numCourses == count
    
    def networkDelayTime(self, times, n, k):
        if n == 1:
            return 0
        
        graph = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        shortest_times = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in shortest_times:
                continue

            shortest_times[node] = time

            for edge, travel_time in graph[node]:
                if edge not in shortest_times:
                    heapq.heappush(heap, (travel_time + time, edge))
        
        return max(shortest_times.values()) if len(shortest_times) == n else -1

solution = Solution()
graph_1 = {
    0: [1, 3],
    1: [0],
    2: [3, 8],
    3: [0, 4, 5, 2],
    4: [3, 6],
    5: [3],
    6: [4, 7],
    7: [6],
    8: [2]
}
print(solution.traversal_bfs(graph_1))
print(solution.traversal_dfs(graph_1))

print(solution.num_of_minutes(8, 4, [2,2,4,6,-1,4,4,5], [0,0,4,0,7,3,6,0]))
print(solution.num_of_minutes(11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]))

print(solution.can_finish(2, [[1,0],[0,1]]))
print(solution.can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))

# print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# print(solution.networkDelayTime([[1,2,1]], 2, 2))
# print(solution.networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 2))
# print(solution.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
print(solution.networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]], 5, 3))