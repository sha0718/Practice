from collections import deque
class Stack:
    def __init__(self):
        self.container = []

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0
    

    def size(self):
        return len(self.container) 

if __name__ == "__main__":       
 stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
print("Peek:", stack.peek()) 
print("pop:", stack.pop())
print("is empty?",stack.is_empty())
print("size of stack",stack.size())