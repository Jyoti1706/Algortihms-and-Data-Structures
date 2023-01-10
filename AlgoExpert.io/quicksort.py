def quicksort(array):
    # Write your code here.
    quicksortalgorithm(array, 0, len(array) - 1)
    return array


def quicksortalgorithm(nums, left, right):
    if left < right:
        partitionIndex = getPartition(nums, left, right)
        quicksortalgorithm(nums, left, partitionIndex - 1)
        quicksortalgorithm(nums, partitionIndex + 1, right)


def getPartition(nums, left, right):
    i = left
    j = left
    while j <= right:
        if nums[j] <= nums[right]:
            swap(nums, i, j)
            i += 1
        j += 1
    return i - 1


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


array=[8, 5, 2, 9, 7, 6, 3]
print(quicksort(array)) ## 5