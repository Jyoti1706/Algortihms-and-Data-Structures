def string_length(str):
    if len(str)==0:
        return 0
    return 1 + string_length(str[1:])

inp = "Binary search recursion"
print(len(inp))
print(string_length(inp))