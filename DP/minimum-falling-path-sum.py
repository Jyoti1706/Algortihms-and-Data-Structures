import math
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [0] * (len(matrix))
        for row in matrix[::-1]:
            results =dp.copy()
            for i, n in enumerate(row):
                chk_idx=[]
                if i == 0:
                    if i+1 == len(row):
                        chk_idx =[i]
                    else:
                        chk_idx = [i,i+1]
                elif i == len(row)-1:
                    chk_idx = [i-1,i]
                else:
                    chk_idx = [i-1,i,i+1]
                minimum= math.inf
                for k in chk_idx:
                    minimum = min(minimum, n+results[k])
                #print(minimum)
                dp[i] =minimum
        results =dp
        return min(results)

# matrix = [[2,1,3],[6,5,4],[7,8,9]]
obj = Solution()
# matrix = [[-19,57],[-40,-5]]
matrix = [[-57]]
print(obj.minFallingPathSum(matrix))