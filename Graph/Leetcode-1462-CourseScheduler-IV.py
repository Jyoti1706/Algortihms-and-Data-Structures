from collections import defaultdict
from typing import *


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]):
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(course):
            if course not in prereqmap:
                prereqmap[course] = set()
                for preReqCrs in adj[course]:
                    prereqmap[course] |= dfs(preReqCrs)  # union operation
                prereqmap[course].add(course)
            return prereqmap[course]

        prereqmap = {}  # map course to there indirect course hashset
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqmap[v])
        return res
