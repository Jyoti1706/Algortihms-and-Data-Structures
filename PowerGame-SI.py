n = int(input())
for _ in range(n):
    n1 = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    i = 0
    j = 0
    count = 0
    while j < n1:
        # print(b[j])
        # print(a[i])
        if (b[j] < a[i]):
            count = count + 1
            i = i + 1
            j = j + 1
        else:
            j = j + 1
    print(count)
