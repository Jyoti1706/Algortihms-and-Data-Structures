class Solution:
    def maxAreaOfIsland(self, grid):
        ROW = len(grid)
        COLUMN = len(grid[0])
        visited = set()

        def dfs(row, column):
            # print(row, column)
            if (row < 0 or column < 0 or row == len(grid) or column == len(grid[0]) or grid[row][column] == 0
                    or (row, column) in visited):
                return 0
            visited.add((row, column))
            return 1 + dfs(row - 1, column) + dfs(row + 1, column) + dfs(row, column - 1) + dfs(row, column + 1)

        area = 0
        for r in range(ROW):
            for c in range(COLUMN):
                area = max(area, dfs(r, c))

        return area


obj = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(obj.maxAreaOfIsland(grid))
