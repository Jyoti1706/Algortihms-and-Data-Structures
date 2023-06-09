


# Complete the isBalanced function below.
def isBalanced(s):
    close = set([']', '}', ')'])
    open_bracket = {'{': '}', '[': ']', '(': ')'}
    stack = []
    s = list(s)
    for bracket in s:
        #print(bracket)
        #print(bracket in close)
        if bracket in close:
            try:
                l = stack.pop()
            except:
                return "NO"
            #print(bracket, open_bracket[l])
            if bracket == open_bracket[l]:
                continue
            else:
                return "No"
        else:
            stack.append(bracket)
    return "Yes"


t = int(input())
for t_itr in range(t):
    s = input()
    result = isBalanced(s)
    print(result)

