"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str):
        """
        T(o) - (4**n) * n
        :param digits:
        :return:
        """
        comb = {1: None, 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        n = len(digits)
        if n == 0:
            return []
        result = []

        def solve(idx, temp):
            if idx >= n:
                result.append(temp)
                return
            for j in comb[int(digits[idx])]:
                temp = temp + j
                solve(idx + 1, temp)
                temp = temp[:-1]

        solve(0, "")
        return result


if __name__ == "__main__":
    obj = Solution()
    digits = "234"
    print(obj.letterCombinations(digits))
    digits = "23"
    print(obj.letterCombinations(digits))
    digits = "2"
    print(obj.letterCombinations(digits))
    digits = ""
    print(obj.letterCombinations(digits))