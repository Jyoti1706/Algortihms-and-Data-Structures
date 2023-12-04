from collections import deque
class Solution:
    def isBipartite(self, graph):
        color = [0 for _ in range(len(graph))] #map node i ->odd=1, even =-1


        for i in range(len(graph)):
            if color[i]==0:
                color[i]=1
                dq = deque()
                dq.append(i)
                while dq:
                    node = dq.popleft()
                    for n in graph[node]:
                        if color[n] == color[node]:
                            return False
                        else:
                            if color[n]==0:
                                dq.append(n)
                                color[n]=-color[node]
        return True


graph = [[1,3],[0,2],[1,3],[0,2]]
obj = Solution()
print(obj.isBipartite(graph))
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(obj.isBipartite(graph))


