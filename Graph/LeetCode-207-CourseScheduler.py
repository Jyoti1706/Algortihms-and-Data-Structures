class Solution:
    def canFinish(self, numCourses, prerequisites):
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
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
