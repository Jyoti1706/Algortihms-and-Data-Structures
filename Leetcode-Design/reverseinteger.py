def reverse( x: int) -> int:
    print((x > 2147483647) or (x < -2147483648))
    if (x > 2147483647) or (x < -2147483648):
        return 0
    flag = False
    if x < 0:
        flag = True
        x = x * -1

    temp = str(x)
    reverse_num = temp[::-1]
    if flag:
        res = int(reverse_num) * -1
    else:
        res = int(reverse_num)
    return res

x= 1534236469
print(reverse(x))