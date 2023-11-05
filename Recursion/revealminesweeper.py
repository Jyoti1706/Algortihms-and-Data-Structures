def revealMinesweeper(board, row, column):
    # Write your code here.
    if board[row][column] == "M":
        board[row][column] = "X"
        return board
    if board[row][column] in ['0','1']:
        return board
    minecount = 0
    neighbours = getNeighbour(board, row, column)
    for nrow, ncol in neighbours:
        if board[nrow][ncol] == "M":
            minecount += 1
    if minecount > 0:
        board[row][column] = minecount
    else:
        board[row][column] = "0"
        for nrow, ncol in neighbours:
            if board[nrow][ncol] == "H":
                revealMinesweeper(board, nrow, ncol)

    return board

def getNeighbour(board, row, column):
    directions = [[0, 1], (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbours = []
    for directionrow, directioncol in directions:
        newrow = row + directionrow
        newcol = column + directioncol
        if 0 <= newrow < len(board) and 0<= newcol < len(board[0]):
            neighbours.append([newrow, newcol])
    return neighbours


board = [
    ["H", "H"],
    ["H", "H"]]
row= 0
column= 0

print(revealMinesweeper(board, row,column))