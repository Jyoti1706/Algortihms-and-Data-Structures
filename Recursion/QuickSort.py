def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


arr = [7, 8, 3, 3, 16, 8, 12, 15, 6, 10, 9, 5]
print(quicksort(arr))
