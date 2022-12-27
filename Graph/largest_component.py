def longestComponent(graphs):
    visited = set()
    longest = 0
    for key in graphs.keys():
        comp_size= traversal(graphs, key, visited)
        if comp_size>longest:
            longest=comp_size
    return longest


def traversal(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size=1
    for neighbour in graph[current]:
        size = size+traversal(graph, neighbour, visited)

    return size

test_00 = {0: [8, 1, 5],
           1: [0],
           5: [0, 8],
           8: [0, 5],
           2: [3, 4],
           3: [2, 4],
           4: [3, 2]}

print(longestComponent(test_00))