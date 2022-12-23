def powerset_iterative(array):
    output=[[],]
    for ele in array:
        for i in range(len(output)):
            subset = output[i]
            output.append(subset+[ele])
    return output

array=[1,2,3]
print(powerset_iterative(array))