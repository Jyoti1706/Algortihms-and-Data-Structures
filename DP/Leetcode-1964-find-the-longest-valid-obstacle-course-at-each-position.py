from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if obstacles[i] >= obstacles[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp



if __name__=="__main__":
    obj = Solution()
    obstacles = [1,2,3,2]
    print(obj.longestObstacleCourseAtEachPosition(obstacles))
    obstacles = [3, 1, 5, 6, 4, 2]
    print(obj.longestObstacleCourseAtEachPosition(obstacles))
