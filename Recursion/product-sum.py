# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    # Write your code here.
    sum = 0
    for i in array:
        if isinstance(i , list):
            val = productSum(i, depth+1)
        else:
            val = i
        sum = sum+val
    return depth*sum


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))