
def reverse(num):
    t = num
    rev=0
    while t > 0:
        rev = rev * 10 + t % 10
        t = t // 10
    return rev
tc = int(input())
for _ in range(tc):
    num = int(input())
    j = num+1
    while True:
        if j == reverse(j):
            break
        j=j+1
    print(j)

