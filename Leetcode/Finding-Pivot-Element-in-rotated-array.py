nums = [4, 5, 6, 7, 8, 10, 2]

def findPivotElement(arr):
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid-1] > arr[mid]:
            return arr[mid]
        elif arr[mid] > arr[mid+1]:
            return arr[mid+1]
        if arr[lo]<=arr[mid]:
            lo=mid+1
        elif arr[mid]<=arr[hi]:
            hi = mid-1
    return -1

print(findPivotElement(nums))