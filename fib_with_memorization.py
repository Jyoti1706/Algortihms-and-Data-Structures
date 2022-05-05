import timeit


def mem_fib(func):
    cache = {}

    def inner(arg):
        if arg not in cache[arg]:
            cache[arg] = func(arg)
        return cache[arg]

    return inner


@mem_fib
def fib(arg):
    if arg == 1:
        return arg
    elif arg == 0:
        return arg
    else:
        return fib(arg - 1) + fib(arg - 2)


print(timeit.timeit('fib(30)', globals=globals(), number=1))
print(timeit.timeit('fib(20)', globals=globals(), number=1))
print(timeit.timeit('fib(40)', globals=globals(), number=1))
