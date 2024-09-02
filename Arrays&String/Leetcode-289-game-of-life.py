class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def count_neighbour(row, col):
            nei = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (i == row and j == col) or i < 0 or col < 0 or i == ROWS or col == COLS:
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for r in range(ROWS):
            for c in range(COLS):
                n = count_neighbour(r, c)
                if board[r][c]:
                    if n in [2, 3]:
                        board[r][c] = 3
                elif n == 3:
                    board[r][c] = 2
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
