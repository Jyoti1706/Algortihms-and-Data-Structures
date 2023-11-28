class Solution:
    def findCenter(self, edges):
        graph = {}
        for e1,e2 in edges:
            if e1 in graph.keys():
                graph[e1].append(e2)
            else:
                graph[e1] = [e2,]

            if e2 in graph.keys():
                graph[e2].append(e1)
            else:
                graph[e2] = [e1,]

        for key in graph:
            if len(graph[key])== len(edges):
                return key


edges = [[1,2],[5,1],[1,3],[1,4]]
obj = Solution()
print(obj.findCenter(edges))

edges = [[1,2],[2,3],[4,2]]
print(obj.findCenter(edges))
