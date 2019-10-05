'''
Created on 05-Oct-2019

@author: Jyoti

Problem Statement

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
 You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
 
 Sample Test Case:
 4
4 3 1 2

output:
3
'''

import os
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    counter=0
    i=0
    while(i < len(arr)):
        if not(i+1 == arr[i]):
            t1 = arr[i]
            t2 = arr[t1-1]
            arr[t1-1],arr[t2-1] = arr[t2-1],arr[t1-1]
            counter=counter+1
            continue
        i=i+1
    return counter




n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(res)

