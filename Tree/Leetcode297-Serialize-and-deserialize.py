class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder_list = []

        def preorder(node):
            if node:
                preorder_list.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                preorder_list.append("N")

        preorder(root)
        return ",".join(preorder_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        preorder_list = data.split(",")
        self.i = 0
        print(data)

        def helper():
            if preorder_list[self.i] == 'N':
                self.i += 1
                return None
            #print(preorder_list[self.i])
            node = TreeNode(int(preorder_list[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
# h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(a))
print(ans.val)
