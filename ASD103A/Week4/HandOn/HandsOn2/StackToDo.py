"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Hands On Exercise Part 2"""
# Implement a Stack data structure using a Python list
 #The isEmpty() and isFull() methods that return Boolean values indicating whether the stack has no items or is at capacity.
# The peek() method checks for an empty stack and returns the top value only if there is one. To avoid errors, 
 #a client program would need to use isEmpty() before calling pop(). 
 #The class also includes methods to measure the stack depth and a string conversion method for convenience in displaying stack contents.
class Stack(object):
    def __init__(self, max): # Constructor
        self.max = max
        # The stack is stored as a list. There are no items initially, initializing an empty list.
        self.stack = []
 
    def push(self, item): # Insert item at top of stack
        # Before pushing, check if the stack is already full.
        if not self.isFull():
            self.stack.append(item) # Append adds the item at the end of the list, the top of the stack.
        else:
            print("Stack is full.")
 
    def pop(self): # Remove top item from stack
        # Check if the stack is not empty.
        if not self.isEmpty():
            return self.stack.pop() # The pop() method removes the last item of the list, which is the top item of the stack.
        else:
            print("Stack is empty.")

    def peek(self): # Return top item
        # Check if the stack is not empty.
        if not self.isEmpty():
            return self.stack[-1] # -1 index is the last item in the list, which is the top item of the stack.
 
    def isEmpty(self): # Check if stack is empty
        # The stack is empty if its length is 0.
        return len(self.stack) == 0
 
    def isFull(self): # Check if stack is full
        # The stack is full if its length is equal to its max capacity.
        return len(self.stack) == self.max
 
    def __len__(self): # Return number of items on stack
        # Using python's len function to get the length of the stack list.
        return len(self.stack)
 
    def __str__(self): # Convert stack to string
        # We can directly convert the list to a string in Python, which will include brackets and commas.
        return str(self.stack)
