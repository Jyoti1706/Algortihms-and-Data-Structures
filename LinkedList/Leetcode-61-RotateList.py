# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        print(count)
        traverse = count-k
        curr = head
        for i in range(traverse-1):
            curr = head.next
        split = curr.next
        curr.next=None
        head2=split
        while split.next:
            split = split.next
        split.next = head
        return head2
