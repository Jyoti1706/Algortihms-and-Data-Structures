import numpy as np
direction =[[-1, 0],
             [0, 1],
             [1, 0],
             [0, -1]]

def DFS_2D_Array(matrix):

    row = len(matrix)
    col = len(matrix[0])
    seen = np.zeros((row,col))
    #print(seen)
    results=[]
    dfs(matrix,0,0,seen,results)
    return results

def BFS_2D_Array(matrix):

    row = len(matrix)
    col = len(matrix[0])
    seen = np.zeros((row,col))
    #print(seen)
    results=[]
    bfs(matrix,2,2,seen,results)
    return results

def dfs(matrix, row, col, seen, values):
     if (row <0) or (col < 0) or (row >= len(matrix)) or (col >= len(matrix[0])) or (seen[row][col]==1):
         return
     values.append(matrix[row][col])
     seen[row][col]=1
     for i in range(len(direction)):
         current_direction = direction[i]
         dfs(matrix,row+current_direction[0], col+current_direction[1], seen, values)
     return values

def bfs(matrix, row,col, seen, values):
    queue = [(row,col)]
    while len(queue)>0:
        row ,col = queue.pop(0)
        if not ((seen[row][col] == 1)):
            values.append(matrix[row][col])
            seen[row][col]=1
        for i in range(len(direction)):
            r = row+direction[i][0]
            c = col+direction[i][1]
            if (r < 0) or (c < 0) or (r >= len(matrix)) or (c >= len(matrix[0])) or (seen[r][c] == 1):
                continue

            queue.append((r,c))
    return values


matrix = [[1 ,2 ,3 ,4 ,5 ],
          [6 ,7 ,8 ,9 ,10],
          [11,12,13,14,15],
          [16,17,18,19,20]]
print(DFS_2D_Array(matrix))
#print(BFS_2D_Array(matrix))