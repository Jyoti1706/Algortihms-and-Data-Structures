'''
problem Description: Next Palindromic Number
https://www.hackerrank.com/contests/smart-interviews/challenges/si-next-palindromic-number
'''

def all9s(num):
    while num > 0:
        digit = num%10
        if digit != 9:
            return False
        num = num//10
    return True


def findpalindrome(num):
    if all9s(num):
        return num+2
    n = len(num)
    mid = n//2
    incremented = False
    if n%2 == 0:
        i = mid//2
        j = mid//2 + 1
        while i > 0 and j < n:
            if num[i] == num[j]:
                i = i-1
                j=j+1
            elif num[i] > num[j]:
                num[j] = num[i]
                i = i-1
                j=j+1

