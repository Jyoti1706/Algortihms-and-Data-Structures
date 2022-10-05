'''

Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet and return true. Else return false.

Solution:

Algorithm :
1. Sort the given array.
2. Loop over the array and fix the first element of the possible triplet, arr[i].
3. loop j trough the array get the sum , keep sum as key in dictionary. (create the hash set of sum of 2 element)
4. single loop trough input, this time search for sum-arr[i] in the hashset create

TC: o(n^2)
space: O(n^2)

'''


def triplet_sum(arr, value):
    hashset = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            data = arr[i] + arr[j]
            try:
                hashset[data].append((arr[i], arr[j]))
            except:
                hashset[data] = [(arr[i], arr[j]), ]

    for i in range(len(arr)):
        data = value - arr[i]
        fetch = hashset.get(data, None)
        if fetch is None:
            continue
        else:
            return arr[i], hashset[data][0][0], hashset[data][0][1]


arr = [12, 3, 4, 1, 6, 9]
value = 24
print(triplet_sum(arr, value))
print("-----------------------")
array = [1, 2, 3, 4, 5]
value = 9
print(triplet_sum(array, value))
