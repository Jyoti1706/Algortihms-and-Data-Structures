from collections import Counter


class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        say = self.countAndSay(n - 1)
        count = process(say)
        print(count, n)
        return count

def process(say):
    output = ""
    i =0
    n = len(say)
    while i < n:
        curr = say[i]
        count=0
        while i <n and curr == say[i]:
            i += 1
            count += 1
        output += str(count) + curr
    return output




obj = Solution()
print(obj.countAndSay(5))
# print(obj.countAndSay(1))
# print(obj.countAndSay(3))
