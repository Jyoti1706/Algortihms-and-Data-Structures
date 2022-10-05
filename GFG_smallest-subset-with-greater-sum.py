'''
Problem Statement: https://practice.geeksforgeeks.org/problems/smallest-subset-with-greater-sum/1

You are given an array Arr of size N containing non-negative integers. Your task is to choose the minimum number of
elements such that their sum should be greater than the sum of the rest of the elements of the array.
ip:
1
6
5 3 2 8 4 1
op: 2
'''

class Solution:
    def minSubset(self, A,N):
        s = sorted(A)
        j = len(s)-1
        m2 = s[j]
        tot_sum = sum(s)
        c=1
        while j>0:
            tot_sum = tot_sum-s[j]
            if m2 > tot_sum:
                return c
            else:
                j=j-1
                m2 = m2+s[j]
                c=c+1
        else:
            return 1

t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.minSubset(A,N)
    print(ans)