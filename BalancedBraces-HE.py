'''
This is a Hackerearth problem
'''


tc = int(input())

dic = {')':'(','}':'{',']':'['}
for i in range(0,tc):
    stack = []
    expr = input()
    flag=0
    for e in expr:
        if e in ('(','{','['):
            stack.append(e)
        else:
            try:
                t = stack.pop()
            except:
                flag = 1
                break
            #print(dic[e])
            #print(t)
            #print(not(dic[e] == t))
            if not(t == dic[e]):
                #print("NO")
                flag = 1
                break
    #print(stack)
    if (len(stack) == 0) and (not(flag == 1)):
        print("YES")
    else:
        print("NO")
