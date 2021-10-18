'''
Find the pair in array which has sum is S
https://statestreet.udemy.com/course/cpp-data-structures-algorithms-levelup-prateek-narang/learn/lecture/24429114#overview
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8]
set_array = set()
s = 8

for a in arr:
    num = s - a
    if num in set_array:
        print(a, num)
    else:
        pass
    set_array.add(a)

print(set_array)
