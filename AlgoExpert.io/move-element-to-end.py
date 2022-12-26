def moveElementToEnd(array, toMove):
    # Write your code here.
    j = len(array)-1
    i = 0
    while i<j:
        if array[i]==toMove:
            # temp = array[j]
            # array[j]=
            array[j], array[i]=array[i], array[j]
            j=j-1
        else:
            i=i+1
    return array

array=[2, 1, 2, 2, 2, 3, 4, 2]
toMove=2
print(moveElementToEnd(array,toMove))