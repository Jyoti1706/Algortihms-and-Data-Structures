"""
https://leetcode.com/problems/similar-string-groups/description/

Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?



Example 1:
===============================================
Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:
===============================================
Input: strs = ["omv","ovm"]
Output: 1
"""


def isSimilar(param, param1):
    n = len(param)
    m = len(param1)
    if n != m:
        return False
    i = 0
    notMatch = 0
    while i < n and notMatch < 3:
        if param[i] != param1[i]:
            notMatch += 1
        i += 1
    return (notMatch == 0) or (notMatch == 2)


class DisjointSet:
    def __init__(self, n):

        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1_parent = self.find(node1)
        node2_parent = self.find(node2)
        if node1_parent == node2_parent:
            return
        if self.rank[node1_parent] > self.rank[node2_parent]:
            self.parent[node2_parent] = node1_parent
        elif self.rank[node2_parent] > self.rank[node1_parent]:
            self.parent[node1_parent] = node2_parent
        else:
            self.parent[node1_parent] = node2_parent
            self.rank[node2_parent] += 1


class Solution:
    def numSimilarGroupsDFS(self, strs):
        """
        1. Create Graph for all string items, items are connected if difference of char is utmost 2.
        2. do a DFS , count of DFS until all node visited is output
        # we can use BFS as well to find connected component
        :param strs:
        :return:
        """
        n = len(strs)
        adj = [[] for _ in range(len(strs))]

        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        visited = [False for _ in range(n)]

        def dfs(i):
            visited[i] = True
            neighbour = adj[i]
            for node in neighbour:
                if not visited[node]:
                    dfs(node)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

    def numSimilarGroupsDU(self, strs):
        n = len(strs)
        adj = [[] for _ in range(len(strs))]

        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        groups = len(strs)
        dsu = DisjointSet(len(adj))
        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]) and dsu.find(i) != dsu.find(j):
                    groups -= 1
                    dsu.union(i, j)
        return groups


if __name__ == "__main__":
    obj = Solution()
    strs = ["tars", "rats", "arts", "star"]
    print(obj.numSimilarGroupsDFS(strs))
    print(obj.numSimilarGroupsDU(strs))
    strs = ["tars", "rats", "arts", "astr", "star", "aaaa"]
    print(obj.numSimilarGroupsDFS(strs))
    print(obj.numSimilarGroupsDU(strs))
