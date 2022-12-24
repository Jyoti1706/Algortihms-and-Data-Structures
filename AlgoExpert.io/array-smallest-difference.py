import math
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    #print(arrayOne, arrayTwo)
    output={}
    i=len(arrayOne)-1
    j = 0
    j_idx = len(arrayTwo)
    while  0<= i < len(arrayOne):
        j = 0
        min_dis=0
        points=[]
        distance = math.inf
        #print(j_idx)
        while j < j_idx:
            #print(i,j)
            if arrayOne[i]<arrayTwo[j]:
                cal_dis = arrayTwo[j]-arrayOne[i]
            else:
                cal_dis = arrayOne[i]-arrayTwo[j]
            if cal_dis < distance:
                distance = cal_dis
                min_dis = cal_dis
                points = [arrayTwo[j],arrayOne[i]]
                j=j+1
            else:
                break
        j_idx = j
        if len(points)>1:
            output[min_dis]=points
        i=i-1
    return sorted(output.items())[0][1]






a1 = [-1, 5, 10, 20, 28, 3]
a2 = [26, 134, 135, 15, 17]

print("---------------")
print(smallestDifference(a1,a2))