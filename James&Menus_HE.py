'''
Problem Statement:
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/howie-and-the-menus-2-48359fe4/
Dificulties : Easy
DS: Arrays
'''

n, m = list(map(int, input().split()))
menu = []
for i in range(n):
    arr = list(map(int, input().split()))
    menu.append(arr)
zero = [0]*m
count = [zero]*n

print(menu)
max_price = []

for j in range(m):
    max = 0
    for i in range(n):
        if menu[i][j] > max:
            max = menu[i][j]
    max_price.append(max)
print(max_price)
k = 0
max_data = {}
max = 0
sum_data = []
for i in range(n):
    count = 0
    sum_row=0
    for j in range(m):
        if menu[i][j] == max_price[j]:
            count = count+1
        sum_row = sum_row+menu[i][j]
    sum_data.append(sum_row)
    if count > max:
        max = count
    try:
        max_data[count].append(i)
    except:
        max_data[count] = [i]

max = 0
output = []
print(f"sum_data :: {sum_data}")
for k in range(n):
    avg = sum_data[k]/int(m)
    if max < avg:
        output = [avg, k]
print(output[1])










