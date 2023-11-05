def getPermutations(array):
    # Write your code here.
    permutations = []
    #helper1(array, [], permutations)
    helper2(0,array, permutations)
    return permutations


def helper1(array, perm, permutations):
    '''
    :param array:
    :param perm:
    :param permutations:
    Solution 1:
    1. Base case , if its empty array and perm has some elements it means we got a permutations
    2. Recursion Logic:
        1. loop through all element.
        2. remove current element from option of element to choose and create a new array and feed to next recursion.
        3. add removed element to intermittent perm list
        4. call with new array and new list
    :return: modifies permutations list with all possible combination
    space: O(n.n!)
    time: O(n.n.n!)
    n! <-- possible combo, n is for no. of element in each perm, and extra n is for step 2 and 3
    '''
    if (len(array) == 0) and len(perm):
        permutations.append(perm)
    else:
        for i in range(len(array)):
            newarray = array[:i] + array[i + 1:]
            newperm = perm + [array[i]]
            helper1(newarray, newperm, permutations)


def helper2(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array,i,j)
            helper2(i+1,array,permutations)
            swap(array, i,j)


def swap(array, i ,j):
    array[i], array[j] = array[j], array[i]


array = [1, 2]
results = getPermutations(array)
print(len(results))
print(results)
