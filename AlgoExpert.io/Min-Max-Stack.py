# Feel free to add new properties and methods to the class.
class MinMaxStack:
    min_stack=[]
    stack=[]
    max_stack=[]
    def peek(self):
        # Write your code here.
        try:
            return self.stack[-1]
        except:
            return []

    def pop(self):
        # Write your code here.
        self.min_stack.pop()
        self.max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        try:
            self.min_stack.append(min(self.min_stack[-1],number))
            self.max_stack.append(max(self.max_stack[-1], number))
        except:
            self.min_stack.append(number)
            self.max_stack.append(number)
        return None

    def getMin(self):
        # Write your code here.
        try:
            return self.min_stack[-1]
        except:
            return []

    def getMax(self):
        # Write your code here.
        try:
            return self.max_stack[-1]
        except:
            return []

st = MinMaxStack()
print(st.push(5))
print(st.getMin())
print(st.getMax())
print(st.peek())
print(st.push(7))
print(st.getMax())
print(st.getMin())
print(st.peek())
print(st.push(2))
