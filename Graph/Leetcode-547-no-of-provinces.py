from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        count = 0

        def bfs(isConnected, u, visited):
            queue = deque()
            queue.append(u)
            visited[u] = True
            while len(queue) > 0:
                u = queue.popleft()

                for v in range(n):
                    if isConnected[u][v] == 1 and not visited[v]:
                        queue.append(v)
                        visited[v] = True

        for i in range(n):
            if not visited[i]:
                bfs(isConnected, i, visited)
                count += 1
        return count


obj = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(obj.findCircleNum(isConnected))
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(obj.findCircleNum(isConnected))
