#Student: Michael Connell Date: 2023-06-19

# Import the Stack class from StackToDo file
from StackToDo import Stack

def reverse_word(word):
    """
    This function takes a word as input and returns the reversed word using a Stack.
    """
    # Define the stack with a maximum size equal to the length of the word
    stack = Stack(len(word))

    # Push all letters to the stack
    for letter in word:
        stack.push(letter)

    # Pop all letters from the stack and append them to the reversed_word
    reversed_word = ""
    while not stack.isEmpty():
        reversed_word += stack.pop()
    
    return reversed_word

# Get input from the user
word = input("Enter a word to reverse: ")

# Reverse the word
reversed_word = reverse_word(word)

# Print the reversed word
print(f"The reverse of {word} is {reversed_word}")
