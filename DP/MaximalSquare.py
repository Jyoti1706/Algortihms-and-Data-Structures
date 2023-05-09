'''
https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&id=dynamic-programming
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]):
        m = len(matrix[0])
        n = len(matrix)
        dp = [[0  for _ in range(m)] for _ in range(n)]
        dp[0] = list(map(int, matrix[0]))
        maximum = max(dp[0])
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            if int(matrix[i][0]) > maximum:
                maximum = int(matrix[i][0])

        for i in range(1,n):
            for j in range(1,m):
                if int(matrix[i][j]) == 0:
                    val = 0
                else:
                    val = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+int(matrix[i][j])
                if val>maximum:
                    maximum = val
                dp[i][j] = val
        print(dp)
        return maximum*maximum

matrix = [["1"]] # [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix1 =[["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
obj = Solution()
print(obj.maximalSquare(matrix1))