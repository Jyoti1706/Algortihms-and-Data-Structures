class Solution:
    def decodeAtIndex_1(self, s: str, k: int) -> str:
        """
        This Approach leads to Memory space exceed
        :param s:
        :param k:
        :return:
        """
        res = ""
        for ch in s:
            if ch.isdigit():
                res += res * (int(ch) - 1)
            else:
                res += ch
            if len(res) > k:
                break
        print(res)
        return res[k - 1]

    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit():
                size = size * int(ch)
            else:
                size += 1
        for i in range(len(s)-1, -1, -1):
            k = k % size
            if k == 0 and s[i].isalpha():
                return s[i]
            #print(s[i])
            if s[i].isalpha():
                size -= 1
            else:
                size = size // int(s[i])
        return ""


if __name__ == "__main__":
    obj = Solution()
    s = "leet2code3"
    k = 10
    print(obj.decodeAtIndex(s, k))
    s = "ha22"
    k = 5
    print(obj.decodeAtIndex(s, k))
    s = "a2345678999999999999999"
    k = 1
    print(obj.decodeAtIndex(s, k))
