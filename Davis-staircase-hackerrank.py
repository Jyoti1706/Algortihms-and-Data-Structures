#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stepPerms function below.
def stepPerms(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
result = {1:1,2:2,3:4}
def stepPermsmemorization(n):
    if n in result.keys():
        return result[n]
    result[n] = stepPermsmemorization(n-3)+stepPermsmemorization(n-1)+stepPermsmemorization(n-2)
    return result[n]




s = int(input())

for s_itr in range(s):
    n = int(input())

    res = stepPermsmemorization(n)

    print(str(res) + '\n')

