'''
https://leetcode.com/problems/unique-paths/?envType=study-plan-v2&id=dynamic-programming
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            grid[i][0] =1
        print(grid)
        for i in range(0,m):
            grid[0][i] =1
        #print(grid)
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
        print(grid)
        return grid[n-1][m-1]