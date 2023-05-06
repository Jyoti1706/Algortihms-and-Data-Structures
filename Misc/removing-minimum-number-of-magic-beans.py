'''
https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.

'''

'''
BruteForce:
loop and find out steps for each element, take the minimum

Solution 1
1. Approach using binary search till an array's max element
2. using binarry array find till magic beans

solution 2:

Mathematics :

magic beans cost for each element at that idx is 

sum(array)-(len(array)-i*array[i])

'''


# def equalize_bags(beans):
#     # Step 1: Calculate the sum of all beans
#     total_beans = sum(beans)
#
#     # Step 2: Iterate over all possible sums of the bags
#     for sum_beans in range(total_beans, beans[0] - 1, -1):
#         # Check if the sum is divisible by the number of bags
#         if sum_beans % len(beans) == 0:
#             # Step 3: Calculate the desired number of beans in each bag
#             equal_beans = sum_beans // len(beans)
#             # Step 4: Calculate the difference between the desired and actual number of beans
#             diff = sum(abs(b - equal_beans) for b in beans)
#             # Step 5: Return the minimum number of beans to remove
#             return diff // 2
#
#     # Step 6: No solution found
#     return -1

def equalize_bags(beans):
    summation = sum(beans)
    n =len(beans)
    beans = sorted(beans)
    max_area = 0
    idx=0
    for i in beans:
        area= i *(n-idx)
        max_area=max(max_area,area)
        print(area)
        idx += 1
    return summation-max_area

beans = [2,10,3,2] #[4,1,6,5]
result = equalize_bags(beans)
print(result)  # Output: 4
