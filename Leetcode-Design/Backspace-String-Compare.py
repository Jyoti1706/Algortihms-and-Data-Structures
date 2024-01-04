def backspaceCompare(s: str, t: str):
    act_s = []
    act_t = []
    for i in s:
        if i != "#":
            act_s.append(i)
        else:
            act_s.pop()
    for j in t:
        if j != "#":
            act_t.append(j)
        else:
            act_t.pop()
    #print(act_s,act_t)
    if act_t == act_s:
        return True
    else:
        return False


s = "ab#c"
t = "ad#c"

print(backspaceCompare(s,t))

s = "ab##"
t = "c#d#"
print(backspaceCompare(s,t))

s="a#c"
t = "b"
print(backspaceCompare(s,t))