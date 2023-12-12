from collections import Counter


def countAnagram(txt, pat):
    i = 0
    window = len(pat)
    j=0
    txt_freq = Counter[pat]
    pat_freq = Counter[pat]
    while j < len(txt):
        if (j-i-1) == window:
            pass



txt = "forxxorfxdofr"
pat = "for"
print(countAnagram(txt, pat))
