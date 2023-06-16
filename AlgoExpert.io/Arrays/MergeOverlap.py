'''
https://www.algoexpert.io/questions/merge-overlapping-intervals
'''

input_data = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    output = []
    temp_interval = []
    if len(intervals) == 0:
        output.append(temp_interval)
    temp_interval = intervals[0]

    for interval in intervals[1:]:

        if temp_interval[1] >= interval[0]:
            if temp_interval[1] < interval[1]:
                temp_interval[1] = interval[1]
        else:
            output.append(temp_interval)
            temp_interval = interval
    output.append(temp_interval)
    return output


input_data = [
    [1, 22],
    [-20, 30]
]
print(mergeOverlappingIntervals(input_data))
