'''
Created on 03-Oct-2019

@author: Jyoti
'''

# Naive Approach --> Check sum of all subpairs and then compare
#Complexity : O(n^2)
'''arr1 = [0,1,0,1,1,1,1]
arr2 = [1,1,1,1,1,1,1]

def longestspan(arr1,arr2,n):
    maxlen = 0
    for i in range(n):
        sum1=0
        sum2=0
        for j in range(i,n):
            sum1 += arr1[j]
            sum2 += arr2[j]
            if (sum1==sum2):
                l = j-i+1
                if l > maxlen :
                    maxlen = l
    return maxlen
print(longestspan(arr1,arr2,7))'''

#Complexity : O(n)

def longestspansum(arr1,arr2,n):
    presum1=0
    maxlen = 0
    presum2 = 0
    diff = {}
    for i in range(n):
        presum1 += arr1[i]
        presum2 += arr2[i]
        currdiff = presum1-presum2
        if currdiff == 0:
            maxlen = i+1
        elif currdiff not in diff:
            diff[currdiff] = i 
        else:
            lengthvar = i - diff[currdiff]
            maxlen = max(maxlen,lengthvar)
    return maxlen

arr1 = [0,1,0,1,1,1,1]
arr2 = [1,1,1,1,1,0,1]
print(longestspansum(arr1,arr2,7))