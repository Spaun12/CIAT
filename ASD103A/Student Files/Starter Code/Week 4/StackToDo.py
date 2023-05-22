# Implement a Stack data structure using a Python list
 #The isEmpty() and isFull() methods that return Boolean values indicating whether the stack has no items or is at capacity.
# The peek() method checks for an empty stack and returns the top value only if there is one. To avoid errors, 
 #a client program would need to use isEmpty() before calling pop(). 
 #The class also includes methods to measure the stack depth and a string conversion method for convenience in displaying stack contents.
class Stack(object):
   def __init__(self, max):                # Constructor
      # The stack stored as a list
      # No items initially
 
   def push(self, item):                   # Insert item at top of stack
      # Advance the pointer
      # Store item
 
   def pop(self):                          # Remove top item from stack
      # Top item
      # Remove item reference
      # Decrease the pointer
      #Return top item
 
   def peek(self):                         # Return top item
      # If stack is not empty
      # Return the top item
 
   def isEmpty(self):                      # Check if stack is empty
      
 
   def isFull(self):                       # Check if stack is full
      
 
   def __len__(self):                      # Return # of items on stack
      
 
   def __str__(self):                      # Convert stack to string
      # Start with left bracket
      # Loop through current items
      # Except next to left bracket,
      # separate items with comma
      # Add string form of item
      # Close with right bracket
     