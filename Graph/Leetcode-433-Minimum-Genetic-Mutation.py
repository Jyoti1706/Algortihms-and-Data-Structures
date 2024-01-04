"""

https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

"""
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set()
        que = deque()
        que.append(startGene)
        level = 0
        visited.add(startGene)

        while que:
            n = len(que)
            while n:
                curr = que.popleft()
                if curr == endGene:
                    return level
                for ch in "ACGT":
                    for i in range(len(curr)):
                        neighbour = curr
                        neighbour = neighbour[:i]+ch+neighbour[i+1:]
                        if not (neighbour in  visited) and (neighbour in bank):
                            que.append(neighbour)
                            visited.add(neighbour)

                n -= 1
            level += 1
        return -1



if __name__ == "__main__":
    obj = Solution()
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]

    print(obj.minMutation(startGene, endGene, bank))
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(obj.minMutation(startGene, endGene, bank))