'''
https://leetcode.com/problems/minimum-path-sum/

'''

grid = [[1,3,1],[1,5,1],[4,2,1]] #[[1,2,3],[4,5,6]]
m = len(grid[0])
n = len(grid)

for i in range(1, m):
    grid[0][i] = grid[0][i-1]+grid[0][i]
print(grid[0])
print(n)
for i in range(1,n):
    grid[i][0] = grid[i][0]+grid[i-1][0]
print(grid)
for i in range(1, n):
    for j in range(1, m):
        print(f"i -- {i},j -- {j}")
        grid[i][j] = min(grid[i-1][j] , grid[i][j - 1])+grid[i][j]
print(grid[-1][-1])
