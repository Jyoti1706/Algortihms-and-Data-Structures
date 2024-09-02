"""
https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/description/

"""

class Solution:
    def countOfPairs(self, n, x, y):
        grid = [[1000] * (n + 1) for _ in range(n + 1)]

        for j in range(1, n):
            grid[j][j+1] = 1
            grid[j+1][j] = 1
        grid[x][y] = 1
        grid[y][x] = 1

        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

        result = [0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    val = grid[i][j]
                    result[val - 1] += 1

        return result


if __name__ == "__main__":
    obj = Solution()
    n = 3
    x = 1
    y = 3
    print(obj.countOfPairs(n,x,y))
    n = 5
    x = 2
    y = 4
    print(obj.countOfPairs(n,x,y))
