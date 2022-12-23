'''
Recursion
'''


def fib_recursion(n):
    if (n == 0) or (n==1):
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(10))
