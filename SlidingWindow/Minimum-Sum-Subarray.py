"""
https://www.youtube.com/watch?v=D2MbogiFXWU&list=PLpIkg8OmuX-J2Ivo9YdY7bRDstPPTVGvN
"""
import math


def minimumsumsubarray(array, target):
    i = 0
    j = 0
    n = len(array)
    s = 0
    res = math.inf
    while n > j >= i:
        s = s + array[j]
        while s >= target:
            res = min(res, j - i + 1)
            s = s - array[i]
            #print(res)
            i += 1
        j += 1
    return -1 if res == math.inf else res


array = [2, 3, 1, 2, 4, 3]
target = 7
print(minimumsumsubarray(array, 7))

array = [1,1,1,1,1,1,1]
target = 10
print(minimumsumsubarray(array, target))
