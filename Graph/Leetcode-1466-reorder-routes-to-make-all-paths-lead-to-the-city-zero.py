"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
"""


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edges = {(a, b) for a, b in connections}
        neighbours = {city: [] for city in range(n)}
        visit = set()
        change = 0
        for a,b in connections:
            print(a,b)
            neighbours[a].append(b)
            neighbours[b].append(a)
        def dfs(n):
            nonlocal edges, neighbours,change,visit
            for neighbour in neighbours[n]:
                if neighbour in visit:
                    continue
                if (neighbour, n) not  in edges:
                    change += 1
                visit.add(neighbour)
                dfs(neighbour)

        visit.add(0)
        dfs(0)
        return change

obj = Solution()
n = 6
con = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(obj.minReorder(n, con))
# Output: 3
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
#Output: 2
print(obj.minReorder(n, con))