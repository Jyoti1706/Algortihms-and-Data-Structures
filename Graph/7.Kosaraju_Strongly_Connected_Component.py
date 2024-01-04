# User function Template for python3

class Solution:

    # Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        stack = []
        visited = [False for _ in range(V)]

        def topoOrder_dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    topoOrder_dfs(nei)
            stack.append(node)

        # 1. populate traversal stack (DFS as topological sort
        for i in range(V):
            if not visited[i]:
                topoOrder_dfs(i)

        # 2. Reverse Graph
        adjReverse = {node:[] for node in range(V)}
        for u in range[V]:
            for v in adj[u]:
                adjReverse[v].append(u)

        # 3. Call dfs on stack order
        scc = 0
        visited = [False for _ in range(V)]

        def dfsTraversal(node):
            visited[node] = True

            for v in adjReverse[node]:
                if not visited[v]:
                    dfsTraversal(v)

        while stack:
            node = stack.pop(-1)
            if not visited[node]:
                dfsTraversal(node)
                scc += 1
        return scc
