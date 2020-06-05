'''
Created on 05-Oct-2019

@author: Jyoti
'''
import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    mp = dict()
    for i in range(n):
        sb = ""
        for j in range(i, n):
            sb = "".join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0)
            mp[sb] += 1
    ana = 0
    # print(mp)
    for k, v in mp.items():
        ana = ana + ((v * (v - 1)) // 2)
    return ana


q = int(input())
for i in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')


