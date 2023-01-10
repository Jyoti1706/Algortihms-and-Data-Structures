def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    li = []
    coinchange(n,denoms,li)
    return len(li)
def coinchange(n,denoms,li,i=0):
    if n < 0:
        return
    if n==0:
        return li.append(True)
    for j in range(i, len(denoms)):
        coin = denoms[j]
        coinchange(n-coin,denoms,li,j)
    return li

n=7
denoms=[1,5,10]

print(numberOfWaysToMakeChange(n,denoms))