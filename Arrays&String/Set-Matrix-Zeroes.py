"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])

        i = 0
        j = 0
        zeros = []
        for m in range(row):
            for n in range(col):
                if matrix[m][n] == 0:
                    zeros.append([m, n])
        print(zeros)
        for li in zeros:
            r, c = li
            print(r, c)
            i = 1
            j = 1
            while r - i >= 0 or r + j < row:

                if r - i >= 0:
                    matrix[r - i][c] = 0
                    i += 1
                if r + j < row:
                    matrix[r + j][c] = 0
                    j += 1
            i = 1
            j = 1
            while c - i >= 0 or c + j < col:

                if c - i >= 0:
                    matrix[r][c - i] = 0
                    i += 1
                if c + j < col:
                    matrix[r][c + j] = 0
                    j += 1
        return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
ob = Solution()
print(ob.setZeroes(matrix))
