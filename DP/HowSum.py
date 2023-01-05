def howSum(target, numbers,memo):
    if target==0:
        return []
    if target<0:
        return None
    try:
        return memo[target]
    except:
        for number in numbers:
            res =howSum(target-number,numbers,memo)
            if res is not None:
                for r in res:
                    try:
                        memo[target].append(r)
                    except:
                        memo[target]=[r,]
                try:
                    memo[target].append(number)
                except:
                    memo[target]=[number,]
                return memo[target]
    memo[target] = None
    return None

memo={}
print(howSum(7,[2,3],{}))
print(howSum(7,[5,3,4,7],{}))
print(howSum(7,[2,4],{}))
print(howSum(7,[2,3,5],{}))
print(howSum(300,[5],{}))
