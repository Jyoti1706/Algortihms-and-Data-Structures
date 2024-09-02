"""
https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=dynamic-programming

"""
import math


class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(m):
            for col in range(n):
                left = math.inf
                down = math.inf
                if row - 1 > -1:
                    down = dp[row - 1][col]
                if col -1 > -1:
                    left = dp[row][col - 1]
                if left == down == math.inf:
                    dp[row][col] = grid[row][col]
                else:
                    dp[row][col] = grid[row][col] + min(down, left)
        return dp[-1][-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    obj = Solution()
    print(obj.minPathSum(grid))
    grid = [[1, 2, 3], [4, 5, 6]]
    print(obj.minPathSum(grid))
