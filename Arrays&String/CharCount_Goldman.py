def charcount(input_string):
    i = 0
    j = 1
    count = 1
    output = ""
    while i != j and j < len(input_string):
        if input_string[i] == input_string[j]:
            count += 1
        else:
            output += input_string[i] + str(count)
            count = 1
            i = j
        j += 1
    output += input_string[i] + str(count)
    print(output)
    return output


assert charcount("aaabbbcccd") == "a3b3c3d1"
assert charcount("abc") == "a1b1c1"
assert charcount("a") == "a1"
