"""
https://leetcode.com/problems/shortest-bridge/

"""
from collections import deque


class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        m = len(grid[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isSafe(idx_x, idx_y):
            return 0 <= idx_x < m and 0 <= idx_y < n

        visit = set()

        def dfs(r, c):
            if (not isSafe(r, c)) or (not grid[r][c]) or ((r, c) in visit):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0 , deque(visit)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        r_ = r+dr
                        c_ = c+dc
                        if not isSafe(r_,c_) or (r_,c_) in visit:
                            continue
                        if grid[r_][c_]:
                            return res
                        visit.add((r_,c_))
                        q.append((r_,c_))
                res += 1

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()


obj = Solution()
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(obj.shortestBridge(grid))
grid = [[0,1,0],[0,0,0],[0,0,1]]
print(obj.shortestBridge(grid))