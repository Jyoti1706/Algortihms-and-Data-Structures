import math


class Solution:
    def minTrioDegree(self, n: int, edges):
        adj_mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
        degree = [0 for _ in range(n+1)]
        res = math.inf
        for n1, n2 in edges:
            adj_mat[n1][n2] = 1
            adj_mat[n2][n1] = 1
            degree[n1] += 1
            degree[n2] += 1
        for i in range(1,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if adj_mat[i][j]==1 and adj_mat[j][k]==1 and adj_mat[k][i]==1:
                        res = min(res, degree[i]+degree[j]+degree[k]-6)
        if res == math.inf:
            return -1
        return res
n = 7
edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
obj = Solution()
print(obj.minTrioDegree(n,edges))