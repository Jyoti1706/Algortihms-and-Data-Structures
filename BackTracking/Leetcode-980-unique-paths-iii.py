"""
https://leetcode.com/problems/unique-paths-iii/

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        1. Non obstacle count and find starting point
        2. call backtrack code, grid , count, x, y
        :param grid:
        :return: no. of unique path covering all non obstacle cell
        T(N) = O(3^(m*n))
        """

        m = len(grid)
        n = len(grid[0])
        nonObs = 0
        start = [-1. - 1]
        result = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    nonObs += 1
                if grid[i][j] == 1:
                    start = [i, j]
        nonObs += 1  # extra for starting point as well
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def backTrack(grid, count, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                if count == nonObs:
                    result[0] += 1
                return
            grid[i][j] = -1
            for dir in directions:
                i_ = i + dir[0]
                j_ = j + dir[1]
                backTrack(grid, count + 1, i_, j_)
            grid[i][j] = 0
        count = 0  # cells visited
        backTrack(grid, count, start[0], start[1])
        return result[0]


if __name__ == "__main__":
    obj = Solution()
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    print(obj.uniquePathsIII(grid))
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    print(obj.uniquePathsIII(grid))
