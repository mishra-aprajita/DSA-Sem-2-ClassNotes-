# <----- Implementation of Stack using List ----->
class Stack:
    # <----- Creating Constructor for Stack Initialization ------>
    def __init__ (self):
        self.stack = []

    # <----- Inserting an Element ----->
    def push(self, data):
        self.stack.append(data)

    # <----- Removing an Element ----->
    def pop(self):
        if len(self.stack)==0:
            print("UnderFlow")
            return
        self.stack.pop()
    
    # <----- Clecking Top Element ----->
    def peek(self):
        if len(self.stack)==0:
            print("UnderFlow")
            return
        print(self.stack[-1])
    
    # <----- Checking stack is Empty or Not ----->
    
    def empty(self):
        if len(self.stack)==0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    # <----- checking the size of the stack ----->
    
    def size(self):
        print(len(self.stack))

# <----- Creating an Object of Stack class----->
s = Stack()
s.push("Aprajita")
s.push("Anushka")
# s.empty()
s.size()
s.peek()
s.pop()
s.peek()
s.pop()
s.empty()