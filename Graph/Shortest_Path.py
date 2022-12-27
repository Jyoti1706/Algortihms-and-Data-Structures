def shortestPath( graph, nodea, nodeb):
    queue=[[nodea,0],]
    visited= set()
    output=[]
    while len(queue)>0:
        node, weight = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        if node == nodeb:
            output.append(weight)
        else:
            for neighbour in graph[node]:
                queue.append([neighbour, weight+1])
    if len(output) == 0:
        return -1
    print(output)
    return min(output)

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

edges = [['w','x'],
         ['x','y'],
         ['z','y'],
         ['z','v'],
         ['w','v']]

graph = build_graph(edges)
print(shortestPath(graph,'w','v'))

