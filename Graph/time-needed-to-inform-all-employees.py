def total_time_to_inform(headID, managers, informTime):
    adjlist_manager = {}
    for i in range(len(managers)):
        adjlist_manager[i]=[]
    for e in range(len(managers)):
        manager = managers[e]
        if manager == -1:
            continue
        adjlist_manager[manager].append(e)
    print(adjlist_manager)
    return dfs(headID, adjlist_manager, informTime)

def dfs(currentID, graph, inform_time):
    if len(graph[currentID]) == 0:
        return 0
    max_time= 0
    for emp in graph[currentID]:
        max_time = max(max_time, dfs(emp, graph, inform_time))
    return max_time+inform_time[currentID]

headID = 4
managers = [2, 2, 4, 6, -1, 4, 4, 5]
informTime = [0, 0, 4, 0, 7, 3, 6, 0]

print(total_time_to_inform(headID, managers, informTime))