'''
You are given an array of n+2 elements. All elements of the array are in range 1 to n.
All elements occur once except two numbers,
which occur twice. Your task is to find the two repeating numbers.
Input
2
8
1 3 2 3 4 6 5 5
10
1 5 2 8 1 4 7 4 3 6

Sample Output 0
3 5
1 4
'''


n = int(input())
for _ in range(n):
    n2 = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr = sorted(arr)
    count=0
    i=0
    while(i < n2-1):
        j = i+1
        if arr[i] == arr[j]:
            print(arr[i], end =' ')
            i = i+2
            count = count+1
            if count==2:
                break
        else:
            i = i+1
    print()
