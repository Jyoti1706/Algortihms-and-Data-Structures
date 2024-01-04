import math
from os import *
from sys import *
from collections import *
from math import *

from typing import *

'''
 https://www.codingninjas.com/studio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
'''


def frogJump(n: int, heights: List[int]) -> int:
    # Write your code here.
    dp = [-1 for _ in range(n + 1)]

    def recursion(idx):
        if idx == 0:
            return 0
        if not (dp[idx] == -1):
            return dp[idx]
        left = recursion(idx - 1) + abs(heights[idx] - heights[idx - 1])
        right = math.inf
        if idx > 1:
            right = recursion(idx - 2) + abs(heights[idx] - heights[idx - 2])
        dp[idx] = min(left, right)
        return dp[idx]

    return recursion(n - 1)


def frogJump_Tabulation(n: int, heights: List[int]) -> int:
    # Write your code here.
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(1, n):
        fs = dp[i - 1] + abs(heights[i] - heights[i - 1])
        ss = math.inf
        if i > 1:
            ss = dp[i - 2] + abs(heights[i] - heights[i - 2])
        dp[i] = min(fs, ss)
    return dp[n - 1]


print(frogJump(4, [10, 20, 30, 10]))
print(frogJump(8, [7, 4, 4, 2, 6, 6, 3, 4]))
