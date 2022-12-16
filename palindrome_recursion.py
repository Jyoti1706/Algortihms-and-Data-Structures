def palindrome(input):
    if len(input) == 0 or len(input)== 1:
        return True
    return input[0]==input[-1] and palindrome(input[1:-1])

print(palindrome("kayak"))
print(palindrome("illumanati"))