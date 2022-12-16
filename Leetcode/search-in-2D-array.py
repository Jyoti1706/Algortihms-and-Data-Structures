'''
https://leetcode.com/problems/search-a-2d-matrix/submissions/860303873/
'''

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def searchMatrix(matrix, target):
    m = len(matrix)

    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][-1]:
            if binary_search(matrix[i], target) == -1:
                return False
            else:
                return True


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(searchMatrix(matrix, target))
