def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i=0
    j=0
    distance = -1
    while i < len(arrayOne) and j<len(arrayTwo):
        if arrayOne[i]<arrayTwo[j]:
            cal_dis = arrayTwo[j]-arrayOne[i]
        else:
            cal_dis = arrayTwo[i] - arrayOne[j]
        if distance == -1:
            distance = cal_dis
        elif cal_dis < distance:
            pass






a1 = [-1, 5, 10, 20, 28, 3]
a2 = [26, 134, 135, 15, 17]