from collections import Counter


def countAnagram(txt, pat):
    window = len(pat)
    pat_count = Counter(pat)
    txt_count = Counter(txt[:window])
    i = window+1
    count = 0
    while i < len(txt):
        if pat_count == txt_count:
            count += 1
        c = txt[i-window-1]
        txt_count[c] -= 1
        if txt_count[c] == 0:
            del txt_count[c]
        txt_count[txt[i]] = txt_count.get(txt[i],0)+1
        i += 1
    return count


txt = "forxxorfxdofr"
pat = "for"
print(countAnagram(txt,pat))


