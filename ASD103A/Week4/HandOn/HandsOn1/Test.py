"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Hands On Exercise Part 1"""
# Import the Stack class from the StackToDo module.
# If the Stack class is not in a module, you don't need this line.
from StackToDo import Stack

def test_stack():
    # Create a stack with a maximum size of 5.
    s = Stack(5)

    # Test the push method by adding items to the stack.
    print("Pushing items onto the stack...")
    for i in range(1, 6):
        print(f"Pushing {i} onto stack")
        s.push(i)
    print(f"Stack after pushing 5 items: {s}")

    # Test the __len__ method
    print(f"Length of stack: {len(s)}")  # Expected output: 5

    # Test the isFull method
    print(f"Is the stack full? {s.isFull()}")  # Expected output: True

    # Try to push another item onto the stack. Since it's already full, this should fail.
    print("Trying to push another item onto the stack...")
    s.push(6)  # Expected output: "Stack is full."

    # Test the peek method
    print(f"Peeking at the top item of the stack: {s.peek()}")  # Expected output: 5

    # Test the pop method
    print(f"Popping the top item from the stack: {s.pop()}")  # Expected output: 5
    print(f"Stack after popping top item: {s}")

    # Test the isEmpty method
    print(f"Is the stack empty? {s.isEmpty()}")  # Expected output: False

    # Try to pop all items from the stack
    print("Popping all items from the stack...")
    while not s.isEmpty():
        print(f"Popping {s.pop()} from the stack")
    print(f"Stack after popping all items: {s}")

    # Try to pop an item from the empty stack. Since it's empty, this should fail.
    print("Trying to pop an item from the empty stack...")
    s.pop()  # Expected output: "Stack is empty."

# Run the test function
if __name__ == "__main__":
    test_stack()
