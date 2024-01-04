def findAnagrams(s: str, p: str):
    dic_p={}
    dic_s={}
    len_p=len(p)
    len_s=len(s)
    for i in range(len_p):
        try:
            dic_p[p[i]] += 1
        except:
            dic_p[p[i]]=1
    j=0
    output=[]
    j=0
    for i in range(len_s):
        while j < len_p+i and j < len_s:
            try:
                dic_s[s[j]] += 1
            except:
                dic_s[s[j]] = 1
            j=j+1
        if dic_s==dic_p:
            output.append(i)

        dic_s[s[i]] = dic_s[s[i]]-1
        if dic_s[s[i]] == 0:
            del dic_s[s[i]]
    return output


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s,p))

s = "abab"
p = "ab"
print(findAnagrams(s,p))


