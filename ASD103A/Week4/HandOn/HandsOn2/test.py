"""Student: Michael Connell Date: 06/16/2023 Chapter 7: Hands On Exercise Part 2"""
# May be unessary but, I wanted another way to test the script
# Import the Stack class and functions from the other scripts
from StackToDo import Stack
from StackClientToDo import stack, words

def test_stack():
    # Test the stack has the correct length after pushing items
    assert len(stack) == len(words)

    # Test that the stack is not full
    assert not stack.isFull()

    # Test popping items off the stack
    popped_words = []
    while not stack.isEmpty():
        popped_words.append(stack.pop())
    # The popped words should be the reverse of the original words
    assert popped_words == list(reversed(words))

if __name__ == "__main__":
    test_stack()
