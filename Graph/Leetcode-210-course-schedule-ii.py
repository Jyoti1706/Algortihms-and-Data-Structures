class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
       :type numCourses: int
       :type prerequisites: List[List[int]]
       :rtype: List[int]
       """
        res = []
        graph = {i:set()for i in range(numCourses)}
        for p in prerequisites:
            graph[p[1]].add(p[0])
        # 1: visited, 0 no visited, -1 in progress
        visit = {i:0 for i in range(numCourses)}
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
           res.insert(0, n)
           return True
        for i in graph:
           if not dfs(i):
               return [] # there is a cycle
        return res


obj = Solution()

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(obj.findOrder(n))

