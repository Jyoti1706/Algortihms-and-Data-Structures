import numpy as np
def firstNonRepeatingCharacter(string):

    # Write your code here.
    counter = [-1,]*len(string)
    search_ch = {}
    for i in range(len(string)):
        s = string[i]
        try:
            idx = search_ch[string[i]]
            counter[idx] += 1
        except:
            search_ch[string[i]] = i
            counter[i] = 1
    print(search_ch,counter)
    for i in range(len(counter)):
        if counter[i]==1:
            return i
    return -1

print(firstNonRepeatingCharacter("abcdcaf"))
