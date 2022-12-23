'''
Recursion
'''


def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    l = MergeSort(arr[:mid])
    r = MergeSort(arr[mid:])

    return merge(l, r)


def merge(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    i, j = 0, 0
    output = []
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i = i + 1
        else:
            output.append(arr2[j])
            j = j + 1

    while i < len1:
        output.append(arr1[i])
        i = i + 1
    while j < len2:
        output.append(arr2[j])
        j=j+1
    return output


print(MergeSort([10,12,4,6,2,5,1,8,0,3]))