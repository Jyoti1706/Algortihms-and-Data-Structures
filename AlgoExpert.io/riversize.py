import math


def numIslands(grid):
    visited = set()
    res=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreland(grid, r, c, visited)
            if size>0:
                res.append(size)

    return res


def exploreland(grid, r, c, visited):
    rowinbound = 0 <= r and r < len(grid)
    colinbound = 0 <= c and c < len(grid[0])
    if (not rowinbound) or (not colinbound):
        return 0
    if grid[r][c] == 0:
        return 0
    pos = (r, c)
    if pos in visited:
        return 0
    visited.add((r, c))
    size = 1
    size += exploreland(grid, r - 1, c, visited)
    size += exploreland(grid, r + 1, c, visited)
    size += exploreland(grid, r, c - 1, visited)
    size += exploreland(grid, r, c + 1, visited)
    return size


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

grid3 = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
print(numIslands(grid3))
#print(numIslands(grid2))
