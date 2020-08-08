import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notification = 0
    j = 0
    odd = 0
    if d%2 == 1:
        median = [(d // 2 + 1)-1,]
    else:
        median = [(d // 2)-1,((d // 2)+1)-1]
    #print(median)
    #print("Loop Starts")
    for i in range(d,len(expenditure)):
        prev_days_expenditure = expenditure[j:i]
        #print(prev_days_expenditure)
        prev_days_expenditure = sorted(prev_days_expenditure)
        try:
            median_data = (prev_days_expenditure[median[0]]+prev_days_expenditure[median[1]])/2
        except:
            median_data = prev_days_expenditure[median[0]]
        if (expenditure[i] > median_data*2) or (expenditure[i]==median_data*2):
            print("Median Data --> ",median_data)
            print(prev_days_expenditure)
            print("Expenditure --> ", expenditure[i])
            notification += 1
        j += 1
    return notification




nd = input().split()

n = int(nd[0])

d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)
print(result)
