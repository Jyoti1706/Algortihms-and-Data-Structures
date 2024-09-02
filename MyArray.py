class MyArray:
    def __init__(self,size):
        self.mylist=[0]*size
        self.count=0

    def insertAtEnd(self,key):
       self.mylist[self.count]=key
       self.count+=1