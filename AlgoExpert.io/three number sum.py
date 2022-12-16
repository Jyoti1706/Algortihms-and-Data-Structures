def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    i = 0
    while i < len(array) - 3:
        first = array[i]
        j=i+1
        st=[]
        k=targetSum-first
        while j < len(array):
            pass

