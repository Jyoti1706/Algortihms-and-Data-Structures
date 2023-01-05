def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    #print(arrayOne[0],arrayTwo[0])
    if not(len(arrayOne) == len(arrayTwo)):
        return False
    if not(arrayOne and arrayTwo):
        return True
    #print(arrayOne[0],arrayTwo[0])
    if arrayOne[0] != arrayTwo[0]:
        return False

    leftarrayOne = [i for i in arrayOne[1:] if i<arrayOne[0]]
    leftarrayTwo = [i for i in arrayTwo[1:] if i<arrayTwo[0]]
    rightarrayOne = [i for i in arrayOne[1:] if i>=arrayOne[0]]
    rightarrayTwo = [i for i in arrayTwo[1:] if i>=arrayTwo[0]]

    left = sameBsts(leftarrayOne,leftarrayTwo)
    right= sameBsts(rightarrayOne,rightarrayTwo)

    return left and right

tc1_arr1=[10, 15, 8, 12, 94, 81, 5, 2, 11]
tc1_arr2=[10, 8, 5, 15, 2, 12, 11, 94, 81]

print(sameBsts(tc1_arr1, tc1_arr2))

tc2_arr1=[10, 15, 8, 12, 94, 81, 5, 2, 11]
tc2_arr2=[11, 8, 5, 15, 2, 12, 11, 94, 81]

print(sameBsts(tc2_arr1, tc2_arr2))