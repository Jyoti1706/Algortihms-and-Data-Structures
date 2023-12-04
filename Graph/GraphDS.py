# Python3 program for above approach

# Graph class represents a undirected graph
# using adjacency list representation
class GraphClass:

    def __init__(self, V):

        # No. of vertices
        self.V = V
        # initialize adjacency lists
        self.adj = [[] for i in range(self.V)]

    # Add an undirected edge
    def addEdge(self, v, w):

        self.adj[v].append(w)
        self.adj[w].append(v)


# Driver code
if __name__ == '__main__':
    g = GraphClass(6)   #pass no. of edges
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(3, 4)

