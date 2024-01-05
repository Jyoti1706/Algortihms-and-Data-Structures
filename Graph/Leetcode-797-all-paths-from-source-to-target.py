from typing import List


class Solution:
    def allPathsSourceTarget(self, graph):
        adj_lst = {i: [] for i in range(len(graph))}
        source = 0
        target = len(graph) - 1
        for i, edge in enumerate(graph):
            for e in edge:
                adj_lst[i].append(e)

        def dfs(u, target, temp):
            temp.append(u)
            if u == target:
                result.append(temp.copy())
            else:
                for v in graph[u]:
                    dfs(v, target, temp)
            temp.pop()

        result = []
        temp = []
        dfs(source, target, temp)
        return result


if __name__ == "__main__":
    obj = Solution()
    graph = [[1, 2], [3], [3], []]
    print(obj.allPathsSourceTarget(graph))
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(obj.allPathsSourceTarget(graph))
