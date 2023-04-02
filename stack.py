"""
An implementation of a stack data structure using Pythons built-in list data structure
"""
class Stack():
    # Initalize an empty list
    def __init__(self):
        self.stack = list()
    
    # Return the item at the end of the list (top of stack)
    def top(self):
        return self.stack[-1]
    
    # Remove and return the last element in list (top element on stack)
    def pop(self):
        return self.stack.pop()

    # Add an item to top of stack
    def push(self, item):
        self.stack.append(item)
    
    # Return the length of the stack
    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return "[ " + "".join(str(i) + " " for i in self.stack) + "]"
    

if __name__ == "__main__":
    stack = Stack()
    print('is_empty():', stack.is_empty())
    print('empty:', stack)
    stack.push(1)
    print('after push(1):', stack)
    print('is_empty():', stack.is_empty())
    stack.push(10)
    print('after push(10):', stack)
    print('pop():', stack.pop())
    print('after pop():', stack)
    stack.push(2)
    print('after push(2):', stack)
    stack.push(3)
    print('after push(3):', stack)
    stack.push(4)   
    print('after push(4):', stack)
    print('pop():', stack.pop())
    print('after pop():', stack)
    print('pop():', stack.pop())
    print('after pop():', stack)
    print('pop():', stack.pop())
    print('after pop():', stack)
    print('pop():', stack.pop())
    print('after pop():', stack)
    print('is_empty():', stack.is_empty())