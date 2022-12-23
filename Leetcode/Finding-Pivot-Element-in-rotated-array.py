nums = [3,4,5,1,2] #
#nums = [11, 13, 15, 17] #[4,5,6,7,0,1,2]
#nums = [2, 3, 4, 5, 1]
#nums=[11]


def findPivotElement(arr):
    lo = 0
    hi = len(arr)-1
    mid = hi + lo // 2
    # if len(arr) <= 1:
    #     return arr[0]
    while lo < hi :

        if mid-1 >= lo and arr[mid - 1] > arr[mid]:
            return arr[mid]
        elif mid + 1 <= hi and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        if arr[lo] <= arr[mid]:
            lo = mid + 1
        elif arr[mid] <= arr[hi]:
            hi = mid - 1
        mid = (lo + hi) // 2
    return arr[0]


print(findPivotElement(nums))
