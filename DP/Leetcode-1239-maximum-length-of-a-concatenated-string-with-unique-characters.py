from typing import List


class Solution:
    def maxLength1(self, arr: List[str]) -> int:
        n = len(arr)
        dp = [set() for _ in range(n)]
        max_len = 0
        for i in range(n):
            if len(arr[i]) == len(set(arr[i])):
                dp[i] = set(arr[i])
                max_len = max(len(arr[i]), max_len)
        for i in range(n):
            for j in range(i):
                if len(dp[i].intersection(dp[j])) == 0:
                    dp[i].extend(dp[j])
                    max_len = max(max_len, len(dp[i]))
        return max_len

    class Solution:
        def maxLength(self, arr: List[str]) -> int:
            n = len(arr)
            res = [""]
            op = 0

            for word in arr:
                for r in res:
                    newRes = r + word
                    if len(newRes) != len(set(newRes)):
                        continue
                    res.append(newRes)
                    op = max(op, len(newRes))
            return op


if __name__ == "__main__":
    # arr = ["un", "iq", "ue"]
    obj = Solution()
    # print(obj.maxLength(arr))
    # arr = ["cha", "r", "act", "ers"]
    # print(obj.maxLength(arr))
    # arr = ["abcdefghijklmnopqrstuvwxyz"]
    # print(obj.maxLength(arr))
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
    print(obj.maxLength(arr))