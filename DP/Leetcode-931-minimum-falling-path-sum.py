class Solution:
    def minFallingPathSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        # Start from the first row and move downwards
        for r in range(1, rows):
            for c in range(cols):
                min_above = matrix[r - 1][c]
                if c > 0:
                    min_above = min(min_above, matrix[r - 1][c - 1])
                if c < cols - 1:
                    min_above = min(min_above, matrix[r - 1][c + 1])
                matrix[r][c] += min_above
        return min(matrix[-1])


if __name__ == "__main__":
    obj = Solution()
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(obj.minFallingPathSum(matrix))
    matrix = [[-19, 57], [-40, -5]]
    print(obj.minFallingPathSum(matrix))