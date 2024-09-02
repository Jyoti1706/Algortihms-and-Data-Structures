from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid)

        visited = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

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





grid = [[2,1,1],[1,1,0],[0,1,1]]