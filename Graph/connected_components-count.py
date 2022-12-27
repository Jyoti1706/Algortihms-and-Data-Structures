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
