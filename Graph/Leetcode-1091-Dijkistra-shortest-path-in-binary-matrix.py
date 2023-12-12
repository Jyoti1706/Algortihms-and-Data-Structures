"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
BFS Approach

"""
import collections
import math
from typing import List
import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """

        :param grid:
        :return: no. of steps to reach from 0,0 to m-1,n-1 (if no path exists return -1)
        :Logic: via Dijkstra using minheap
            pre-requisite:
                1. create results matrix and initialize cell to math.inf
                2. create direction list
                3. create a isSafe function to check index
            1. Create MinHeap and Push (0,0)'s (distance, node) => (0, (0,0))
            2. loop minheap, check results matrix for that cell, if cell distance in more than current node distance
               is assigned
            3. process all neighbouring directions using directions list, if not marked and is safe then push to minheap
            4. return -1 if results[m - 1][n - 1] == math.inf otherwise results[m - 1][n - 1] + 1
        """
        m = len(grid)
        n = len(grid[0])
        results = [[math.inf for _ in range(n)] for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        if m == 0 or n == 0 or grid[0][0] == 1:
            return -1

        def isSafe(idx_x, idx_y):
            return 0 <= idx_x < m and 0 <= idx_y < n

        minheap = [(0, (0, 0)),]
        heapq.heapify(minheap)
        while minheap:
            dis, cord = heapq.heappop(minheap)
            x = cord[0]
            y = cord[1]
            results[x][y] = min(results[x][y], dis)
            for dir in directions:
                x_ = x + dir[0]
                y_ = y + dir[1]
                if isSafe(x_, y_) and grid[x_][y_] == 0 and results[x_][y_] > dis + 1:
                    heapq.heappush(minheap, (dis + 1, (x_, y_)))
                    grid[x_][y_] = 1
        return -1 if results[m - 1][n - 1] == math.inf else results[m - 1][n - 1] + 1


obj = Solution()
# grid = [[0, 1], [1, 0]]
# print(obj.shortestPathBinaryMatrix(grid))
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(obj.shortestPathBinaryMatrix(grid))
grid = [[0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0]]
print(obj.shortestPathBinaryMatrix(grid))
