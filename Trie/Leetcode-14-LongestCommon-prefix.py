from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Trie()
        for st in strs:
            t.insert(st)
        curr = t.root
        c = 0
        while len(curr.children) == 1:
            if curr.end:
                break
            c += 1
            curr = list(curr.children.values())[0]
        return strs[0][:c]


if __name__ == "__main__":

    obj = Solution()
    strs = ["flower", "flow", "flight"]
    print(obj.longestCommonPrefix(strs))
    strs = ["ab", "a"]
    print(obj.longestCommonPrefix(strs))