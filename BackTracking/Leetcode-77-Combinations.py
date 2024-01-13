"""
Given two integers n and k,
return all possible combinations of k numbers chosen from the range [1, n].
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, temp):
            if i > n:
                if len(temp) == k:
                    ans.append(temp.copy())
                    return
                else:
                    return
            temp.append(i)
            backtrack(i + 1, temp)
            del temp[-1]
            backtrack(i + 1, temp)

        ans = []
        backtrack(1, [])
        return ans


if __name__ == "__main__":
    n = 4
    k = 2
    obj = Solution()
    print(obj.combine(n, k))
