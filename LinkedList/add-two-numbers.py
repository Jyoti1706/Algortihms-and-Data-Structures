from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNum(l1):
    actual_num = 0
    i = 0
    while l1.next != None:
        num = l1.val * pow(10, i)
        actual_num = actual_num + num
        i += 1
        l1 = l1.next
    actual_num = actual_num + l1.val * pow(10, i)
    return actual_num


def getlinkedlist(num):
    Node = top = ListNode()
    for i in num:
        Node.val = int(i)
        Node.next = ListNode()

    return top


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = getNum(l1)
        num2 = getNum(l2)

        sol = num1 + num2
        solution_ll = getlinkedlist(str(sol))
        return solution_ll
