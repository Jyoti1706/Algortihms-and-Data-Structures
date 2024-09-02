"""
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

Solving using DSU

"""
from collections import defaultdict


class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        Brute Force:
        1. Do DFS/BFS for each Query.
        complexity : O(m*(V+E))
        Optimal Approach:
        Using DSU
        1. Sort Edge List
        2. add index to queries and sort the queries array as well
        3. iterate through query, build DSU only till path less than threshold. check parent of src and des after build
        if it is same update result[idx] = True, else False
        :param n: 
        :param edgeList: 
        :param queries: 
        :return: 
        """
        dict1, n = defaultdict(int), len(queries)

        def find(x):
            if x not in dict1:
                return x
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        def union(x, y):
            a, b = find(x), find(y)

            if a != b:
                dict1[b] = a

        # so we will build till query threshold
        edgeList.sort(key=lambda x: x[2])

        i, res = 0, [False] * n
        # add index to queries to avoid index mess-up for result
        for limit, x, y, idx in sorted((q[2], q[0], q[1], i) for i, q in enumerate(queries)):
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[idx] = find(x) == find(y)

        return res


if __name__ == "__main__":
    obj = Solution()
    n = 3
    edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    queries = [[0, 1, 2], [0, 2, 5]]
    print(obj.distanceLimitedPathsExist(n, edgeList, queries))
