def exp_recurion(a,n):
    if n == 1:
        return a
    return a * exp_recurion(a, n-1)

assert exp_recurion(5,3) == 125
assert exp_recurion(2,5) == 32