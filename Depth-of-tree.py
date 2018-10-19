d=0
class Node:
    def __init__(self,data,d):
        self.data=data
        self.left=None
        self.right = None
        self.depth=d
    def insert(self,val,d):
        
        
        if self.data or self.data == 0:
            d=d+1
            if self.data > val:
                if self.left is None:
                    self.left = Node(val,d)
                else:
                    self.left.insert(val,d)
            elif val > self.data:
                if self.right is None:
                    self.right=Node(val,d)
                else:
                    self.right.insert(val,d)
        else:
            self.data =val
            self.depth=d 

def printdepth(root,val):
    current = root
    while True:
        if val < current.data:
            if current.left:
                current = current.left
            else:
                break
        elif val > current.data:
            if current.right:
                current = current.right
            else:
                break
        else:
            print(current.depth,end=" ")
            break 
    
        
tc = int(input())
for _ in range(tc):

    t = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0],0)
    #print(root.data)
    d=0
    for i in range(1,t):
        root.insert(arr[i],0)
    for i in range(0,t):
        printdepth(root,arr[i])
    print()
        
                