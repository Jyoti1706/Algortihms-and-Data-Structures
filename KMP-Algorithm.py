'''
Created on Sep 15, 2020

@author: kumarijy
'''
#  Knuth-Morris-Pratt algorithm 


# Compute temporary array to maintain size of suffix which is same as prefix
# Time/space complexity is O(size of pattern)
def compute_temporary_array(pattern):
    n = len(pattern)
    print("Just a test print statement")
    lsp = [0 for j in range(n)]
    index = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[index]:
            lsp[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = lsp[index - 1]
            else:
                lsp[i] = 0
                i += 1
    return lsp


# KMP algorithm of pattern matching.
def kmp(text, pattern,c):
    lsp = compute_temporary_array(pattern)
    i = 0
    j = 0
    
    while i < len(text) :
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                j = lsp[j - 1]
                c = c+1

        else:
            if j != 0:
                j = lsp[j - 1]
            else:
                i += 1

    return c

tc = int(input())
for _ in range(tc):
    sub_string,src = input().split()
    c=0
    result = kmp(src, sub_string,c)
    print(result)