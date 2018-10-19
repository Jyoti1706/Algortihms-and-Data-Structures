def precalculate_prime():
    arr=[0]*1000001
    j=0
    for i in range(2,1000001):
        j=2
        while((j*i)<1000001):
            arr[j*i]=1
            j=j+1
    return arr 

arr = precalculate_prime()
#print(arr[:20])
n=121
for i in range(2,n):
    if arr[i]==0:
        print(i,end=" ")
