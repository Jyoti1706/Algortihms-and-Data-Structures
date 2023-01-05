def numIslands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if exploreland(grid, r, c, visited):
                count += 1

    return count


def exploreland(grid, r, c, visited):
    rowinbound = 0 <= r and r < len(grid)
    colinbound = 0 <= c and c < len(grid[0])
    if (not rowinbound) or (not colinbound):
        return False
    if grid[r][c] == "0":
        return False
    pos = (r, c)
    if pos in visited:
        return False
    visited.add((r, c))

    exploreland(grid, r - 1, c, visited)
    exploreland(grid, r + 1, c, visited)
    exploreland(grid, r, c - 1, visited)
    exploreland(grid, r, c + 1, visited)
    return True


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
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# print(numIslands(grid))
print(numIslands(grid2))
# print(numIslands(grid3))
