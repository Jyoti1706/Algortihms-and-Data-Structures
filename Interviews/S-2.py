def is_substring_with_wildcard(s, pattern):
    s_len, pattern_len = len(s), len(pattern)
    i, j = 0, 0

    while i < s_len and j < pattern_len:
        if pattern[j] == '*':
            # If '*' is the last character in the pattern, it matches the rest of the string.
            if j == pattern_len - 1:
                return True

            # Move the pointer in the pattern until a non-wildcard character is found.
            while j < pattern_len - 1 and pattern[j + 1] == '*':
                j += 1

            # Move the pointer in the string until a character matching the next character in the pattern is found.
            while i < s_len and (s[i] != pattern[j + 1] and pattern[j + 1] != '*'):
                i += 1
        elif s[i] == pattern[j]:
            i += 1
            j += 1
        else:
            return False

    # If there are remaining characters in the pattern, but they are all '*'
    while j < pattern_len and pattern[j] == '*':
        j += 1

    return i == s_len and j == pattern_len

# Example usage:
string_to_check = "abcdefg"
pattern_with_wildcard = "a*c*fg"

result = is_substring_with_wildcard(string_to_check, pattern_with_wildcard)
print(result)
