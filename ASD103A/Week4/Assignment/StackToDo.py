"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Assignment Exceptions"""
#Implement a Stack data structure using a Python list
 #The isEmpty() and isFull() methods that return Boolean values indicating whether the stack has no items or is at capacity.
# The peek() method checks for an empty stack and returns the top value only if there is one. To avoid errors, 
 #a client program would need to use isEmpty() before calling pop(). 
 #The class also includes methods to measure the stack depth and a string conversion method for convenience in displaying stack contents.
class Stack(object):
    # Constructor that initializes the stack to an empty list and sets the max capacity of the stack
    def __init__(self, max): 
        self.max = max
        self.stack = []
 
    # Method to add an item to the stack
    # If the stack is full, an exception is raised
    def push(self, item): 
        if not self.isFull(): 
            self.stack.append(item) 
        else:
            raise Exception("Stack is full. Cannot push to a full stack.")
 
    # Method to remove an item from the stack
    # If the stack is empty, an exception is raised
    def pop(self): 
        if not self.isEmpty():
            return self.stack.pop() 
        else:
            raise Exception("Stack is empty. Cannot pop from an empty stack.")
 
    # Method to peek at the top item of the stack without removing it
    # Returns the top item if the stack is not empty
    def peek(self): 
        if not self.isEmpty():
            return self.stack[-1] 
 
    # Method to check if the stack is empty
    # Returns True if the stack is empty and False otherwise
    def isEmpty(self): 
        return len(self.stack) == 0
 
    # Method to check if the stack is full
    # Returns True if the stack is full and False otherwise
    def isFull(self): 
        return len(self.stack) == self.max
 
    # Special method to return the number of items in the stack when len() is called
    def __len__(self): 
        return len(self.stack)
 
    # Special method to return a string representation of the stack when print() is called
    def __str__(self): 
        return str(self.stack)

