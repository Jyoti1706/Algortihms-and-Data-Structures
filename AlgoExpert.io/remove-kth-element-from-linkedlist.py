# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    temp = head
    count=0
    while temp:
        count=count+1
        temp=temp.next
    cfs = count-k-1
    print(cfs,count)
    curr = head
    if cfs < 0:
        head=head.next
    while cfs > 0:
        curr = curr.next
        cfs = cfs - 1
    curr.next = curr.next.next
    return head
def print_ll(head):
    while head:
        print(head.value, end="-->")
        head=head.next
    print("None")

n1=LinkedList(0)
n2=LinkedList(1)
n3=LinkedList(2)
n4=LinkedList(3)
n5=LinkedList(4)
n6=LinkedList(5)
n7=LinkedList(6)
n8=LinkedList(7)
n9=LinkedList(8)
n10=LinkedList(9)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
n8.next=n9
n9.next=n10


print_ll(removeKthNodeFromEnd(n1,10))