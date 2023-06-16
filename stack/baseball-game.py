from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for ele in operations:
            if ele == 'D':
                temp = 2*int(st[-1])
                st.append(temp)
            elif ele == 'C':
                st.pop()
            elif ele == "+":
                st.append(int(st[-2])+int(st[-1]))
            else:
                st.append(ele)

        return sum(map(int,st))
ops = ["1","C"] #["5","-2","4","C","D","9","+","+"] #["5","2","C","D","+"]
ob = Solution()
print(ob.calPoints(ops))