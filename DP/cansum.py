def cansum(target, numbers,memo):
    if target==0:
        return True
    if target<0:
        return False
    try:
        return memo[target]
    except:
        for number in numbers:
            memo[target]=cansum(target-number,numbers,memo)
            if memo[target]:
                return True
    memo[target] = False
    return False

memo={}
print(cansum(7,[2,3],{}))
print(cansum(7,[5,3,4,7],{}))
print(cansum(7,[2,4],{}))
print(cansum(7,[2,3,5],{}))
print(cansum(300,[5],{}))
