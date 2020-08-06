import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    i = 0
    sum = 0
    count = 0
    while(i < len(prices) and prices[i] < k):
        sum = sum + prices[i]
        if (sum > k):
            return count
        count = count+1
        i = i+1
    return count




nk = input().split()

n = int(nk[0])

k = int(nk[1])

prices = list(map(int, input().rstrip().split()))


result = maximumToys(prices, k)
print(result)