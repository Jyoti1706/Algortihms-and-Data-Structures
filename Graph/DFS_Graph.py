def create_graph_AL(vertices, list):
    adj_list = {vertice: list[vertice] for vertice in range(vertices)}
    return adj_list


from collections import deque
from queue import Queue


def DFS(graph, node, visited: set, result: list):
    if node in visited:
        return
    visited.add(node)
    result.append(node)
    for neighbour in graph[node]:
        DFS(graph, neighbour, visited, result)
    return result


def BFS(graph, start, visited: set, result: list):
    queue = deque()
    queue.append(start)
    visited.add(start)
    result.append(start)
    while len(queue) > 0:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(neighbour)
            result.append(neighbour)
    return result


V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
graph = create_graph_AL(V, adj)
print(graph)

print(DFS(graph, 0, visited=set(), result=[]))
print(BFS(graph, 0, visited=set(), result=[]))

V = 4
adj = [[1, 3], [2, 0], [1], [0]]
graph = create_graph_AL(V, adj)
print(graph)

print(DFS(graph, 0, visited=set(), result=[]))
print(BFS(graph, 0, visited=set(), result=[]))
