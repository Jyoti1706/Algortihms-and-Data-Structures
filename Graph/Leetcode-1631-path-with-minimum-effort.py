import heapq
import math
from typing import List


class Solution:
    def minimumEffortPath(self, heights):
        """

        :param heights:
        :return: no. of steps to reach from 0,0 to m-1,n-1 (if no path exists return -1)
        :Logic: via Dijkstra using minheap with trick to update results data
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
        m = len(heights)
        n = len(heights[0])
        results = [[math.inf for _ in range(n)] for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isSafe(idx_x, idx_y):
            return 0 <= idx_x < m and 0 <= idx_y < n

        minheap = [(0, (0, 0)), ]
        results[0][0] = 0
        heapq.heapify(minheap)
        while minheap:
            diff, cell = heapq.heappop(minheap)
            x = cell[0]
            y = cell[1]

            for dir in directions:
                x_ = x + dir[0]
                y_ = y + dir[1]
                if isSafe(x_, y_):
                    abs_diff = abs(heights[x][y] - heights[x_][y_])
                    diff = max(results[x][y], abs_diff)
                    if diff < results[x_][y_]:
                        results[x_][y_] = diff
                        heapq.heappush(minheap, (int(diff), (x_, y_)))
        return results[m - 1][n - 1]


obj = Solution()
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(obj.minimumEffortPath(heights))  # 2
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
print(obj.minimumEffortPath(heights))  # 1
heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
print(obj.minimumEffortPath(heights))  # 0
