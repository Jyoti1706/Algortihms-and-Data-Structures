'''
https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&id=dynamic-programming
'''
import math


class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n=len(grid[0])
        ## making obs as inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = math.inf
        # intializing the grid
        for i in range(m):
            if grid[i][0] == math.inf or (grid[i-1][0] == math.inf and i >0):
                grid[i][0] = math.inf
            else:
                grid[i][0] =1

        for i in range(n):
            if grid[0][i] == math.inf or (grid[0][i-1] == math.inf and i >0):
                grid[0][i] = math.inf
                continue
            grid[0][i] =1
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == math.inf or (grid[i-1][j] == math.inf and grid[i][j-1] == math.inf):
                    grid[i][j] = math.inf
                elif grid[i-1][j] == math.inf :
                    grid[i][j] =grid[i][j-1]
                elif grid[i][j-1] == math.inf:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i][j]+grid[i-1][j]+grid[i][j-1]
        print(0 if grid[-1][-1]==math.inf else grid[-1][-1])
        return 0 if grid[-1][-1]==math.inf else grid[-1][-1]

inp_obstacleGrid = [[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]],[[0,0],[1,1],[0,0]] ,[[1]],[[0,0,0],[0,1,0],[0,0,0]] ,[[0,1,0],[0,0,0],[1,0,0],[0,0,0]]  ]
output = [10,0,0,2,3]
on = Solution()
i=0
assert (on.uniquePathsWithObstacles(inp_obstacleGrid[0]) == output[0])
assert (on.uniquePathsWithObstacles(inp_obstacleGrid[1]) == output[1])
assert (on.uniquePathsWithObstacles(inp_obstacleGrid[2]) == output[2])
assert (on.uniquePathsWithObstacles(inp_obstacleGrid[3]) == output[3])

