"""
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.

"""
import math
from typing import List


class Solution:
    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        resultant = [0 for _ in range(n)]
        m = len(requests)
        result = math.inf*-1

        def solve(idx, count, n , resultant, requests):
            global result
            if idx >= m:
                allZero = True
                for x in resultant:
                    if x != 0:
                        allZero = False
                    break
                if allZero:
                    result = max(result, count)
                    return
            frombuild = requests[idx][0]
            to = requests[idx][1]

            resultant[frombuild] = -1
            resultant[to] = +1
            solve(idx+1, count+1,n, resultant, requests)
            resultant[frombuild] = 1
            resultant[to] = -1
            solve(idx+1, count,n, resultant, requests)

        solve(0,0,n, resultant, requests)
        return result

    def maximumRequests(self, n: int, requests):
        resultant = [0 for i in range(n)]
        for i, j in requests:
            resultant[i] -= 1
            resultant[j] += 1
        resultant = list(map(abs, resultant))
        return len(requests) - max(resultant)

if __name__ == "__main__":
    obj = Solution()
    n = 5
    requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    print(obj.maximumRequests(n,requests))
    n=3
    requests = [[0, 0], [1, 2], [2, 1]]
    print(obj.maximumRequests(n, requests))