'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/



'''



class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp_stack=[]
        move = []
        '''
        1. put bracket in temp_stack, if its opening
        2. if its closing , pop the stack.
            if stack is empty, store index in move list and continue
            else, continue
        3. after loop end if len(temp_stack) > 0, move indexes in output list
        '''
        for i in range(len(s)):
            if s[i] == '(':
                temp_stack.append(i)
            elif s[i] == ')':
                try:
                    temp_stack.pop()
                except:
                    move.append(i)

        print(temp_stack)
        if len(temp_stack) > 0:
            for i in temp_stack:
                move.append(i)
        s = list(s)
        move = sorted(move, reverse=True)
        for replace_idx in move:
            s.pop(replace_idx)
        return "".join(s)

obj = Solution()
s = "lee(t(c)o)de)("
#s2 = ")("

move = obj.minRemoveToMakeValid(s)


print(move)