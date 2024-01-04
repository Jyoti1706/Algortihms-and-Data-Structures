from typing import *


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 0], [0, -1]]
        ROWS = len(board)
        COLS = len(board[0])
        board[rMove][cMove] = color

        def legal(row, col, color, direc):
            dr, dc = direc
            row, col = row + dr, col + dc
            length = 1
            while 0 <= row < ROWS and 0 <= col < COLS:
                length += 1
                if board[row][col] == ".": return False
                if board[row][col] == color:
                    return length >= 3
                row, col = row + dr, col + dc
            return False

        for d in directions:
            if legal(rMove, cMove, color, d): return True
        return False


obj = Solution()
board = [[".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "W", ".", ".", ".", "."],
         [".", ".", ".", "W", ".", ".", ".", "."],
         [".", ".", ".", "W", ".", ".", ".", "."],
         ["W", "B", "B", ".", "W", "W", "W", "B"],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "W", ".", ".", ".", "."]]

rMove = 4
cMove = 3
color = "B"
print(obj.checkMove(board, rMove, cMove, color))

board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", "B", ".", ".", "W", ".", ".", "."],
         [".", ".", "W", ".", ".", ".", ".", "."],
         [".", ".", ".", "W", "B", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", "B", "W", ".", "."],
         [".", ".", ".", ".", ".", ".", "W", "."],
         [".", ".", ".", ".", ".", ".", ".", "B"]]

rMove = 4
cMove = 4
color = "W"
print(obj.checkMove(board, rMove, cMove, color))
