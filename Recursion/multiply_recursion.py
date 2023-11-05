def multiply_recursion(n,a):
    if n == 1:
        return a
    return a + multiply_recursion(n-1, a)

assert multiply_recursion(5, 4) == 20
assert multiply_recursion(5, -4) == -20
assert multiply_recursion(1,4) == 4
assert multiply_recursion(7, 8) == 56