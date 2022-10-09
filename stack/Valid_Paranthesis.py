'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''


def isValid(data):
    brackets = {"}": "{", ")": "(", "]": "["}
    close_bracket = ["}", "]", ")"]
    stack = []
    for d in data:
        if not (d in close_bracket):
            stack.append(d)
        else:
            if stack:
                if stack[-1] == brackets[d]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    return True


# data = "(()())"
data = ")"
print(isValid(data))

