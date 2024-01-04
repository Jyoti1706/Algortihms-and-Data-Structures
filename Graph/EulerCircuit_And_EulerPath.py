class Solution:
    def isconnected(self, V, adj):
        nonzeroidx = -1
        visited = [False for _ in range(V)]
        for i in range(V):
            if len(adj[i]) > 0:
                nonzeroidx = i
                break

        def DFS(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    DFS(nei)

        DFS(nonzeroidx)

        for i in range(V):
            if visited[i] == False and len(adj[i]) > 0:
                return False
        return True

    def isEulerCircuitExist(self, V, adj):
        # Code here
        if not self.isconnected(V, adj):
            return 0

        oddDegreeVertex = 0
        for i in range(V):
            if len(adj[i])%2 != 0:
                oddDegreeVertex += 1
        if oddDegreeVertex > 2:
            return 0  # Nothing
        if oddDegreeVertex == 2:
            return 1  # Euler path
        return 2  # Euler Circuit


adj = {0:[1],1:[2],2:[1]}
v = 3
obj = Solution()
print(obj.isEulerCircuitExist(v,adj))