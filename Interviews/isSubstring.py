def is_substring_with_wildcard(s, pattern):
    s_len, pattern_len = len(s), len(pattern)
    i, j = 0, 0
    if pattern_len > s_len or pattern == "":
        return -1
    while j < pattern_len and pattern[j] == "*":
        i += 1
        j += 1

    start = j
    if j == pattern_len:
        return i - start

    while i < s_len and j < pattern_len:
        k = i
        while k < s_len and j < pattern_len and (pattern[j] == '*' or s[k] == pattern[j]):
            k += 1
            j += 1

        if j == pattern_len:
            return i - start
        i += 1
        j = start

    return -1


# Example usage:
string_to_check = "*pqrsabcdfg"
pattern_with_wildcard = "a*c*fg"  # 5

# result = is_substring_with_wildcard(string_to_check, pattern_with_wildcard)
# print(result)
#
# # Example usage:
#
print(is_substring_with_wildcard("helloWorld", "he*"))  # True
print(is_substring_with_wildcard("helloWorld", "*lo"))  # True
print(is_substring_with_wildcard("helloWorld", "he*lo"))  # True
print(is_substring_with_wildcard("helloWorld", "Wor**"))  # True
print(is_substring_with_wildcard("helloWorld", "*he*"))  # False
print(is_substring_with_wildcard("hello", "hello*"))  # False

print(is_substring_with_wildcard("hello", "*******"))  # False
