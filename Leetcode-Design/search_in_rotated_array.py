# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan&id=algorithm-ii

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0


def search_rotated_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[low]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] <= arr[high]:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(search_rotated_array(nums, 0))
