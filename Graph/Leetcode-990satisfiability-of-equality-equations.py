"""
You are given an array of strings equations that represent relationships between variables where each string
equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names to satisfy all the given equations, or false
otherwise.

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

"""

class DisjointSet:
    def __init__(self, n=26):
        self.rank = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if ulp_v == ulp_u:
            return
        if self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if ulp_v == ulp_u:
            return
        if self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        ds = DisjointSet()
        for s in equations:
            if s[1] == "=":
                ds.unionByRank(ord(s[0])-97, ord(s[3])-97)

        for s in equations:
            if s[1] == "!":
                first = s[0]
                second = s[3]
                parentFirst = ds.findParent(ord(first)-97)
                parentSecond = ds.findParent(ord(second)-97)
                if parentSecond == parentFirst:
                    return False
        return True


if __name__ == "__main__":
    obj = Solution()
    equations = ["a==b","b!=a"]
    print(obj.equationsPossible(equations))
    equations = ["b==a", "a==b"]
    print(obj.equationsPossible(equations))
