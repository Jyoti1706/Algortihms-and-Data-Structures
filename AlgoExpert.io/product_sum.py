def productSum(array,cnt=1):
    # Write your code here.
    product_sum=0
    for i in array:
        #print(i)
        if type(i) is list:
            #print(i)
            #cnt=cnt+1
            print(cnt)
            product_sum=product_sum + productSum(i,cnt+1)
        else:
            product_sum=product_sum+i
    #print(product_sum)
    return cnt*product_sum

arr=[5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))