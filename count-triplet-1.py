def countTriplets(arr, r):
    d = {}
    for i in arr:
        try:
            d[i] = d[i] + 1
        except:
            d[i] = 1
    # print(d.keys())
    # loop_count = 0
    loop_count = len(list(d.keys()))
    i = 1
    j = 1
    pair = 0
    if len(arr) < 3:
        return 0
    elif loop_count < 3 and r != 1:
        return 0
    elif loop_count < 3 and r == 1:
        pair = d[1]
        return pair
    while i < loop_count - 1:
        pair = pair + d[j] * d[j * r] * d[j * r * r]
        # print(pair)
        i = i + 1
        j = j * r
    return pair


nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])

arr = list(map(int, input().rstrip().split()))
ans = countTriplets(arr, r)
print(ans)
