"""You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given
a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices
ai and bi. Return the number of complete connected components of the graph. A connected component is a subgraph of a
graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a
vertex outside the subgraph.
A connected component is said to be complete if there exists an edge between every pair of its vertices.

Example :
draw graph manually:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
"""

"""
Alvin: Youtube

def connectedComponentCount(graphs):
    visited = set()
    count = 0
    for key in graphs.keys():
        if traversal(graphs, key, visited):
            count = count + 1
    return count


def traversal(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbour in graph[current]:
        traversal(graph, neighbour, visited)
    return True


test_00 = {0: [8, 1, 5],
           1: [0],
           5: [0, 8],
           8: [0, 5],
           2: [3, 4],
           3: [2, 4],
           4: [3, 2]}

print(connectedComponentCount(test_00))

"""
from Graph.adjacencyList_undirected import create_GraphList


class Solution:
    def countComponents(self, n, edges):
        # Create adj list, not only node provide in edges will be added
        graph = create_GraphList(edges)
        # initialise id and marked
        id = [-1 for _ in range(n)]
        marked = [False for _ in range(n)]
        # set count as Zero
        count = 0

        def dfs(graph, vertex):
            # marked source as True
            marked[vertex] = True
            # loop through neighbours of source
            for neighbour in graph[vertex]:
                # if not marked process perform DFS on them
                if not marked[neighbour]:
                    id[neighbour] = count
                    dfs(graph, neighbour)

        for v in range(n):
            if not (marked[v]):
                count += 1
                id[v] = count
                if v in graph.keys():
                    dfs(graph, v)
        return count


# Driver code
if __name__ == '__main__':
    obj = Solution()

    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    print(obj.countComponents(n, edges))
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    print(obj.countComponents(n, edges))
