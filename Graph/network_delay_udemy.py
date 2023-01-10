'''
https://leetcode.com/problems/network-delay-time/
'''
import math

def networkDelay(times, N, k):
    distance = [float('inf'),]*N
    distance[k-1]=0
    for i in range(N):
        count=0
        for j in range(len(times)):
            source = times[j][0]
            dest = times[j][1]
            weight = times[j][2]
            if distance[source-1]+weight < distance[dest-1]:
                distance[dest-1]=distance[source-1]+weight
                count +=1
        if count==0:
            break

    res = max(distance)
    if res == float('inf'):
        return -1
    return res

t = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6],[3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(networkDelay(t, 5, 1))
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelay(times, 4, 2))
times = [[1,2,1]]
print(networkDelay(times, 2, 1))