class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: set() for i in range(numCourses)}
        for p in prerequisites:
            graph[p[1]].add(p[0])
        # 1: visited, 0 no visited, -1 in progress
        visit = {i: 0 for i in range(numCourses)}

        # post-order DFS. The key in toplogical sort
        def dfs(n):
            if visit[n] == 1:
                return True
            if visit[n] == -1:
                return False
            visit[n] = -1
            for neighbor in graph[n]:
                if not dfs(neighbor):
                    return False
            visit[n] = 1
            return True

        for i in graph:
            if not dfs(i):
                return False  # there is a cycle
        return True



obj = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(obj.canFinish(numCourses,prerequisites))

numCourses = 2
prerequisites = [[1,0]]
print(obj.canFinish(numCourses,prerequisites))

numCourses = 6
prerequisites = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [3, 0]]
print(obj.canFinish(numCourses, prerequisites))
