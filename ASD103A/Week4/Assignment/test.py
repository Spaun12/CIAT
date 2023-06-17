"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Assignment Exceptions"""
# Import the Stack class from the StackToDo module
from StackToDo import Stack

def test_stack_exception():
    # Create a small stack with a maximum size of 2.
    s = Stack(2)

    # Try pushing 3 items onto the stack. The third one should raise an exception.
    try:
        s.push(1)
        s.push(2)
        print("Successfully pushed two items onto the stack.")
        s.push(3)
    except Exception as e:
        print(f"Caught an exception: {str(e)}")

    # Try popping 3 items from the stack. The third one should raise an exception.
    try:
        print(f"Popped {s.pop()} from the stack.")
        print(f"Popped {s.pop()} from the stack.")
        print("Successfully popped two items from the stack.")
        s.pop()
    except Exception as e:
        print(f"Caught an exception: {str(e)}")

# Run the test function
if __name__ == "__main__":
    test_stack_exception()
