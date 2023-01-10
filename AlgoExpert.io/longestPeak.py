def longestPeak(array):
    longestpeaklength = 0
    i=1
    while i < len(array)-1:

        if array[i-1] < array[i] > array[i+1]:
            leftidx = i-2
            while leftidx >=0 and array[leftidx]<array[leftidx+1]:
                leftidx -= 1
            rightidx = i+2
            while rightidx < len(array) and array[rightidx]<array[rightidx-1]:
                rightidx += 1
            currentpeak = rightidx-leftidx-1
            longestpeaklength = max(currentpeak,longestpeaklength)
            i = rightidx
        else:
            i +=1
    return longestpeaklength

array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))