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
                print(curr_node.value)
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


# N1 = Node(2)
# N2 = Node(3)
# N3 = Node(5)
# N4 = Node(4)
#
# LL = LinkedList(N1)
# LL.add(N2)
# LL.add(N3)
# LL.add(N4)
# LL.print_node()

llist = LinkedList()
llist.add(6)

# Insert 7 at the beginning. So
# linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning. So
# linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end. So linked list
# becomes 1->7->6->4->None
llist.add(4)

# Insert 8, after 7. So linked list
# becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)

print('Created linked list is:')
llist.print_node()