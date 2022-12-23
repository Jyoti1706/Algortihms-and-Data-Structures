def Binary_Search_Recursion(arr, lo, hi, target):
    if lo > hi:
        return -1
    mid = (lo+hi)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        hi = mid-1
        return Binary_Search_Recursion(arr, lo, hi, target)
    else:
        lo=lo+1
        return Binary_Search_Recursion(arr, lo, hi, target)

arr = [-1,0,1,2,3,4,7,9,10,20]
target = 10
print(f"index of target is :: {Binary_Search_Recursion(arr,0, len(arr),10)}")