class Solution:
    # def numIslands(self, grid):
    #     ROW = len(grid)
    #     COLUMN = len(grid[0])
    #     visited = set()
    #     count = 0
    #
    #     def dfs(grid, row, column):
    #         #print(row, column)
    #         if (row < 0 or column < 0 or row == len(grid) or column == len(grid[0]) or grid[row][column] == "0"
    #                 or (row, column) in visited):
    #             return
    #         visited.add((row, column))
    #         dfs(grid, row - 1, column)
    #         dfs(grid, row + 1, column)
    #         dfs(grid, row, column - 1)
    #         dfs(grid, row, column + 1)
    #
    #     for r in range(ROW):
    #         for c in range(COLUMN):
    #             if grid[r][c] == "1":
    #                 if (r, c) not in visited:
    #                     dfs(grid, r, c)
    #                     count += 1
    #     return count
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        count = 0
        visited = set()

        def dfs(grid, r, c, visited):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == "0":
                return False
            if (r, c) in visited:
                return False
            visited.add((r, c))
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c - 1, visited)
            dfs(grid, r + 1, c, visited)
            dfs(grid, r, c + 1, visited)
            return True

        for r in range(row):
            for c in range(col):
                if dfs(grid, r, c, visited):
                    count += 1
        return count


obj = Solution()
grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

#print(obj.numIslands(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid =[["1","0","1","1","0","1","1"]]
print(obj.numIslands(grid))
