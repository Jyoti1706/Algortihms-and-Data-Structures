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


def mergedLL(head1, head2):

    sorted_ll = Node(None)
    head = sorted_ll
    while head1 and head2:
        if head1.value < head2.value:
            sorted_ll.next = head1
            sorted_ll = sorted_ll.next
            head1 = head1.next
        elif head1.value > head2.value:
            sorted_ll.next = head2
            sorted_ll = sorted_ll.next
            head2 = head2.next
        else:
            sorted_ll.next=head1
            sorted_ll=sorted_ll.next
            sorted_ll.next = head2
            sorted_ll = sorted_ll.next
            head2 = head2.next
            head1 = head1.next
    head = head.next
    return head

def printLL(head):
    while head:
        print(head.value, end="-->")
        head=head.next
    #print("--------------")
ll1 = LinkedList()
ll1.add(1)
ll1.add(3)
ll1.add(5)
ll1.add(7)

ll2 = LinkedList()
ll2.add(2)
ll2.add(4)
ll2.add(6)
ll2.add(8)

ml = mergedLL(ll1.head,ll2.head)
print(printLL(ml))

