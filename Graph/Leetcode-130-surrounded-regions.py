class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        1. Capture Un
        """
        ROWS, COLUMNS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLUMNS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Capture unsorrounded region and mark as T , find border 0 and perform DFS to find connected point
        # and mark as T

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O" and (r in [0, ROWS - 1]) or (c in [0, COLUMNS - 1]):
                    dfs(r, c)

        # 2. Plain Traverse the board and mark all 0 to X
        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Plain Traverse the board and unmark all T to 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "T":
                    board[r][c] = "O"

obj = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj.solve(board)
print(board)