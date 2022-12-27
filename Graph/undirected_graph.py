edges = [['i', 'j'],
         ['k', 'i'],
         ['m', 'k'],
         ['k', 'l'],
         ['o', 'n']]


def build_graph(edges):
    graph = {}
    for edge in edges:
        try:
            graph[edge[0]].append(edge[1])
        except:
            graph[edge[0]] = [edge[1], ]
        try:
            graph[edge[1]].append(edge[0])
        except:
            graph[edge[1]] = [edge[0], ]
    return graph

def undirected_graph_path(edges, node1, node2):
    graph = build_graph(edges)
    visited=set()
    return hash_path(graph, node1, node2,visited)

def hash_path(graph, src, dest, visited):
    if src == dest:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        if hash_path(graph, neighbour, dest,visited):
            return True
    return False


graph = build_graph(edges)
print(graph)
print(undirected_graph_path(edges,'i','k'))
print(undirected_graph_path(edges,'i','o'))