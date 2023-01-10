def quickselect(array, k):
    # Write your code here.
    return quickselectalgorithm(array, 0, len(array) - 1, k-1)


def quickselectalgorithm(nums, left, right, indexToFind):
    partitionIndex = getPartition(nums, left, right)
    if partitionIndex == indexToFind:
        return nums[partitionIndex]
    elif indexToFind < partitionIndex:
        return quickselectalgorithm(nums, left, partitionIndex - 1, indexToFind)
    else:
        return quickselectalgorithm(nums, partitionIndex + 1, right, indexToFind)


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
k=3
print(quickselect(array,k)) ## 5