def decimal2binary(num):
    if num in [0, 1]:
        return str(num)
    rem = num % 2
    num = num // 2
    return decimal2binary(num) + str(rem)


print(decimal2binary(9))