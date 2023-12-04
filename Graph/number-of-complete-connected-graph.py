from collections import defaultdict

from Graph.GraphDS import GraphClass


# class Solution:
    # def countCompleteComponents(self, n, edges):
    #     graph = GraphClass(n)
    #     for e in edges:
    #         graph.addEdge(e[0],e[1])
    #     marked = [False for _ in range(n)]
    #     count = 0
    #     for v in range(n):
    #         if not marked[v]:
    #             marked[v] = True
    #             neighbour = graph.adj[v].copy()
    #             if neighbour == []:
    #                 count += 1
    #             else:
    #                 neighbour.append(v)
    #                 nodesv = set(neighbour)
    #                 flag = False
    #                 i = 0
    #                 while i < len(neighbour) and neighbour[i] != v:
    #                     n = neighbour[i]
    #                     if not marked[n]:
    #                         ne = graph.adj[n].copy()
    #                         ne.append(n)
    #                         lst = set(ne)
    #
    #                         if lst == nodesv:
    #                             flag = True
    #                         #marked[n] = True
    #                     i += 1
    #                 if flag:
    #                     count += 1
    #
    #     return count

class Solution:
    def countCompleteComponents(self, n: int, edges):

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):

            component.add(i)
            for child in adj[i]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)

        ans = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                component = set()
                visited.add(i)
                dfs(i)
                if all(len(adj[node]) == len(component) - 1 for node in component):
                    ans += 1

        return ans


obj = Solution()
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(obj.countCompleteComponents(n, edges)==3)

n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
print(obj.countCompleteComponents(n, edges)==1)

n = 4
edges = [[1,0],[2,0],[2,1],[3,1]]#[[1,0],[2,1]]
print(obj.countCompleteComponents(n, edges)==0)

n = 1
edges = []#[[1,0],[2,1]]
print(obj.countCompleteComponents(n, edges)==1)


