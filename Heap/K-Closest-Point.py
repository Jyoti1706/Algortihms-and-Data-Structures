import heapq
import math


class Solution:
    def kClosest(self, points,k):
        self.closest = []
        res =[]
        for point in points:
            d = self.getdistance(point)
            heapq.heappush(self.closest, (d,point))
        for _ in range(k):
            res.append(heapq.heappop(self.closest)[1])
        return res

    def getdistance(self, point):
        return math.sqrt(pow(point[0],2)+pow(point[1],2))


points = [[3,3],[5,-1],[-2,4]]
k = 2
obj = Solution()
print(obj.kClosest(points,k))