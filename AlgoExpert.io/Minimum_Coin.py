
def coinchange(n, denoms ,memo):
    if n in memo.keys():
        return memo[n]
    if n == 0:
        return []
    if n< 0:
        return None
    shortestcomb = None
    for num in denoms:
        rem = n - num


        remainder_combination = coinchange(rem, denoms, memo)
        if remainder_combination is not None:
            comb = remainder_combination + [num,]
            if (shortestcomb is None) or (len(comb) < len(shortestcomb)):
                shortestcomb = comb
    memo[n] = shortestcomb
    return shortestcomb
def minNumberOfCoinsForChange(n, denoms):
    res = coinchange(n,denoms,{})
    return len(res)

n = 7
denoms = [1, 2, 5, 10]
memo={}
print(coinchange(n, denoms,memo))
n1 = 100
denoms1 = [25,1,2,5]
memo1={}
print(coinchange(n1, denoms1,memo1))