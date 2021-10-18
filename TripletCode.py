'''

Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet and return true. Else return false.

Solution:

Algorithm :
1. Sort the given array.
2. Loop over the array and fix the first element of the possible triplet, arr[i].
3. Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
    If the sum is smaller than the required sum, increment the first pointer.
    Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
    Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
'''


def triplet_count(arr, value):
    arr = sorted(arr)

    for i in range(0, len(arr)):
        target_sum = value - arr[i]
        j = i + 1
        k = len(arr)-1
        while j < k:
            current_sum = arr[j] + arr[k]
            if current_sum == target_sum:
                print(arr[i], arr[j], arr[k])
                j += 1
                k -= 1

            elif current_sum > target_sum:
                k -= 1
            else:
                j += 1


arr = [12, 3, 4, 1, 6, 9]
value = 24
triplet_count(arr, value)
print("-----------------------")
array = [1, 2, 3, 4, 5]
value = 9
triplet_count(array, value)