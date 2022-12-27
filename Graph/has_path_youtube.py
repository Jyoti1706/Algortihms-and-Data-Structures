def has_path(graph, src, dest):
    if src == dest:
        return True
    neighbours = graph[src]
    for neighbour in neighbours:
        if has_path(graph, neighbour, dest):
            return True
    return False


graph = {'f':['g','i'], 'g':['h'], 'i':['g','k'],'j':['i'],'k':[],'h':[]}
print(has_path(graph, 'f','k'))
print(has_path(graph, 'k','h'))