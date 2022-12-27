# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_at_start(value, head):
    temp = LinkedList(value)
    temp.next = head
    head = temp
    return head


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    count = 0
    num1 = 0
    while linkedListOne:
        num1 = num1 *10 + linkedListOne.value
        linkedListOne = linkedListOne.next
        count += 1
    print(num1)
    count = 0
    num2 = 0
    while linkedListTwo:
        num2 = num2 *10 + linkedListTwo.value
        linkedListTwo = linkedListTwo.next
        count += 1
    print(num2)
    result = str(num1 + num2)
    print(result)
    head = LinkedList(int(result[0]))
    for i in result[1:]:
        head = insert_at_start(i, head)
    return head

def print_ll(head):
    while head:
        print(head.value, end=" --> ")
        head=head.next
    print("None")

n1=LinkedList(2)
n2 = LinkedList(4)
n3 = LinkedList(7)
n4 = LinkedList(1)
n4.next=n3
n3.next=n2
n2.next=n1

m1=LinkedList(9)
m2 = LinkedList(4)
m3 = LinkedList(5)
m3.next=m2
m2.next=m1
head=sumOfLinkedLists(n4, m3)
print(print_ll(head))