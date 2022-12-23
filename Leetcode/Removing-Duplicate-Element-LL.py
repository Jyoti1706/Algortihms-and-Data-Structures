from collections import Counter


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node_data = Node(data)
        if self.head is None:
            self.head = node_data
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node_data

    def print_node(self):
        if self.head is None:
            print(f"No element added in linked list")
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.value, end="-->")
                curr_node = curr_node.next

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        # 1. Check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

def deleteDuplicates1(head):
    if head is None:
        return "empty Linked List"
    if head.next is None:
        return head
    curr_node=head
    prev = Node(None)
    prev.next = head
    while (curr_node is not None) and curr_node  :
        dup_flag = False
        while (curr_node.next is not None) and (curr_node.value == curr_node.next.value) :
            curr_node.next = curr_node.next.next
            dup_flag=True
        if dup_flag :
            print(dup_flag, prev.value, curr_node.value)
            prev.next = curr_node.next
        prev=curr_node
        curr_node = curr_node.next
    head = prev


def deleteDuplicates_samespace(head):
    dummy = Node(None)
    dummy.next = head
    prev=dummy
    while head :
        #dup_flag = False
        print(head.value, head.next)
        if head.next and (head.value == head.next.value) :
            while head.next and head.value == head.next.value:
                head = head.next
            prev.next = head.next
        else:
            prev=prev.next
        head = head.next
    return dummy.next

def deleteDuplicates_extraspace(head):
    node_list=[]
    while head:
        node_list.append(head.value)
        head = head.next
    node_freq = Counter(node_list)
    temp = [k for k,v in node_freq.items() if v==1]
    print(temp)
    dummy = cur = Node()
    for i in temp:
        cur.next=Node(i)
        cur = cur.next
    return dummy.next




# ll = LinkedList()
# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.add(3)
# ll.add(3)
# ll.add(4)
# ll.add(5)
#
#
# print(ll.print_node())
# deleteDuplicates(ll.head)
# print(ll.print_node())

ll1 = LinkedList()
ll1.add(1)
ll1.add(1)
ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(3)
ll1.add(5)


print(ll1.print_node())
ll1.head = deleteDuplicates_extraspace(ll1.head)
print(ll1.print_node())
