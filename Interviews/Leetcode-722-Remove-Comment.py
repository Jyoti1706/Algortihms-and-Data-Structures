"""
https://leetcode.com/problems/remove-comments/description/
"""


class Solution:
    def removeComments(self, source):
        output = []
        multiflag = False
        st = ""
        for comment in source:
            i = 0
            n = len(comment)
            if not multiflag:
                st = ""
            while i < n:
                ch = comment[i:i + 2]
                if multiflag:
                    if ch == "*/":
                        multiflag = False
                        i += 2
                        continue
                    i += 1
                else:
                    if ch == "//" :
                        break
                    if ch == "/*" :
                        multiflag = True
                        i += 2
                        continue

                    st += comment[i]
                    i += 1
            if st and not multiflag:
                output.append(st)
        return output


# Source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# obj = Solution()
# print(obj.removeComments(Source))
#
# source = ["a/*comment", "line", "more_comment*/b"]
source = ["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"]
source = ["d/*/e/*/f"]

obj = Solution()
print(obj.removeComments(source))
