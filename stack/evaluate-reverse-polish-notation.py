'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/

'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for ele in tokens:
            if ele == "+":
                temp = int(st[-2]) + int(st[-1])
                st.pop()
                st.pop()
                st.append(int(temp))
            elif ele == "-":
                temp = int(st[-2]) - int(st[-1])
                st.pop()
                st.pop()
                st.append(int(temp))
            elif ele == "/":
                temp = int(st[-2]) / int(st[-1])
                st.pop()
                st.pop()
                st.append(int(temp))
            elif ele == "*":
                temp = int(st[-2]) * int(st[-1])
                st.pop()
                st.pop()
                st.append(int(temp))
            else:
                st.append(int(ele))

        return st[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
ob = Solution()
print(ob.evalRPN(tokens))
