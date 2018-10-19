'''
Created on Oct 16, 2018

@author: kumarijy
'''
from collections import deque
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


    
def height(root):
    if root is None:
        return 0
    else:
        return (1+max(height(root.left),height(root.right)))  
    
def printLevelOrder(root): 
    # Base Case 
    if root is None: 
        return
      
    # Create an empty queue for level order traversal 
    queue = [] 
  
    # Enqueue Root and initialize height 
    queue.append(root) 
    queue.append('*')
    while (len(queue) > 0) : 
        if len(queue)==1:
            if queue[0]=='*':
                break
        # Print front of queue and remove it from queue 
        if queue[0] == '*':
            print()
            queue.append('*')
            node = queue.pop(0)
            
        else:
            print(queue[0].data,end=" ")
            node = queue.pop(0) 
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
  
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right)  
        #print(queue)
            
        
tc = int(input())
for _ in range(tc):

    t = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0],0)
    #print(root.data)
    d=0
    for i in range(1,t):
        root.insert(arr[i],0)
    printLevelOrder(root)
    print()
    print()
        
                