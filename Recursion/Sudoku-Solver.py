"""
https://leetcode.com/problems/sudoku-solver/

"""


def isValidDigit(val,row,col,board):
    rowvalid = val not in board[row]
    colvalid = val not in map(lambda r: r[col], board)
    if not(rowvalid) or not(colvalid):
       return False
    gridrow = row//3
    gridcol = col//3
    for rowidx in range(3):
        for colidx in range(3):
            rowtocheck = gridrow*3+rowidx
            coltocheck = gridcol*3+colidx
            existingval = board[rowtocheck][coltocheck]
            if existingval == val:
                return False
    return True


def tryDigitAtPosition(row, col, board):
    for digit in range(1,10):
        if isValidDigit(str(digit), row,col, board):
            board[row][col] = str(digit)
            if partialSudokuSolver(row,col+1,board):
                return True

    board[row][col] = 0
    return False



def partialSudokuSolver(row,col,board):
    currentrow=row
    currentcol = col
    if currentcol == len(board[row]):
        currentrow += 1
        currentcol = 0
        if currentrow ==  len(board):
            return True

    if board[currentrow][currentcol] == ".":
        return tryDigitAtPosition(currentrow, currentcol, board)

    return partialSudokuSolver(currentrow, currentcol+1, board)


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        partialSudokuSolver(0,0, board)
        return board


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

ob = Solution()
board = ob.solveSudoku(board)
for row in board:
    print(row)
    print()