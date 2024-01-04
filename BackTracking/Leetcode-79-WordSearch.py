"""
https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def find(i, j, idx, word):
            if idx == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "$":
                return False
            if board[i][j] != word[idx]:
                return False
            temp = board[i][j]  # storing char to backtrack in case of word doesn't exist
            board[i][j] = "$"  # way to mark a cell as visited
            for dir in directions:
                i_ = i + dir[0]
                j_ = j + dir[1]
                if find(i_, j_, idx + 1, word):
                    return True
            board[i][j] = temp  # changing back the character
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0, word):
                    return True
        return False


if __name__ == "__main__":
    obj = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(obj.exist(board,word))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(obj.exist(board, word))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(obj.exist(board, word))