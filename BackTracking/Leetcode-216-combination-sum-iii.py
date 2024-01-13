from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        high = 9

        def backtrack(ind, n, k, ds, res):
            if len(ds) == k and sum(ds) == n:
                res.append(ds[:])
                return
            for i in range(ind, high + 1):
                ds.append(i)
                backtrack(i + 1, n, k, ds, res)
                ds.pop()

        res = []
        backtrack(1, n, k, [], res)
        return res

if __name__ == "__main__":
    obj = Solution()
    k=3
    n = 7
    print(obj.combinationSum3(k, n))
    k=3
    n = 9
    print(obj.combinationSum3(k, n))