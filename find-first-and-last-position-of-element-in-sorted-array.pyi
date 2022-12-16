'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

def binary_search_index(arr, target, left_bias):
    i=-1
    l , h=0, len(arr)-1
    m = (l+h)//2
    if arr[m]>target:
        h=m-1
    elif arr[m]<target:
        l=m+1
    else:
        i=m
        if left_bias:
            h=m-1
        else:
            l=m+1

    return i

def search_first_last_index(arr, target):
    l = binary_search_index(arr,target,True)
    r = binary_search_index(arr, target, False)

    print(l,r)

arr = [1,1,2,2,2,2,2,4,5,6]
search_first_last_index(arr, 2)