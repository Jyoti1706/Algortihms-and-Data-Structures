'''

https://leetcode.com/problems/next-permutation/

'''


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
        permutations.add(tuple(perm))
    else:
        for i in range(len(array)):
            newarray = array[:i] + array[i + 1:]
            newperm = perm + [array[i]]
            helper1(newarray, newperm, permutations)


class Solution:
    def nextPermutation(self, array):

        permutations = set()
        helper1(array, [], permutations)
        permutations = list(permutations)
        permutations.sort()
        print(permutations)
        for i in range(len(permutations)):
            try:
                if list(permutations[i]) == array:
                    return list(permutations[i + 1])
            except:
                return list(permutations[0])


nums = [3, 2, 1]
#nums = [1, 1, 5]
nums=[1,2,3]
ob = Solution()
print(ob.nextPermutation(nums))
