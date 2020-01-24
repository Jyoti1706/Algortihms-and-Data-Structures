'''
Created on 27-Jul-2019

@author: Jyoti
'''
n = int(input())
for i in range(n):
    p = int(input())
    p1 = bin(p).replace("0b","")
    li=list()
    for i in p1:
        li.append(i)
    c0=0
    c1=0
    full_count_1=0
    full_count_0=0
    for i in range(len(li)):
        c0=0
        c1=0
        if li[i] == 0:
            full_count_0 += 1
            c0=1
        else:
            full_count_1 += 1
            c1 = 1
        for j in range(i+1,len(li)):
            print(li[j:])
            if li[j] == 0:
                c0 += 1
                if c0 % 2 == 1:
                    full_count_0 += 1
            else:
                c1 += 1
                if c1 % 2 == 1:
                    full_count_1 += 1
    print(full_count_0,full_count_1)
                    