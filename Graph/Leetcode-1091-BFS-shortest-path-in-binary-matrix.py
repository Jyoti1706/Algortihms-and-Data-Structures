"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
BFS Approach

"""
import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """

        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1],[-1,1],[1,-1]]
        if m == 0 or n == 0 or grid[0][0] == 1:
            return -1

        def isSafe(idx_x, idx_y):
            return 0 <= idx_x < m and 0 <= idx_y < n

        queue = collections.deque()
        queue.append((0, 0))
        grid[0][0] = 1
        level = 0
        while queue:
            size = len(queue)
            level += 1
            while size:
                size -= 1
                curr = queue.popleft()
                x = curr[0]
                y = curr[1]
                if x == m - 1 and y == n - 1:
                    return level

                for dir in directions:
                    x_ = x + dir[0]
                    y_ = y + dir[1]

                    if isSafe(x_, y_) and grid[x_][y_] == 0:
                        queue.append((x_, y_))
                        grid[x_][y_] = 1
        return -1


obj = Solution()
# grid = [[0, 1], [1, 0]]
# print(obj.shortestPathBinaryMatrix(grid))
# grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
# print(obj.shortestPathBinaryMatrix(grid))
grid = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
print(obj.shortestPathBinaryMatrix(grid))
