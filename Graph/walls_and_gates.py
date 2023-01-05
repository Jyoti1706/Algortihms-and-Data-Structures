import math

WALL = -1
GATE = 0
EMPTY = 2147483647

direction =[[-1, 0],
             [0, 1],
             [1, 0],
             [0, -1]]
def dfs(matrix, row, col, current_step):
    rowinbound = 0 <= row and row < len(matrix)
    colinbound = 0 <= col and col < len(matrix[0])
    if not(rowinbound) or not(colinbound) or current_step> matrix[row][col]:
        return
    matrix[row][col] = current_step
    for i in range(len(direction)):
        current_direction = direction[i]
        dfs(matrix, row+current_direction[0], col+current_direction[1], current_step+1)

def wallsAndGates(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == GATE:
                dfs(matrix,r,c,0)
    return matrix





testMatrix = [
  [math.inf, -1, 0, math.inf],
  [math.inf, math.inf, math.inf, 0],
  [math.inf, -1, math.inf, -1],
  [0, -1, math.inf, math.inf]
]

testMatrix = wallsAndGates(testMatrix)
print(testMatrix)

