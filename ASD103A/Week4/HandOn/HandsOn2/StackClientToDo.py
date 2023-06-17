"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Hands On Exercise Part 2"""
#import Stack file, created in the previous step called StackToDo.py
#Description- The program allocates  a small stack of 10 elements, pushes some strings onto the stack, displays the contents, then pops them off, 
#printing them left to right, separated by spaces. 

from StackToDo import Stack

# The client creates a small stack of 10 elements 
stack = Stack(10)

# The client pushes some strings onto the stack
words = ["May", "the", "force", "be", "with", "you"]
for word in words:
    stack.push(word)

# The client displays the contents of the stack
print(f"After pushing 6 words on the stack, it contains:\n {stack}")

# The client checks if the stack is full
print(f"Is stack full? {stack.isFull()}")

# The client pops the items off the stack, 
# and prints them left to right separated by spaces
print("Popping items off the stack:")
while not stack.isEmpty():
    print(stack.pop(), end=' ')
