class Solution:

    def isSameTreeViaTraversal(self, p, q) -> bool:
        def traversal(root, res):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            traversal(root.left, res)
            traversal(root.right, res)
            return res

        inorderP = traversal(p, [])
        inorderQ = traversal(q, [])
        print(inorderP)
        print(inorderQ)
        if inorderP == inorderQ:
            return True
        else:
            return False

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        else:
            return False
